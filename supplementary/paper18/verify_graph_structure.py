#!/usr/bin/env python3
"""
Paper XVIII: Verify the graph structure of anticommuting pairs for n=4 K₅s.

Prediction (collaborator): the 5 commuting cross-context pairs form a perfect
matching of K(5,2), so the 10 anticommuting pairs form K(5,2) minus a perfect
matching = two disjoint 5-cycles.

Usage: python3 verify_graph_structure.py [n=4] [n_lag=500] [max_k5=200] [seed=42]
"""
import sys, time, random
from collections import Counter, defaultdict
from functools import reduce
import operator

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 4
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 500
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 200
SEED   = int(sys.argv[4]) if len(sys.argv) > 4 else 42

DIM  = 2 * N; _SZ = 2**DIM; _MSK = (1 << N) - 1
random.seed(SEED); t0 = time.time()

_PN = [bin(i).count('1') & 1 for i in range(1 << N)]
_XT = [[_PN[i & j] for j in range(1 << N)] for i in range(1 << N)]
def symp(v, w):
    vlo = v & _MSK; vhi = (v >> N) & _MSK
    wlo = w & _MSK; whi = (w >> N) & _MSK
    return _XT[vlo][whi] ^ _XT[vhi][wlo]

def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)):
            if (mask >> i) & 1: s ^= basis[i]
        if s: span.add(s)
    return span

ALL_VEC = list(range(1, _SZ))
def random_lagrangian():
    basis = []; span = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands: return None
        v = random.choice(cands)
        basis.append(v); span = xor_span(basis)
    return frozenset(span)

print(f"n={N}  n_lag={N_LAG}  max_k5={MAX_K5}  seed={SEED}", flush=True)
lag_set = set(); lags = []
while len(lags) < N_LAG:
    lag = random_lagrangian()
    if lag and lag not in lag_set:
        lag_set.add(lag); lags.append(lag)
n_lag = len(lags)
print(f"[1] {n_lag} Lagrangians  ({time.time()-t0:.1f}s)", flush=True)

adj = [set() for _ in range(n_lag)]
for i in range(n_lag):
    for j in range(i+1, n_lag):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)
print(f"[2] adjacency done  ({time.time()-t0:.1f}s)", flush=True)

def cycle_lengths(edges, vertices):
    """Find cycle structure of a graph given as edge list."""
    nbr = defaultdict(list)
    for p1, p2 in edges:
        nbr[p1].append(p2); nbr[p2].append(p1)
    visited = set()
    lengths = []
    for start in vertices:
        if start in visited: continue
        curr = start; prev = None; L = 0
        while curr not in visited:
            visited.add(curr); L += 1
            nexts = [v for v in nbr[curr] if v != prev]
            if nexts: prev, curr = curr, nexts[0]
        lengths.append(L)
    return sorted(lengths)

def analyze_k5(idx5):
    five = [lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a+1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1: return None
            shared[(a,b)] = next(iter(inter))
    if len(set(shared.values())) != 10: return None

    comm = []; anti = []
    for (a,b),vab in shared.items():
        for (c,d),vcd in shared.items():
            if (c,d) <= (a,b) or {a,b} & {c,d}: continue
            (anti if symp(vab,vcd) == 1 else comm).append(((a,b),(c,d)))

    # Check commuting pairs = perfect matching of K(5,2)
    uses = Counter()
    for p1, p2 in comm:
        uses[p1] += 1; uses[p2] += 1
    is_pm = (len(comm) == 5 and
              all(v == 1 for v in uses.values()) and
              len(uses) == 10)

    # Find cycle structure of anticommuting subgraph
    vertices = list(shared.keys())
    cyc = cycle_lengths(anti, vertices)

    return len(comm), len(anti), is_pm, cyc

# ── K₅ search ─────────────────────────────────────────────────────────────────
print(f"[3] Analyzing K₅ structures...", flush=True)
results = Counter()
n_k5 = 0; done = False

for i in range(n_lag):
    if done: break
    ai = adj[i]
    for j in ai:
        if j<=i or done: continue
        aij = ai & adj[j]
        for k in aij:
            if k<=j or done: continue
            aijk = aij & adj[k]
            for l in aijk:
                if l<=k or done: continue
                aijkl = aijk & adj[l]
                for m in aijkl:
                    if m<=l: continue
                    r = analyze_k5((i,j,k,l,m))
                    if r is None: continue
                    n_comm, n_anti, is_pm, cyc = r
                    results[(n_comm, n_anti, is_pm, tuple(cyc))] += 1
                    n_k5 += 1
                    if n_k5 >= MAX_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n[4] Results  n={N}  K₅s analyzed: {n_k5}  ({time.time()-t0:.1f}s)")
print(f"    (n_comm, n_anti, is_perfect_matching, cycle_structure) → count")
for key, cnt in sorted(results.items()):
    n_c, n_a, pm, cyc = key
    pm_str = "PM ✓" if pm else "NOT PM"
    print(f"    comm={n_c}  anti={n_a}  [{pm_str}]  cycles={list(cyc)}  →  {cnt}")

if len(results) == 1:
    key = next(iter(results))
    n_c, n_a, pm, cyc = key
    if pm and list(cyc) == [5, 5]:
        print(f"\n>>> CONFIRMED: anticommuting graph = K(5,2) minus perfect matching = two 5-cycles.")
    elif pm:
        print(f"\n>>> Perfect matching confirmed; cycle structure: {list(cyc)}")
    else:
        print(f"\n>>> NOT a perfect matching for some K₅s.")
