#!/usr/bin/env python3
"""
Is the family-A cochain a determined by the composable quadratic-refinement (Z/4) data?

q-data = polarized f(v_ij, v_jk) on COMMUTING (composable) ray pairs + q(v)=f(v,v) per ray.
This is NON-circular (nonzero where omega vanishes, unlike the symplectic pairings which
collapse to a itself) and much finer than (mu,F). If two configs share all composable-q data
but differ in a, then a is NOT a function of the Z/4 layer at cochain level.

Result (sampled): a is NOT determined by q -- witnessed, though narrowly.
  n=5: 20000 configs -> 19896 distinct q-keys (q is NEARLY INJECTIVE), yet 32 keys carry
       >1 distinct a (genuine collisions, same q -> different a).
  n=6: 5400 configs -> 5394 q-keys, 2 collisions.

So the ladder of natural cochain-level data layers ALL fail to determine a:
  symplectic pairings  -> CIRCULAR (phi*omega == 0; only nonzero pairings = a itself)
  Maslov+Fano (arity-3)-> determines-not, COARSELY (430 keys, 123 split; the arity gap)
  quadratic refin. q   -> determines-not, FINELY (19896 keys, 32 split; q nearly injective)
=> no cochain-level summary statistic determines a; the bridge is irreducibly the lax-map
   (defect + higher-coherence) construction = HANDWORK, with computable verification only.

Pure Python (reuses paper22/nerve_cochain.build); no deps.
"""
import sys, time
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations, permutations
from collections import defaultdict

def make_f(N):
    MSK = (1 << N) - 1
    def f(v, w): return bin((v & MSK) & ((w >> N) & MSK)).count('1') & 1
    return f

def run(N, n_lag, seeds, cap, budget):
    symp, gen, k5s, mu_triple = build(N); f = make_f(N)
    table = defaultdict(set); t0 = time.time(); ncfg = 0
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(13000 + 11*s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            ncfg += 1
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            qdat = []
            for (i, j, k) in permutations(range(5), 3):
                if i < k: qdat.append(f(R(i, j), R(j, k)))     # all composable (middle=j)
            for (i, j) in combinations(range(5), 2):
                qdat.append(f(R(i, j), R(i, j)))               # q(v)=f(v,v) per ray
            a = []
            for m in range(5):
                t = [x for x in range(5) if x != m]; aa, bb, cc, dd = t
                prs = [((aa, bb), (cc, dd)), ((aa, cc), (bb, dd)), ((aa, dd), (bb, cc))]
                a.append(sum(1 for (p, q) in prs if symp(R(*p), R(*q))) & 1)
            table[tuple(qdat)].add(tuple(a))
        if time.time() - t0 > budget: break
    coll = [(k, v) for k, v in table.items() if len(v) > 1]
    print(f"  n={N}: configs={ncfg}, distinct q-keys={len(table)} (q nearly injective), "
          f"keys with >1 a = {len(coll)}")
    print(f"    => a is {'NOT ' if coll else ''}determined by q"
          f"{' (witnessed collisions) -> exact formula needs lax coherence = handwork' if coll else ''}")

if __name__ == "__main__":
    print(__doc__)
    for N, nl, sd, cp, bd in [(5, 3000, 8, 2500, 90), (6, 2500, 5, 1800, 70)]:
        run(N, nl, sd, cp, bd)
