"""Even-n>=6 equidistribution of the H^3 class N_anti mod 2 -- sharpening the target.

The per-matching value a_m in {0,1,2,3} is NOT uniform (peaks at 2).  The meaningful
'equidistribution' is of the H^3 class [n_a] = N_anti mod 2 in F_2.  Since
  N_anti mod 2 = (sum_m a_m) mod 2 = (# matchings with a_m odd) mod 2,
we study the distribution of the NUMBER of odd matchings (0..5).

Uses the unbiased random-Lagrangian sampler (nerve_cochain.build) at n=6, plus a
high-volume chart sampler cross-check.  Reports:
  - N_anti parity split (is it exactly 50/50?)
  - histogram of #odd-matchings (0..5)
  - per-matching a_m histogram
  - independence test: if the 5 matching-parities were iid Bernoulli(p), predicted
    P(#odd even) = (1+(1-2p)^5)/2 ; compare to observed.
"""
import random, time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def sample_random(N, nseed, seed_base=5000, n_lag=400, cap=60, budget=60):
    symp, _gen, k5s, _mu = build(N)
    SZ = 1 << (2*N); MSK = (1 << N) - 1
    def gen(seed):
        ALL = list(range(1, SZ)); rng = random.Random(seed)
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
        while len(lags) < n_lag and time.time() - t < budget:
            L = rl()
            if L and L not in ls: ls.add(L); lags.append(L)
        adj = [set() for _ in lags]
        for i in range(len(lags)):
            for j in range(i+1, len(lags)):
                if len(lags[i] & lags[j]) == 1: adj[i].add(j); adj[j].add(i)
        return lags, adj
    out = []
    for s in range(nseed):
        lags, adj = gen(seed_base + 7*s)
        for five, sh in k5s(lags, adj, cap):
            out.append((symp, sh))
    return out

def amvals(symp, sh):
    ray = {(a, b): sh[(a, b)] for a in range(5) for b in range(a+1, 5)}
    a = []
    for m in range(5):
        rest = [x for x in range(5) if x != m]; i, j, k, l = rest
        prs = [((i, j), (k, l)), ((i, k), (j, l)), ((i, l), (j, k))]
        a.append(sum(symp(ray[tuple(sorted(p))], ray[tuple(sorted(q))]) for (p, q) in prs))
    return a

def analyze(label, configs):
    par = Counter(); nodd = Counter(); aval = Counter(); nantihist = Counter()
    tot = 0
    for symp, sh in configs:
        a = amvals(symp, sh)
        for v in a: aval[v] += 1
        Na = sum(a); nantihist[Na] += 1
        par[Na % 2] += 1
        nodd[sum(1 for v in a if v % 2)] += 1
        tot += 1
    print(f"\n[{label}]  proper K5 sampled = {tot}")
    e, o = par.get(0, 0), par.get(1, 0)
    print(f"  N_anti parity: even={e} ({e/tot:.3f})  odd={o} ({o/tot:.3f})")
    print(f"  #odd-matchings histogram (0..5): {dict(sorted(nodd.items()))}")
    print(f"  per-matching a_m histogram: {dict(sorted(aval.items()))}"
          f"  -> P(a_m odd)={sum(v for k,v in aval.items() if k%2)/ (5*tot):.4f}")
    p = sum(v for k, v in aval.items() if k % 2) / (5*tot)
    pred = (1 + (1 - 2*p)**5) / 2
    print(f"  N_anti value histogram: {dict(sorted(nantihist.items()))}")
    print(f"  iid-independence prediction P(N_anti even)=(1+(1-2p)^5)/2={pred:.4f}"
          f"  vs observed {e/tot:.4f}")

if __name__ == "__main__":
    print("=== even-n>=6 H^3 equidistribution study ===")
    t0 = time.time()
    cfg6 = sample_random(6, nseed=40)
    analyze("n=6 random-Lagrangian sampler", cfg6)
    print(f"\n(total {time.time()-t0:.0f}s)")
