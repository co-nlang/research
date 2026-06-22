#!/usr/bin/env python3
"""
Item 21, M4 (the crux): build the INTRINSIC EXOTIC at K6 and test whether it tracks the H^4 fiber.

This lifts Paper XIX's arity-4 Arf-exclusion (sec:arf, P2) to arity 5. At K5 XIX found: an intrinsic
quadratic refinement q (vanishing on the 10 rays) exists generically, but Arf(Q|_W)=0 ALWAYS while
N_anti splits 404/103 -- so the Arf invariant is BLIND to the fiber. M4 asks the same at K6.

Construction (the faithful lift):
  - 6 Lagrangians in proper position -> 15 rays r_{ij} in F_2^{2n}, span W6.
  - Restrict to the GENERIC stratum (dim W6 = 2n, NONDEGENERATE -- M2's (2n,2n,0)); there omega|_W6 is
    a nondegenerate symplectic form and the Arf invariant is a clean single bit.
  - INTRINSIC EXOTIC Q6 = the quadratic refinement of omega on W6 with Q6(r_{ij}) = 0 for all 15 rays
    and polarization omega (Q6(u+v)=Q6(u)+Q6(v)+omega(u,v)). Pick a basis B of 2n rays; Q6(b)=0 forces
    Q6 unique; it EXISTS iff every other ray r=XOR_{i in S} b_i satisfies sum_{i<j in S} omega(b_i,b_j)=0
    (this is exactly M2's o6|_R6 == 0 consistency condition). When it exists it is UNIQUE and Sp-invariant.
  - Arf(Q6) in {0,1}: extract a symplectic basis greedily, Arf = XOR_pairs Q6(e)Q6(f).

The H^4 fiber to test correlation against (arity-<=4 data, all Sp-invariant, all VARY across configs):
  - c = (c_0..c_5),  c_m = N_anti(face m) mod 2     [the six sub-K5 H^3 classes; A4=sum c_m == 0 by M1]
  - M  = N_anti(all 6) mod 2                          [the K6 total disjoint-pair anti-count, varies]

THE REDUCIBILITY TEST (what decides (a)/(b)/(c)):
  - Arf(Q6) is REDUCIBLE to the arity-<=4 signature iff it is CONSTANT within every (c, M) bucket.
  - (a) Arf exists but is constant / a function of (c,M)  -> blind or redundant: supports item 21.
  - (b) Arf does not exist on the generic stratum        -> P2 template inapplicable, re-plan.
  - (c) Arf VARIES within a (c,M) bucket                  -> a candidate IRREDUCIBLE arity-5 invariant:
        item 21 in jeopardy. (Caveat O1: could mean the signature is missing some arity-<=4 invariant,
        not that Arf is exotic -- so (c) is a FLAG for deeper scrutiny, not an immediate falsification.)

SCOPING (carry in): this is bounded-sample evidence on the generic stratum, NOT a nonexistence proof.
Rates are population-dependent; we report orderings, n=6 limits, and whether Arf is constant-vs-varies,
never lean on a single raw %.  Pure Python; reuses paper22/k6_truncation.
"""
import sys, random
from itertools import combinations
from collections import Counter, defaultdict
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import k6, symp, nanti


def basis_pick(rints):
    """Return indices of a maximal F_2-independent subset of the ray ints, plus the pivot table."""
    piv = {}; bidx = []
    for i, r in enumerate(rints):
        x = r
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; bidx.append(i); break
    return bidx, piv


def coords_in_basis(r, basis_rints):
    """Express ray int r as XOR of basis rays; return mask over basis (or None if not in span)."""
    piv = {}  # head bit -> (residual, basis-mask)
    for k, b in enumerate(basis_rints):
        x = b; m = 1 << k
        while x:
            h = x.bit_length() - 1
            if h in piv:
                x ^= piv[h][0]; m ^= piv[h][1]
            else:
                piv[h] = (x, m); break
    x = r; mask = 0
    while x:
        h = x.bit_length() - 1
        if h in piv:
            x ^= piv[h][0]; mask ^= piv[h][1]
        else:
            return None
    return mask


def arf(d, Om, Qval):
    """Arf invariant of quadratic form Qval (callable on bitmask) with polarization Om (matrix as
    list of row-ints over a d-dim F_2 space). Greedy symplectic-basis extraction."""
    def om(u, v):
        return sum(((u >> i) & 1) * ((Om[i] >> j) & 1) * ((v >> j) & 1)
                   for i in range(d) for j in range(d)) & 1
    pool = [1 << i for i in range(d)]
    a = 0
    while pool:
        v = pool.pop(0)
        wi = next((k for k, w in enumerate(pool) if om(v, w)), None)
        if wi is None:
            continue  # v in radical: nondegenerate => only happens once pool is exhausted-equivalent
        w = pool.pop(wi)
        a ^= Qval(v) & Qval(w)
        pool = [u ^ (v if om(u, w) else 0) ^ (w if om(u, v) else 0) for u in pool]
    return a


def run(N, target, seed, budget=120):
    import time
    rng = random.Random(seed); t0 = time.time()
    order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    found = 0; generic = 0; q_exists = 0; basis_mismatch = 0
    arf_dist = Counter()                  # Arf value over configs where Q exists on generic stratum
    arf_vs_M = Counter()                  # (Arf, M)
    bucket = defaultdict(Counter)         # COARSE (c-vector, M) -> Counter of Arf  [reducibility test]
    rich = defaultdict(Counter)           # RICH arity-<=4 signature -> Counter of Arf  [O1 stress-test]
    a4_check = Counter()
    subs4 = list(combinations(range(6), 4))   # 15 four-subsets
    subs5 = [tuple(x for x in range(6) if x != m) for m in range(6)]  # 6 five-subsets
    while found < target and time.time() - t0 < budget:
        ray = k6(N, rng)
        if ray is None: continue
        found += 1
        rints = [ray[p][0] | (ray[p][1] << N) for p in order]
        bidx, _ = basis_pick(rints)
        dW = len(bidx)
        if dW != 2 * N:
            continue                       # restrict to generic nondegenerate stratum
        generic += 1
        basis = [rints[i] for i in bidx]
        msk = (1 << N) - 1
        def xz(b): return (b & msk, b >> N)
        # consistency: every ray's Q must be 0  <=> Q exists (o6|_R6 == 0)
        Om = [[symp(xz(basis[i]), xz(basis[j])) for j in range(2 * N)]
              for i in range(2 * N)]
        Omr = [sum(Om[i][j] << j for j in range(2 * N)) for i in range(2 * N)]
        def Qcoord(mask):
            s = 0
            bits = [i for i in range(2 * N) if (mask >> i) & 1]
            for a_, b_ in combinations(bits, 2):
                s ^= Om[a_][b_]
            return s
        ok = True
        for r in rints:
            m = coords_in_basis(r, basis)
            if m is None or Qcoord(m) != 0:
                ok = False; break
        if not ok:
            continue                       # intrinsic Q does not exist on this config
        q_exists += 1
        A = arf(2 * N, Omr, Qcoord)
        # VALIDATION: Arf(Q6) is intrinsic (basis-independent) -- recompute from a different ray-basis
        bidx2, _ = basis_pick(list(reversed(rints)))
        if len(bidx2) == 2 * N:
            basis2 = [list(reversed(rints))[i] for i in bidx2]
            Om2 = [[symp(xz(basis2[i]), xz(basis2[j])) for j in range(2 * N)] for i in range(2 * N)]
            Om2r = [sum(Om2[i][j] << j for j in range(2 * N)) for i in range(2 * N)]
            def Q2(mask):
                s = 0
                bits = [i for i in range(2 * N) if (mask >> i) & 1]
                for a_, b_ in combinations(bits, 2): s ^= Om2[a_][b_]
                return s
            if arf(2 * N, Om2r, Q2) != A:
                basis_mismatch += 1
        # fiber data
        faces = [tuple(x for x in range(6) if x != m) for m in range(6)]
        c = tuple(nanti(ray, f) % 2 for f in faces)
        M = nanti(ray, range(6)) % 2
        a4_check[sum(c) % 2] += 1
        arf_dist[A] += 1
        arf_vs_M[(A, M)] += 1
        bucket[(c, M)][A] += 1
        # rich arity-<=4 signature: every 4- and 5-subset N_anti  (all arity <=4 data)
        sig = (tuple(nanti(ray, T) % 2 for T in subs4),
               tuple(nanti(ray, T) % 2 for T in subs5), M)
        rich[sig][A] += 1
    # report
    print(f"  n={N}: proper K6 sampled={found}; generic-stratum (dW=2n)={generic}; "
          f"intrinsic Q exists={q_exists}", flush=True)
    if q_exists == 0:
        print(f"    -> OUTCOME (b): no intrinsic exotic on the generic stratum; P2 template inapplicable.",
              flush=True)
        return
    print(f"    Arf(Q6) distribution: {dict(arf_dist)}  "
          f"({'CONSTANT' if len(arf_dist)==1 else 'VARIES'})", flush=True)
    print(f"    [validation] Arf basis-independence mismatches: {basis_mismatch}/{q_exists} "
          f"(0 => intrinsic/Sp-invariant, machinery sound)", flush=True)
    print(f"    sanity A4=sum c_m: {dict(a4_check)} (expect all 0 by M1)", flush=True)
    print(f"    Arf vs M (total anti parity): {dict(sorted(arf_vs_M.items()))}", flush=True)
    # reducibility test: is Arf constant within each (c,M) bucket?
    split = {k: dict(v) for k, v in bucket.items() if len(v) > 1}
    nb = len(bucket); nsplit = len(split)
    print(f"    REDUCIBILITY: {nb} distinct (c,M) buckets; {nsplit} contain BOTH Arf values.", flush=True)
    if nsplit == 0:
        print(f"    -> coarse signature: Arf constant in every (c,M) bucket "
              f"=> already a function of (c,M).", flush=True)
    else:
        ex = next(iter(split.items()))
        print(f"    -> coarse signature: Arf VARIES within {nsplit} (c,M) bucket(s), e.g. {ex} "
              f"=> (c,M) too coarse; apply O1 stress-test below.", flush=True)
    # O1 STRESS-TEST: enrich to the full arity-<=4 signature (all 4- & 5-subset N_anti's)
    rsplit = {k: dict(v) for k, v in rich.items() if len(v) > 1}
    npop = sum(1 for v in rich.values() if sum(v.values()) > 1)   # non-singleton rich buckets
    inj = ' [INJECTIVE on sample: buckets all singletons => statistic VACUOUS; rely on structural ' \
          'proof that Arf reads only the arity-<=4 Gram]' if npop == 0 else ''
    print(f"    O1 STRESS-TEST (rich arity-<=4 signature: 15 four- + 6 five-subset N_anti's): "
          f"{len(rich)} buckets ({npop} non-singleton); {len(rsplit)} still contain BOTH Arf "
          f"values.{inj}", flush=True)
    if len(rsplit) == 0 and len(arf_dist) > 1:
        print(f"    -> OUTCOME (a): Arf VARIES but is CONSTANT within every rich arity-<=4 bucket "
              f"=> a function of arity-<=4 data => REDUCIBLE. The coarse (c)-flag was an O1 artifact; "
              f"no genuine arity-5 escape. (Mechanism differs from K5: there Arf is killed by being "
              f"CONSTANT; here by being REDUCIBLE.)", flush=True)
    elif len(rsplit) == 0:
        print(f"    -> OUTCOME (a): Arf constant within every rich arity-<=4 bucket => REDUCIBLE "
              f"(supports item 21).", flush=True)
    else:
        print(f"    -> OUTCOME (c) STANDS: Arf varies even within the rich arity-<=4 signature "
              f"=> genuinely-irreducible candidate; item 21 in jeopardy. Scrutinize further "
              f"(richer signature / larger sample / direct orbit check).", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== M4: intrinsic exotic at K6 vs the H^4 fiber ===", flush=True)
    run(4, 200, 11)     # n=4: M2 says intrinsic-q existence 0% -> expect outcome (b) here
    run(5, 200, 22)
    run(6, 160, 33)
