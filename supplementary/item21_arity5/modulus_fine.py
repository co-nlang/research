#!/usr/bin/env python3
"""
Item 21 modulus FFT, step 1: IDENTIFY the fine modulus invariant (what separates (G,Arf)-collisions).

lemmaB_test refuted "Arf is the complete non-omega radical invariant": distinct degenerate 5-config
orbits share (canon-G, Arf) but differ in R. So the radical/modulus carries invariants BEYOND N_anti
(which is G-determined) and Arf (~0). To do the modulus FFT we must first NAME the missing generator(s).

Candidate (natural, S5-invariant, NOT a function of G): the WEIGHT ENUMERATOR of the relation space R
viewed as a binary code in F_2^10 (10 rays = edges of K5; S5 permutes edges preserving weights). Also
test the simpler bits [all-ones 1 in R] and dim(R cap cycle-space of K5).

TEST: dedupe degenerate 5-config orbits by orbit_id = canon-(G,R). For each orbit compute
  base   = (canon-G, Arf)              [refuted: not complete],
  +wenum = (canon-G, Arf, weightenum(R)),
and check how many distinct orbits each fingerprint conflates. If +wenum is INJECTIVE (no collisions)
the weight enumerator is THE missing modulus generator; if it still collides, more structure remains.

Firewall: specific natural invariants (G, Arf, weight enumerator), not indicators -> no over-counting.
Pure Python; reuses k6_truncation.make, m4_cochain.face_arf, lemmaB_test.canon.
"""
import sys, random
from itertools import combinations
from collections import defaultdict, Counter
sys.path.insert(0, "supplementary/paper22")
sys.path.insert(0, "supplementary/item21_arity5")
from k6_truncation import make
from m4_cochain import face_arf
from lemmaB_test import k5_sample, canon, relations, f2rank


def weight_enum(Rbasis, L=10):
    """Multiset of Hamming weights over all 2^{|Rbasis|} codewords of R -> canonical tuple."""
    words = [0]
    for b in Rbasis:
        words += [w ^ b for w in words]
    wc = Counter(bin(w).count('1') for w in words)
    return tuple(sorted(wc.items()))


def ones_in_R(Rbasis, L=10):
    """Is the all-ones vector (sum of all 10 rays = 0) in R?"""
    target = (1 << L) - 1
    piv = {}
    for b in Rbasis:
        x = b
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; break
    x = target
    for h in sorted(piv, reverse=True):
        x = min(x, x ^ piv[h])
    return int(x == 0)


def run(N, target, seed, budget=180):
    import time
    rng = random.Random(seed); t0 = time.time()
    orbits = {}    # orbit_id -> dict of fingerprint pieces
    got = 0
    while got < target and time.time() - t0 < budget:
        ray = k5_sample(N, rng)
        if ray is None: continue
        got += 1
        rays = [ray[(i, j)] for i, j in combinations(range(5), 2)]
        if f2rank(rays) == 2 * N:        # nondegenerate -> skip (no modulus)
            continue
        ok, a = face_arf(rays, N)
        if not ok:
            continue
        cG, cGR = canon(ray, N)
        if cGR in orbits:
            continue
        Rb = relations(rays, 10)
        orbits[cGR] = {"cG": cG, "arf": a, "wenum": weight_enum(Rb),
                       "ones": ones_in_R(Rb)}
    def collisions(keyfn):
        b = defaultdict(set)
        for oid, d in orbits.items():
            b[keyfn(d)].add(oid)
        return sum(len(v) - 1 for v in b.values() if len(v) > 1), \
            sum(1 for v in b.values() if len(v) > 1)
    base_c = collisions(lambda d: (d["cG"], d["arf"]))
    wen_c = collisions(lambda d: (d["cG"], d["arf"], d["wenum"]))
    won_c = collisions(lambda d: (d["cG"], d["arf"], d["wenum"], d["ones"]))
    gw_c = collisions(lambda d: (d["cG"], d["wenum"]))
    print(f"  n={N}: distinct degenerate orbits (Arf-defined) = {len(orbits)}", flush=True)
    print(f"    (canon-G, Arf)                 collisions: {base_c[0]} extra / {base_c[1]} buckets "
          f"[Lemma B refuted -- baseline]", flush=True)
    print(f"    (canon-G, Arf, wenum R)        collisions: {wen_c[0]} extra / {wen_c[1]} buckets", flush=True)
    print(f"    (canon-G, Arf, wenum R, 1inR)  collisions: {won_c[0]} extra / {won_c[1]} buckets", flush=True)
    print(f"    (canon-G, wenum R)  [no Arf]   collisions: {gw_c[0]} extra / {gw_c[1]} buckets", flush=True)
    if wen_c[0] == 0:
        print(f"    -> weight enumerator of R SEPARATES all (G,Arf)-collisions: it IS the missing"
              f" modulus generator (mod this sample).", flush=True)
    else:
        print(f"    -> weight enumerator REDUCES but does not fully separate ({base_c[0]}->{wen_c[0]});"
              f" more modulus structure remains.", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== modulus FFT step 1: identify the fine invariant beyond (G, Arf) ===", flush=True)
    run(5, 2000, 22)
    run(6, 1500, 33)
