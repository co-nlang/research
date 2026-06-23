#!/usr/bin/env python3
"""
Item 21, grounding the D-bridge REFRAME: the over-counters are PHASE-BLIND (not arbitrary exclusion).

The D-bridge reframe (DBRIDGE.md §3) says a GENUINE contextuality obstruction is a class pulled from
H*(BH) -- a characteristic class of the OPERATOR structure (the phases omega/q) -- not an arbitrary
Sp-invariant function of configuration tuples. The firewall worry: is excluding the "climbing"
over-counters (A_w = weight-enumerator of the relation code R, modulus_climb.py) PRINCIPLED, or just a
convenient definition that throws away whatever doesn't fit?

This script shows the exclusion is principled by a STRUCTURAL fact + a decisive check:

  STRUCTURAL.  A_w is computed from R = {subsets of the 15 rays summing to 0 in V} -- the F2-LINEAR
  DEPENDENCY code of the ray vectors. It never references the symplectic form omega. Hence A_w is a
  function of R alone, and R is preserved by EVERY g in GL(2n,F2) (linear maps preserve dependencies:
  sum g v_i = g sum v_i = 0 iff sum v_i = 0). So A_w is GL(2n,F2)-INVARIANT.

  But contextuality is a PHASE phenomenon: the genuine obstruction n_a = sum of omega over disjoint
  pairs is built from omega, which is preserved by Sp(2n,F2) but NOT by the larger GL(2n,F2). So n_a is
  Sp-invariant and NOT GL-invariant.

  DECISIVE CHECK.  Apply random g in GL(2n,F2) \\ Sp to a proper K6's 15 ray vectors. Predict + verify:
    (i)  R (hence A_w, and the whole weight enumerator) is UNCHANGED  -- the over-counter is blind to g;
    (ii) n_a / N_anti CHANGES for generic g  -- the genuine obstruction sees the phase g destroyed.

  CONCLUSION.  A_w is constant exactly where the genuine contextuality obstruction varies: it lives at
  the GL (incidence) level, n_a lives at the Sp (phase) level. So A_w CANNOT witness contextuality --
  its Sum_m A_w != 0 is incidence-combinatorics of R, not an operator-phase obstruction. The reframe's
  exclusion is therefore PRINCIPLED (phase-blind invariants are not contextuality witnesses), not a
  fiat. This is the operational content behind "genuine obstruction = pulled from H*(BH)".

Pure Python; reuses k6_truncation.k6 (the proper-K6 sampler) and modulus_climb-style R/weight code.
Rays are encoded as 2n-bit ints  v = x | (z << n).
"""
import sys, random
from itertools import combinations
from collections import Counter
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import k6


def symp(v, w, n):
    """Standard symplectic form on 2n-bit ints v=x|(z<<n)."""
    mask = (1 << n) - 1
    xv, zv = v & mask, v >> n
    xw, zw = w & mask, w >> n
    return (bin(xv & zw).count('1') ^ bin(zv & xw).count('1')) & 1


def rref(vectors):
    """Row-reduce a list of F2 ints to a canonical sorted RREF basis (for code equality)."""
    piv = {}
    for v in vectors:
        x = v
        for h, p in piv.items():
            if (x >> h) & 1:
                x ^= p
        if x:
            h = x.bit_length() - 1
            # reduce existing rows against the new pivot too (true RREF)
            for k in list(piv):
                if (piv[k] >> h) & 1:
                    piv[k] ^= x
            piv[h] = x
    return tuple(sorted(piv.values()))


def relation_code(rays):
    """R = subsets of `rays` (list of F2 ints) summing to 0; return canonical basis over the 15 slots."""
    L = len(rays)
    piv = {}        # high bit of vector -> (vector, membership mask)
    rels = []
    for i in range(L):
        rv = rays[i]; em = 1 << i
        while rv:
            h = rv.bit_length() - 1
            if h in piv:
                rv ^= piv[h][0]; em ^= piv[h][1]
            else:
                piv[h] = (rv, em); break
        if rv == 0:
            rels.append(em)
    return rref(rels)


def weight_enum(Rbasis):
    """A_w = (#weight-w codewords in R) mod 2, w=0..15."""
    words = [0]
    for b in Rbasis:
        words += [w ^ b for w in words]
    wc = Counter(bin(w).count('1') for w in words)
    return tuple(wc.get(w, 0) & 1 for w in range(16))


def nanti_vec(rays_by_pair, n):
    """Per-face n_a vector (6 faces of K6) + N_anti, from the symplectic form."""
    order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    rd = {p: rays_by_pair[p] for p in order}
    c = []
    for m in range(6):
        V = [x for x in range(6) if x != m]
        tot = 0
        for a, b, cc, d in combinations(V, 4):
            for (p, q) in (((a, b), (cc, d)), ((a, cc), (b, d)), ((a, d), (b, cc))):
                tot ^= symp(rd[p], rd[q], n)
        c.append(tot)
    # N_anti over all 6
    tot6 = 0
    for a, b, cc, d in combinations(range(6), 4):
        for (p, q) in (((a, b), (cc, d)), ((a, cc), (b, d)), ((a, d), (b, cc))):
            tot6 ^= symp(rd[p], rd[q], n)
    return tuple(c), tot6


def rand_gl(n, rng):
    """Random invertible 2n x 2n matrix over F2, as a list of 2n row-ints; retry until full rank."""
    N = 2 * n
    while True:
        rows = [rng.getrandbits(N) for _ in range(N)]
        # full rank?
        piv = []
        for r in rows:
            x = r
            for p in piv:
                x = min(x, x ^ p)
            if x:
                piv.append(x); piv.sort(reverse=True)
        if len(piv) == N:
            return rows


def apply_gl(g, v, n):
    """g (list of 2n row-ints) applied to vector v (2n-bit int)."""
    out = 0
    for i in range(2 * n):
        if bin(g[i] & v).count('1') & 1:
            out |= 1 << i
    return out


def is_symplectic(g, n):
    """Does g preserve omega on the standard basis? (g in Sp iff omega(g e_i, g e_j)=omega(e_i,e_j))."""
    N = 2 * n
    e = [1 << i for i in range(N)]
    ge = [apply_gl(g, e[i], n) for i in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            if symp(ge[i], ge[j], n) != symp(e[i], e[j], n):
                return False
    return True


def run(n, target, seed, gl_per=12):
    rng = random.Random(seed)
    order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
    found = 0
    Aw_mismatch = 0          # times A_w changed under GL  (predict: 0)
    R_mismatch = 0           # times R changed under GL     (predict: 0)
    nanti_changed = 0        # times N_anti changed under non-Sp GL (predict: many)
    gl_total = 0; gl_nonsp = 0
    while found < target:
        ray = k6(n, rng)
        if ray is None:
            continue
        found += 1
        # 15 ray vectors as 2n-bit ints, in fixed order
        rays = [(ray[p][0] | (ray[p][1] << n)) for p in order]
        R0 = relation_code(rays); A0 = weight_enum(R0)
        _, M0 = nanti_vec({p: rays[k] for k, p in enumerate(order)}, n)
        for _ in range(gl_per):
            g = rand_gl(n, rng); gl_total += 1
            sp = is_symplectic(g, n)
            grays = [apply_gl(g, v, n) for v in rays]
            R1 = relation_code(grays); A1 = weight_enum(grays and R1)
            _, M1 = nanti_vec({p: grays[k] for k, p in enumerate(order)}, n)
            if R1 != R0:
                R_mismatch += 1
            if A1 != A0:
                Aw_mismatch += 1
            if not sp:
                gl_nonsp += 1
                if M1 != M0:
                    nanti_changed += 1
    print(f"  n={n}: proper K6 sampled={found}, GL applications={gl_total} "
          f"(non-symplectic={gl_nonsp})", flush=True)
    print(f"    [i]  R changed under GL : {R_mismatch}/{gl_total}   (predict 0 -- R is GL-invariant)",
          flush=True)
    print(f"    [i]  A_w changed under GL: {Aw_mismatch}/{gl_total}   (predict 0 -- A_w blind to phase)",
          flush=True)
    pct = (100.0 * nanti_changed / gl_nonsp) if gl_nonsp else 0.0
    print(f"    [ii] N_anti changed under non-Sp GL: {nanti_changed}/{gl_nonsp} ({pct:.0f}%)  "
          f"(predict many -- n_a IS phase-dependent)", flush=True)
    verdict = ("PHASE-BLIND confirmed: A_w invariant where contextuality (N_anti) varies"
               if R_mismatch == 0 and Aw_mismatch == 0 and nanti_changed > 0
               else "UNEXPECTED -- inspect")
    print(f"    => {verdict}", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== reframe grounding: over-counter A_w is GL-invariant (phase-blind); n_a is not ===",
          flush=True)
    run(4, 60, 401)
    run(5, 60, 402)
    run(6, 40, 403)
