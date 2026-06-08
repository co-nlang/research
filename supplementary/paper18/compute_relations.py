#!/usr/bin/env python3
"""
Paper XVIII: Compute the 2 linear relations among the 10 context rays of n=4 K₅s.

For a proper K₅ in Sp(8,F₂), the 10 rays v_{ij} lie in F₂^8 (dim 8).
Prediction: rank({v_{ij}}) = 8, giving exactly 2 F₂-linear relations.
These two relations constrain the ω-pattern → Σ_m = 0 → N_anti = 10.

Usage: python3 compute_relations.py [n_k5=10] [seed=42]
"""
import sys, time, random
from collections import Counter

N_K5 = int(sys.argv[1]) if len(sys.argv) > 1 else 10
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 42

N = 4; DIM = 8; _SZ = 256; _MSK = 15
random.seed(SEED); t0 = time.time()

_PN = [bin(i).count('1') & 1 for i in range(16)]
_XT = [[_PN[i & j] for j in range(16)] for i in range(16)]
def symp(v, w):
    return _XT[v & _MSK][(w >> N) & _MSK] ^ _XT[(v >> N) & _MSK][w & _MSK]

def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)): s ^= basis[i] if (mask >> i) & 1 else 0
        if s: span.add(s)
    return span

ALL_VEC = list(range(1, _SZ))
def random_lagrangian():
    basis = []; span = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands: return None
        v = random.choice(cands); basis.append(v); span = xor_span(basis)
    return frozenset(span)

lag_set = set(); lags = []
while len(lags) < 500:
    lag = random_lagrangian()
    if lag and lag not in lag_set: lag_set.add(lag); lags.append(lag)
n_lag = len(lags)

adj = [set() for _ in range(n_lag)]
for i in range(n_lag):
    for j in range(i+1, n_lag):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)
print(f"[init] {n_lag} Lagrangians, adjacency done  ({time.time()-t0:.1f}s)", flush=True)

def null_space_f2(rays_list):
    """Null space of matrix M (rows = rays as DIM-bit vectors) over F₂.
    Returns list of frozensets: each is the support of one relation."""
    n_r = len(rays_list)
    # Augmented matrix [M | I] of size n_r × (DIM + n_r)
    M = []
    for i, r in enumerate(rays_list):
        row = [(r >> j) & 1 for j in range(DIM)] + [int(j == i) for j in range(n_r)]
        M.append(row)
    W = DIM + n_r
    pivot_row = 0
    for col in range(DIM):
        found = next((r for r in range(pivot_row, n_r) if M[r][col]), None)
        if found is None: continue
        M[found], M[pivot_row] = M[pivot_row], M[found]
        for r in range(n_r):
            if r != pivot_row and M[r][col]:
                M[r] = [(M[r][j] ^ M[pivot_row][j]) for j in range(W)]
        pivot_row += 1
    return [frozenset(j for j in range(n_r) if row[DIM + j])
            for row in M if not any(row[:DIM])]

def analyze_k5(idx5):
    five = [lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a+1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1: return None
            shared[(a,b)] = next(iter(inter))
    if len(set(shared.values())) != 10: return None
    return shared

# Key set ordering: enumerate all 10 cross-context pairs in a canonical order
ALL_PAIRS = [(a,b) for a in range(5) for b in range(a+1,5)]  # 10 pairs, sorted

def pair_label(pair):
    return f"v{pair[0]}{pair[1]}"

# ── Find K₅s and compute relations ────────────────────────────────────────────
print(f"[1] Computing linear relations for {N_K5} K₅s...", flush=True)

n_k5 = 0; done = False
for i in range(n_lag):
    if done: break
    ai = adj[i]
    for j in ai:
        if j<=i or done: continue
        for k in (ai & adj[j]):
            if k<=j or done: continue
            for l in (ai & adj[j] & adj[k]):
                if l<=k or done: continue
                for m in (ai & adj[j] & adj[k] & adj[l]):
                    if m<=l: continue
                    shared = analyze_k5((i,j,k,l,m))
                    if shared is None: continue

                    # Build ordered list of 10 rays
                    rays = [shared[p] for p in ALL_PAIRS]
                    rank = 10 - len(null_space_f2(rays))
                    rels = null_space_f2(rays)

                    n_k5 += 1
                    print(f"\nK₅ #{n_k5}:")
                    print(f"  rank = {rank}  (10 rays in F₂^8)")
                    print(f"  {len(rels)} linear relations:")
                    for r_idx, rel in enumerate(rels):
                        rel_pairs = [ALL_PAIRS[k] for k in sorted(rel)]
                        rel_str = " ⊕ ".join(pair_label(p) for p in rel_pairs)
                        print(f"    R{r_idx+1}: {rel_str} = 0")
                        # Classify pairs by matching membership
                        for m_idx in range(5):
                            others = sorted(x for x in range(5) if x != m_idx)
                            a,b,c,d = others
                            m_pairs = {(a,b),(c,d),(a,c),(b,d),(a,d),(b,c)}
                            cross = m_pairs - {p for p in m_pairs if not ({p[0],p[1]} & set())}
                            # The 3 cross-context pairs in this matching:
                            match_cross = {(a,b),(c,d)}, {(a,c),(b,d)}, {(a,d),(b,c)}
                            in_rel = sum(1 for pair_set in match_cross
                                        if any(p in rel or tuple(reversed(p)) in rel
                                               for p in pair_set))
                        # Show which matchings each pair belongs to
                        for p in rel_pairs:
                            # Which matching m is this pair from?
                            pa, pb = p
                            for m_idx in range(5):
                                others = sorted(x for x in range(5) if x != m_idx)
                                a,b,c,d = others
                                match_edges = [(a,b),(c,d),(a,c),(b,d),(a,d),(b,c)]
                                # As cross-context pairs:
                                cross = [((a,b),(c,d)),((a,c),(b,d)),((a,d),(b,c))]
                                for cp in cross:
                                    if set(cp) == {p, (a,b)} or p in cp:
                                        pass  # complex, skip for now

                    # Compute N_anti and matchings
                    n_anti = sum(1 for p1 in ALL_PAIRS for p2 in ALL_PAIRS
                                 if p2 > p1 and not set(p1)&set(p2)
                                 and symp(shared[p1], shared[p2]) == 1)
                    print(f"  N_anti = {n_anti}")

                    # Show Σ_m values
                    sigs = []
                    for m_idx in range(5):
                        a,b,c,d = sorted(x for x in range(5) if x != m_idx)
                        s = (symp(shared[(a,b)],shared[(c,d)]) ^
                             symp(shared[(a,c)],shared[(b,d)]) ^
                             symp(shared[(a,d)],shared[(b,c)]))
                        sigs.append(s)
                    print(f"  Σ_m = {sigs}  (should be all 0)")

                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n[done]  ({time.time()-t0:.1f}s)")
