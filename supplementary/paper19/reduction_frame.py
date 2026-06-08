#!/usr/bin/env python3
"""
Paper XIX, Remark rem:reduction  --  the symplectic-reduction frame and the
dimension-stratification of the realizability layer.

For every proper K5 in Sp(10,F2) the radical quotient  Wbar = W / rad(omega|_W)
is a non-degenerate symplectic space of dimension rankG, and each Lagrangian L_a
descends to an isotropic Lbar_a (its rays lie in the isotropic L_a, hence commute).
So a proper K5 projects to a five-Lagrangian configuration in Sp(rankG, F2), and
N_anti is the anticommuting count of the projected rays.

This script reports:
  (1) how often W is coisotropic (rad W = 10 - dim W);   [generic, NOT universal]
  (2) the projected rays of each L_a are isotropic;       [tautological sanity check]
  (3) the forced-stratum table: N_anti distribution by
        (dimW, rankG, radW, all-L_a-project-to-full-Lagrangian?, no-q bit),
      exhibiting that N_anti is pinned by these low-arity invariants through
      dimW=8 but splits at dimW=9 -- the realizability layer is itself
      dimension-stratified.

The two realizability problems are the small instances:
  rankG=4 -> Sp(4,2) ( = S6 ),  forced N_anti=6 at stratum level;
  rankG=6 + (no-q)  -> Sp(6,2),  forced N_anti=9 (needs the ell|_R selector).

Usage: python3 reduction_frame.py [N=5] [N_LAG=4000] [MAX_K5=500] [SEEDS=10]
Seeds 80000+131s, disjoint from the other paper19 scripts.
"""
import sys, time, random
from collections import Counter, defaultdict

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
    return rad

def main():
    idxp = {}; c = 0
    for a in range(5):
        for b in range(a+1, 5): idxp[(a, b)] = c; c += 1
    coiso_ok = coiso_tot = 0
    iso_viol = iso_tot = 0
    tab = defaultdict(Counter)
    for s in range(SEEDS):
        lags, adj = gen(80000 + 131*s)
        for sh in k5s(lags, adj, MAX_K5):
            rays = [sh[(min(a, b), max(a, b))] for a in range(5) for b in range(a+1, 5)]
            basis = f2_basis(rays); dimW = len(basis)
            G = [0]*10
            for i in range(10):
                for j in range(10):
                    if i != j and symp(rays[i], rays[j]): G[i] |= (1 << j)
            rankG = 10 - len(nullspace(G, 10)); radW = dimW - rankG
            neff = rankG // 2
            coiso_tot += 1
            if radW == 10 - dimW: coiso_ok += 1
            rad = radical_basis(basis); d0 = len(f2_basis(rad[:]))
            dims = []
            for a in range(5):
                vs = [rays[idxp[tuple(sorted((a, b)))]] for b in range(5) if b != a]
                dims.append(len(f2_basis(rad[:] + vs)) - d0)
                for x in range(len(vs)):
                    for y in range(x+1, len(vs)):
                        iso_tot += 1
                        if symp(vs[x], vs[y]) != 0: iso_viol += 1
            allfull = all(x == neff for x in dims)
            Rspan = span(left_nullspace([coords(r, basis) for r in rays], dimW))
            def o(a):
                bits = [i for i in range(10) if (a >> i) & 1]; acc = 0
                for x in range(len(bits)):
                    for y in range(x+1, len(bits)):
                        if (G[bits[x]] >> bits[y]) & 1: acc ^= 1
                return acc
            noq = 0 if all(o(a) == 0 for a in Rspan) else 1
            Nanti = sum(popcount(G[i]) for i in range(10)) // 2
            tab[(dimW, rankG, radW, allfull, noq)][Nanti] += 1
    print(f"reduction_frame  N={N} N_LAG={N_LAG} MAX_K5={MAX_K5} SEEDS={SEEDS}\n")
    print(f"(1) W coisotropic (radW == 10-dimW): {coiso_ok}/{coiso_tot} "
          f"({100*coiso_ok/coiso_tot:.1f}%, generic not universal)")
    print(f"(2) projected L_a isotropic (rays commute): violations {iso_viol}/{iso_tot} "
          f"(tautological)")
    print(f"\n(3) (dimW,rankG,radW,allfull,noq) -> N_anti  [single value = FORCED]:")
    for K in sorted(tab):
        d = tab[K]; n = sum(d.values())
        if n < 5: continue
        tag = "  <<FORCED " + str(list(d)[0]) if len(d) == 1 else ""
        print(f"  {K} n={n}: {dict(sorted(d.items()))}{tag}")

if __name__ == "__main__":
    main()
