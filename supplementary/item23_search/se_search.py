#!/usr/bin/env python3
"""
The self-rep map is NEVER simplicial (w_ijk = r_ij+r_jk+r_ik != 0 always, se_expand.py), so f#c is
not closed and the naive functional-Sq1 expansion does not apply on the nerve. BUT the 2-cell
defects w_ijk are explicit vectors -- a coherent (lax) lift assigns them, and the resulting
secondary 3-cocycle should be an explicit formula in (rays, defects). This searches for it.

We need a per-tetrahedron correction  CORR_m := (n_a)_m XOR PRIMARY_m  (PRIMARY = simplicial cup_1
of f#c) expressed as an F_2-linear combination of NON-circular defect terms -- terms involving the
2-cell defects w (pure-ray symplectic terms are circular: they ARE n_a, phi_omega_zero.py). Basis:
  const, q(r_e) [6 edges], q(w_f) [4 faces], c(w_f,w_g) ordered [12], omega(w_f,w_g) [6].
Solve CORR_m = sum_i coeff_i * B_i(rays,defects) over (config x 5 tetra) by F_2 Gaussian elimination.
  consistent  -> explicit secondary formula FOUND & VERIFIED (the Steenrod-Epstein expansion, in
                 the only data that can carry it: the coherent-lift defects);
  inconsistent-> the correction is NOT a function of these defect data => the bridge content lives
                 in higher coherence (genuinely the cited d_3 transgression), not a finite formula.

Either way is a real, honest result. Pure Python; reuses paper22/nerve_cochain.build.
"""
import sys, time
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations

def make_cq(N):
    MSK = (1 << N) - 1
    def Xv(v): return v & MSK
    def Zv(v): return (v >> N) & MSK
    def c(x, y): return bin(Xv(x) & Zv(y)).count('1') & 1
    def q(v): return bin(Xv(v) & Zv(v)).count('1') & 1
    return c, q

def run(N, n_lag, seeds, cap, budget=45, allow_ray_defect=False):
    symp, gen, k5s, mu = build(N); c, q = make_cq(N)
    rows = []   # each: (bitmask of basis terms that are 1, rhs)
    nterms = [0]
    t0 = time.time()
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(41000 + 17 * s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            for m in range(5):
                Vt = sorted(x for x in range(5) if x != m)        # 4 verts
                edges = list(combinations(range(4), 2))           # 6 local edge-pairs
                rr = {e: R(Vt[e[0]], Vt[e[1]]) for e in edges}
                faces = list(combinations(range(4), 3))           # 4 faces
                ww = {f: R(Vt[f[0]], Vt[f[1]]) ^ R(Vt[f[1]], Vt[f[2]]) ^ R(Vt[f[0]], Vt[f[2]])
                      for f in faces}
                # n_a (target)
                a, b, cc, d = 0, 1, 2, 3
                prs = [((a, b), (cc, d)), ((a, cc), (b, d)), ((a, d), (b, cc))]
                na = sum(1 for (p, r) in prs if symp(rr[p], rr[r])) & 1
                # PRIMARY simplicial cup_1 of f#c on (0,1,2,3)
                def u(i, j, k): return c(R(Vt[i], Vt[j]), R(Vt[j], Vt[k]))
                P = (u(0, 1, 3) & u(1, 2, 3)) ^ (u(0, 2, 3) & u(0, 1, 2))
                corr = na ^ P
                # build basis vector
                terms = [1]                                       # const
                terms += [q(rr[e]) for e in edges]                # 6
                terms += [q(ww[f]) for f in faces]                # 4
                fl = list(faces)
                terms += [c(ww[fl[i]], ww[fl[j]]) for i in range(4) for j in range(4) if i != j]  # 12 ordered
                terms += [symp(ww[fl[i]], ww[fl[j]]) for i in range(4) for j in range(i+1, 4)]    # 6
                if allow_ray_defect:   # (circular-risk) ray<->defect symplectic cross terms
                    terms += [symp(rr[e], ww[f]) for e in edges for f in faces]                    # 24
                nterms[0] = len(terms)
                mask = 0
                for i, b_ in enumerate(terms):
                    if b_ & 1: mask |= (1 << i)
                rows.append((mask, corr))
    # F_2 Gaussian elimination with consistency check (augmented bit at position NT)
    NT = nterms[0]; pivots = {}; bad = 0; nrows = len(rows)
    for (mask, rhs) in rows:
        cur = mask | (rhs << NT)
        for col, prow in pivots.items():
            if (cur >> col) & 1: cur ^= prow
        body = cur & ((1 << NT) - 1)
        if body == 0:
            if (cur >> NT) & 1: bad += 1
            continue
        col = (body & -body).bit_length() - 1
        for pc in list(pivots):
            if (pivots[pc] >> col) & 1: pivots[pc] ^= cur
        pivots[col] = cur
    tag = "+ray-defect" if allow_ray_defect else "defect-only"
    print(f"  n={N} [{tag}]: rows={nrows}, basis={NT}, rank={len(pivots)}, "
          f"contradictory rows={bad}  ->  {'CONSISTENT (formula found)' if bad == 0 else 'INCONSISTENT'}",
          flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(4, 1200, 4, 1500, allow_ray_defect=False)
    run(5, 3000, 5, 2500, allow_ray_defect=False)
    print("  --- allowing ray<->defect cross terms (circular-risk, only to see if they help): ---")
    run(4, 1200, 4, 1500, allow_ray_defect=True)
    run(5, 3000, 5, 2500, allow_ray_defect=True)
