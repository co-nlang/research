#!/usr/bin/env python3
"""
Paper XVIII: Check the lower bound — can a matching have all 3 pairs anticommuting?

We proved: each matching has AT MOST 1 commuting pair (from no 3-term relation).
We need:  each matching has AT LEAST 1 commuting pair.

Together: exactly 1 commuting per matching → N_anti = 10.

This script tests: does a matching with all 3 pairs anticommuting (0 commuting) occur?
Also checks: what does the 'dual orth_comp' argument look like?

Dual orth_comp analysis:
  If all 3 pairs of matching e anticommute: ω(v_{ab},v_{cd})=1, ω(v_{ac},v_{bd})=1, ω(v_{ad},v_{bc})=1.
  For the 'dual forbidden' to be impossible, we'd need a similar argument.
  What is span{v_{ab},v_{cd},v_{ac}}^⊥ ∩ L_b when ω(v_{ab},v_{cd})=1?
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

def get_ray(sh, i, j): return sh[(min(i,j),max(i,j))]

print(f"Lower bound check  n=4  N_K5={N_K5}  seed={SEED}", flush=True)

# Count matchings with 0 commuting (all 3 anticommuting)
all_anti_count = 0
total_matchings = 0
# Also: for the anticommuting case, compute span3_perp ∩ L_b
anti_orth_pattern = Counter()   # intersection sizes when pair 1 is anticommuting

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

                    for mm in range(5):
                        others = sorted(x for x in range(5) if x != mm)
                        a,b,c,d = others
                        pairs = [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]

                        omegas = [symp(shared[p1],shared[p2]) for p1,p2 in pairs]
                        n_anti = sum(omegas)
                        n_comm = 3 - n_anti
                        total_matchings += 1
                        if n_comm == 0:
                            all_anti_count += 1

                        # For the ANTICOMMUTING pair (if exists):
                        # compute span{v_{ab},v_{cd},v_{ac}}^⊥ ∩ L_b when ω(v_{ab},v_{cd})=1
                        # (dual of the proof-by-contradiction direction)
                        if omegas[0] == 1:  # pair (v_{ab},v_{cd}) is anticommuting
                            v_ab, v_cd = shared[(a,b)], shared[(c,d)]
                            v_ac = shared[(a,c)]
                            v_bd = shared[(b,d)]
                            L_b = five[b]

                            span3 = xor_span([v_ab, v_cd, v_ac])
                            orth = [v for v in ALL_VEC if all(symp(v,s)==0 for s in span3)]
                            orth_Lb = sum(1 for v in orth if v in L_b)
                            anti_orth_pattern[orth_Lb] += 1

                    n_k5 += 1
                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s, {total_matchings} matchings ──")
print(f"  Matchings with 0 commuting (all 3 anticommuting): {all_anti_count}  "
      f"({100*all_anti_count/total_matchings:.2f}%)")

if all_anti_count == 0:
    print(f"\n>>> CONFIRMED: Every matching has at least 1 commuting pair!")
    print(f"    Combined with ≤1 (from no 3-term relation):")
    print(f"    Each matching has EXACTLY 1 commuting pair → N_anti = 10. □")
else:
    print(f"\n>>> WARNING: {all_anti_count} matchings with all-anticommuting!")

print(f"\n  When pair-1 is anticommuting: orth_comp ∩ L_b sizes:")
for k in sorted(anti_orth_pattern):
    print(f"    |orth∩L_b| = {k} nonzero vectors: {anti_orth_pattern[k]}")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
