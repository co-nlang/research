#!/usr/bin/env python3
"""
Item 21 / M5: is the arity-5 invariant ring omega-Gram-generated on the nondegenerate stratum?

Completeness lemma: every Sp-invariant of a 5-config is a function of (G, R) -- ray-Gram + relation
space.  G is omega-data (arity-<=4 atoms).  The structural question: is R EXTRA data beyond G, or
recoverable from G?  Linear algebra says: with rays as rows of M, G = M Omega M^T and R = leftnull(M);
since a in R => a^T G = a^T M Omega M^T = 0, we have ALWAYS  R subset ker(G), and the k6 skeleton
identity gives  ker(G)/R  ~  rad(omega|_W).  Hence:

    R = ker(G)   <=>   rad(omega|_W) = 0   (the NONDEGENERATE stratum).

CONSEQUENCE (the reduction, value-level): on the nondegenerate stratum R = ker(G) is RECOVERED FROM G,
so (G,R) = (G, ker G) and EVERY arity-5 invariant is a function of the omega-Gram G ALONE -- the whole
generic-stratum invariant ring is omega-generated (XXII's domain).  Any exotic arity-5 invariant must
therefore live either (a) as an omega-Gram-function on the nondegenerate stratum, or (b) in the radical
data of a degenerate stratum.  This localizes the M5 exotic hunt.

This script VERIFIES (firewall: confirm before asserting), for 5-configs (the arity-5 objects) at
n=4,5,6:
  (1) R subset ker(G) always;
  (2) dim ker(G) - dim R == dim rad(omega|_W)  (the skeleton identity), hence R = ker(G) iff rad = 0;
  (3) the (dim W, dim rad) stratum breakdown and the NONDEGENERATE (rad=0) fraction -- how much of the
      arity-5 world is omega-Gram-generated.
n=4 is the control (rad=0 expected: rays span F_2^8 nondegenerately -> R = ker(G), fully omega-generated).
Pure Python; reuses paper22/k6_truncation.make.
"""
import sys, random
from itertools import combinations
from collections import Counter
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import make


def k5_sample(N, rng, tries=4000):
    matvec, rank, ker_vec, rand_sym, dm = make(N)
    mats = []
    for _ in range(tries):
        if len(mats) == 5: break
        S = rand_sym(rng)
        if all(rank(dm(S, T)) == N - 1 for T in mats): mats.append(S)
    if len(mats) != 5: return None
    ray = {}
    for i in range(5):
        for j in range(i + 1, 5):
            k = ker_vec(dm(mats[i], mats[j])); ray[(i, j)] = k | (matvec(mats[i], k) << N)
    if len(set(ray.values())) != 10: return None
    return [ray[(i, j)] for i, j in combinations(range(5), 2)]


def f2rank(vs):
    piv = {}
    for v in vs:
        x = v
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; break
    return len(piv)


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
    pivots = set(piv); ker = []
    for f in (c for c in range(ncols) if c not in pivots):
        v = 1 << f
        for c, pr in piv.items():
            if (pr >> f) & 1: v |= (1 << c)
        ker.append(v)
    return ker


def run(N, target, seed, budget=90):
    import time
    rng = random.Random(seed); t0 = time.time(); msk = (1 << N) - 1
    def isymp(u, v):
        return (bin((u & msk) & ((v >> N) & msk)).count('1')
                ^ bin(((u >> N) & msk) & (v & msk)).count('1')) & 1
    L = 10
    found = 0; Rsub = Counter(); ident = Counter(); strata = Counter(); nondeg = Counter()
    while found < target and time.time() - t0 < budget:
        rays = k5_sample(N, rng)
        if rays is None: continue
        found += 1
        dW = f2rank(rays)
        G = [[isymp(rays[i], rays[j]) for j in range(L)] for i in range(L)]
        Grows = [sum(G[i][j] << j for j in range(L)) for i in range(L)]
        R = relations(rays, L); dR = L - dW
        kerG = nullspace(Grows, L); dKer = len(kerG)
        # (1) R subset ker(G)
        Rsub[all(all((bin(Grows[i] & a).count('1') & 1) == 0 for i in range(L)) for a in R)] += 1
        dRad = dKer - dR
        # (2) skeleton identity: dim ker G - dim R == dim rad(omega|_W); verify rad independently
        # rad(omega|_W) = {w in W : omega(w, r_k)=0 all k}; compute via Gram-on-basis nullspace
        bidx = []; piv = {}
        for i, r in enumerate(rays):
            x = r
            while x:
                h = x.bit_length() - 1
                if h in piv: x ^= piv[h]
                else: piv[h] = x; bidx.append(i); break
        basis = [rays[i] for i in bidx]
        Gb = [sum(isymp(basis[i], basis[j]) << j for j in range(dW)) for i in range(dW)]
        dRad_true = len(nullspace(Gb, dW))
        ident[(dKer - dR) == dRad_true] += 1
        strata[(dW, dRad_true)] += 1
        nondeg[dRad_true == 0] += 1
    print(f"  n={N}: K5 sampled={found}", flush=True)
    print(f"    (1) R subset ker(G): {Rsub[True]}/{found}", flush=True)
    print(f"    (2) dim ker(G) - dim R == dim rad(omega|_W): {ident[True]}/{found}", flush=True)
    print(f"    (3) stratum (dim W, dim rad): {dict(sorted(strata.items(), key=lambda kv:-kv[1]))}", flush=True)
    nd = nondeg[True]; tot = nondeg[True] + nondeg[False]
    print(f"        NONDEGENERATE (rad=0 => R=ker(G) => omega-Gram-generated): {nd}/{tot}"
          f"{'  <-- CONTROL: expect all (rays span F_2^8 nondeg)' if N==4 else ''}", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== M5 reduction: R = ker(G) on the nondeg stratum => arity-5 ring is omega-generated ===", flush=True)
    run(4, 400, 11)
    run(5, 400, 22)
    run(6, 300, 33)
