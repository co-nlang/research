"""Paper XXII seed -- the arity/configuration resonance tower.

Claim: an obstruction built from arity-a symplectic data is an (a-1)-cochain on the
index nerve; on K_N (nerve S^{N-2}) it hits TOP cohomology iff N = a+1.  Natural data:
Maslov mu (arity 3, 2-cochain) -> resonates at K4 (S^2, H^2);  anticommutation na=delta mu
(arity 4, 3-cochain) -> resonates at K5 (S^3, H^3).  No natural arity-5 -> K6/H^4 empty
(truncation, already verified in k6_truncation.py).

This script verifies the NEW rung: the K4 / H^2 Maslov resonance.  For a proper K4 the
nerve is the boundary of a tetrahedron ~ S^2 whose top cells are the 4 triangles; mu is a
2-cocycle there and the H^2 class is  <mu,[S^2]> = sum over the 4 triples of mu  (mod 2).
Prediction from rank-parity (XX):  mu=0 (n=3) and mu=1 (even n) make the sum 0 (RIGID);
only odd n>=5 (mu varies) opens H^2.  So H^2 opens at ODD n>=5 only -- the dichotomy's
odd branch -- while H^3 (K5) opens at ALL n>=5.
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

def k4_maslov_class(N, target, seed, n_lag=400, budget=40):
    rng = random.Random(seed)
    symp, lags = gen_lags(N, n_lag, budget, rng)
    _, _, _, mu_triple = build(N)
    def ray(A, B):
        it = A & B
        return next(iter(it)) if len(it) == 1 else None
    n = len(lags); adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            if len(lags[i] & lags[j]) == 1: adj[i].add(j); adj[j].add(i)
    cls = Counter(); musum = Counter(); tot = 0
    for i in range(n):
        if tot >= target: break
        for j in adj[i]:
            if j <= i: continue
            for k in (adj[i] & adj[j]):
                if k <= j: continue
                for l in (adj[i] & adj[j] & adj[k]):
                    if l <= k: continue
                    idx = (i, j, k, l)
                    rays = {}
                    ok = True
                    for a in range(4):
                        for b in range(a+1, 4):
                            rr = ray(lags[idx[a]], lags[idx[b]])
                            if rr is None: ok = False; break
                            rays[(a, b)] = rr
                        if not ok: break
                    if not ok or len(set(rays.values())) != 6: continue
                    # 4 triples of the K4; Maslov bit each
                    s = 0
                    for (a, b, c) in combinations(range(4), 3):
                        s ^= mu_triple(lags[idx[a]], lags[idx[b]], lags[idx[c]])
                    cls[s] += 1; tot += 1
                    if tot >= target: break
                if tot >= target: break
            if tot >= target: break
    verdict = "RIGID (H^2 trivial)" if set(cls) <= {0} else "OPEN (H^2 nontrivial)"
    print(f"  n={N}: proper K4={tot}   <mu,[S^2]> dist={dict(sorted(cls.items()))}   => {verdict}")

if __name__ == "__main__":
    print("=== K4 / H^2 Maslov resonance: <mu,[S^2]> by n ===")
    print("  predict: n=3 RIGID(mu=0); n=4 RIGID(mu=1,sum=0); n=5 OPEN; n=6 RIGID(mu=1)")
    for N in (3, 4, 5, 6):
        k4_maslov_class(N, target=400, seed=300+N)
