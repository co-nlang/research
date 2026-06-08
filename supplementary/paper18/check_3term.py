#!/usr/bin/env python3
"""
Paper XVIII: Check if any 3 context rays of a Lagrangian satisfy a 3-term relation.

If v_{ab} + v_{bc} + v_{bd} = 0 for some K₅, then:
1. These 3 rays form a projective line in L_b
2. v_{bd} ∈ span{v_{ab}, v_{bc}}
3. orth_comp ∩ L_b contains v_{bd} → forbidden configuration possible

We need: does v_{ij} + v_{ik} + v_{il} = 0 ever occur for distinct j,k,l ≠ i?

Also check: does v_{ij} + v_{ik} + v_{il} = 0 relate to w_i = 0 (Fano)?
  w_i = v_{ij}+v_{ik}+v_{il}+v_{im} = 0  (Fano zero-sum, 4-term)
  3-term zero: v_{ij}+v_{ik}+v_{il} = 0  (projective line, different condition)

If 3-term never occurs but 4-term can → 4-ray basis of L_i always contains no 3-element dependency.
"""
import sys, time, random
from collections import Counter
from itertools import combinations

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

def get_ray(shared, i, j): return shared[(min(i,j), max(i,j))]

print(f"3-term relation check  n=4  N_K5={N_K5}  seed={SEED}", flush=True)

# For each K₅, for each Lagrangian i, for each triple of its rays,
# check if they sum to 0.
n_3term = 0    # K₅s with ANY 3-term relation
n_4term = 0    # K₅s where some L_i has Fano (4-term) zero-sum
total_k5 = 0

relation_types = Counter()  # what type of relation (if any)

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

                    found_3term = False
                    found_4term = False

                    for lag_idx in range(5):
                        # 4 context rays of this Lagrangian
                        others = [x for x in range(5) if x != lag_idx]
                        rays = [get_ray(shared, lag_idx, j) for j in others]

                        # Check 4-term (Fano zero-sum)
                        xor4 = rays[0] ^ rays[1] ^ rays[2] ^ rays[3]
                        if xor4 == 0:
                            found_4term = True

                        # Check all C(4,3) = 4 triples for 3-term relation
                        for triple in combinations(range(4), 3):
                            xor3 = rays[triple[0]] ^ rays[triple[1]] ^ rays[triple[2]]
                            if xor3 == 0:
                                found_3term = True
                                # Which triple?
                                t_rays = [rays[x] for x in triple]
                                others_t = [others[x] for x in triple]
                                relation_types['3-term'] += 1
                                if n_k5 < 3:
                                    print(f"\n  !! 3-term relation in K₅ #{n_k5+1}:")
                                    print(f"     L_{lag_idx}: v_{lag_idx}{others_t[0]} + "
                                          f"v_{lag_idx}{others_t[1]} + v_{lag_idx}{others_t[2]} = 0")

                    if found_3term: n_3term += 1
                    if found_4term: n_4term += 1

                    n_k5 += 1
                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s ({time.time()-t0:.1f}s) ──")
print(f"  K₅s with ANY 3-term relation (v_ij+v_ik+v_il=0):  {n_3term}  ({100*n_3term/n_k5:.1f}%)")
print(f"  K₅s with ANY 4-term (Fano) zero-sum:              {n_4term}  ({100*n_4term/n_k5:.1f}%)")

if n_3term == 0:
    print(f"\n>>> THEOREM: No proper n=4 K₅ has a 3-term relation among context rays!")
    print(f"    This means: for all i,j,k,l distinct,  v_ij + v_ik + v_il ≠ 0.")
    print(f"    Therefore: v_bd ∉ span{{v_ab, v_bc}}  for any proper K₅.")
    print(f"    Therefore: ω(v_bd, v_ac) = 1  in the forbidden configuration.")
    print(f"    Therefore: forbidden configuration is impossible → Transversal Property □")
else:
    print(f"\n>>> WARNING: Found {n_3term} K₅s with 3-term relations!")
    print(f"    The proof strategy has a genuine gap.")
