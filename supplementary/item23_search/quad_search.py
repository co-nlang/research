#!/usr/bin/env python3
"""
Item 23, parametrized correction search (collaborator's idea, done by F2 linear algebra).

Question: is the family-A cochain  a_T = (n_a)_T mod 2  on each tetrahedron T of the
nerve dDelta^4 expressible as a FIXED degree-<=2 F2-polynomial in T's face data
  { mu(f0..f3), F(f0..f3) }   (8 bits/T; F = Fano indicator [v+v+v=0]),
uniformly across all proper-K5 configurations?  This family (37 coeffs: 1 + 8 linear
+ 28 quadratic) contains the naive cup-1 (two of the mu*mu terms) AND Fano-weighted
corrections (the mu*F terms) -- exactly the "coherence-corrected cup-1" candidates.

Solve the F2 system  a_T = sum_i c_i B_i(T)  over (config x 5 tetrahedra) by Gaussian
elimination.  CONSISTENT => a formula exists in this family (segments 1&2 of item 23
done at sampled n); print it + uniqueness (kernel dim).  INCONSISTENT => the correction
is NOT degree-<=2 in (mu,F) -> needs richer data (defect vectors / beta / higher degree).

Also: class-level test  N_anti mod 2 = sum_T (poly)  (1 eqn/config), the weaker/bridge
form.  And a VALIDATION: at n=4 alone the cochain system must be consistent with the
known a = delta mu (Paper XX).

Pure Python (reuses paper22/nerve_cochain.build); no deps.
"""
import sys, time
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations

# ---- the 8 face-data bits per tetrahedron, and the 37 degree-<=2 monomials ----
# linear: 0..3 = mu(f0..f3), 4..7 = F(f0..f3).  Then const + 8 linear + 28 pairs.
PAIRS = list(combinations(range(8), 2))           # 28
NCOL = 1 + 8 + len(PAIRS)                          # 37
def monomials(bits):
    """bits = [m0..m3, F0..F3]; return the 37-bit feature vector (as int).
    column 0 = const(=1); columns 1..8 = the 8 linear; columns 9..36 = the 28 pairs."""
    f = 1                                          # bit0 = const = 1 always
    idx = 1
    for b in bits:                                 # 8 linear
        if b: f |= (1 << idx)
        idx += 1
    for (i, j) in PAIRS:                           # 28 quadratic
        if bits[i] and bits[j]: f |= (1 << idx)
        idx += 1
    return f

def faces_of(m):
    """tetrahedron opposite vertex m: its 4 triangular faces (drop each remaining vtx)."""
    rest = [x for x in range(5) if x != m]
    return [tuple(y for y in rest if y != d) for d in rest]   # 4 faces, canonical order

def gather(N, n_lag, seeds, cap_per_pool, time_budget):
    symp, gen, k5s, mu_triple = build(N)
    rows_cochain = []   # (feat, rhs) per (config, tetra)
    rows_class = []     # (feat_sum, rhs) per config
    t0 = time.time(); ncfg = 0
    for s in range(seeds):
        if time.time() - t0 > time_budget: break
        lags, adj = gen(4000 + 17*s, n_lag)
        for five, sh in k5s(lags, adj, cap_per_pool):
            ncfg += 1
            ray = {}
            for a in range(5):
                for b in range(a+1, 5): ray[(a, b)] = sh[(a, b)]
            def R(i, j): return ray[(i, j)] if i < j else ray[(j, i)]
            # mu and F on all 10 triangles
            mu = {}; F = {}
            for (a, b, c) in combinations(range(5), 3):
                mu[(a, b, c)] = mu_triple(five[a], five[b], five[c])
                F[(a, b, c)] = 1 if (R(a, b) ^ R(b, c) ^ R(a, c)) == 0 else 0
            # target a_m and N_anti
            a_cochain = []
            for m in range(5):
                rest = [x for x in range(5) if x != m]; aa, bb, cc, dd = rest
                prs = [((aa, bb), (cc, dd)), ((aa, cc), (bb, dd)), ((aa, dd), (bb, cc))]
                a_cochain.append(sum(1 for (p, q) in prs
                                     if symp(R(*p), R(*q))) & 1)
            Nanti = sum(a_cochain) & 1
            feat_sum = 0
            for m in range(5):
                fs = faces_of(m)
                bits = [mu[fs[0]], mu[fs[1]], mu[fs[2]], mu[fs[3]],
                        F[fs[0]],  F[fs[1]],  F[fs[2]],  F[fs[3]]]
                feat = monomials(bits)
                rows_cochain.append((feat, a_cochain[m]))
                feat_sum ^= feat
            rows_class.append((feat_sum, Nanti))
        if time.time() - t0 > time_budget: break
    return rows_cochain, rows_class, ncfg

def solve(rows, label):
    """F2 Gaussian elim of  M c = rhs ; report consistency, rank, kernel dim."""
    pivots = {}; inconsistent = 0; nrows = 0
    for (feat, rhs) in rows:
        nrows += 1
        f, r = feat, rhs
        while f:
            lb = f.bit_length() - 1
            if lb in pivots:
                pf, pr = pivots[lb]; f ^= pf; r ^= pr
            else:
                pivots[lb] = (f, r); break
        else:
            if r == 1: inconsistent += 1
    rank = len(pivots)
    print(f"  [{label}] rows={nrows}  feature-rank={rank}/{NCOL}  "
          f"kernel(free params)={NCOL - rank}  inconsistent-rows={inconsistent}")
    return inconsistent == 0, pivots, rank

def extract_solution(pivots):
    """back-substitute one particular solution c (int over 37 cols), if consistent."""
    c = 0
    for lb in sorted(pivots):
        pf, pr = pivots[lb]
        val = pr
        ff = pf & ~(1 << lb)
        while ff:
            b = ff.bit_length() - 1
            if (c >> b) & 1: val ^= 1
            ff &= ~(1 << b)
        if val: c |= (1 << lb)
    return c

def name_cols():
    names = ["1"]
    names += [f"mu{i}" for i in range(4)] + [f"F{i}" for i in range(4)]
    lin = ["mu0","mu1","mu2","mu3","F0","F1","F2","F3"]
    names += [f"{lin[i]}*{lin[j]}" for (i, j) in PAIRS]
    return names

if __name__ == "__main__":
    print(__doc__)
    print("="*70)
    print("VALIDATION: n=4 cochain system must be consistent (a = delta mu).")
    rc4, rk4, n4 = gather(4, 1500, 6, 1500, 50)
    ok4, piv4, _ = solve(rc4, f"n=4 cochain  (configs={n4})")
    if ok4:
        c = extract_solution(piv4); nm = name_cols()
        terms = [nm[i] for i in range(NCOL) if (c >> i) & 1]
        print(f"     n=4 solution: a_T = {' + '.join(terms)}")
    print("="*70)

    print("FULL SEARCH: pool n=4,5,6 together (cochain level).")
    rc, rcl, ncfg = [], [], {}
    for N, nl, sd, cp, tb in [(4,1500,4,1200,40),(5,3000,8,2000,90),(6,2500,5,1500,70)]:
        a, b, k = gather(N, nl, sd, cp, tb); rc += a; rcl += b; ncfg[N] = k
    print(f"  configs gathered: {ncfg}")
    ok, piv, rank = solve(rc, "ALL cochain")
    if ok:
        c = extract_solution(piv); nm = name_cols()
        terms = [nm[i] for i in range(NCOL) if (c >> i) & 1]
        print(f"  *** FOUND cochain formula: a_T = {' + '.join(terms)} ***")
    else:
        print("  cochain level: NO degree-<=2 (mu,F) formula (correction is richer).")
    print("-"*70)
    print("CLASS LEVEL: N_anti mod 2 = sum_T (degree-<=2 poly).")
    okc, pivc, rankc = solve(rcl, "ALL class")
    if okc:
        c = extract_solution(pivc); nm = name_cols()
        terms = [nm[i] for i in range(NCOL) if (c >> i) & 1]
        print(f"  *** FOUND class formula: N_anti = sum_T [ {' + '.join(terms)} ] ***")
    else:
        print("  class level: NO degree-<=2 (mu,F) formula either.")
