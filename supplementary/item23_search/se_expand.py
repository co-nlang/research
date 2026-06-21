#!/usr/bin/env python3
"""
THE LAST STEP, expanded and TESTED (not asserted): does the standard simplicial cup-1 of the
pulled-back extension cocycle, evaluated on the K5 3-cycle, reproduce N_anti / the per-tetra n_a?

Setup on the nerve partial-Delta^4 (5 Lagrangian vertices, edge (i,j) -> ray r_ij in V):
  c(x,y) = X_x . Z_y (mod 2)                         -- the extension/cup cocycle, [c]=omega
  self-rep pullback on a 2-face (i<j<k):  u(i,j,k) := c(r_ij, r_jk)   (Alexander-Whitney/bar)
  Steenrod simplicial cup-1 on an ordered tetra (0,1,2,3):
     (u cup_1 u)(0,1,2,3) = u(0,1,3) u(1,2,3) + u(0,2,3) u(0,1,2)

We compute, per K5 config:
  PRIMARY_m  = (u cup_1 u)(facet_m)                 facet_m = sorted(5 verts \ {m})
  sum_m PRIMARY_m   vs   N_anti mod 2               -- is the primary cup-1 sum the pairing?
  per-tetra PRIMARY_m vs (n_a)_m                    -- does it match cochain-wise?
  also the secondary candidate using the triangle-defects w_ijk = r_ij+r_jk+r_ik and q:
     SECpatch_m = PRIMARY_m XOR [correction], several candidates, let the computer pick.

This is "expand a known formula and check the algebra" -- with the computer doing the bookkeeping.
We report exactly what matches and what does not (science is the checking, not being right a priori).

Pure Python; reuses paper22/nerve_cochain.build.
"""
import sys
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def make_cq(N):
    MSK = (1 << N) - 1
    def Xv(v): return v & MSK
    def Zv(v): return (v >> N) & MSK
    def c(x, y): return bin(Xv(x) & Zv(y)).count('1') & 1     # X_x . Z_y
    def q(v): return bin(Xv(v) & Zv(v)).count('1') & 1        # diagonal X_v . Z_v
    return c, q

def run(N, n_lag, seeds, cap, budget=40):
    import time
    symp, gen, k5s, mu_triple = build(N); c, q = make_cq(N)
    t0 = time.time()
    res_primary_total = Counter()     # sum_m PRIMARY_m == N_anti ?
    res_primary_tetra = Counter()     # PRIMARY_m == (n_a)_m ?
    res_w_zero = Counter()            # triangle defects w_ijk == 0 (is f simplicial?)
    res_dfc_closed = Counter()        # delta(f#c)_m == 0 (is f#c a cocycle?)
    res_dfc_tetra = Counter()         # delta(f#c)_m == (n_a)_m ?
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(31000 + 13 * s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            # N_anti and per-tetra n_a
            na = []
            for m in range(5):
                t = [x for x in range(5) if x != m]; a, b, cc, d = t
                prs = [((a, b), (cc, d)), ((a, cc), (b, d)), ((a, d), (b, cc))]
                na.append(sum(1 for (p, r) in prs if symp(R(*p), R(*r))) & 1)
            Na = sum(na) & 1
            # is the self-rep map simplicial? -> all triangle defects w_ijk = 0 ?
            for (i, j, k) in combinations(range(5), 3):
                w = R(i, j) ^ R(j, k) ^ R(i, k)
                res_w_zero[w == 0] += 1
            # is f#c a 2-COCYCLE on the nerve? delta(f#c) on each facet:
            #   d(f#c)(0,1,2,3) = u(1,2,3)+u(0,2,3)+u(0,1,3)+u(0,1,2)
            primary = []; dfc = []
            for m in range(5):
                V = sorted(x for x in range(5) if x != m)        # [v0,v1,v2,v3]
                def u(i, j, k): return c(R(V[i], V[j]), R(V[j], V[k]))
                P = (u(0, 1, 3) & u(1, 2, 3)) ^ (u(0, 2, 3) & u(0, 1, 2))
                primary.append(P)
                d = u(1, 2, 3) ^ u(0, 2, 3) ^ u(0, 1, 3) ^ u(0, 1, 2)
                dfc.append(d)
                # triangle defects of this tetra and q-correction candidate
                wsum = 0
                for (i, j, k) in combinations(range(4), 3):
                    w = R(V[i], V[j]) ^ R(V[j], V[k]) ^ R(V[i], V[k])
                    wsum ^= q(w)
            # tallies
            for m in range(5):
                res_primary_tetra[primary[m] == na[m]] += 1
                res_dfc_closed[dfc[m] == 0] += 1           # f#c closed on facet m?
                res_dfc_tetra[dfc[m] == na[m]] += 1        # delta(f#c)_m == (n_a)_m?
            res_primary_total[(sum(primary) & 1) == Na] += 1
    def pct(cnt):
        t = cnt[True] + cnt[False]
        return f"{cnt[True]}/{t} ({100*cnt[True]//max(t,1)}%)"
    print(f"  n={N}:")
    print(f"    self-rep simplicial?  triangle defect w_ijk==0 : {pct(res_w_zero)}")
    print(f"    f#c closed on nerve?  delta(f#c)_m == 0        : {pct(res_dfc_closed)}")
    print(f"    PRIMARY cup1, TOTAL   sum_m P_m == N_anti      : {pct(res_primary_total)}")
    print(f"    PRIMARY cup1, TETRA   P_m     == (n_a)_m       : {pct(res_primary_tetra)}")
    print(f"    delta(f#c)_m == (n_a)_m  (defect candidate)    : {pct(res_dfc_tetra)}", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(4, 1200, 5, 1500)
    run(5, 3000, 6, 2500)
