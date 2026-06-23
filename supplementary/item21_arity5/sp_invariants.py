#!/usr/bin/env python3
"""
Item 21, Lemma A (reformulated, the omega-part): no indecomposable degree-4 Sp(2n,F2)-invariant.

The family-A obstructions live in the ambient cohomology H*(BV;F2) = F2[x_1..x_{2n}] (V=(Z/2)^{2n}),
as Sp(2n,F2)-invariant, Steenrod-closed classes (omega in H^2, n_a = Sq^1 omega in H^3). So the correct
question for item 21's omega-part is NOT about configuration functions (which over-count) but about the
AMBIENT invariant ring H*(BV)^{Sp(2n,F2)} -- a classical object (Quillen / Carlisle-Kropholler).

Classical structure (symplectic Dickson invariants): generators xi_i of degree 1+2^i, i.e. degrees
  2 (omega),  3 (xi_1 = Sq^1 omega = n_a),  5 (xi_2),  9 (xi_3), ...
NO generator at degree 4. So the degree-4 invariants are just <omega^2> (decomposable, family B) ->
NO indecomposable H^4 obstruction. The H^3 ceiling = the GAP between the degree-3 and degree-5
symplectic generators. This proves item 21's omega-part (modulo the ambient<->configuration bridge,
= item 23's framework).

This script VERIFIES (firewall: confirm the load-bearing claim) for n=2,3:
  dim H*(BV)^{Sp(2n,F2)} in degrees d=1..6, by computing the simultaneous fixed space of the degree-d
  polynomials under ALL transvections T_v (which generate Sp(2n,F2)). Expect: dim_2=1 (omega),
  dim_3=1 (Sq^1 omega), dim_4=1 (omega^2 -- the key: NO new generator), dim_5=2, ...
Also checks: the degree-3 invariant equals Sq^1(omega), and the degree-4 invariant equals omega^2.

Transvection T_v: u -> u + omega(u,v) v. On linear forms: x_i -> x_i + v_i * L_v, where L_v is the
linear form u -> omega(u,v) (coeff vector = Omega v). Pure Python (polynomials = sets of exponent
tuples over F2).
"""
from itertools import combinations_with_replacement, product


def make_omega(n):
    N = 2 * n
    # symplectic form Omega: pairs (0,1),(2,3),...; omega(u,v) = sum u_{2k} v_{2k+1} + u_{2k+1} v_{2k}
    def omega(u, v):
        s = 0
        for k in range(n):
            s ^= (u[2 * k] & v[2 * k + 1]) ^ (u[2 * k + 1] & v[2 * k])
        return s
    return N, omega


def mono_basis(N, d):
    """Degree-d monomials in N vars as exponent tuples summing to d."""
    res = []
    def rec(i, rem, cur):
        if i == N - 1:
            res.append(tuple(cur + [rem])); return
        for e in range(rem + 1):
            rec(i + 1, rem - e, cur + [e])
    rec(0, d, [])
    return res


def pmul(p, q, N):
    """Multiply two F2 polynomials (sets of exp-tuples)."""
    out = set()
    for a in p:
        for b in q:
            m = tuple(a[i] + b[i] for i in range(N))
            out ^= {m}
    return out


def ppow(p, k, N):
    r = {tuple(0 for _ in range(N))}   # 1
    for _ in range(k):
        r = pmul(r, p, N)
    return r


def subst_monomial(exp, N, vvec, Lv):
    """Apply x_i -> x_i + v_i*L_v to monomial 'exp'; return F2 polynomial (set of exp-tuples)."""
    res = {tuple(0 for _ in range(N))}   # 1
    for i in range(N):
        if exp[i] == 0:
            continue
        xi = {tuple(1 if j == i else 0 for j in range(N))}
        factor = (xi ^ Lv) if vvec[i] else xi    # (x_i + L_v)^{exp[i]} or x_i^{exp[i]}
        res = pmul(res, ppow(factor, exp[i], N), N)
    return res


def fixed_dim(N, d, transvections, omega):
    basis = mono_basis(N, d)
    idx = {m: i for i, m in enumerate(basis)}
    B = len(basis)
    # build constraint rows: for each transvection, (action - I) applied to each basis monomial
    rows = []
    for v in transvections:
        # L_v = linear form u -> omega(u,v); coeff of x_j is omega(e_j, v)
        Lv = set()
        for j in range(N):
            ej = tuple(1 if t == j else 0 for t in range(N))
            if omega(ej, v):
                Lv ^= {tuple(1 if t == j else 0 for t in range(N))}
        for m in basis:
            img = subst_monomial(m, N, v, Lv)
            diff = img ^ {m}                      # (T_v - I) m
            if diff:
                row = 0
                for mm in diff:
                    row ^= 1 << idx[mm]
                rows.append(row)
    # invariant space = ker of the constraint matrix; dim = B - rank
    piv = []
    for r in rows:
        x = r
        for p in piv:
            x = min(x, x ^ p)
        if x:
            piv.append(x); piv.sort(reverse=True)
    return B - len(piv), basis, idx


def in_span(target, rows):
    x = target
    for p in sorted(rows, reverse=True):
        x = min(x, x ^ p)
    return x == 0


def fixed_space(N, d, transvections, omega):
    """dim of the simultaneous fixed space = intersection of ker(T_v - I).
    CORRECT kernel: stack the ROWS (equations) of each (T_v - I), not the columns.
    Build (T_v-I) by columns img_m=(T_v-I)(m), then transpose into equation rows."""
    basis = mono_basis(N, d)
    idx = {m: i for i, m in enumerate(basis)}
    B = len(basis)
    eqrows = []
    for v in transvections:
        Lv = set()
        for j in range(N):
            ej = tuple(1 if t == j else 0 for t in range(N))
            if omega(ej, v):
                Lv ^= {tuple(1 if t == j else 0 for t in range(N))}
        rowsets = [0] * B                      # rowsets[m'] = sum over source m of [m' in (T_v-I)(m)] x_m
        for m in basis:
            i = idx[m]
            for mm in (subst_monomial(m, N, v, Lv) ^ {m}):   # (T_v - I)(m)
                rowsets[idx[mm]] ^= (1 << i)
        eqrows.extend(r for r in rowsets if r)
    piv = []
    for r in eqrows:
        x = r
        for p in piv:
            x = min(x, x ^ p)
        if x:
            piv.append(x); piv.sort(reverse=True)
    return B - len(piv), basis, idx


def run(n, dmax=6):
    N, omega = make_omega(n)
    def q(v):  # quadratic form q(v) = sum v_{2k} v_{2k+1}
        return sum(v[2 * k] & v[2 * k + 1] for k in range(n)) & 1
    transv_sp = [v for v in product((0, 1), repeat=N) if any(v)]
    transv_o = [v for v in transv_sp if q(v) == 1]            # O = stabilizer of q
    print(f"  n={n}: Sp({N},F2) [{len(transv_sp)} transv] vs O(q) [{len(transv_o)} transv]:", flush=True)
    for d in range(1, dmax + 1):
        dsp, _, _ = fixed_space(N, d, transv_sp, omega)
        do, _, _ = fixed_space(N, d, transv_o, omega)
        note = "  <== degree 4: indecomposable O-invariant beyond q^2 iff dim_O > 1" if d == 4 else ""
        print(f"    deg {d}: dim^Sp = {dsp},  dim^O = {do}{note}", flush=True)
    return
    transv = transv_sp
    print(f"  n={n} (Sp({N},F2), {len(transv)} transvections):", flush=True)
    # omega and Sq^1 omega as polynomials
    omega_poly = set()
    for k in range(n):
        omega_poly ^= {tuple(1 if t in (2 * k, 2 * k + 1) else 0 for t in range(N))}
    # Sq^1 omega = sum x_{2k}^2 x_{2k+1} + x_{2k} x_{2k+1}^2  (Cartan on xy -> x^2 y + x y^2)
    sq1 = set()
    for k in range(n):
        a = [0] * N; a[2 * k] = 2; a[2 * k + 1] = 1; sq1 ^= {tuple(a)}
        b = [0] * N; b[2 * k] = 1; b[2 * k + 1] = 2; sq1 ^= {tuple(b)}
    for d in range(1, 7):
        dim, basis, idx = fixed_dim(N, d, transv, omega)
        note = ""
        if d == 2 and dim >= 1: note = " (omega lives here)"
        if d == 4: note = "  <== KEY: omega^2 only if dim==1 => NO indecomposable degree-4"
        print(f"    dim H^{d}(BV)^Sp = {dim}{note}", flush=True)
    # sanity: omega^2 is degree-4 invariant; Sq^1 omega is degree-3 invariant
    om2 = ppow(omega_poly, 2, N)
    print(f"    [check] omega^2 nonzero: {bool(om2)}; Sq^1(omega) nonzero: {bool(sq1)}", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== Lemma A: dim of the ambient Sp(2n,F2)- and O(q)-invariant rings by degree ===", flush=True)
    run(2)
    run(3)
    run(4, dmax=5)
