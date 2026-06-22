#!/usr/bin/env python3
"""
Reduce Conley-Ovsienko's cross-ratio relations mod 2 -- and find what (if anything) survives.

C-O's continuous invariant is the symplectic cross-ratio [x1,x2;y1,y2]=w(x1,y1)w(x2,y2)/w(x1,y2)w(x2,y1),
a RATIO of omega-values. Over F2, omega in {0,1}, so every defined cross-ratio = 1, and their single
relation (e.g. hexagon: 1/c0+1/c1+1/c2=1) becomes 1+1+1=1 (3=1 mod 2) -- a TAUTOLOGY. So the cross-ratio
relation is VACUOUS over F2. The only non-ratio (polynomial) form C-O give is the PFAFFIAN of a Gram
matrix; a Pfaffian reduces mod 2 sensibly. We test whether THAT carries F2 content on the framework's
K5 configs.

Pf(alternating A) mod 2 = [A nonsingular] = [rank A = full]. So for the 10x10 ray-Gram G of a proper
K5, Pf(G) mod 2 = [rank G = 10]. We tally rank G (hence Pf) and compare to N_anti and to XIX's stratum.

Expected (and the point): the ray-Gram is DEGENERATE generically (XIX (8,6,2): rank 6 < 10), so
Pf(G)=0 -- ALSO vacuous. If so: BOTH naive mod-2 reductions (cross-ratio and Pfaffian) carry no F2
content -- confirming the continuous C-O data degenerates totally over F2, and the framework's
obstruction is a genuinely different (discrete/cohomological) object, NOT a reduction of C-O.

Pure Python; reuses paper22/nerve_cochain.build.
"""
import sys
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def f2rank_rows(rows):
    piv = []
    for r in rows:
        x = r
        for p in piv:
            x = min(x, x ^ p)
        if x: piv.append(x); piv.sort(reverse=True)
    return len(piv)

def run(N, n_lag, cap, seeds, budget=40):
    import time
    symp, gen, k5s, mu = build(N); t0 = time.time()
    rankG = Counter(); pf = Counter(); pf_vs_na = Counter(); tot = 0
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(71000 + 29 * s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            rays = [R(i, j) for i, j in combinations(range(5), 2)]   # 10 rays
            G = [[symp(rays[i], rays[j]) for j in range(10)] for i in range(10)]
            Grows = [sum(G[i][j] << j for j in range(10)) for i in range(10)]
            rk = f2rank_rows(Grows)
            Pf = 1 if rk == 10 else 0           # Pf(alternating) mod2 = [nonsingular]
            Na = 0
            for m in range(5):
                t = [x for x in range(5) if x != m]; a, b, c, d = t
                for (p, q) in [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]:
                    Na ^= symp(R(*p), R(*q))
            rankG[rk] += 1; pf[Pf] += 1; pf_vs_na[(Pf, Na)] += 1; tot += 1
        if time.time() - t0 > budget: break
    print(f"  n={N}: K5 sampled={tot}", flush=True)
    print(f"    ray-Gram rank distribution: {dict(sorted(rankG.items()))}", flush=True)
    print(f"    Pf(ray-Gram) mod2 = [rank=10]: {dict(pf)}  "
          f"({'VACUOUS (always 0 = degenerate)' if pf[1]==0 else 'nonzero sometimes!'})", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(4, 800, 1200, 5)
    run(5, 3000, 1500, 5)
    run(6, 2500, 1200, 4)
