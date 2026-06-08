#!/usr/bin/env python3
"""
Paper XIX, Proposition prop:noq_odd  --  structural skeleton + sharp realizability.

In the (dimW, rankG, radW) = (8,6,2) stratum (V = F2^10, n=5), we verify the
following PROVEN structural lemma (each clause is a 0-violation check here; the
proofs are short F2 linear algebra, see the paper):

  Setup. rays r_1..r_10 span W (dim 8). G_ij = omega(r_i,r_j) (10x10 Gram).
         R   = {a in F2^10 : sum_i a_i r_i = 0}     (ray relation space, dim 2)
         o(a)= sum_{i<j} a_i a_j G_ij               (quadratic, polarization G)
         T   = sum_i r_i                            (the Paper-XII T-vector)
         1   = all-ones vector,  N_anti = o(1) = #anticommuting cross pairs.

  (S1) R subseteq ker G.                 [G a = M Omega M^T a = 0 for a in R]
  (S2) dim ker G = 4,  ker G / R  ~=  rad(W) (dim 2). [the (8,6,2) signature;
        W is coisotropic, W^perp = rad(W) subset W]
  (S3) o is LINEAR on ker G  (call it ell). [polarization vanishes on ker G]
  (S4) intrinsic-q exists  <=>  ell|_R == 0.   [consistency of Q(r_i)=0]
  (S5) when intrinsic-q Q exists, Q(T) = N_anti; and  1 in ker G <=> T in rad(W).

Sharp realizability (conjecture-grade, 0 exceptions across disjoint seed families):

  (P)  no intrinsic-q (ell|_R != 0)  =>  N_anti = 9, realised by the single
       anti-graph degree-sequence class (0,0,2,2,2,2,2,2,3,3) (Petersen minus 6
       edges).  In particular N_anti is odd (= prop:noq_odd).

This is the SAME kind of statement as rankG=4 => N_anti=6: a realizability
characterization of the anti-graph at fixed symplectic rank, not a formal
consequence of the quadratic form alone (the q-exists bucket realises BOTH
parities, so o + ell do not by themselves force the value).

Usage: python3 noq_odd_proof.py [N=5] [N_LAG=4000] [MAX_K5=600] [SEEDS=8]
Seeds used here (7000+53s, 31000+71s, 50000+97s) are disjoint from the other
paper19 scripts.
"""
import sys, time, random
from collections import Counter, defaultdict

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 5
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 600
SEEDS  = int(sys.argv[4]) if len(sys.argv) > 4 else 8

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

# ---- F2 linear algebra on python ints (bit i = coordinate i) ----
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
    m = len(rows)
    work = [[rows[i], 1 << i] for i in range(m)]; r = 0
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
    free = [c for c in range(n) if c not in pivcol]
    basis = []
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

def intrinsic_exists_and_Q(rays, basis):
    """Return (exists, Qe) where Qe encodes a particular solution Q(e_k) (bit k),
       or (False, None) if no intrinsic-q. Q(e_k)=1 iff bit k set in Qe."""
    d = len(basis); rows = []
    for r in rays:
        c = coords(r, basis); quad = 0
        bits = [i for i in range(d) if (c >> i) & 1]
        for a in range(len(bits)):
            for b in range(a+1, len(bits)): quad ^= symp(basis[bits[a]], basis[bits[b]])
        rows.append([c, quad])
    piv = {}; rank = 0
    for col in range(d):
        p = next((i for i in range(rank, len(rows)) if (rows[i][0] >> col) & 1), None)
        if p is None: continue
        rows[rank], rows[p] = rows[p], rows[rank]
        for i in range(len(rows)):
            if i != rank and (rows[i][0] >> col) & 1:
                rows[i][0] ^= rows[rank][0]; rows[i][1] ^= rows[rank][1]
        piv[col] = rank; rank += 1
    for lin, rhs in rows:
        if lin == 0 and rhs == 1: return (False, None)
    Qe = 0
    for col, ri in piv.items():
        if rows[ri][1] & 1: Qe |= (1 << col)
    return (True, Qe)

def Qval(v, basis, Qe):
    c = coords(v, basis); bits = [i for i in range(len(basis)) if (c >> i) & 1]; val = 0
    for i in bits:
        if (Qe >> i) & 1: val ^= 1
    for a in range(len(bits)):
        for b in range(a+1, len(bits)): val ^= symp(basis[bits[a]], basis[bits[b]])
    return val

def run(seed_base, seed_step, label):
    s1 = s3 = s4 = s5 = target = 0
    tot = noq = 0
    by_exists = {True: Counter(), False: Counter()}
    noq_nanti = Counter(); noq_degseq = Counter()
    for s in range(SEEDS):
        lags, adj = gen(seed_base + seed_step*s)
        for sh in k5s(lags, adj, MAX_K5):
            rays = [sh[(min(a, b), max(a, b))] for a in range(5) for b in range(a+1, 5)]
            basis = f2_basis(rays)
            if len(basis) != 8: continue
            G = [0]*10
            for i in range(10):
                for j in range(10):
                    if i != j and symp(rays[i], rays[j]): G[i] |= (1 << j)
            kerG = nullspace(G, 10); rankG = 10 - len(kerG)
            if (8, rankG, 8 - rankG) != (8, 6, 2): continue
            tot += 1
            Rspan = span(left_nullspace([coords(r, basis) for r in rays], 8))
            kerspan = span(kerG)
            def o(a):
                bits = [i for i in range(10) if (a >> i) & 1]; acc = 0
                for x in range(len(bits)):
                    for y in range(x+1, len(bits)):
                        if (G[bits[x]] >> bits[y]) & 1: acc ^= 1
                return acc
            if not (Rspan <= kerspan): s1 += 1
            if any(o(a ^ b) != (o(a) ^ o(b)) for a in kerG for b in kerG): s3 += 1
            lR0 = all(o(a) == 0 for a in Rspan)
            exists, Qe = intrinsic_exists_and_Q(rays, basis)
            if exists != lR0: s4 += 1
            T = 0
            for r in rays: T ^= r
            Nint = sum(popcount(G[i]) for i in range(10)) // 2
            allones = (1 << 10) - 1
            if exists and (Qval(T, basis, Qe) & 1) != (Nint & 1): s5 += 1
            by_exists[exists][Nint] += 1
            if not exists:
                noq += 1
                noq_nanti[Nint] += 1
                noq_degseq[tuple(sorted(popcount(G[i]) for i in range(10)))] += 1
                if Nint % 2 == 0: target += 1   # prop:noq_odd violation
    print(f"--- {label}  (seeds {seed_base}+{seed_step}s) ---")
    print(f"(8,6,2) configs: {tot}   no-q: {noq}")
    print(f"  S1 R<=kerG          : {s1}/{tot} violations")
    print(f"  S3 o linear on kerG : {s3}/{tot} violations")
    print(f"  S4 exists<=>o|_R==0 : {s4}/{tot} violations")
    print(f"  S5 Q(T)==N_anti     : {s5}/{tot} violations (over q-exists)")
    print(f"  prop:noq_odd (no-q => N_anti odd): {target}/{noq} violations")
    print(f"  no-q N_anti values : {dict(sorted(noq_nanti.items()))}")
    print(f"  no-q degree-seqs   : {dict(noq_degseq)}")
    print(f"  N_anti by exists=True : {dict(sorted(by_exists[True].items()))}")
    return tot, noq

if __name__ == "__main__":
    print(f"noq_odd_proof  N={N} N_LAG={N_LAG} MAX_K5={MAX_K5} SEEDS={SEEDS}\n")
    a = run(7000, 53, "family A")
    print()
    b = run(31000, 71, "family B (disjoint)")
    print(f"\nTOTAL (8,6,2)={a[0]+b[0]}  no-q={a[1]+b[1]} across two disjoint families.")
