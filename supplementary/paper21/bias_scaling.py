"""Scaling of the matching-parity bias with n (unbiased random sampler).

Leading-order theory (single-constraint uniform-foot lemma): each foot-bit has bias
1/(2^n-1).  Question: does the TRUE per-matching parity bias (all constraints, uniform
proper K4) also scale ~2^-n, i.e. is the equidistribution genuinely asymptotic?

For each N we sample proper K4 (4 mutually proper Lagrangians, 6 distinct rays) and
report the bias E[(-1)^Sigma] = 1 - 2 P(Sigma=1), plus the three term-biases
E[(-1)^{w(v_ab,v_cd)}].  Compare n=6 vs n=8.
"""
import random, time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def gen_lags(N, n_lag, budget, rng):
    symp, *_ = build(N)
    SZ = 1 << (2*N); ALL = list(range(1, SZ))
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
    return symp, lags

def measure(N, n_lag, budget, target_k4, seed):
    rng = random.Random(seed)
    symp, lags = gen_lags(N, n_lag, budget, rng)
    def ray(A, B):
        it = A & B
        return next(iter(it)) if len(it) == 1 else None
    # adjacency
    n = len(lags)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if len(lags[i] & lags[j]) == 1: adj[i].add(j); adj[j].add(i)
    sigpar = Counter(); term = [Counter(), Counter(), Counter()]; tot = 0
    for i in range(n):
        if tot >= target_k4: break
        for j in adj[i]:
            if j <= i: continue
            for k in (adj[i] & adj[j]):
                if k <= j: continue
                for l in (adj[i] & adj[j] & adj[k]):
                    if l <= k: continue
                    idx = (i, j, k, l)
                    r = {}
                    ok = True
                    for a in range(4):
                        for b in range(a+1, 4):
                            rr = ray(lags[idx[a]], lags[idx[b]])
                            if rr is None: ok = False; break
                            r[(a, b)] = rr
                        if not ok: break
                    if not ok or len(set(r.values())) != 6: continue
                    t0 = symp(r[(0, 1)], r[(2, 3)])
                    t1 = symp(r[(0, 2)], r[(1, 3)])
                    t2 = symp(r[(0, 3)], r[(1, 2)])
                    term[0][t0] += 1; term[1][t1] += 1; term[2][t2] += 1
                    sigpar[(t0 ^ t1 ^ t2)] += 1
                    tot += 1
                    if tot >= target_k4: break
                if tot >= target_k4: break
            if tot >= target_k4: break
    e, o = sigpar.get(0, 0), sigpar.get(1, 0)
    bias = (e - o) / tot if tot else 0
    print(f"  N={N}: {len(lags)} lags, {tot} proper K4")
    print(f"    P(Sigma=1)={o/tot:.4f}   bias E[(-1)^Sigma]={bias:+.4f}   "
          f"(1/(2^n-1)={1/(2**N-1):.4f})")
    for q in range(3):
        eo = term[q]; b = (eo.get(0,0)-eo.get(1,0))/tot
        print(f"    term{q} P(=1)={eo.get(1,0)/tot:.4f} bias={b:+.4f}", end="")
    print()

if __name__ == "__main__":
    print("=== matching-parity bias scaling (unbiased random sampler) ===")
    measure(6, n_lag=500, budget=60, target_k4=4000, seed=101)
    measure(8, n_lag=300, budget=240, target_k4=2000, seed=202)
