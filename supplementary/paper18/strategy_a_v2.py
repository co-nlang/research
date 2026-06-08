#!/usr/bin/env python3
"""
Paper XVIII: Strategy A — Forbidden Configuration (constructive approach).

Tests: for each matching in a proper K₅, take the 1 commuting pair +
1 anticommuting pair. Are the 4 rays "almost" isotropic?

If all 6 pairings were isotropic, this would be a forbidden configuration.
We measure how close each case is to forbidden.
"""
import sys, time, random
from collections import Counter

N = 4; DIM = 8; _SZ = 256; _MSK = 15
random.seed(42); t0 = time.time()

_PN = [bin(i).count('1') & 1 for i in range(16)]
_XT = [[_PN[i & j] for j in range(16)] for i in range(16)]
def symp(v, w):
    return _XT[v & _MSK][(w >> N) & _MSK] ^ _XT[(v >> N) & _MSK][w & _MSK]

def gf2_rank_int(vecs):
    """Compute GF(2) rank of integer vectors."""
    if not vecs: return 0
    rows = list(vecs)
    rank = 0
    for col in range(DIM):
        pivot = next((r for r in range(rank, len(rows)) if (rows[r] >> col) & 1), None)
        if pivot is None: continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for r in range(len(rows)):
            if r != rank and (rows[r] >> col) & 1:
                rows[r] ^= rows[rank]
        rank += 1
    return rank

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

adj = [set() for _ in range(len(lags))]
for i in range(len(lags)):
    for j in range(i+1, len(lags)):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)

def get_ray(shared, i, j):
    return shared[(min(i,j), max(i,j))]

ALL_PAIRS = [(a,b) for a in range(5) for b in range(a+1,5)]

def matching_pairs(m):
    others = sorted(x for x in range(5) if x != m)
    a,b,c,d = others
    return [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]

print(f"Strategy A: Forbidden Configuration Analysis  n=4  seed=42", flush=True)

n_k5 = 0; done = False
n_lag = len(lags)

almost_iso_count = Counter()
near_forbidden = Counter()

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
                    five = [lags[x] for x in (i,j,k,l,m)]
                    shared = {}
                    ok = True
                    for a in range(5):
                        for b in range(a+1, 5):
                            inter = five[a] & five[b]
                            if len(inter) != 1: ok = False; break
                            shared[(a,b)] = next(iter(inter))
                        if not ok: break
                    if not ok or len(set(shared.values())) != 10: continue

                    for mm in range(5):
                        pairs = matching_pairs(mm)
                        comm = []; anti = []
                        for p1, p2 in pairs:
                            v1, v2 = shared[p1], shared[p2]
                            if symp(v1, v2) == 0:
                                comm.append((p1, p2, v1, v2))
                            else:
                                anti.append((p1, p2, v1, v2))

                        if len(comm) != 1:
                            print(f"  WARNING: matching {mm} has {len(comm)} commuting!")
                            continue

                        c_p1, c_p2, c_v1, c_v2 = comm[0]
                        for a_p1, a_p2, a_v1, a_v2 in anti:
                            rays_4 = [c_v1, c_v2, a_v1, a_v2]
                            n_iso = 0
                            for x in range(4):
                                for y in range(x+1, 4):
                                    if symp(rays_4[x], rays_4[y]) == 0:
                                        n_iso += 1
                            almost_iso_count[n_iso] += 1

                            if n_iso >= 5:
                                lag_counts = {}
                                for li, lag in enumerate(five):
                                    cnt = sum(1 for r in rays_4 if r in lag)
                                    lag_counts[li] = cnt
                                rank = gf2_rank_int(rays_4)
                                near_forbidden[(n_iso, rank, tuple(sorted(lag_counts.values())))] += 1

                    n_k5 += 1
                    if n_k5 >= 500: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s ({time.time()-t0:.1f}s) ──")
total_tests = sum(almost_iso_count.values())
print(f"\nAlmost-isotropic distribution (4 rays from comm+anti pair):")
for n_iso in sorted(almost_iso_count.keys()):
    cnt = almost_iso_count[n_iso]
    pct = 100 * cnt / total_tests
    marker = " ← FORBIDDEN!" if n_iso == 6 else ""
    print(f"  {n_iso}/6 isotropic pairs: {cnt} ({pct:.1f}%){marker}")

if near_forbidden:
    print(f"\nNear-forbidden configs (n_iso >= 5):")
    for key in sorted(near_forbidden.keys()):
        n_iso, rank, lag_dist = key
        cnt = near_forbidden[key]
        print(f"  n_iso={n_iso}, rank={rank}, lag_intersections={lag_dist}: {cnt}")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
