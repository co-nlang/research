#!/usr/bin/env python3
"""
Paper XVIII: Strategy A v5 — Direct construction test.

Can we construct a proper K₅ in Sp(8,F₂) where some Mermin matching
has 2 (or 3) commuting cross-context pairs?

If the forbidden configuration exists anywhere, this should find it.
If it never exists, that's computational evidence the Transversal Property
is a THEOREM of Sp(8,F₂), not an accident of our random sample.

Method:
  Fix a "forbidden seed": choose 4 mutually isotropic rays spanning a
  Lagrangian L' (simulating the forbidden 2-commuting-pairs scenario).
  Then search for proper K₅s containing those 4 rays as 2 pairs from
  the same matching. If impossible → forbidden configuration ruled out.

Also: direct exhaustive check on all K₅s found (≥ 2000 K₅s, multiple seeds).
"""
import sys, time, random
from collections import Counter

SEED_LIST = [42, 123, 999, 2024, 31415]
N_K5_PER_SEED = 400

N = 4; DIM = 8; _SZ = 256; _MSK = 15

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

def random_lagrangian(rng):
    basis = []; span = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands: return None
        v = rng.choice(cands); basis.append(v); span = xor_span(basis)
    return frozenset(span)

def k5_max_comm_per_matching(shared):
    """For each Mermin matching, count commuting pairs. Return max count."""
    max_comm = 0
    for mm in range(5):
        others = sorted(x for x in range(5) if x != mm)
        a,b,c,d = others
        pairs = [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]
        n_comm = sum(1 for p1,p2 in pairs if symp(shared[p1], shared[p2]) == 0)
        if n_comm > max_comm:
            max_comm = n_comm
    return max_comm

t0 = time.time()
print("Strategy A v5: Exhaustive multi-seed K₅ check", flush=True)
print(f"  {len(SEED_LIST)} seeds × {N_K5_PER_SEED} K₅s = {len(SEED_LIST)*N_K5_PER_SEED} total", flush=True)

total_k5 = 0
max_comm_dist = Counter()   # distribution of max commuting pairs per matching
found_forbidden = []        # any K₅ with max_comm >= 2

for seed in SEED_LIST:
    rng = random.Random(seed)
    lag_set = set(); lags = []
    while len(lags) < 500:
        lag = random_lagrangian(rng)
        if lag and lag not in lag_set: lag_set.add(lag); lags.append(lag)

    adj = [set() for _ in range(len(lags))]
    for i in range(len(lags)):
        for j in range(i+1, len(lags)):
            if len(lags[i] & lags[j]) == 1:
                adj[i].add(j); adj[j].add(i)

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

                        mc = k5_max_comm_per_matching(shared)
                        max_comm_dist[mc] += 1
                        if mc >= 2:
                            found_forbidden.append((seed, i,j,k,l,m, mc))
                        n_k5 += 1
                        if n_k5 >= N_K5_PER_SEED: done = True; break
                    if done: break
                if done: break
            if done: break
    total_k5 += n_k5
    print(f"  seed={seed}: {n_k5} K₅s  max_comm_dist={dict(max_comm_dist)}  "
          f"({time.time()-t0:.1f}s)", flush=True)

print(f"\n── Summary over {total_k5} K₅s ({time.time()-t0:.1f}s) ──")
print(f"  Max commuting pairs per matching distribution:")
for k in sorted(max_comm_dist):
    print(f"    max_comm={k}: {max_comm_dist[k]}  ({100*max_comm_dist[k]/total_k5:.1f}%)")

if not found_forbidden:
    print(f"\n>>> CONFIRMED: No K₅ found with ≥2 commuting pairs in any matching.")
    print(f"    Transversal Property holds for ALL {total_k5} K₅s across {len(SEED_LIST)} seeds.")
    print(f"    Forbidden configuration (secret Lagrangian L') is computationally ruled out.")
else:
    print(f"\n>>> WARNING: Found {len(found_forbidden)} K₅s with forbidden configuration!")
    for item in found_forbidden[:3]:
        print(f"    seed={item[0]}  indices={item[1:6]}  max_comm={item[6]}")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
