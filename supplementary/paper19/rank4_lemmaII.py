#!/usr/bin/env python3
"""
Paper XIX -- structural anatomy of lemma (II) for the rank-4 reduction.

(II): radW = span(the rays lying in radW)  [= the isolated vertices of the anti-graph].

This script establishes the pieces of the proof of (II):

  FACT 1.  The ONLY F2-linear dependencies among triples of rays of a proper K5
           (n=5) are Fano stars  v_ij + v_ik + v_il = 0  (three rays of one
           Lagrangian).  These occur because B0 (no Fano vertex) FAILS for n>=5;
           every other index-pattern of a dependent triple contradicts properness.
           [verified: every rank<3 ray-triple has index pattern (4 indices; deg 3,1,1,1)]

  FACT 2.  In the (7,4,3) stratum the anti-graph has >=3 isolated vertices, and the
           inner rays contain 3 INDEPENDENT rays:
             * C6 type  (4 isolated): a triangle {v_cd,v_ce,v_de}  (pattern 3;2,2,2),
             * tree type (3 isolated): a "cherry+edge" (pattern 5;2,1,1,1,1).
           Neither pattern is a Fano star, so (by FACT 1) the triple is independent;
           being 3 independent vectors inside radW (dim 3) they SPAN it  ==>  (II).

Caveat / open: a fully unconditional (II) still needs that the realizable rank-4
anti-graph is C6 or tree (the doily lifting classification); the Fano star could
a priori break (II) only if the inner rays themselves formed a star, which does
not occur in the C6/tree structures.

Usage: python3 rank4_lemmaII.py [N=5] [N_LAG=4000] [MAX_K5=400] [SEEDS=8]
"""
import sys, time, random
from collections import Counter
from itertools import combinations

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 5
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 400
SEEDS  = int(sys.argv[4]) if len(sys.argv) > 4 else 8

SZ = 1 << (2*N); MSK = (1 << N) - 1
PN = [bin(i).count('1') & 1 for i in range(1 << N)]
XT = [[PN[i & j] for j in range(1 << N)] for i in range(1 << N)]
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

PAIRS = [(a, b) for a in range(5) for b in range(a+1, 5)]
def tri_pattern(t):
    deg = Counter(); uni = set()
    for i in t:
        for v in PAIRS[i]: deg[v] += 1; uni.add(v)
    return (len(uni), tuple(sorted(deg.values())))

def main():
    dep_pat = Counter()                  # FACT 1: patterns of dependent triples
    iso_pat = Counter()                  # FACT 2: inner-ray patterns by stratum type
    iso_rank = Counter()
    II_viol = 0; tot743 = 0
    for s in range(SEEDS):
        lags, adj = gen(7000 + 53*s)
        for sh in k5s(lags, adj, MAX_K5):
            rays = [sh[(min(a, b), max(a, b))] for a in range(5) for b in range(a+1, 5)]
            for t in combinations(range(10), 3):
                if len(f2_basis([rays[t[0]], rays[t[1]], rays[t[2]]])) < 3:
                    dep_pat[tri_pattern(t)] += 1
            basis = f2_basis(rays); dimW = len(basis)
            G = [0]*10
            for i in range(10):
                for j in range(10):
                    if i != j and symp(rays[i], rays[j]): G[i] |= (1 << j)
            rankG = 10 - len(nullspace(G, 10)); radW = dimW - rankG
            if (dimW, rankG, radW) != (7, 4, 3): continue
            tot743 += 1
            iso = [i for i in range(10) if G[i] == 0]
            typ = 'C6(4iso)' if len(iso) == 4 else ('tree(3iso)' if len(iso) == 3 else f'other({len(iso)})')
            # find an independent inner triple
            best = max((len(f2_basis([rays[i] for i in tt]))
                        for tt in combinations(iso, 3)), default=0) if len(iso) >= 3 else 0
            iso_pat[typ] += 1
            iso_rank[(typ, best)] += 1
            if best < 3: II_viol += 1   # no independent inner triple -> (II) would fail
    print(f"rank4_lemmaII  N={N}\n")
    print("FACT 1 -- index-patterns of dependent ray-triples (rank<3):")
    for k, v in dep_pat.most_common():
        tag = "  = FANO STAR (v_ij+v_ik+v_il=0)" if k == (4, (1, 1, 1, 3)) else "  (unexpected!)"
        print(f"   pattern (#indices, edge-degseq)={k}: {v}{tag}")
    print(f"\nFACT 2 -- (7,4,3) configs={tot743}, anti-graph type: {dict(iso_pat)}")
    print(f"   max rank of an inner triple, by type: {dict(iso_rank)}")
    print(f"   (II) would-fail (no rank-3 inner triple): {II_viol}/{tot743}")

if __name__ == "__main__":
    main()
