"""Paper XX -> XXI seed: does the n=4 rigidity recur at n=6?

We already PROVED (Thm rank-parity) that mu==1 for all proper triples at every
even n, so Part B (delta mu == 0) holds automatically at n=6.  The ONLY open
question for n=6 rigidity is Part A: is n_m even for every matching?

If Part A holds at n=6 -> n == delta mu == 0 -> N_anti even universally at n=6
-> "even n rigid, odd n>=5 modulus" PERIODICITY law (refines XX's "opens at
n>=5").  This script tests Part A (and re-confirms Part B) at n=6.
"""
import time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def experiment6(N, n_lag, max_k5, nseed, gen_budget=90):
    symp, _gen, k5s, mu_triple = build(N)

    # rebuild gen with a larger per-seed time budget (Sp(12) is sparser)
    import random
    SZ = 1 << (2*N)
    def gen(seed, nl):
        ALL = list(range(1, SZ)); rng = random.Random(seed)
        MSK = (1 << N) - 1
        def xspan(b):
            s = {0}
            for x in b: s |= {y ^ x for y in s}
            return s
        def rl():
            b = []; sp = {0}
            for _ in range(N):
                c = [v for v in ALL if v not in sp and all(symp(v, x) == 0 for x in b)]
                if not c: return None
                v = rng.choice(c); b.append(v); sp = xspan(b)
            return frozenset(x for x in sp if x)
        lags = []; ls = set(); t = time.time()
        while len(lags) < nl and time.time() - t < gen_budget:
            L = rl()
            if L and L not in ls: ls.add(L); lags.append(L)
        adj = [set() for _ in lags]
        for i in range(len(lags)):
            for j in range(i+1, len(lags)):
                if len(lags[i] & lags[j]) == 1: adj[i].add(j); adj[j].add(i)
        return lags, adj

    nanti_parity = Counter(); na_eq_dmu = 0; tot = 0
    mu_all_one = 0; na_dist = Counter(); nanti_vals = Counter()
    t0 = time.time()
    for s in range(nseed):
        lags, adj = gen(2000 + 11*s, n_lag)
        for five, sh in k5s(lags, adj, max_k5):
            tot += 1
            ray = {(a, b): sh[(a, b)] for a in range(5) for b in range(a+1, 5)}
            na = []
            for m in range(5):
                rest = [x for x in range(5) if x != m]; a, b, c, dd = rest
                prs = [((a, b), (c, dd)), ((a, c), (b, dd)), ((a, dd), (b, c))]
                na.append(sum(1 for (p, q) in prs
                              if symp(ray[tuple(sorted(p))], ray[tuple(sorted(q))])))
            for v in na: na_dist[v] += 1
            Nanti = sum(na); nanti_parity[Nanti % 2] += 1; nanti_vals[Nanti] += 1
            mu = {t: mu_triple(five[t[0]], five[t[1]], five[t[2]])
                  for t in combinations(range(5), 3)}
            if all(v == 1 for v in mu.values()): mu_all_one += 1
            dmu = []
            for m in range(5):
                rest = tuple(x for x in range(5) if x != m)
                dmu.append(sum(mu[f] for f in combinations(rest, 3)) % 2)
            if all((na[m] % 2) == dmu[m] for m in range(5)): na_eq_dmu += 1
    print(f"  n={N}: proper K5 sampled = {tot}  ({time.time()-t0:.0f}s)")
    print(f"    mu == 1 on all 10 triples (Part B check): {mu_all_one}/{tot}")
    print(f"    per-matching na value distribution: {dict(sorted(na_dist.items()))}")
    print(f"    N_anti value distribution: {dict(sorted(nanti_vals.items()))}")
    print(f"    N_anti parity (0=even,1=odd): {dict(nanti_parity)}")
    print(f"    na_m == (delta mu)_m for all m: {na_eq_dmu}/{tot}")
    print(f"    => Part A (n_m even per matching) holds: "
          f"{'YES' if set(na_dist) <= {0,2} else 'NO (odd na_m present)'}")

if __name__ == "__main__":
    print("=== n=6 periodicity test: does the n=4 rigidity recur at n=6? ===")
    experiment6(6, n_lag=400, max_k5=40, nseed=8)
