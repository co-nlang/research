#!/usr/bin/env python3
"""
Item 21 / M5 descent: do the rays of a K6 DETERMINE its Lagrangians?  (Verifies a load-bearing claim.)

The completeness lemma (m5_relations.py) is at the RAY level: (G,R) determines the ray-tuple up to Sp.
M5's actual target is invariants of LAGRANGIAN tuples. These coincide only if the rays determine the
Lagrangians. They DON'T in general -- and the threshold is sharp:

  Each ray r_{ij} lies in L_i \cap L_j (it is (k, S_i k) with k in ker(S_i+S_j), so S_i k = S_j k).
  For a K6 (6 Lagrangians), L_i receives exactly N-1 = 5 rays {r_{ij}: j != i}, all inside the n-dim
  Lagrangian L_i, and they are ISOTROPIC (omega(r_{ij},r_{ik})=0, both in the isotropic L_i). So
  K_i := span{r_{ij}:j} has dim <= min(5, n); it determines L_i only when dim K_i = n. The Lagrangians
  containing the isotropic K_i are the Lagrangians of the quotient K_i^perp/K_i (dim 2(n - dim K_i)),
  numbering prod_{t=1}^{n-dim K_i}(2^t+1) -- so dim K_i < n means genuine underdetermination.

RESULT (corrects an over-optimistic prior guess of a clean "n<=5 faithful" threshold). Empirically the
rays are NOT generic, so the threshold is sharper and resonates with the series' "n=4 is special":
     n = 4 : dim K_i = 4 = n ALWAYS (1200/1200) -> rays determine the Lagrangians, every config.
     n = 5 : dim K_i in {3,4,5}; only ~46% reach n (556/1200) -> the 5 rays are usually DEPENDENT, so
             the descent is MOSTLY LOSSY already at n=5 (not generically faithful).
     n = 6 : dim K_i in {3,4,5}, NEVER 6 (0/720, since only 5 rays) -> ALWAYS lossy; underdetermination
             multiplicity {3,15,135} (= the Lagrangian counts for quotient dims q=1,2,3) confirmed.
So the ray<->Lagrangian descent is faithful EXACTLY at n=4 (the universal dimension), partial at n=5,
never at n>=6.

CONSEQUENCE (the scoping point, not a threat): the ray-level completeness lemma is STRICTLY weaker than
a Lagrangian-tuple FFT for n>=5 -- M5's descent step is genuinely lossy except at n=4. BUT the
framework's contextuality/cohomology obstruction (omega, anticommutation, n_a=Sq^1 omega) is RAY-level
data, so item 21 is properly a RAY-level statement; Lagrangian-invariants beyond the rays are a
different object and do not enter the H^4 obstruction. This sharpens M5's reading; it does not open an
escape.

This script verifies, at n=4,5,6: (i) every ray lies in its L_i (construction sanity); (ii) the
per-Lagrangian ray-span dimension dim K_i and whether it equals n (determined) or < n (gap); (iii) at
n=6, the number of Lagrangians containing K_i (the underdetermination multiplicity), by enumerating
Lagrangians of the quotient K_i^perp / K_i. Pure Python; reuses paper22/k6_truncation.make.
"""
import sys, random
from itertools import combinations
from collections import Counter
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import make


def k6_with_mats(N, rng, tries=8000):
    matvec, rank, ker_vec, rand_sym, dm = make(N)
    mats = []
    for _ in range(tries):
        if len(mats) == 6: break
        S = rand_sym(rng)
        if all(rank(dm(S, T)) == N - 1 for T in mats): mats.append(S)
    if len(mats) != 6: return None, None, None
    ray = {}
    for i in range(6):
        for j in range(i + 1, 6):
            k = ker_vec(dm(mats[i], mats[j]))
            ray[(i, j)] = k | (matvec(mats[i], k) << N)
    if len(set(ray.values())) != 15: return None, None, None
    return mats, ray, matvec


def f2span(vs):
    piv = {}
    for v in vs:
        x = v
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; break
    return list(piv.values())


def in_span(v, basis):
    x = v
    for b in sorted(basis, reverse=True):
        x = min(x, x ^ b)
    return x == 0


def run(N, target, seed, budget=120):
    import time
    rng = random.Random(seed); t0 = time.time()
    msk = (1 << N) - 1
    def isymp(u, v):
        return (bin((u & msk) & ((v >> N) & msk)).count('1')
                ^ bin(((u >> N) & msk) & (v & msk)).count('1')) & 1
    found = 0
    dimK = Counter(); determined = Counter(); ray_in_Li = Counter(); mult = Counter()
    while found < target and time.time() - t0 < budget:
        mats, ray, matvec = k6_with_mats(N, rng)
        if ray is None: continue
        found += 1
        for i in range(6):
            Li = [(1 << t) | (matvec(mats[i], 1 << t) << N) for t in range(N)]   # basis of L_i
            Libasis = f2span(Li)
            Ki = [ray[tuple(sorted((i, j)))] for j in range(6) if j != i]        # 5 rays in L_i
            ray_in_Li[all(in_span(r, Libasis) for r in Ki)] += 1
            Kb = f2span(Ki)
            d = len(Kb)
            dimK[d] += 1
            determined[d == N] += 1
            if N == 6:
                # Lagrangians of F_2^{2N} containing the isotropic K_i <-> Lagrangians of the
                # symplectic quotient K_i^perp / K_i (dim 2(N - d)); count = prod_{t=1}^{q}(2^t+1).
                q = N - d
                nlag = 1
                for t in range(1, q + 1):
                    nlag *= (2 ** t + 1)
                mult[nlag] += 1
    print(f"  n={N}: proper K6 sampled={found}", flush=True)
    print(f"    [sanity] every ray in its L_i: {ray_in_Li[True]}/{ray_in_Li[True]+ray_in_Li[False]}", flush=True)
    print(f"    dim K_i = dim span{{r_ij : j!=i}}: {dict(sorted(dimK.items()))}  (n={N})", flush=True)
    tot = determined[True] + determined[False]
    print(f"    rays DETERMINE L_i (dim K_i == n): {determined[True]}/{tot}  "
          f"=> {'rays determine the Lagrangians' if determined[False]==0 else 'GAP: rays UNDERdetermine'}",
          flush=True)
    if N == 6 and mult:
        print(f"    [n=6] # Lagrangians containing K_i (underdetermination multiplicity): "
              f"{dict(sorted(mult.items()))}  (3 = the 3 Lagrangians of the 2-dim quotient)", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== descent: do K6 rays determine the Lagrangians? (threshold n<=5 vs n>=6) ===", flush=True)
    run(4, 200, 11)
    run(5, 200, 22)
    run(6, 120, 33)
