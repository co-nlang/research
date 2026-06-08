#!/usr/bin/env python3
"""
Paper XIX -- low-rank rigidity, RIGOROUS backing + empirical strata.

Two independent layers:

(A) GRAPH-THEORETIC THEOREM (exhaustive, seed-free):
    Over all 2^15 subgraphs of the Petersen graph K(5,2), the F2-rank of the
    adjacency matrix vs the edge count. Establishes the load-bearing bound
        rankG = 4  =>  N_anti <= 6           (rank-4 subgraphs cap at 6 edges)
    and shows the bound is sharp only for a specific family (not all rank-4
    subgraphs reach 6) -- which is why the LOWER bound N_anti>=6 is NOT
    graph-theoretic and must come from realizability (the Maslov problem).

(B) EMPIRICAL STRATA (multi-seed, proper K5 in Sp(2n,F2)):
    rankG=0 <=> N_anti=0 (tautological), rankG=4 => N_anti=6 (conjectural =),
    and the rarity of rankG=2.

Usage: python3 lowrank_rigidity.py [n=5] [n_lag=3000] [max_k5=600] [seeds=8]
"""
import sys, time, random
from collections import Counter, defaultdict
from itertools import combinations

# ----------------------------------------------------------------------
# (A) Exhaustive Petersen-subgraph theorem  (no randomness)
# ----------------------------------------------------------------------
def petersen_edges():
    verts = list(combinations(range(5), 2))           # 10 cross-context rays
    edges = []
    for a in range(10):
        for b in range(a+1, 10):
            if set(verts[a]).isdisjoint(verts[b]):    # disjoint index pairs
                edges.append((a, b))
    assert len(edges) == 15
    return edges

def f2rank_sym(rows, n):
    rows = rows[:]; rank = 0
    for col in range(n):
        piv = None
        for i in range(rank, n):
            if (rows[i] >> col) & 1: piv = i; break
        if piv is None: continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(n):
            if i != rank and (rows[i] >> col) & 1: rows[i] ^= rows[rank]
        rank += 1
    return rank

def exhaustive_petersen():
    edges = petersen_edges()
    rank_edges = defaultdict(set)          # rank -> set of edge counts realized
    rank_max   = defaultdict(int)
    # also: among rank-4 subgraphs, which edge counts and how connected
    rank4_by_edges = Counter()
    for mask in range(1 << 15):
        rows = [0]*10; ne = 0
        for e in range(15):
            if (mask >> e) & 1:
                a, b = edges[e]; rows[a] |= 1 << b; rows[b] |= 1 << a; ne += 1
        r = f2rank_sym(rows, 10)
        rank_edges[r].add(ne)
        if ne > rank_max[r]: rank_max[r] = ne
        if r == 4: rank4_by_edges[ne] += 1
    print("=== (A) EXHAUSTIVE Petersen-subgraph theorem (all 2^15) ===")
    for r in sorted(rank_max):
        print(f"  rank={r:2d}: edge-counts={sorted(rank_edges[r])}  MAX={rank_max[r]}")
    print(f"\n  THEOREM rankG=4 => N_anti<=6 : rank-4 max edges = {rank_max[4]}  "
          f"({'OK' if rank_max[4]==6 else 'FAIL'})")
    print(f"  rank-4 subgraphs by edge count: {dict(sorted(rank4_by_edges.items()))}")
    print(f"  -> lower bound N_anti>=6 is NOT graph-theoretic "
          f"(rank-4 subgraphs with <6 edges exist: "
          f"{sorted(e for e in rank4_by_edges if e<6)})")
    print()

# ----------------------------------------------------------------------
# (B) Empirical strata over proper K5  (multi-seed)
# ----------------------------------------------------------------------
def run_empirical(N, N_LAG, MAX_K5, SEEDS):
    SZ = 1 << (2*N); MSK = (1 << N) - 1
    PN = [bin(i).count('1') & 1 for i in range(1 << N)]
    XT = [[PN[i & j] for j in range(1 << N)] for i in range(1 << N)]
    def symp(v, w): return XT[v & MSK][(w >> N) & MSK] ^ XT[(v >> N) & MSK][w & MSK]
    def xspan(b):
        s = {0}
        for x in b: s |= {y ^ x for y in s}
        return s
    def f2rank(vs):
        bs = []
        for v in vs:
            x = v
            for b in bs: x = min(x, x ^ b)
            if x: bs.append(x); bs.sort(reverse=True)
        return len(bs)
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
        return lags, adj, symp, f2rank
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
    def f2rank_rows(rows, ncols):
        rows = list(rows); rank = 0
        for col in range(ncols):
            piv = None
            for i in range(rank, len(rows)):
                if (rows[i] >> col) & 1: piv = i; break
            if piv is None: continue
            rows[rank], rows[piv] = rows[piv], rows[rank]
            for i in range(len(rows)):
                if i != rank and (rows[i] >> col) & 1: rows[i] ^= rows[rank]
            rank += 1
        return rank

    strat = defaultdict(Counter)     # rankG -> Counter(N_anti)
    rankG_dist = Counter(); total = 0
    print(f"=== (B) EMPIRICAL strata, n={N}, seeds={SEEDS} ===")
    for s in range(SEEDS):
        lags, adj, symp, f2rank = gen(1000 + 37*s)
        for sh in k5s(lags, adj, MAX_K5):
            def Rr(x, y): return sh[(min(x, y), max(x, y))]
            rays = [Rr(a, b) for a in range(5) for b in range(a+1, 5)]
            Nanti = 0
            for a in range(10):
                for b in range(a+1, 10):
                    Nanti += symp(rays[a], rays[b])
            dimW = f2rank(rays)
            G = [0]*10
            for x in range(10):
                for y in range(10):
                    if x != y and symp(rays[x], rays[y]): G[x] |= 1 << y
            rankG = f2rank_rows(G, 10)
            strat[rankG][Nanti] += 1; rankG_dist[rankG] += 1; total += 1
    print(f"  K5 total={total}  rankG dist={dict(sorted(rankG_dist.items()))}")
    for r in sorted(strat):
        d = dict(sorted(strat[r].items()))
        det = "DETERMINISTIC" if len(d) == 1 else "spread"
        print(f"  rankG={r:2d}: N_anti={d}  [{det}]")
    r2 = rankG_dist.get(2, 0)
    print(f"\n  rankG=2 occurrences: {r2}/{total} "
          f"({100*r2/total:.3f}%)  -> rare but NOT forbidden")

if __name__ == "__main__":
    N      = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
    MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 600
    SEEDS  = int(sys.argv[4]) if len(sys.argv) > 4 else 8
    exhaustive_petersen()
    run_empirical(N, N_LAG, MAX_K5, SEEDS)
