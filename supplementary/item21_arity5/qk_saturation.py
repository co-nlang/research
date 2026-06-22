#!/usr/bin/env python3
"""
Item 21, Steenrod-module route -- first probe: does the arity-4 "absorption" pattern persist to
arity 5?  Paper XIX's arity-4 Maslov/Kashiwara quadruple bit q4 is built from omega and is SATURATED
(q4==1 in ~99.5% of n=5 configs -> no fiber information). If the natural arity-5 analogue q5 also
saturates, that is evidence (NOT proof) the natural omega-Maslov tower truncates -- no arity-5 escape
from the omega-generated invariants (the genuinely-exotic Arf-type escape is separate, addressed by
Paper XIX's Arf exclusion at arity 4).

General arity-k Maslov bit (Paper XIX Def. def:q4 generalised; k=4 IS q4):
  given Lagrangians L_{a_1},...,L_{a_{k-1}} (free) and L_{a_k} (distinguished),
    D_k = { (v_1,...,v_{k-1}) in prod L_{a_m} : sum_m v_m in L_{a_k} }   (a linear subspace)
    Q_k(v_1,...,v_{k-1}) = sum_{m<m'} omega(v_m, v_{m'})                  (sum of pairwise omega)
    q_k = [ Q_k not-identically-0 on D_k ].
k=4: 3 free vectors x,y,z, Q4=omega(x,y)+omega(x,z)+omega(y,z), cond x+y+z in L_d -- matches XIX.

D_k is built as the kernel of the membership map (sum_m v_m in L_{a_k} <=> omega(sum, b)=0 for b in
basis(L_{a_k})); Q_k is then evaluated by SAMPLING random kernel elements (a nonzero F_2 quadratic
form is !=0 on >=1/4 of points, so ~64 samples detect it with miss prob <=(3/4)^64 ~ 1e-8).

UNIT TEST: k=4 must reproduce XIX's saturation (q4==1 nearly always). Then report q5.
Pure Python; reuses paper22/nerve_cochain.build.
"""
import sys, random
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def basis_of(vectors):
    """GF(2) basis (list of ints) of the span of `vectors`."""
    piv = {}
    for v in vectors:
        x = v
        while x:
            h = x.bit_length() - 1
            if h in piv:
                x ^= piv[h]
            else:
                piv[h] = x
                break
    return list(piv.values())

def nullspace(rows, ncols):
    """Kernel basis (list of ints, each an ncols-bit mask) of the F_2 matrix `rows` (list of ints)."""
    rows = [r for r in rows]
    pivcol = {}    # col -> row
    r = 0
    mat = rows[:]
    # forward elimination to RREF
    basis_rows = []
    used = []
    for row in mat:
        x = row
        for c, pr in pivcol.items():
            if (x >> c) & 1:
                x ^= pr
        if x:
            c = (x & -x).bit_length() - 1   # lowest set col as pivot
            # reduce existing
            for cc in list(pivcol):
                if (pivcol[cc] >> c) & 1:
                    pivcol[cc] ^= x
            pivcol[c] = x
    pivots = set(pivcol.keys())
    free = [c for c in range(ncols) if c not in pivots]
    ker = []
    for f in free:
        v = 1 << f
        for c, pr in pivcol.items():
            if (pr >> f) & 1:
                v |= (1 << c)
        ker.append(v)
    return ker

def make_qk(symp):
    def qk(free_bases, dist_basis, samples=64, rng=None):
        k1 = len(free_bases); n = len(dist_basis)
        # membership map M: coeff space F_2^{k1*n} -> F_2^n  (one row per dist basis vector)
        # col index (m,t) -> m*n+t ; entry = omega(free_bases[m][t], dist_basis[i])
        ncols = k1 * n
        rows = []
        for i in range(n):
            row = 0
            b = dist_basis[i]
            for m in range(k1):
                for t in range(n):
                    if symp(free_bases[m][t], b):
                        row |= 1 << (m * n + t)
            rows.append(row)
        ker = nullspace(rows, ncols)
        if not ker:
            return 0
        for _ in range(samples):
            # random combo of kernel basis
            c = 0
            for kv in ker:
                if rng.getrandbits(1):
                    c ^= kv
            if c == 0:
                continue
            # reconstruct v_m and evaluate Q_k
            vs = []
            for m in range(k1):
                vm = 0
                for t in range(n):
                    if (c >> (m * n + t)) & 1:
                        vm ^= free_bases[m][t]
                vs.append(vm)
            Q = 0
            for a in range(k1):
                for b in range(a + 1, k1):
                    Q ^= symp(vs[a], vs[b])
            if Q:
                return 1
        return 0
    return qk

def run(N, k, n_lag, cap, seeds, budget=60):
    import time
    symp, gen, k5s, mu = build(N); qk = make_qk(symp); rng = random.Random(12345)
    sat = Counter(); per_config = Counter(); t0 = time.time()
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(51000 + 19 * s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            B = [basis_of(L) for L in five]      # 5 Lagrangian bases
            # all choices: distinguished e, and (k-1) free from the remaining 4 (k=4) or all (k=5)
            vals = []
            for combo in combinations(range(5), k):           # k Lagrangians involved
                for di in range(k):                           # which is distinguished
                    dist = combo[di]
                    free = [combo[j] for j in range(k) if j != di]
                    v = qk([B[m] for m in free], B[dist], rng=rng)
                    vals.append(v); sat[v] += 1
            if vals:
                per_config[all(v == 1 for v in vals)] += 1
        if time.time() - t0 > budget: break
    n1 = sat[1]; n0 = sat[0]; T = n1 + n0
    pc = per_config[True] + per_config[False]
    print(f"  n={N}, q{k}: instances={T}; q{k}==1: {n1}/{T} ({100*n1//max(T,1)}%); "
          f"q{k}==0: {n0}/{T}; configs fully-saturated(all==1): {per_config[True]}/{pc}", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    print("UNIT TEST (must reproduce XIX: q4 saturated ~99.5%):", flush=True)
    run(5, 4, 3000, 1200, 4)
    run(6, 4, 2500, 1000, 3)
    print("PROBE (q5 -- the arity-5 question):", flush=True)
    run(5, 5, 3000, 1200, 4)
    run(6, 5, 2500, 1000, 3)
