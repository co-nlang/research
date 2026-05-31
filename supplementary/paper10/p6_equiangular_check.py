#!/usr/bin/env python3
"""P6: Check if ALL Mermin pentagrams have equiangular Lagrangian configuration."""

import itertools
from collections import defaultdict
import numpy as np
import time

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
FANO_LABEL = {(1,0,0):1,(0,1,0):2,(0,0,1):3,(1,1,0):4,(1,0,1):5,(0,1,1):6,(1,1,1):7}

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

t0 = time.time()
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

print("\n[4/5] Building adjacency...")
nn = len(contexts)
ctx_sets = [set(ctx[0]) for ctx in contexts]
adj = [[] for _ in range(nn)]
for i in range(nn):
    for j in range(i+1,nn):
        if len(ctx_sets[i] & ctx_sets[j])==1:
            adj[i].append(j); adj[j].append(i)
adj_sets = [set(a) for a in adj]

print(f"\n[5/5] Checking equiangular property for all Mermin pentagrams...")
t1 = time.time()

total_mermin = 0
equiangular_count = 0
non_equiangular_count = 0
non_equiangular_patterns = defaultdict(int)

# Also check by type
type_counts = defaultdict(int)
type_equiangular = defaultdict(int)

for i in range(nn):
    si = adj_sets[i]
    for j_pos in range(len(adj[i])):
        j = adj[i][j_pos]
        sj = adj_sets[j]
        parity_ij = (1 if signs[i]==-1 else 0)+(1 if signs[j]==-1 else 0)
        common_k = si & sj
        for k in common_k:
            if k<=j: continue
            sk = adj_sets[k]
            parity_ijk = parity_ij+(1 if signs[k]==-1 else 0)
            common_m = common_k & sk
            for m in common_m:
                if m<=k: continue
                sm = adj_sets[m]
                parity_ijkm = parity_ijk+(1 if signs[m]==-1 else 0)
                common_p = common_m & sm
                for p in common_p:
                    if p<=m: continue

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

                    parity = parity_ijkm+(1 if signs[p]==-1 else 0)
                    if parity%2==0: continue

                    total_mermin += 1

                    # Get Lagrangian indices
                    lag_indices = [contexts[idx][1] for idx in clique]

                    # Compute pairwise Lagrangian intersection dimensions
                    dims = []
                    for a in range(5):
                        for b in range(a+1,5):
                            d = dim_intersection(lagrangians[lag_indices[a]],
                                                 lagrangians[lag_indices[b]])
                            dims.append(d)

                    is_equiangular = all(d == 1 for d in dims)
                    if is_equiangular:
                        equiangular_count += 1
                    else:
                        non_equiangular_count += 1
                        pattern = tuple(sorted(dims))
                        non_equiangular_patterns[pattern] += 1

                    # Classify by type
                    fano_pts = []
                    for idx in clique:
                        _,lag_idx = contexts[idx]
                        L = lagrangians[lag_idx]
                        inter = L & V_SET
                        if len(inter)==1:
                            v = next(iter(inter))
                            fano_pts.append(FANO_LABEL[(v[0],v[1],v[2])])
                        elif len(inter)==0:
                            fano_pts.append(0)
                        else:
                            fano_pts.append(-1)

                    nonzero = [x for x in fano_pts if x>0]
                    distinct = len(set(nonzero))
                    transverse = fano_pts.count(0)

                    if transverse==0 and distinct==4:
                        type_str = "B"
                    elif transverse==2:
                        type_str = "F2"
                    elif transverse==4:
                        type_str = "F4"
                    elif transverse==0 and distinct==5:
                        type_str = "A"
                    else:
                        type_str = f"Other(t={transverse},d={distinct})"

                    type_counts[type_str] += 1
                    if is_equiangular:
                        type_equiangular[type_str] += 1

                    if total_mermin % 10000 == 0:
                        print(f"  Total: {total_mermin}, Equi: {equiangular_count} ({time.time()-t1:.1f}s)")

print(f"\n  Done ({time.time()-t1:.1f}s)")

print(f"\n{'='*70}")
print("P6: Equiangular Lagrangian Configuration Check")
print(f"{'='*70}")

print(f"\nTotal Mermin pentagrams: {total_mermin}")
print(f"Equiangular (all dims=1): {equiangular_count} ({equiangular_count/total_mermin*100:.1f}%)")
print(f"Non-equianglar: {non_equiangular_count} ({non_equiangular_count/total_mermin*100:.1f}%)")

if non_equiangular_count > 0:
    print(f"\nNon-equangular patterns:")
    for pat in sorted(non_equiangular_patterns.keys(), key=lambda x: -non_equiangular_patterns[x])[:10]:
        cnt = non_equiangular_patterns[pat]
        print(f"  {pat}: {cnt}")

print(f"\nEquiangular by type:")
for type_str in sorted(type_counts.keys()):
    total = type_counts[type_str]
    equi = type_equiangular.get(type_str, 0)
    print(f"  {type_str}: {equi}/{total} ({equi/total*100:.1f}%)")

print(f"\nTotal time: {time.time()-t0:.1f}s")
