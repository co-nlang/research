#!/usr/bin/env python3
"""
The chase's terminus: WHY no symplectic-pairing formula for a exists (it's circular).

On the nerve, a COMPOSABLE pairing omega(v_ij, v_jk) pairs two rays that both lie in the
shared Lagrangian L_j -- so they COMMUTE and the pairing VANISHES.  Verified: every
composable pairing is 0 (0/933000 across n=4,5,6).  Consequences:

  (1) phi*omega == 0 at the COCHAIN level (not just the class).  So the family-A pullback
      a = Sq^1 omega has NO primary part -- it is a PURELY secondary operation, the
      strongest possible form of "the bridge is secondary/lax".
  (2) The ONLY nonzero symplectic pairings on the nerve are the DISJOINT ones
      omega(v_ij, v_kl), {i,j} cap {k,l} = empty -- and their sum over matchings IS a.
      Defect pairings reduce to these too: omega(w_ijk, v_il) = omega(v_jk, v_il) (a
      disjoint pairing), since the same-Lagrangian terms vanish.  So every symplectic
      expression in the rays/defects is a linear combination of the disjoint pairings =
      a itself.  => ANY "formula for a in the symplectic pairing data" is CIRCULAR.

So the parametrized-search program cannot produce a non-trivial bridge over symplectic
data: there is no "lower" symplectic datum to build a from.  The bridge content is NOT a
pairing-identity; it is the topological assembly of the defects into the universal class
Sq^1 omega -- i.e. the lax/A_inf map (the genuine insight-bound pitch).

The one nonzero "lower" datum that is NOT a symplectic pairing: the polarized cocycle
f(v_ij, v_jk) (the quadratic refinement q / Z4 structure), which is nonzero even on
commuting pairs.  But cup-1 of it matches a only ~74%/61% (n=4/n=5; see the confounded
b_f rows), so the correct object is the Z/4-BOCKSTEIN of q (Sq^1 omega = beta_{Z/4}),
not cup-1 -- a convention-heavy chain-level computation = the identified next step.

This script verifies (1): composable pairings all vanish; and shows the earlier
"b_omega cup_1" match% equals the a==0 frequency (confounded).  Pure Python; no deps.
"""
import sys, time
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def run(N, n_lag, seeds, cap, budget):
    symp, gen, k5s, mu_triple = build(N)
    comp_nz = 0; comp_tot = 0; a0 = Counter(); tot = 0; t0 = time.time()
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(9000 + 11*s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            for (i, j, k) in combinations(range(5), 3):
                for (p, q) in [((i, j), (j, k)), ((i, j), (i, k)), ((i, k), (j, k))]:
                    comp_tot += 1; comp_nz += symp(R(*p), R(*q))
            for m in range(5):
                t = [x for x in range(5) if x != m]; a, b, c, d = t
                prs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
                av = sum(1 for (p, q) in prs if symp(R(*p), R(*q))) & 1
                a0[av == 0] += 1; tot += 1
        if time.time() - t0 > budget: break
    print(f"  n={N}: composable pairings nonzero = {comp_nz}/{comp_tot}  "
          f"(phi*omega == 0 at cochain level: {comp_nz == 0})")
    print(f"         per-tetra a==0 frequency = {100*a0[True]/tot:.1f}%  "
          f"(= the earlier 'b_omega cup1' match% -> that test was confounded)")

if __name__ == "__main__":
    print(__doc__)
    print("Composable pairings vanish? (=> phi*omega==0; symplectic formula-search circular)")
    for N, nl, sd, cp, bd in [(4,1500,5,1500,40),(5,3000,8,2500,80),(6,2500,5,1800,60)]:
        run(N, nl, sd, cp, bd)
