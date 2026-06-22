#!/usr/bin/env python3
"""
Item 21, M2: extend Paper XIX's structural skeleton (lem:skeleton, K5/10-ray) to K6/15-ray.

For a proper K6 (6 Lagrangians, 15 rays r_1..r_15 in F_2^{2n}):
  W6  = ray span,   G6 = 15x15 Gram, G6[i][j]=omega(r_i,r_j),
  R6  = {a in F_2^15 : sum a_i r_i = 0}  (relation space),
  o6(a)=sum_{i<j} a_i a_j G6[i][j]  (quadratic form, polarization G6),
  kerG6 = {a : G6 a = 0},   ell6 = o6|_{kerG6}  (linear, since o6(a+b)+o6(a)+o6(b)=a^T G6 b).

Deliverables:
  (1) the generic STRATUM (dim W6, rank G6, dim rad W6) at n=4,5,6 -- the K6 analog of XIX's (8,6,2);
  (2) verify the structural skeleton facts hold at K6:
        R6 subset kerG6;  o6|_{kerG6} linear;  dim R6 = 15 - dim W6;
        dim kerG6 - dim R6 = dim rad W6 (i.e. kerG6/R6 ~ rad W6);
        coisotropy W6^perp subset W6  <=>  dim rad W6 = 2n - dim W6;
  (3) PREVIEW for M4: intrinsic-q exists  <=>  ell6|_{R6} == 0  (o6 vanishes on R6) -- existence rate.

Reuses paper22/k6_truncation.k6 (symmetric-matrix chart sampler). Pure Python.
"""
import sys, random
from itertools import combinations
from collections import Counter
sys.path.insert(0, "supplementary/paper22")
from k6_truncation import k6

def basis_of(vs):
    piv = {}
    for v in vs:
        x = v
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; break
    return list(piv.values())

def f2rank(vs): return len(basis_of(vs))

def ray_relations(rints):
    """R6 basis: masks a in F_2^15 with XOR_{i in a} rints[i] = 0."""
    piv = {}; rels = []
    for i, r in enumerate(rints):
        rv = r; em = 1 << i
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
    pivots = set(piv)
    ker = []
    for f in (c for c in range(ncols) if c not in pivots):
        v = 1 << f
        for c, pr in piv.items():
            if (pr >> f) & 1: v |= (1 << c)
        ker.append(v)
    return ker

def run(N, target, seed, budget=90):
    import time
    rng = random.Random(seed); MSK = (1 << N) - 1
    def isymp(v, w):
        return (bin((v & MSK) & ((w >> N) & MSK)).count('1')
                ^ bin(((v >> N) & MSK) & (w & MSK)).count('1')) & 1
    strata = Counter(); coiso = Counter(); Rsub = Counter(); olin = Counter()
    dimchk = Counter(); intrinsic = Counter(); found = 0; att = 0; t0 = time.time()
    while found < target and time.time() - t0 < budget:
        att += 1
        ray = k6(N, rng)
        if ray is None: continue
        found += 1
        order = [(i, j) for i in range(6) for j in range(i + 1, 6)]
        rints = [ray[p][0] | (ray[p][1] << N) for p in order]
        dW = f2rank(rints)
        G = [[isymp(rints[i], rints[j]) for j in range(15)] for i in range(15)]
        Grows = [sum(G[i][j] << j for j in range(15)) for i in range(15)]
        rkG = f2rank(Grows); dRad = dW - rkG
        strata[(dW, rkG, dRad)] += 1
        coiso[dRad == (2 * N - dW)] += 1
        R6 = ray_relations(rints)
        dimchk[len(R6) == 15 - dW] += 1
        # R6 subset kerG6: G6 a = 0 for each rel a
        ok = all(all(bin(Grows[i] & a).count('1') & 1 == 0 for i in range(15)) for a in R6)
        Rsub[ok] += 1
        kerG = nullspace(Grows, 15)
        def o6(a): return sum(G[i][j] for i in range(15) for j in range(i + 1, 15)
                              if (a >> i) & 1 and (a >> j) & 1) & 1
        # kerG6/R6 ~ rad W6
        dimchk[(len(kerG) - len(R6)) == dRad] += 1
        # o6 linear on kerG6 (check on basis pairs)
        lin = True
        for x in range(len(kerG)):
            for y in range(x + 1, len(kerG)):
                if o6(kerG[x] ^ kerG[y]) != (o6(kerG[x]) ^ o6(kerG[y])): lin = False; break
            if not lin: break
        olin[lin] += 1
        # PREVIEW (M4): intrinsic-q exists <=> o6|R6 == 0
        intrinsic[all(o6(a) == 0 for a in R6)] += 1
    print(f"  n={N}: proper K6 sampled={found} (att={att})", flush=True)
    print(f"    stratum (dimW6, rankG6, dim radW6): {dict(sorted(strata.items(), key=lambda kv:-kv[1]))}", flush=True)
    print(f"    structural facts: R6<=kerG6 {Rsub[True]}/{found}; o6|kerG6 linear {olin[True]}/{found}; "
          f"dim identities {dimchk[True]}/{2*found}; coisotropic {coiso[True]}/{found}", flush=True)
    print(f"    [M4 preview] intrinsic-q exists (o6|R6==0): {intrinsic[True]}/{found}", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(4, 150, 11)
    run(5, 150, 22)
    run(6, 120, 33)
