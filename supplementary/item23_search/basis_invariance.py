#!/usr/bin/env python3
"""
Collaborator's basis-change test: the closed form  N_anti = q(T) XOR XOR_i q(v_i)  is
Sp-invariant (it equals N_anti, a count) even though q itself is NOT an Sp-invariant.

Under a symplectic change of basis (here: a composition of transvections T_u(v)=v+omega(v,u)u,
which preserve omega), we expect:
  (1) the individual q(v_i), q(T) to CHANGE  (q is coordinate-dependent), and
  (2) the net XOR q(T) XOR XOR_i q(v_i) to stay = N_anti (the formula is invariant).

This makes concrete the phrase "coordinate closed form, not intrinsic bridge": the summands are
frame-dependent, only their combination is invariant.  (If (2) ever failed, the formula itself
would be basis-dependent -- a red flag; it does not.)

Result: formula value invariant & = N_anti  900/900 (n=4,5);  some per-ray q changed ~97%.

Pure Python (reuses paper22/nerve_cochain.build); no deps.
"""
import sys, time, random
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def make_q(N):
    MSK = (1 << N) - 1
    def q(v): return bin((v & MSK) & ((v >> N) & MSK)).count('1') & 1
    return q

def run(N, n_lag, seed, ntests):
    symp, gen, k5s, mu_triple = build(N); q = make_q(N); rng = random.Random(seed)
    lags, adj = gen(seed, n_lag); SZ = 1 << (2*N)
    def transv(v, u): return v ^ u if symp(v, u) else v   # T_u(v)=v+omega(v,u)u, preserves omega
    fi = Counter(); qc = Counter(); tested = 0
    for five, sh in k5s(lags, adj, ntests):
        def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
        rays = [R(i, j) for i, j in combinations(range(5), 2)]
        Na = 0
        for m in range(5):
            t = [x for x in range(5) if x != m]; a, b, c, d = t
            for (p, r) in [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]:
                Na ^= symp(R(*p), R(*r))
        def formula(rs):
            T = 0
            for r in rs: T ^= r
            val = q(T)
            for r in rs: val ^= q(r)
            return val
        A = formula(rays)
        us = [rng.randrange(1, SZ) for _ in range(6)]
        rays2 = rays[:]
        for u in us: rays2 = [transv(v, u) for v in rays2]
        B = formula(rays2)
        changed = any(q(a) != q(b) for a, b in zip(rays, rays2))
        fi[A == B == Na] += 1; qc[changed] += 1; tested += 1
    print(f"  n={N}: tested={tested}; formula invariant & =N_anti: {fi[True]}/{tested}; "
          f"per-ray q changed under basis change: {qc[True]}/{tested}", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(4, 800, 123, 400)
    run(5, 2500, 77, 500)
