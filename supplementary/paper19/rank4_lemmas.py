#!/usr/bin/env python3
"""
Paper XIX -- the rank-4 lower bound, reduced to two F2-linear-algebra lemmas.

Combined with doily_rank4.py (the exhaustive downstairs dichotomy
"q-bar exists  <=>  N_anti=6" over the S6 doily), the rank-4 conjecture
   rankG = 4  =>  N_anti = 6
is proved CONDITIONAL on two facts about a proper K5 with ray-span W in the
(dimW,rankG,radW)=(7,4,3) stratum:

  (I)  ell|_R == 0          (the upstairs intrinsic refinement Q exists), where
       R = {a : sum_i a_i r_i = 0} is the ray relation space and
       ell(a) = sum_{i<j in a} omega(r_i, r_j).
  (II) radW = span(the rays r_ab that lie in radW).

THE IMPLICATION (I) and (II)  =>  N_anti = 6  IS RIGOROUS:
  * radW = W cap W^perp is isotropic, so the rays inside it pairwise commute;
  * Q vanishes on every ray, so for w = sum(inner rays) in radW,
        Q(w) = sum Q(inner) + sum omega(inner,inner) = 0 + 0 = 0,
    hence Q|radW = 0 (using (II) to write every w in radW as such a sum);
  * therefore Q descends to a refinement q-bar on W-bar = W/radW with
    q-bar(r-bar_i) = 0, i.e. q-bar EXISTS downstairs;
  * by the exhaustive doily dichotomy (doily_rank4.py), q-bar exists => N_anti = 6.

This script verifies (I), (II) and the chain over proper K5 in the (7,4,3) stratum,
across disjoint seed families. (I) and (II) are 0-exception empirically; their
proofs are the remaining open step.

Usage: python3 rank4_lemmas.py [N=5] [N_LAG=4000] [MAX_K5=500] [SEEDS=10]
"""
import sys, time, random
from collections import Counter

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 5
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 500
SEEDS  = int(sys.argv[4]) if len(sys.argv) > 4 else 10

SZ  = 1 << (2*N); MSK = (1 << N) - 1
PN  = [bin(i).count('1') & 1 for i in range(1 << N)]
XT  = [[PN[i & j] for j in range(1 << N)] for i in range(1 << N)]
def symp(v, w): return XT[v & MSK][(w >> N) & MSK] ^ XT[(v >> N) & MSK][w & MSK]

def xspan(b):
    s = {0}
    for x in b: s |= {y ^ x for y in s}
    return s

def gen(seed):
    ALL = list(range(1, SZ)); rng = random.Random(seed)
    def rl():
        b = []; sp = {0}
        for _ in range(N):
            c = [v for v in ALL if v not in sp and all(symp(v, x) == 0 for x in b)]
            if not c: return None
            v = rng.choice(c); b.append(v); sp = xspan(b)
        return frozenset(x for x in sp if x)
    lags = []; ls = set(); t = time.time()
    while len(lags) < N_LAG and time.time()-t < 120:
        L = rl()
        if L and L not in ls: ls.add(L); lags.append(L)
    adj = [set() for _ in lags]
    for i in range(len(lags)):
        for j in range(i+1, len(lags)):
            if len(lags[i] & lags[j]) == 1: adj[i].add(j); adj[j].add(i)
    return lags, adj

def k5s(lags, adj, cap):
    n = len(lags); out = []
    for i in range(n):
        if len(out) >= cap: break
        ai = adj[i]
        for j in ai:
            if j <= i: continue
            aij = ai & adj[j]
            for k in aij:
                if k <= j: continue
                aijk = aij & adj[k]
                for l in aijk:
                    if l <= k: continue
                    for m in (aijk & adj[l]):
                        if m <= l: continue
                        five = [lags[x] for x in (i, j, k, l, m)]; sh = {}; ok = True
                        for a in range(5):
                            for b in range(a+1, 5):
                                it = five[a] & five[b]
                                if len(it) != 1: ok = False; break
                                sh[(a, b)] = next(iter(it))
                            if not ok: break
                        if not ok or len(set(sh.values())) != 10: continue
                        out.append(sh)
                        if len(out) >= cap: return out
    return out

def f2_basis(vs):
    bs = []
    for v in vs:
        x = v
        for b in bs: x = min(x, x ^ b)
        if x: bs.append(x); bs.sort(reverse=True)
    return bs

def coords(v, basis):
    chosen = 0; x = v
    for pos in sorted(range(len(basis)), key=lambda i: basis[i], reverse=True):
        b = basis[pos]; hb = b.bit_length() - 1
        if (x >> hb) & 1: x ^= b; chosen |= (1 << pos)
    return chosen if x == 0 else None

def left_nullspace(rows, width):
    m = len(rows); work = [[rows[i], 1 << i] for i in range(m)]; r = 0
    for col in range(width):
        piv = next((i for i in range(r, m) if (work[i][0] >> col) & 1), None)
        if piv is None: continue
        work[r], work[piv] = work[piv], work[r]
        for i in range(m):
            if i != r and (work[i][0] >> col) & 1:
                work[i][0] ^= work[r][0]; work[i][1] ^= work[r][1]
        r += 1
    return [work[i][1] for i in range(m) if work[i][0] == 0]

def nullspace(M, n):
    rows = M[:]; m = len(rows); pivcol = {}; r = 0
    for col in range(n):
        piv = next((i for i in range(r, m) if (rows[i] >> col) & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(m):
            if i != r and (rows[i] >> col) & 1: rows[i] ^= rows[r]
        pivcol[col] = r; r += 1
    free = [c for c in range(n) if c not in pivcol]; basis = []
    for f in free:
        x = 1 << f
        for col, ri in pivcol.items():
            if (rows[ri] >> f) & 1: x |= (1 << col)
        basis.append(x)
    return basis

def span(basis):
    s = {0}
    for b in basis: s |= {y ^ b for y in s}
    return s

def popcount(x): return bin(x).count('1')

def radical_basis(Wb):
    d = len(Wb); Gr = [0]*d
    for i in range(d):
        for j in range(d):
            if symp(Wb[i], Wb[j]): Gr[i] |= (1 << j)
    rad = []
    for c in nullspace(Gr, d):
        w = 0
        for k in range(d):
            if (c >> k) & 1: w ^= Wb[k]
        if w: rad.append(w)
    return f2_basis(rad)

def in_span(v, basis):
    x = v
    for b in f2_basis(basis[:]):   # reduce the spanning set first (robust membership test)
        x = min(x, x ^ b)
    return x == 0

def run(base, step, label):
    tot = I_ok = II_ok = both = n6 = chain_viol = 0
    for s in range(SEEDS):
        lags, adj = gen(base + step*s)
        for sh in k5s(lags, adj, MAX_K5):
            rays = [sh[(min(a, b), max(a, b))] for a in range(5) for b in range(a+1, 5)]
            basis = f2_basis(rays); dimW = len(basis)
            G = [0]*10
            for i in range(10):
                for j in range(10):
                    if i != j and symp(rays[i], rays[j]): G[i] |= (1 << j)
            rankG = 10 - len(nullspace(G, 10)); radW = dimW - rankG
            if (dimW, rankG, radW) != (7, 4, 3): continue
            tot += 1
            def o(a):
                bits = [i for i in range(10) if (a >> i) & 1]; acc = 0
                for x in range(len(bits)):
                    for y in range(x+1, len(bits)):
                        if (G[bits[x]] >> bits[y]) & 1: acc ^= 1
                return acc
            Rspan = span(left_nullspace([coords(r, basis) for r in rays], dimW))
            I = all(o(a) == 0 for a in Rspan)
            radB = radical_basis(basis)
            inner = [r for r in rays if in_span(r, radB)]
            II = (len(f2_basis(inner[:])) == radW) and all(in_span(b, inner) for b in radB)
            Nanti = sum(popcount(G[i]) for i in range(10)) // 2
            I_ok += I; II_ok += II; both += (I and II); n6 += (Nanti == 6)
            if (I and II) and Nanti != 6: chain_viol += 1
    print(f"{label}: (7,4,3) configs = {tot}")
    print(f"   (I)  ell|_R == 0                 : {I_ok}/{tot}")
    print(f"   (II) radW = span(rays in radW)   : {II_ok}/{tot}")
    print(f"   (I) and (II)                     : {both}/{tot}")
    print(f"   N_anti == 6                      : {n6}/{tot}")
    print(f"   chain [(I)&(II) but N!=6]        : {chain_viol}/{tot}  (must be 0)")
    return tot

if __name__ == "__main__":
    print(f"rank4_lemmas  N={N} N_LAG={N_LAG} MAX_K5={MAX_K5} SEEDS={SEEDS}\n")
    a = run(7000, 53, "family A")
    print()
    b = run(31000, 71, "family B (disjoint)")
    print()
    c = run(80000, 131, "family C (disjoint)")
    print(f"\nTOTAL (7,4,3) = {a+b+c} across three disjoint seed families.")
