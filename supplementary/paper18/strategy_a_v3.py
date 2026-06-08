#!/usr/bin/env python3
"""
Paper XVIII: Strategy A — Forbidden Configuration (impossibility test).

Key finding from v2: comm+anti pair gives 5/6 isotropic, lag_intersections=(0,2,2,2,2).
The 4 rays span rank=4, intersect 4 Lagrangians in dim=2 each.

If the 6th pair were also isotropic, these 4 rays would span a 4-dim
isotropic subspace L' in F₂⁸. Since n=4, L' would be a Lagrangian!

This script tests: can a proper K₅ in Sp(8,F₂) coexist with a Lagrangian
L' that has dim=2 intersection with 4 of its Lagrangians?

If not, this proves the forbidden configuration is impossible →
no matching can have 2 commuting pairs → Transversal Property.
"""
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

def extend_to_lagrangian(isotropic_basis):
    """Extend an isotropic set to a full Lagrangian."""
    basis = list(isotropic_basis)
    span = xor_span(basis)
    for _ in range(N - len(basis)):
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

print(f"Strategy A: Forbidden Configuration Impossibility Test  n=4", flush=True)

n_k5 = 0; done = False
n_lag = len(lags)

# For each K₅, for each matching, construct the "forbidden" Lagrangian L'
# from the 4 rays (assuming the 6th pair is also isotropic).
# Then check: can L' coexist with the K₅ structure?

forbidden_lag_stats = Counter()
contradictions = Counter()

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

                        # Get the 4 rays from comm pair + 1 anti pair
                        c_p1, c_p2, c_v1, c_v2 = comm[0]
                        for a_p1, a_p2, a_v1, a_v2 in anti:
                            rays_4 = [c_v1, c_v2, a_v1, a_v2]

                            # The 4 rays span rank=4 (verified in v2)
                            # They have 5/6 isotropic pairings
                            # The non-isotropic pair is (a_v1, a_v2)

                            # Strategy A: what if we REPLACE a_v2 with a_v2'
                            # such that symp(a_v1, a_v2') = 0?
                            # Then all 4 rays would be mutually isotropic → Lagrangian L'

                            # Instead of modifying, let's check:
                            # The span of these 4 rays is rank=4.
                            # If we add the constraint symp(a_v1, a_v2)=0,
                            # does this force a contradiction?

                            # Key test: the span of {c_v1, c_v2, a_v1} is rank=3.
                            # a_v2 is NOT in this span (rank=4).
                            # But a_v2 has symp(a_v1, a_v2)=1.
                            # If we required symp(a_v1, a_v2)=0, a_v2 would be
                            # in the orthogonal complement of span{c_v1,c_v2,a_v1}.

                            # Let's check: what is the orthogonal complement?
                            span_3 = xor_span([c_v1, c_v2, a_v1])
                            orth_comp = [v for v in ALL_VEC
                                        if all(symp(v, s) == 0 for s in span_3)]

                            # How many of these are in the K₅ Lagrangians?
                            in_lag_counts = {}
                            for li, lag in enumerate(five):
                                cnt = sum(1 for v in orth_comp if v in lag)
                                in_lag_counts[li] = cnt

                            forbidden_lag_stats[tuple(sorted(in_lag_counts.values()))] += 1

                            # Check: is a_v2 in orth_comp? (it shouldn't be, since symp(a_v1,a_v2)=1)
                            a_v2_in_orth = a_v2 in orth_comp
                            if a_v2_in_orth:
                                contradictions["a_v2 in orth_comp (unexpected!)"] += 1

                            # Check: how many vectors in orth_comp are in each Lagrangian?
                            # If orth_comp ∩ L_a has dim > 2 for some a, contradiction?

                    n_k5 += 1
                    if n_k5 >= 500: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s ({time.time()-t0:.1f}s) ──")
print(f"\nOrthogonal complement intersection with K₅ Lagrangians:")
for key in sorted(forbidden_lag_stats.keys()):
    cnt = forbidden_lag_stats[key]
    print(f"  {key}: {cnt}")

if contradictions:
    print(f"\nContradictions found:")
    for key, cnt in contradictions.items():
        print(f"  {key}: {cnt}")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
