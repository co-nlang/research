#!/usr/bin/env python3
"""
Item 21 modulus FFT, step 2: does the primary modulus generator (weight enumerator of R) CLIMB to H^4?

modulus_fine.py identified the weight enumerator of the relation space R (as a binary code in F_2^10)
as the dominant fine modulus generator (Arf is subsumed). Its natural F2-valued components are
  A_w(5-config) = (# weight-w codewords in R) mod 2,  w = 0..10.
Each A_w is a SPECIFIC natural arity-5 invariant (not an indicator) -> firewall-clean to test climbing.

CLIMB TEST (the M1 standard): form the degree-4 cochain c^w_m = A_w(face m) on the K6 nerve and check
the H^4 pairing  Sum_m A_w(face m) == 0  for every config.

RESULT (2026-06-23): Sum_m A_w != 0 for w=4..10 at n=5,6 (n=4 gives all 0). This is NOT a genuine H^4
escape -- it is the h4_cohomology OVER-COUNTING trap. A_w is a non-coboundary invariant that varies
across orbits, so it pairs !=0 generically (the 6 faces of a K6 are generically distinct orbits at
n>=5), exactly like an orbit-indicator. N_anti gives Sum=0 ONLY because it is an exact coboundary
(delta of the arity-4 anticommutation, M1); A_w is not a coboundary, so it pairs nontrivially. The n=4
"control" is WEAK: at n=4 there are so few orbits that delta^4=0 for ALL functions, so Sum=0 there is
not specific to A_w. CONSEQUENCE (the real finding): even the identified modulus generators over-count,
so the modulus no-climb theorem CANNOT be the naive Sum_m=0 test -- it requires the natural/
indecomposable-data delimitation, which is the insight-bound crux. The over-counting wall is reached
from inside the modulus too. Pure Python; reuses k6_truncation.k6.
"""
import sys, random
from itertools import combinations
from collections import Counter
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import k6


def relations(rints, L):
    piv = {}; rels = []
    for i in range(L):
        rv = rints[i]; em = 1 << i
        while rv:
            h = rv.bit_length() - 1
            if h in piv:
                rv ^= piv[h][0]; em ^= piv[h][1]
            else:
                piv[h] = (rv, em); break
        if rv == 0:
            rels.append(em)
    return rels


def weight_parities(Rbasis):
    """A_w = (#weight-w codewords in R) mod 2, for w=0..10 -> tuple of 11 bits."""
    words = [0]
    for b in Rbasis:
        words += [w ^ b for w in words]
    wc = Counter(bin(w).count('1') for w in words)
    return [wc.get(w, 0) & 1 for w in range(11)]


def run(N, target, seed, budget=150):
    import time
    rng = random.Random(seed); t0 = time.time()
    order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    found = 0
    sums = [Counter() for _ in range(11)]      # per-w distribution of Sum_m A_w(face m)
    while found < target and time.time() - t0 < budget:
        ray = k6(N, rng)
        if ray is None: continue
        found += 1
        raydict = {p: (ray[p][0] | (ray[p][1] << N)) for p in order}
        acc = [0] * 11
        for m in range(6):
            V = [x for x in range(6) if x != m]
            frays = [raydict[(i, j)] for i, j in combinations(V, 2)]   # 10 rays of the face
            Aw = weight_parities(relations(frays, 10))
            for w in range(11):
                acc[w] ^= Aw[w]
        for w in range(11):
            sums[w][acc[w]] += 1
    print(f"  n={N}: proper K6 sampled={found}", flush=True)
    climbed = [w for w in range(11) if len(sums[w]) > 1]
    for w in range(11):
        if sums[w].get(1, 0) or len(sums[w]) > 1:
            print(f"    w={w}: Sum_m A_w distribution {dict(sums[w])}", flush=True)
    if not climbed:
        tag = ("  (n=4: delta^4=0 for ALL functions -- few orbits -- so this is a WEAK control, "
               "not specific to A_w)" if N == 4 else "")
        print(f"    -> Sum_m A_w == 0 for all w.{tag}", flush=True)
    else:
        print(f"    -> Sum_m A_w != 0 for w in {climbed}. *** NOT a genuine escape: this is the"
              f" h4_cohomology OVER-COUNTING trap. A_w is a non-coboundary invariant that varies across"
              f" orbits, so it pairs !=0 generically (the 6 faces of a K6 are generically distinct"
              f" orbits at n>=5) -- exactly like an orbit-indicator. N_anti gives Sum=0 ONLY because it"
              f" is an exact coboundary (delta of arity-4, M1); A_w is not. So 'climbing' here just means"
              f" 'not a coboundary', NOT a genuine contextuality obstruction. CONSEQUENCE: even the"
              f" identified modulus generators over-count, so the no-climb theorem CANNOT be the naive"
              f" Sum_m=0 test -- it needs the natural/indecomposable-data delimitation (insight-bound).",
              flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== modulus FFT step 2: does weight-enum(R) climb to H^4? (Sum_m A_w =?= 0) ===", flush=True)
    run(4, 400, 11)
    run(5, 400, 22)
    run(6, 300, 33)
