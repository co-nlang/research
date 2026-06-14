"""Localising the even-n>=6 matching-parity balance: the L_4 fiber.

Reduction: the H^3 class N_anti mod 2 is 50/50 iff each matching parity
  Sigma = w(v12,v34)+w(v13,v24)+w(v14,v23)   (proper K4 on {1,2,3,4})
is an unbiased bit.  Sigma depends on the 6 rays of the K4.  Fix a proper K3
(L1,L2,L3); as the 4th Lagrangian L4 ranges over completions to a proper K4,
how is Sigma distributed?  If it is 50/50 *within each fiber*, an involution on
the L4-fiber is the mechanism.
"""
import random, time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def fiber_study(N, n_lag=700, nbase=12, budget=70, seed=314):
    symp, _gen, _k5s, _mu = build(N)
    SZ = 1 << (2*N)
    def gen(sd):
        ALL = list(range(1, SZ)); rng = random.Random(sd)
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
        return lags
    def ray(A, B):
        it = A & B
        return next(iter(it)) if len(it) == 1 else None

    lags = gen(seed)
    print(f"  N={N}: generated {len(lags)} Lagrangians")
    # find base proper K3s (triples pairwise dim-1, distinct rays)
    fiber_hist = []          # per-base Sigma counts
    agg = Counter()
    bases_done = 0
    for (i, j, k) in combinations(range(len(lags)), 3):
        if bases_done >= nbase: break
        L1, L2, L3 = lags[i], lags[j], lags[k]
        r12, r13, r23 = ray(L1, L2), ray(L1, L3), ray(L2, L3)
        if None in (r12, r13, r23): continue
        if len({r12, r13, r23}) != 3: continue
        # collect all L4 completing to a proper K4
        cnt = Counter()
        for L4 in lags:
            if L4 in (L1, L2, L3): continue
            r14, r24, r34 = ray(L1, L4), ray(L2, L4), ray(L3, L4)
            if None in (r14, r24, r34): continue
            rays6 = {r12, r13, r23, r14, r24, r34}
            if len(rays6) != 6: continue
            # Sigma on K4 {1,2,3,4}: pairs (12,34),(13,24),(14,23)
            Sig = (symp(r12, r34) ^ symp(r13, r24) ^ symp(r14, r23))
            cnt[Sig] += 1
        if sum(cnt.values()) >= 8:        # only fibers with enough completions
            fiber_hist.append((cnt.get(0, 0), cnt.get(1, 0)))
            agg[0] += cnt.get(0, 0); agg[1] += cnt.get(1, 0)
            bases_done += 1
    print(f"  studied {bases_done} base K3 fibers")
    for idx, (z, o) in enumerate(fiber_hist):
        tot = z + o
        print(f"    fiber {idx:2d}: Sigma=0:{z:4d}  Sigma=1:{o:4d}   "
              f"(P[Sigma=1]={o/tot:.3f}, n={tot})")
    Z, O = agg[0], agg[1]
    print(f"  AGGREGATE over fibers: Sigma=0:{Z}  Sigma=1:{O}  "
          f"P[Sigma=1]={O/(Z+O):.4f}")

if __name__ == "__main__":
    print("=== L4-fiber distribution of the K4 matching parity Sigma (n=6) ===")
    fiber_study(6)
