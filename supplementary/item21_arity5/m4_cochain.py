#!/usr/bin/env python3
"""
Item 21, M4 closure (cochain-level): the DIRECT test M1 did for N_anti, now for the exotic Arf.

A collaborator caught a real gap: M4's earlier n=6 conclusion "no H^4 escape" was argued from
"Arf is a Dickson polynomial in arity-<=4 Gram entries" -- a VALUE-level reducibility statement. But
the session itself proved (n=4 control, m5_relations) that value-level arity-reducibility is NOT
equivalent to cochain-level exactness. So that leap is unjustified. Two fixes are needed and done here:

  (1) RIGHT OBJECT.  The H^4 question is about an ARITY-5 invariant (a 4-cochain), assembled over the
      6 facets of K6.  M4 had computed Arf(Q6) = Arf of the whole 6-Lagrangian config = an ARITY-6
      invariant (a 5-cochain -> H^5/K7), the wrong degree.  The item-21-relevant object is the exotic
      arity-5 invariant  c'_m = Arf(Q5 of face m)  -- the Arf of each 5-Lagrangian face's ray-span.

  (2) RIGHT TEST.  M1's mechanism: form the degree-4 cochain c'_m = Arf(face m) on the K6 nerve and
      verify it pairs to zero with the fundamental class:  Sum_m c'_m == 0  (=> [c']=0 in H^4(S^4),
      cochain-level EXACT, genuine "no H^4 escape").  This is a direct cochain-level check, not a
      value-level inference.

Arf(Q5) of a 5-Lagrangian face: 10 rays, span W5, intrinsic Q5 = quadratic refinement with Q5(ray)=0
and polarization omega; EXISTS iff consistent on all 10 rays; DESCENDS to W5/rad(omega|_W5) iff Q5
vanishes on the radical; then Arf is the well-defined Arf of the nondegenerate quotient (greedy
symplectic pairing, skipping radical directions).  Reports:
  - per-face Arf(Q5) distribution (is it constant ~0, as XIX found at K5/n=4?  built-in validation);
  - Sum_m c'_m distribution over configs where all 6 faces have a defined Arf (the M1-style obstruction);
  - existence/descent coverage.

FINDINGS (2026-06-23, validated: arf() unit-tested; Arf basis-independent 0 mismatches; n=5 reproduces
XIX's "Arf=0 essentially always", 533/534 standalone -- NOTE Paper XIX is the n>=5 program, so its
intrinsic-q/Arf results are at n>=5, NOT n=4):
  - n=4: intrinsic Q5 NEVER exists (0/2400; dimW=8 spans, but consistency fails) -> no Arf cochain at
    all (vacuous; consistent with n=4 being settled).
  - n>=5: Arf(Q5) defined on ~88-93% of faces; where defined it is ESSENTIALLY ALWAYS 0 (value-level
    ~constant, XIX-consistent), with RARE 1's.  Sum_m c'_m is mostly 0 with sporadic 1's that occur
    <=> an ODD number of the 6 faces hit the rare Arf=1 -- sporadic rare events, NOT a structured H^4
    class (no escape).  AND Arf(Q5) is a PARTIAL function (undefined where Q5 doesn't exist), so it is
    NOT a total arity-5 invariant/cochain -> the H^4 pairing is ill-posed for this candidate.

VERDICT: NO evidence of an H^4 escape; but also NOT a clean cochain-level exactness proof (the candidate
is partial).  This RETRACTS the earlier claim that M4 closed item 21 at cochain level "by reducibility"
(that was a value->cochain leap, flagged by a collaborator) -- M4 contributes a VALUE-level absorption
data point (Arf(Q5) ~ const 0, XIX-consistent), not a cohomological theorem.  Pure Python; reuses
paper22/k6_truncation.k6.
"""
import sys, random
from itertools import combinations
from collections import Counter
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import k6


def nullspace(rows, ncols):
    piv = {}
    for row in rows:
        x = row
        for c, pr in piv.items():
            if (x >> c) & 1: x ^= pr
        if x:
            c = (x & -x).bit_length() - 1
            for cc in list(piv):
                if (piv[cc] >> c) & 1: piv[cc] ^= x
            piv[c] = x
    pivots = set(piv)
    ker = []
    for f in (c for c in range(ncols) if c not in pivots):
        v = 1 << f
        for c, pr in piv.items():
            if (pr >> f) & 1: v |= (1 << c)
        ker.append(v)
    return ker


def arf(d, Om, Qval):
    """Arf of quadratic Qval with polarization Om (row-int matrix) on a d-dim space; greedy symplectic
    pairing, skipping radical directions (=> Arf of the nondegenerate quotient W/rad)."""
    def om(u, v):
        return sum(((u >> i) & 1) * ((Om[i] >> j) & 1) * ((v >> j) & 1)
                   for i in range(d) for j in range(d)) & 1
    pool = [1 << i for i in range(d)]
    a = 0
    while pool:
        v = pool.pop(0)
        wi = next((k for k, w in enumerate(pool) if om(v, w)), None)
        if wi is None:
            continue                       # v in radical of remaining span -> skip (quotient)
        w = pool.pop(wi)
        a ^= Qval(v) & Qval(w)
        pool = [u ^ (v if om(u, w) else 0) ^ (w if om(u, v) else 0) for u in pool]
    return a


def face_arf(rays, N):
    """Arf(Q5) of a face given its ray ambient-ints. Returns (defined, arf_bit)."""
    msk = (1 << N) - 1
    def isymp(u, v):
        return (bin((u & msk) & ((v >> N) & msk)).count('1')
                ^ bin(((u >> N) & msk) & (v & msk)).count('1')) & 1
    # ray-basis
    piv = {}; basis = []
    for r in rays:
        x = r
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; basis.append(r); break
    d = len(basis)
    if d == 0:
        return (False, None)
    Om = [[isymp(basis[i], basis[j]) for j in range(d)] for i in range(d)]
    Omr = [sum(Om[i][j] << j for j in range(d)) for i in range(d)]
    # coords of an ambient ray in the basis (Gaussian)
    cpiv = {}
    for k, b in enumerate(basis):
        x = b; m = 1 << k
        while x:
            h = x.bit_length() - 1
            if h in cpiv:
                x ^= cpiv[h][0]; m ^= cpiv[h][1]
            else:
                cpiv[h] = (x, m); break
    def coords(r):
        x = r; mask = 0
        while x:
            h = x.bit_length() - 1
            if h in cpiv:
                x ^= cpiv[h][0]; mask ^= cpiv[h][1]
            else:
                return None
        return mask
    def Q(mask):
        s = 0; bits = [i for i in range(d) if (mask >> i) & 1]
        for a_, b_ in combinations(bits, 2): s ^= Om[a_][b_]
        return s
    # existence: Q vanishes on every ray
    for r in rays:
        m = coords(r)
        if m is None or Q(m) != 0:
            return (False, None)
    # descent: Q vanishes on radical of omega|_W
    for v in nullspace(Omr, d):
        if Q(v) != 0:
            return (False, None)
    return (True, arf(d, Omr, Q))


def run(N, target, seed, budget=180):
    import time
    rng = random.Random(seed); t0 = time.time()
    order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    found = 0
    perface = Counter(); allsix = 0; sumdist = Counter(); cover = Counter()
    while found < target and time.time() - t0 < budget:
        ray = k6(N, rng)
        if ray is None: continue
        found += 1
        raydict = {p: (ray[p][0] | (ray[p][1] << N)) for p in order}
        cs = []
        for m in range(6):
            V = [x for x in range(6) if x != m]
            frays = [raydict[(i, j)] for i, j in combinations(V, 2)]   # 10 rays of the face
            ok, a = face_arf(frays, N)
            cover[ok] += 1
            if ok:
                perface[a] += 1
            cs.append(a if ok else None)
        if all(c is not None for c in cs):
            allsix += 1
            sumdist[sum(cs) % 2] += 1
    print(f"  n={N}: proper K6 sampled={found}", flush=True)
    print(f"    Arf(Q5) defined-per-face: {cover[True]}/{cover[True]+cover[False]}", flush=True)
    print(f"    per-face Arf(Q5) distribution: {dict(perface)}  "
          f"({'CONSTANT 0' if set(perface)<= {0} else 'VARIES'})", flush=True)
    print(f"    configs with all 6 faces defined: {allsix}/{found}", flush=True)
    if allsix:
        ones = sumdist.get(1, 0)
        print(f"    Sum_m c'_m (c'_m = Arf(face m), all-6-defined configs only): {dict(sumdist)}", flush=True)
        print(f"      NOTE: Sum=1 occurs in {ones}/{allsix} <=> an ODD number of the 6 faces hit the"
              f" RARE Arf=1 (~{100*perface.get(1,0)/max(1,sum(perface.values())):.1f}% of faces). This is"
              f" sporadic rare events, NOT a structured H^4 class. And Arf(Q5) is PARTIAL (undefined"
              f" where Q5 doesn't exist), so it is not a total arity-5 cochain -> the H^4 pairing is"
              f" ill-posed for this candidate. => NO evidence of escape; also NOT a clean cochain-exactness"
              f" proof. (n=4: Q5 never exists -> no cochain at all, vacuous.)", flush=True)
    else:
        print(f"    (no config had all 6 faces defined -- at n=4 the intrinsic Q5 never exists)", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== M4 cochain-level closure: Sum_m Arf(face m) =?= 0 over K6 (the M1-style test) ===", flush=True)
    run(4, 400, 11)
    run(5, 400, 22)
    run(6, 300, 33)
