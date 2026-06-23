#!/usr/bin/env python3
"""
Item 21, (b-neg) step 2: phase-derived data = the q/omega-Gram (polarization + Witt FFT over F2).

The D-bridge's classification direction (b-neg) -- the only half item 21 needs -- rests on:
  (1) genuine obstruction => phase-derived            [phase_blind.py, done]
  (2) phase-derived       => function of the q/omega-Gram {q(v_i), omega(v_i,v_j)}   <== THIS SCRIPT
  (3) assembled deg-4     => ambient class in H^4(BV)^O = <q^2>     [sp_invariants.py, done]
  (4) q^2 decomposable    => no exotic.

Step (2) is NOT the hard Kudo realization (that is (b-pos)/item 23). It is two classical facts, verified
here in-setting:

  POLARIZATION (elementary, ALL n).  q is a quadratic refinement of omega, so for ANY subset S of rays
     q( sum_{i in S} v_i ) = sum_{i in S} q(v_i)  XOR  sum_{i<j in S} omega(v_i, v_j).
  Hence the q-value of EVERY ray-sum (= every phase datum on the span W) is DETERMINED by the Gram
  {q(v_i), omega(v_i,v_j)}. So "phase-derived data" = "function of the Gram", with no extra input. (This
  is the same polarization that powers item 23 link (A).)

  WITT FFT (classical, verified n=2).  Two vector tuples with the SAME (q/omega-Gram, linear-relation
  pattern) lie in the SAME O(q)-orbit (Witt's extension theorem over F2). So the Gram (+ relations) is a
  COMPLETE O-invariant of a vector tuple: every O-invariant is a function of it. Combined with phase_blind
  (the relation part is GL-invariant = phase-blind, hence not genuine), the GENUINE (phase-derived)
  O-invariants are exactly the functions of the q/omega-Gram = nerve-evaluations of ambient H*(BV)^O
  classes. NO secondary-operation / Kudo input is used.

VERIFIES:
  (A) polarization identity, exhaustively over all subsets, random tuples, n=2,3,4 (all-n mechanism);
  (B) Witt FFT at n=2: build O(q) (72 or 120 elts), and check for ordered k-tuples (k=2,3) that
      O-orbit  <=>  (q/omega-Gram, relation-pattern)  -- i.e. the Gram+relations is a complete invariant.
Pure Python.
"""
from itertools import product, combinations


# ---------- n-general symplectic / quadratic on 2n-bit ints v = x | (z<<n) ----------
def symp(v, w, n):
    m = (1 << n) - 1
    xv, zv = v & m, v >> n
    xw, zw = w & m, w >> n
    return (bin(xv & zw).count('1') ^ bin(zv & xw).count('1')) & 1


def qform(v, n):
    m = (1 << n) - 1
    return bin((v & m) & (v >> n)).count('1') & 1     # q(x,z) = x . z


# ---------- (A) polarization identity, all n ----------
def check_polarization(n, k, trials, seed):
    import random
    rng = random.Random(seed)
    bad = 0; tot = 0
    for _ in range(trials):
        vs = [rng.getrandbits(2 * n) for _ in range(k)]
        for r in range(1, k + 1):
            for S in combinations(range(k), r):
                ssum = 0
                for i in S:
                    ssum ^= vs[i]
                lhs = qform(ssum, n)
                rhs = 0
                for i in S:
                    rhs ^= qform(vs[i], n)
                for i, j in combinations(S, 2):
                    rhs ^= symp(vs[i], vs[j], n)
                tot += 1
                if lhs != rhs:
                    bad += 1
    return bad, tot


# ---------- (B) Witt FFT at n=2: build O(q) and compare orbits to (Gram, relations) ----------
def omega_vec(v, n):
    """Omega v as a 2n-bit int (swap x<->z blocks)."""
    m = (1 << n) - 1
    x, z = v & m, v >> n
    return z | (x << n)      # (Omega v): coordinate u -> omega(u,v) = u . (Omega v)


def transvection_perm(vv, n):
    """T_{vv}(u) = u + omega(u,vv) vv, as a permutation array over all 2^{2n} vectors."""
    N = 1 << (2 * n)
    ov = omega_vec(vv, n)
    perm = [0] * N
    for u in range(N):
        t = bin(u & ov).count('1') & 1
        perm[u] = u ^ vv if t else u
    return tuple(perm)


def build_O(n):
    """O(q) built DIRECTLY (avoids the O+_4(2) transvection-generation exception): an isometry is a
    linear map sending the standard basis e_i to images b_i with q(b_i)=q(e_i) and
    omega(b_i,b_j)=omega(e_i,e_j) (matching q+omega on a basis => isometry, by polarization). Enumerate
    all such ordered basis-images; build the permutation of all 2^{2n} vectors."""
    N = 1 << (2 * n)
    M = 2 * n
    e = [1 << i for i in range(M)]
    qe = [qform(e[i], n) for i in range(M)]
    ome = [[symp(e[i], e[j], n) for j in range(M)] for i in range(M)]

    isoms = []

    def rec(imgs):
        i = len(imgs)
        if i == M:
            isoms.append(list(imgs)); return
        for b in range(N):
            if qform(b, n) != qe[i]:
                continue
            if any(symp(b, imgs[j], n) != ome[i][j] for j in range(i)):
                continue
            # independence: b not in span(imgs)
            span = {0}
            for v in imgs:
                span |= {s ^ v for s in span}
            if b in span:
                continue
            imgs.append(b); rec(imgs); imgs.pop()

    rec([])
    # turn each basis-image into a permutation of all vectors
    group = set()
    for b in isoms:
        perm = [0] * N
        for u in range(N):
            img = 0
            for i in range(M):
                if (u >> i) & 1:
                    img ^= b[i]
            perm[u] = img
        group.add(tuple(perm))
    return group


def signature(tup, n):
    """(q-values, pairwise omega, relation-pattern) of an ordered tuple."""
    k = len(tup)
    qs = tuple(qform(v, n) for v in tup)
    om = tuple(symp(tup[i], tup[j], n) for i, j in combinations(range(k), 2))
    rel = 0
    for r in range(1, k + 1):
        for bitpos, S in enumerate(combinations(range(k), r)):
            s = 0
            for i in S:
                s ^= tup[i]
            # encode "this subset sums to 0"
    # build relation pattern as frozenset of subsets summing to 0
    relset = []
    allsubsets = []
    idx = 0
    for r in range(1, k + 1):
        for S in combinations(range(k), r):
            s = 0
            for i in S:
                s ^= tup[i]
            if s == 0:
                relset.append(S)
    return (qs, om, tuple(relset))


def check_witt(n, k):
    N = 1 << (2 * n)
    G = build_O(n)
    # orbit partition of ordered k-tuples
    seen = {}
    orbit_id = {}
    nid = 0
    tuples = list(product(range(N), repeat=k))
    for t in tuples:
        if t in orbit_id:
            continue
        # compute orbit
        oid = nid; nid += 1
        stack = [t]; orbit_id[t] = oid
        while stack:
            cur = stack.pop()
            for g in G:
                img = tuple(g[c] for c in cur)
                if img not in orbit_id:
                    orbit_id[img] = oid; stack.append(img)
    # check: orbit <=> signature
    sig_of_orbit = {}
    ok = True; clashes = 0
    # group tuples by signature, see if each signature = exactly one orbit
    by_sig = {}
    for t in tuples:
        s = signature(t, n)
        by_sig.setdefault(s, set()).add(orbit_id[t])
    multi = sum(1 for s, oids in by_sig.items() if len(oids) > 1)
    # and: does each orbit have a single signature? (automatic, since signature is O-invariant)
    return len(G), nid, len(by_sig), multi


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== (A) polarization: q(ray-sum) determined by the Gram (phase data = Gram), all n ===",
          flush=True)
    for n in (2, 3, 4):
        for k in (4, 5):
            bad, tot = check_polarization(n, k, 300, seed=900 + 10 * n + k)
            print(f"    n={n}, k={k}: polarization mismatches {bad}/{tot}"
                  f"  {'OK (phase data = Gram)' if bad == 0 else '*** FAIL'}", flush=True)

    print("\n=== (B) Witt FFT at n=2: O-orbit  <=>  (q/omega-Gram, relation-pattern) ===", flush=True)
    for k in (2, 3):
        nG, norb, nsig, multi = check_witt(2, k)
        print(f"    n=2, k={k}: |O(q)|={nG}, #orbits={norb}, #signatures={nsig}, "
              f"signatures splitting >1 orbit = {multi}  "
              f"{'OK (Gram+relations COMPLETE => orbit<=>signature)' if multi == 0 else '*** some signature hosts multiple orbits'}",
              flush=True)
