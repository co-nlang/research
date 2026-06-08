#!/usr/bin/env python3
"""Strategy A v4: Identify WHICH Lagrangians are in the orth_comp."""
import sys, time, random
from collections import Counter

N = 4; DIM = 8; _SZ = 256; _MSK = 15
random.seed(42); t0 = time.time()

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

def matching_pairs(m):
    others = sorted(x for x in range(5) if x != m)
    a,b,c,d = others
    return [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]

print(f"Strategy A v4: Which Lagrangians are in orth_comp?", flush=True)

n_k5 = 0; done = False
n_lag = len(lags)

which_lag = Counter()

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

                        if len(comm) != 1: continue

                        c_p1, c_p2, c_v1, c_v2 = comm[0]
                        for a_p1, a_p2, a_v1, a_v2 in anti:
                            span_3 = xor_span([c_v1, c_v2, a_v1])
                            orth_comp = set([0]) | {v for v in ALL_VEC
                                        if all(symp(v, s) == 0 for s in span_3)}

                            # Which Lagrangians are fully contained (7 nonzero vectors)?
                            full_lags = []
                            for li, lag in enumerate(five):
                                # lag is a frozenset of 7 nonzero vectors
                                # orth_comp includes 0 plus nonzero vectors
                                nonzero_orth = {v for v in orth_comp if v != 0}
                                if lag.issubset(nonzero_orth):
                                    full_lags.append(li)

                            which_lag[tuple(sorted(full_lags))] += 1

                    n_k5 += 1
                    if n_k5 >= 500: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s ({time.time()-t0:.1f}s) ──")
print(f"\nWhich Lagrangian indices are fully in orth_comp:")
for key in sorted(which_lag.keys()):
    cnt = which_lag[key]
    print(f"  L{key}: {cnt}")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
