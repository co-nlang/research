import numpy as np
import pandas as pd
import scipy.linalg
from astropy.cosmology import FlatLambdaCDM
from pathlib import Path

HERE = Path(__file__).parent

# ============================================================
# 0. Constants
# ============================================================
C = 299792.458  # km/s

# ΛCDM (Planck 2018, Wiltshire 2024 baseline)
H0_LCDM = 67.4
OM0_LCDM = 0.315

# Timescape (Wiltshire 2024 best fit, Table 2)
H0_TIMESCAPE = 67.4
FV0_TIMESCAPE = 0.72

MASS_SPLIT = 10.0
STEP_SIZE = 0.06

# ============================================================
# 1. Data Loading
# ============================================================
def load_pantheon(data_path=None):
    if data_path is None:
        data_path = HERE / 'Pantheon+SH0ES.dat'
    df = pd.read_csv(data_path, sep=r'\s+')
    for col in ['HOST_LOGMASS', 'HOST_LOGMASS_ERR', 'RA', 'DEC',
                'HOST_RA', 'HOST_DEC', 'MWEBV']:
        if col in df.columns:
            df[col] = df[col].replace(-999, np.nan).replace(-999.0, np.nan)
    return df


def load_covariance(cov_path=None, which='STAT+SYS'):
    """Load Pantheon+ covariance from .cov file (N header + N² values)."""
    if cov_path is None:
        cov_path = HERE / f'Pantheon+SH0ES_{which}.cov'
    with open(cov_path) as f:
        n = int(f.readline().strip())
    vals = np.loadtxt(cov_path, skiprows=1)
    return vals.reshape(n, n)


# ============================================================
# 2. Model Predictions
# ============================================================
def mu_lcdm(z, H0=H0_LCDM, Om0=OM0_LCDM):
    cosmo = FlatLambdaCDM(H0=H0, Om0=Om0)
    return np.asarray(cosmo.distmod(z).value, dtype=np.float64)


def _solve_x(z, f_v0):
    """Solve f_v0 x³ + (1-f_v0)x² - 1/(1+z)³ = 0 for x = t/t₀."""
    z = np.atleast_1d(np.asarray(z, dtype=np.float64))
    a = f_v0
    b = 1.0 - f_v0
    x = np.empty_like(z)
    for i, zi in enumerate(z):
        rhs = 1.0 / (1 + zi)**3
        if zi < 0.01:
            x[i] = np.sqrt(rhs / b)
        else:
            lo, hi = 0.0, 1.0
            for _ in range(50):
                mid = 0.5 * (lo + hi)
                val = a * mid**3 + b * mid**2
                if val > rhs:
                    hi = mid
                else:
                    lo = mid
            x[i] = 0.5 * (lo + hi)
    return x


def _f_v(z, f_v0, x=None):
    """Void fraction f_v(z) from tracker solution (empty voids + EdS walls)."""
    if x is None:
        x = _solve_x(z, f_v0)
    return f_v0 * x / (1.0 - f_v0 + f_v0 * x)


def mu_timescape(z, H0_dressed=H0_TIMESCAPE, f_v0=FV0_TIMESCAPE):
    """Timescape dressed distance modulus (tracker solution).

    Uses the correct bare-frame expansion with:
      a_w³ ∝ (t/t₀)², a_v³ ∝ (t/t₀)³  (empty voids, EdS walls)
    then dresses the distance.
    """
    z_arr = np.atleast_1d(np.asarray(z, dtype=np.float64))

    Om_bar = 0.5 * (1 - f_v0) * (2 + f_v0)
    Ok_bar = 1.0 - Om_bar

    # Bare H̄₀ from dressed H₀: H_dressed(0) = H̄₀ * (2+f_v0) / (2*(1+f_v0))
    H0_bar = H0_dressed * 2 * (1 + f_v0) / (2 + f_v0)

    # Solve for x = t/t₀ at each z
    x = _solve_x(z_arr, f_v0)
    fv = _f_v(z_arr, f_v0, x)

    # Dressed Hubble rate: H(z) = H̄(z) * (2+f_v(z)) / (2*(1+f_v(z)))
    nint = max(10000, int(z_arr.max() * 5000 + 100))
    z_grid = np.linspace(0, z_arr.max(), nint)
    dz = z_grid[1] - z_grid[0]

    x_grid = _solve_x(z_grid, f_v0)
    fv_grid = _f_v(z_grid, f_v0, x_grid)
    E_bar = np.sqrt(Om_bar * (1 + z_grid)**3 + Ok_bar * (1 + z_grid)**2)
    H_bar = H0_bar * E_bar
    H_dressed = H_bar * (2 + fv_grid) / (2 * (1 + fv_grid))

    I_cumulative = np.cumsum(1.0 / H_dressed) * dz
    I_z = np.interp(z_arr, z_grid, I_cumulative)

    d_L = 299792.458 * (1 + z_arr) * I_z  # Mpc
    mu = 5.0 * np.log10(d_L * 1e5)
    return np.asarray(mu, dtype=np.float64)


# ============================================================
# 3. χ² Computation (submatrix, invert on the fly)
# ============================================================
def compute_chi2_group(mu_obs, mu_theory, cov_full, indices):
    """χ² = (μ_obs - μ_theory)ᵀ C_sub⁻¹ (μ_obs - μ_theory)
    
    Parameters
    ----------
    mu_obs, mu_theory : array, length n
    cov_full : (N, N) full covariance
    indices : array of ints, length n — positions in the full cov
    """
    delta = mu_obs - mu_theory
    mask = ~(np.isnan(delta) | np.isnan(mu_obs) | np.isnan(mu_theory))
    delta = delta[mask]
    idx = indices[mask]
    if len(idx) < 2:
        return 0.0, 0
    C_sub = cov_full[np.ix_(idx, idx)]
    C_sub_inv = scipy.linalg.inv(C_sub)
    chi2 = delta @ C_sub_inv @ delta
    return chi2, len(idx)


# ============================================================
# 4. Group Analysis
# ============================================================
def group_chi2_analysis(df, cov_full, mass_col='HOST_LOGMASS',
                        mu_col='MU_SH0ES', redshift_col='zHD'):
    """Compute χ² for wall and void groups, both models."""
    df = df.dropna(subset=[mass_col, mu_col, redshift_col]).copy()
    df = df[df[redshift_col] > 0.01].copy()

    q25 = df[mass_col].quantile(0.25)
    q75 = df[mass_col].quantile(0.75)

    results = {}
    for group_name, dfg in [('Wall', df[df[mass_col] >= q75]),
                            ('Void', df[df[mass_col] <= q25])]:
        z = dfg[redshift_col].values
        mu_obs = dfg[mu_col].values
        indices = dfg.index.values

        mu_l = mu_lcdm(z)
        chi2_l, n_l = compute_chi2_group(mu_obs, mu_l, cov_full, indices)

        mu_t = mu_timescape(z)
        chi2_t, n_t = compute_chi2_group(mu_obs, mu_t, cov_full, indices)

        results[group_name] = {
            'n': n_l,
            'chi2_lcdm': chi2_l,
            'chi2_lcdm_red': chi2_l / n_l if n_l > 0 else 0,
            'chi2_timescape': chi2_t,
            'chi2_timescape_red': chi2_t / n_t if n_t > 0 else 0,
            'delta_chi2': chi2_l - chi2_t,
        }
    return results


# ============================================================
# 5. Main
# ============================================================
def main():
    print("=" * 65)
    print("Timescape MVP: χ² Showdown — Wall vs Void")
    print("=" * 65)

    df = load_pantheon()
    print(f"Loaded {len(df)} SNe from Pantheon+")

    print("Loading STAT+SYS covariance (1701×1701)...")
    cov = load_covariance(which='STAT+SYS')

    for tag, label, mu_key in [
        ('A', 'MU_SH0ES (standard)', 'MU_SH0ES'),
        ('B', 'MU_UNCORRECTED (mass step reversed)', None),
    ]:
        print(f"\n{'='*65}")
        print(f"Version {tag}: {label}")
        print('='*65)

        if mu_key is None:
            df_ver = df.copy()
            df_ver['MU_UNCORRECTED'] = np.where(
                df_ver['HOST_LOGMASS'] > MASS_SPLIT,
                df_ver['MU_SH0ES'] + STEP_SIZE / 2,
                df_ver['MU_SH0ES'] - STEP_SIZE / 2
            )
            mu_key = 'MU_UNCORRECTED'
        else:
            df_ver = df

        res = group_chi2_analysis(df_ver, cov, mu_col=mu_key)

        for group, r in res.items():
            dchi = r['delta_chi2']
            winner = "Timescape" if dchi > 0 else "ΛCDM"
            print(f"\n  [{group}] n={r['n']}")
            print(f"    ΛCDM:       χ²={r['chi2_lcdm']:.1f}  χ²/ν={r['chi2_lcdm_red']:.3f}")
            print(f"    Timescape:  χ²={r['chi2_timescape']:.1f}  χ²/ν={r['chi2_timescape_red']:.3f}")
            print(f"    Δχ² = χ²_Λ − χ²_T = {dchi:+6.1f}  ({winner} wins)")

        # Store for summary
        if tag == 'A':
            res_a = res
        else:
            res_b = res

    print(f"\n{'='*65}")
    print("Summary: Δχ² = χ²_ΛCDM − χ²_Timescape")
    print(f"{'='*65}")
    print(f"{'Version':<30} {'Wall Δχ²':>12} {'Void Δχ²':>12}")
    print('-'*54)
    for tag, r in [('A (MU_SH0ES)', res_a), ('B (MU_UNCORRECTED)', res_b)]:
        print(f"{tag:<30} {r['Wall']['delta_chi2']:+12.1f} {r['Void']['delta_chi2']:+12.1f}")

    print(f"\nPrediction: Δχ²_void >> Δχ²_wall  (especially in Version B)")


if __name__ == '__main__':
    main()
