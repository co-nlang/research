#!/usr/bin/env python3
"""
Item 21, M5: does the ABSTRACT Sp-invariant cochain complex model item 21?  ANSWER (this script): NO.
A documented methodological NEGATIVE -- the n=4 control rules out the abstract-cohomology route.

The tempting model: build the complex
    C^k = {Sp-invariant F2-valued functions of (k+1) Lagrangians in proper position},
    delta = simplicial coboundary  (delta f)(S) = XOR_{v in S} f(S without v),
and claim item 21 <=> H^4 = 0, H^4 = ker(delta^4)/im(delta^3) = |C^4| - rank(d4) - rank(d3).
Enabled by the completeness lemma + Witt: every Sp-invariant of m labeled Lagrangians is a function of
the fingerprint (G,R) [ray-Gram + relation space]; same (G,R) => omega-preserving iso of ray-spans =>
extends to Sp by WITT'S THEOREM (all strata). So C^k basis = distinct (G,R) fingerprints (canonicalized
over vertex permutations for the unordered simplicial complex).

WHY IT FAILS (the n=4 CONTROL, settled: NO H^4 obstruction).  Computed: |O4|=1,|O5|=2,|O6|=3,
rank d4=0, rank d3=1 => abstract H^4 = 2-0-1 = 1, NOT 0.  No arithmetic bug (delta^2=0 holds; the
hand-count agrees).  The spurious class is the invariant "is this K5 in orbit #1": it is a COCYCLE
(pairs to 0 on every K6 nerve, since d4=0) -> furnishes ZERO per-config obstruction -> NO contextuality
content -> yet it is not a coboundary, so abstract H^4 counts it.  The abstract complex OVER-COUNTS via
orbit combinatorics.  (The alternative reading "rank d4" over-counts the other way: at n=5 there are
~135 K5-orbits, so a K6's 6 faces are generically all-distinct and an orbit-INDICATOR pairs to 1 -- a
pure combinatorial 'obstruction' with no contextuality meaning; it would absurdly 'falsify' item 21 at
every n>=5.)  So NEITHER the abstract H^4 nor rank d4 models item 21.

CONCLUSION.  Item 21 is NOT "H^4 of the invariant complex = 0"; it is the exactness of the SPECIFIC
natural anticommutation-type arity-5 datum (the generalization of N_anti = Sq^1 omega).  That is why
the right tools are M1 (N_anti exact, proven) and M4 (Arf reducible) -- testing named natural
candidates -- not the abstract complex.  This is the THIRD route the n=4 control has ruled out this
session (after co_reduce's C-O reduction and m5_relations' arity-reduction).  The machinery here is
SOUND (delta^2=0 verified); only the MODEL is wrong.  Kept as a signpost so M5 work does not re-attempt
the abstract-cohomology route.  Pure Python; reuses paper22/k6_truncation.k6.
"""
import sys, random
from itertools import combinations, permutations
from collections import defaultdict
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import k6


def rref_tuple(masks, ncols):
    """Reduced row echelon basis of F2 row-masks (over ncols bits) as a canonical sorted tuple."""
    piv = {}
    for m in masks:
        x = m
        for c in sorted(piv, reverse=True):
            if (x >> c) & 1:
                x ^= piv[c]
        if x:
            c = x.bit_length() - 1
            for cc in list(piv):
                if (piv[cc] >> c) & 1:
                    piv[cc] ^= x
            piv[c] = x
    return tuple(sorted(piv.values()))


def ray_relations(rints, L):
    """Basis of {a in F2^L : XOR_{i in a} rints[i] = 0}."""
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


def fp_ordered(rays, N):
    """(G, R) fingerprint of an ordered ray list (ambient ints, x|z<<N)."""
    msk = (1 << N) - 1
    def isymp(u, v):
        return (bin((u & msk) & ((v >> N) & msk)).count('1')
                ^ bin(((u >> N) & msk) & (v & msk)).count('1')) & 1
    L = len(rays)
    G = tuple(isymp(rays[i], rays[j]) for i in range(L) for j in range(i + 1, L))
    R = rref_tuple(ray_relations(rays, L), L)
    return (G, R)


def canon_fp(V, raydict, N):
    """Canonical fingerprint of the sub-config on vertex set V (min over vertex permutations)."""
    m = len(V); slots = list(combinations(range(m), 2))
    best = None
    for sigma in permutations(range(m)):
        pv = [V[sigma[t]] for t in range(m)]
        rays = [raydict[tuple(sorted((pv[a], pv[b])))] for a, b in slots]
        f = fp_ordered(rays, N)
        if best is None or f < best:
            best = f
    return best


def f2rank(rows):
    piv = []
    for r in rows:
        x = r
        for p in piv:
            x = min(x, x ^ p)
        if x:
            piv.append(x); piv.sort(reverse=True)
    return len(piv)


def run(N, target, seed, budget=240):
    import time
    rng = random.Random(seed); t0 = time.time()
    faces6 = {}      # fp6 -> sorted tuple of its 6 fp5
    faces5 = {}      # fp5 -> sorted tuple of its 5 fp4
    O4, O5, O6 = set(), set(), set()
    seen6_curve = []
    found = 0
    while found < target and time.time() - t0 < budget:
        ray = k6(N, rng)
        if ray is None: continue
        found += 1
        raydict = {p: (ray[p][0] | (ray[p][1] << N)) for p in ray}
        fp6 = canon_fp((0, 1, 2, 3, 4, 5), raydict, N)
        f5 = []
        for m in range(6):
            V5 = tuple(x for x in range(6) if x != m)
            fp5 = canon_fp(V5, raydict, N)
            f5.append(fp5); O5.add(fp5)
            if fp5 not in faces5:
                f4 = []
                for q in range(5):
                    V4 = tuple(x for k, x in enumerate(V5) if k != q)
                    fp4 = canon_fp(V4, raydict, N); f4.append(fp4); O4.add(fp4)
                faces5[fp5] = tuple(sorted(f4))
            else:
                O4.update(faces5[fp5])
        faces6[fp6] = tuple(sorted(f5)); O6.add(fp6)
        if found % 25 == 0:
            seen6_curve.append(len(O6))
    # index
    idx4 = {f: i for i, f in enumerate(sorted(O4))}
    idx5 = {f: i for i, f in enumerate(sorted(O5))}
    # delta^3: rows over O5, each a bitmask over O4 (parity of face multiplicities)
    M3 = []
    for fp5 in sorted(O5):
        row = 0
        for fp4 in faces5[fp5]:
            row ^= 1 << idx4[fp4]
        M3.append(row)
    # delta^4: rows over O6, each a bitmask over O5
    M4 = []
    for fp6 in sorted(O6):
        row = 0
        for fp5 in faces6[fp6]:
            row ^= 1 << idx5[fp5]
        M4.append(row)
    # delta^2 = 0 check: (M4 . M3) over F2 == 0, i.e. for each fp6, XOR of M3-rows of its 5-faces == 0
    d2 = 0
    for fp6 in sorted(O6):
        acc = 0
        for fp5 in faces6[fp6]:
            acc ^= M3[idx5[fp5]]
        if acc != 0:
            d2 += 1
    rank3 = f2rank(M3)
    rank4 = f2rank(M4)
    dimC4 = len(O5)
    H4 = dimC4 - rank4 - rank3
    print(f"  n={N}: proper K6 sampled={found}", flush=True)
    print(f"    orbit counts |C^3|=|O4|={len(O4)}  |C^4|=|O5|={len(O5)}  |C^5|=|O6|={len(O6)}", flush=True)
    print(f"    O6-saturation curve (per +25 samples): {seen6_curve[-8:]}", flush=True)
    print(f"    rank(delta^3)={rank3}  rank(delta^4)={rank4}  dim ker(delta^4)={dimC4-rank4}", flush=True)
    print(f"    [validation] delta^4.delta^3 nonzero rows: {d2}/{len(O6)} (0 => machinery sound, it IS a complex)", flush=True)
    print(f"    abstract H^4 = |C^4| - rank d4 - rank d3 = {dimC4} - {rank4} - {rank3} = {H4}", flush=True)
    if N == 4:
        ok = "as predicted" if H4 != 0 else "UNEXPECTED"
        print(f"    *** n=4 CONTROL: master theorem => NO H^4 contextuality obstruction, yet abstract"
              f" H^4 = {H4} != 0 ({ok}). => the abstract complex OVER-COUNTS (spurious orbit-combinatorics"
              f" class). The abstract-cohomology route does NOT model item 21. Route ruled out.", flush=True)
    else:
        sat = "SATURATED" if (len(seen6_curve) >= 2 and seen6_curve[-1] == seen6_curve[-2]) else "UNSATURATED (undersampled)"
        print(f"    (n={N}: doubly unreliable -- wrong model AND orbits {sat}; not an item-21 number.)", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== item 21: does abstract H^4 of the Sp-invariant complex model it? (n=4 control) ===", flush=True)
    run(4, 400, 11)
    run(5, 300, 22)
    run(6, 180, 33)
