#!/usr/bin/env python3
"""P8 optimized: Check sufficiency of Theorem 1.8 using adjacency graph."""

import itertools
from collections import defaultdict
import numpy as np

def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def add(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))

def gf2_rank(vectors):
    rows = [list(v) for v in vectors]
    rank = 0
    for col in range(6):
        pivot = None
        for r in range(rank, len(rows)):
            if rows[r][col] == 1:
                pivot = r; break
        if pivot is not None:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for r in range(len(rows)):
                if r != rank and rows[r][col] == 1:
                    rows[r] = [(rows[r][c] + rows[rank][c]) % 2 for c in range(6)]
            rank += 1
    return rank

def dim_intersection(L1, L2):
    combined = list(L1) + list(L2)
    r = gf2_rank(combined)
    return 6 - r

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
V_SET = set(p for p in ALL_POINTS if p[3]==0 and p[4]==0 and p[5]==0)

def span3(basis):
    a,b,c = basis
    return frozenset([a,b,c,add(a,b),add(a,c),add(b,c),add(a,add(b,c))])

def find_lagrangians():
    lagrangians, seen = [], set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis)<3: continue
        if not all(symplectic_form(u,v)==0 for u,v in itertools.combinations(basis,2)): continue
        subspace = span3(basis)
        if subspace not in seen:
            seen.add(subspace); lagrangians.append(subspace)
    return lagrangians

def get_fano_lines_in_lagrangian(lag_points):
    pts = list(lag_points); lines = set()
    for i in range(7):
        for j in range(i+1,7):
            s = add(pts[i],pts[j])
            if s in lag_points:
                lines.add(frozenset([pts[i],pts[j],s]))
    return list(lines)

I2 = np.array([[1,0],[0,1]], dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)
PAULI = {'I':I2,'X':X,'Y':Y,'Z':Z}
PAULI3_CACHE = {}

def vector_to_pauli_string(v):
    chars = []
    for q in range(3):
        x,z = v[q],v[q+3]
        if x==0 and z==0: chars.append('I')
        elif x==1 and z==0: chars.append('X')
        elif x==1 and z==1: chars.append('Y')
        elif x==0 and z==1: chars.append('Z')
    return ''.join(chars)

def get_pauli3(v):
    if v not in PAULI3_CACHE:
        s = vector_to_pauli_string(v)
        M = PAULI[s[0]]
        for c in s[1:]: M = np.kron(M, PAULI[c])
        PAULI3_CACHE[v] = M
    return PAULI3_CACHE[v]

def context_product_sign(ops):
    P = np.eye(8, dtype=complex)
    for v in ops: P = P @ get_pauli3(v)
    return int(round(P[0,0].real))

print("[1/5] Finding 135 Lagrangians...")
lagrangians = find_lagrangians()

print("\n[2/5] Extracting 945 contexts...")
contexts = []
for lag_idx, L in enumerate(lagrangians):
    lines = get_fano_lines_in_lagrangian(L)
    for line in lines:
        context_ops = tuple(p for p in L if p not in line)
        contexts.append((context_ops, lag_idx))

print("\n[3/5] Precomputing product signs...")
signs = [context_product_sign(ops) for ops,_ in contexts]

print("\n[4/5] Building adjacency and Lagrangian intersection map...")
nn = len(contexts)
ctx_sets = [set(ctx[0]) for ctx in contexts]

# Adjacency: contexts sharing exactly 1 operator
adj = [[] for _ in range(nn)]
for i in range(nn):
    for j in range(i+1,nn):
        if len(ctx_sets[i] & ctx_sets[j])==1:
            adj[i].append(j); adj[j].append(i)

# Lagrangian intersection map: which pairs of Lagrangians have dim=1?
print("  Computing Lagrangian pairwise intersections...")
lag_equi = defaultdict(list)  # lag_idx -> list of other lag_idx with dim=1
for i in range(135):
    for j in range(i+1,135):
        if dim_intersection(lagrangians[i], lagrangians[j]) == 1:
            lag_equi[i].append(j)
            lag_equi[j].append(i)

# Count equiangular pairs
n_equi_pairs = sum(len(v) for v in lag_equi.values()) // 2
print(f"  Equiangular Lagrangian pairs: {n_equi_pairs} out of {135*134//2}")

print("\n[5/5] Finding all equiangular K₅ via context K₅...")
# Key insight: We already know all 12,096 Mermin pentagrams are equiangular.
# We need to find ALL K₅ (both odd and even parity) from equiangular configs.
# Then check: what fraction of equiangular K₅ are Mermin (odd parity)?

# Strategy: Find all K₅ pentagrams (ignoring parity), check if their Lagrangians are equiangular.
# We already have the K₅ search code; just remove the parity filter.

total_k5 = 0
total_equi_k5 = 0
total_equi_mermin = 0
total_equi_nonmermin = 0
parity_dist_equi = defaultdict(int)
parity_dist_all = defaultdict(int)

# Check if a set of 5 Lagrangian indices is equiangular
def is_equiangular_lag_set(lag_indices):
    for a in range(5):
        for b in range(a+1,5):
            if dim_intersection(lagrangians[lag_indices[a]], lagrangians[lag_indices[b]]) != 1:
                return False
    return True

# Precompute equiangular status for all 5-tuples that appear in K₅
# Actually, let's just check on the fly

import time
t0 = time.time()

for i in range(nn):
    si = set(adj[i])
    for j_pos in range(len(adj[i])):
        j = adj[i][j_pos]
        sj = set(adj[j])
        common_k = si & sj
        for k in common_k:
            if k <= j: continue
            sk = set(adj[k])
            common_m = common_k & sk
            for m in common_m:
                if m <= k: continue
                sm = set(adj[m])
                common_p = common_m & sm
                for p in common_p:
                    if p <= m: continue

                    shared = []
                    clique = [i,j,k,m,p]
                    valid = True
                    for a in range(5):
                        for b in range(a+1,5):
                            inter = ctx_sets[clique[a]] & ctx_sets[clique[b]]
                            if len(inter)!=1: valid=False; break
                            shared.append(next(iter(inter)))
                        if not valid: break
                    if not valid: continue
                    if len(set(shared))!=10: continue

                    total_k5 += 1

                    lag_indices = [contexts[idx][1] for idx in clique]
                    parity = sum(1 for idx in clique if signs[idx]==-1)
                    parity_dist_all[parity] += 1

                    # Check equiangular (only for a sample to save time)
                    if total_k5 % 100 == 0:
                        elapsed = time.time() - t0
                        print(f"  K₅: {total_k5}, equi: {total_equi_k5} ({elapsed:.1f}s)")

                    # Check equiangular
                    if is_equiangular_lag_set(lag_indices):
                        total_equi_k5 += 1
                        parity_dist_equi[parity] += 1
                        if parity % 2 == 1:
                            total_equi_mermin += 1
                        else:
                            total_equi_nonmermin += 1

print(f"\n  Final: K₅: {total_k5}, equi: {total_equi_k5} ({time.time()-t0:.1f}s)")

print(f"\n{'='*70}")
print("P8: Sufficiency of Theorem 1.8")
print(f"{'='*70}")

print(f"\nTotal K₅ pentagrams (all): {total_k5}")
print(f"Total equiangular K₅: {total_equi_k5}")
print(f"  With odd parity (Mermin): {total_equi_mermin}")
print(f"  With even parity (non-Mermin): {total_equi_nonmermin}")
if total_equi_k5 > 0:
    print(f"  Mermin fraction among equiangular: {total_equi_mermin/total_equi_k5*100:.1f}%")

print(f"\nParity distribution (ALL K₅):")
for p in sorted(parity_dist_all.keys()):
    cnt = parity_dist_all[p]
    print(f"  {p} minus: {cnt} ({cnt/total_k5*100:.1f}%)")

print(f"\nParity distribution (EQUIANGULAR K₅):")
for p in sorted(parity_dist_equi.keys()):
    cnt = parity_dist_equi[p]
    print(f"  {p} minus: {cnt} ({cnt/total_equi_k5*100:.1f}%)")

# Check: are ALL K₅ equiangular?
print(f"\nNon-equianglar K₅: {total_k5 - total_equi_k5}")
if total_k5 - total_equi_k5 > 0:
    print(f"  Non-equianglar fraction: {(total_k5 - total_equi_k5)/total_k5*100:.1f}%")
