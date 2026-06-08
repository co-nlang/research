#!/usr/bin/env python3
"""
Paper XVIII: Count Fano zero-sum Lagrangians per K₅ in Sp(8,F₂).

Hypothesis: in every proper n=4 K₅, exactly ONE Lagrangian satisfies
w_a = XOR_{b≠a} v_{ab} = 0 (Fano zero-sum).

If true: the 'Fano Lagrangian' is a canonical special member of each K₅.
"""
import sys, time, random
from collections import Counter

N_K5 = int(sys.argv[1]) if len(sys.argv) > 1 else 500
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

adj = [set() for _ in range(len(lags))]
for i in range(len(lags)):
    for j in range(i+1, len(lags)):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)

def get_ray(shared, i, j):
    return shared[(min(i,j), max(i,j))]

print(f"Counting Fano zero-sum Lagrangians per K₅  n=4  seed={SEED}", flush=True)

fano_count_dist = Counter()   # how many w_a=0 per K₅
n_anti_by_fano  = Counter()   # N_anti per K₅ (should always be 10)

n_k5 = 0; done = False
n_lag = len(lags)

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
                    # Build shared rays
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

                    # Count w_a = 0
                    n_fano = 0
                    fano_idx = []
                    for a in range(5):
                        wa = 0
                        for b in range(5):
                            if b != a: wa ^= get_ray(shared, a, b)
                        if wa == 0:
                            n_fano += 1
                            fano_idx.append(a)

                    # N_anti
                    n_anti = sum(
                        1 for (p,q),vpq in shared.items()
                          for (r,s),vrs in shared.items()
                          if (r,s)>(p,q) and not ({p,q}&{r,s}) and symp(vpq,vrs)==1
                    )

                    fano_count_dist[n_fano] += 1
                    n_anti_by_fano[(n_fano, n_anti)] += 1
                    n_k5 += 1
                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s ──")
print(f"  Fano count distribution (# Lagrangians with w_a=0 per K₅):")
for k in sorted(fano_count_dist):
    print(f"    {k} Lagrangians: {fano_count_dist[k]} K₅s  ({100*fano_count_dist[k]/n_k5:.1f}%)")

print(f"\n  (n_fano, N_anti) distribution:")
for key in sorted(n_anti_by_fano):
    print(f"    {key}: {n_anti_by_fano[key]}")

if fano_count_dist.get(1, 0) == n_k5:
    print(f"\n>>> THEOREM CANDIDATE: Every proper n=4 K₅ has EXACTLY ONE Fano Lagrangian!")
    print(f"    (w_a = XOR of 4 rays = 0 for exactly one a per K₅)")
elif fano_count_dist.get(0, 0) == n_k5:
    print(f"\n>>> ALL K₅s have zero Fano Lagrangians.")
else:
    print(f"\n>>> MIXED: Fano count varies across K₅s.")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
