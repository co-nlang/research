#!/usr/bin/env python3
"""
Decisive test behind quad_search's negative: is the family-A cochain
  a_m = (n_a)_m mod 2   (per tetrahedron)
DETERMINED by the full Maslov+Fano data (mu, F on all 10 triangles) at all?

If two proper-K5 configs share identical (mu, F) but differ in a, then a is NOT any
function of (mu,F) -- of ANY degree -- so the entire "(mu,F)-polynomial correction"
family (quad_search.py, the parametrized cup-1 idea) is ruled out wholesale, not just
at degree 2.

Result (sampled): YES, collisions abound.
  n=5: among ~430 distinct (mu,F)-keys, ~123 carry >1 distinct a (e.g. same (mu,F)
       gives both a=(0,0,0,0,0) and (1,0,0,0,0)).
  n=6: even n forces mu==1 everywhere and F constant -> a SINGLE (mu,F)-key, yet a
       ranges over all 32 values. (mu,F) is totally blind to the family-A class here.

Interpretation: this is the arity gap. a is intrinsically arity-4 (anticommutation of
ray PAIRS); mu and F are arity-3 (triangle data). The resonance separation H^2(K4) vs
H^3(K5) is exactly the statement that the arity-4 class is irreducible to arity-3 data
-- so no (mu,F) formula can produce a. The collision test is an empirical shadow of
Paper XIX's modulus (arity-<=k invariants do not classify the H^3 fiber).

Pure Python (reuses paper22/nerve_cochain.build); no deps.
"""
import sys, time
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import defaultdict

def run(N, n_lag, seeds, cap, budget):
    symp, gen, k5s, mu_triple = build(N)
    table = defaultdict(set)            # (mu-vec, F-vec) -> set of a-vecs
    t0 = time.time(); ncfg = 0
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(7000 + 11*s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            ncfg += 1
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            tri = list(combinations(range(5), 3))
            mu = tuple(mu_triple(five[a], five[b], five[c]) for (a, b, c) in tri)
            F  = tuple(1 if (R(a, b) ^ R(b, c) ^ R(a, c)) == 0 else 0 for (a, b, c) in tri)
            a = []
            for m in range(5):
                rest = [x for x in range(5) if x != m]; aa, bb, cc, dd = rest
                prs = [((aa, bb), (cc, dd)), ((aa, cc), (bb, dd)), ((aa, dd), (bb, cc))]
                a.append(sum(1 for (p, q) in prs if symp(R(*p), R(*q))) & 1)
            table[(mu, F)].add(tuple(a))
        if time.time() - t0 > budget: break
    collisions = [(k, v) for k, v in table.items() if len(v) > 1]
    print(f"  n={N}: configs={ncfg}, distinct (mu,F)-keys={len(table)}, "
          f"keys with >1 distinct a = {len(collisions)}")
    if collisions:
        k, v = max(collisions, key=lambda kv: len(kv[1]))
        print(f"    collision (same (mu,F), #distinct a = {len(v)}); e.g. {sorted(v)[:3]}...")
        print(f"    => a is NOT a function of (mu,F) at ANY degree; (mu,F) family ruled out.")
    else:
        print(f"    no collision on this sample.")

if __name__ == "__main__":
    print(__doc__)
    print("Decisive (mu,F)-determinacy test for the family-A cochain a:")
    for N, nl, sd, cp, bd in [(5, 3000, 8, 2500, 80), (6, 2500, 5, 1800, 70)]:
        run(N, nl, sd, cp, bd)
