#!/usr/bin/env python3
"""P4: Type F4 analysis — 1 Fano point, 4 transverse contexts."""

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

print(f"\n[5/5] Finding Type F4 pentagrams and analyzing...")
t1 = time.time()

type_f4_total = 0
type_f4_fano_point = defaultdict(int)  # which Fano point
type_f4_5sign = defaultdict(int)
type_f4_transverse_signs = defaultdict(int)  # 4 transverse context signs
type_f4_nontrans_sign = defaultdict(int)  # 1 non-transverse context sign
type_f4_distinct = defaultdict(int)  # distinct Fano point count

# Also track: is the single Fano point's context +I or -I?
type_f4_nontrans_plus = 0
type_f4_nontrans_minus = 0

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
                    clique_signs = [signs[idx] for idx in clique]
                    five_sign_key = tuple(sorted(clique_signs))

                    if transverse==4:
                        type_f4_total += 1
                        type_f4_5sign[five_sign_key] += 1
                        type_f4_distinct[distinct] += 1

                        # Which Fano point(s)?
                        if len(nonzero) >= 1:
                            fp = nonzero[0]
                            type_f4_fano_point[fp] += 1
                        else:
                            type_f4_fano_point[0] += 1  # no Fano point at all

                        # Transverse context signs (4 of them)
                        trans_idx = [ci for ci,fp_v in enumerate(fano_pts) if fp_v==0]
                        trans_s = tuple(clique_signs[ci] for ci in trans_idx)
                        n_minus_trans = sum(1 for s in trans_s if s==-1)
                        type_f4_transverse_signs[n_minus_trans] += 1

                        # Non-transverse context sign(s)
                        nontrans_idx = [ci for ci,fp_v in enumerate(fano_pts) if fp_v>0]
                        if len(nontrans_idx) >= 1:
                            nt_sign = clique_signs[nontrans_idx[0]]
                            type_f4_nontrans_sign[1 if nt_sign==-1 else 0] += 1
                            if nt_sign == -1:
                                type_f4_nontrans_minus += 1
                            else:
                                type_f4_nontrans_plus += 1

                    if type_f4_total % 5000 == 0:
                        print(f"  F4: {type_f4_total} ({time.time()-t1:.1f}s)")

print(f"\n  Done ({time.time()-t1:.1f}s)")

print(f"\n{'='*70}")
print("P4: Type F4 Analysis (1 Fano point, 4 transverse contexts)")
print(f"{'='*70}")

print(f"\nTotal Type F4: {type_f4_total}")

print(f"\nDistinct Fano point count distribution:")
for d in sorted(type_f4_distinct.keys()):
    cnt = type_f4_distinct[d]
    print(f"  {d} distinct: {cnt} ({cnt/type_f4_total*100:.1f}%)")

print(f"\nFano point distribution:")
for fp in sorted(type_f4_fano_point.keys()):
    cnt = type_f4_fano_point[fp]
    print(f"  Point {fp}: {cnt} ({cnt/type_f4_total*100:.1f}%)")

print(f"\nNon-transverse (single Fano context) sign:")
n_plus = type_f4_nontrans_sign.get(0,0)
n_minus = type_f4_nontrans_sign.get(1,0)
print(f"  +I: {n_plus} ({n_plus/type_f4_total*100:.1f}%)")
print(f"  -I: {n_minus} ({n_minus/type_f4_total*100:.1f}%)")

print(f"\n4 transverse context sign distribution:")
for n in range(5):
    cnt = type_f4_transverse_signs.get(n,0)
    print(f"  {n} minus: {cnt:>6} ({cnt/type_f4_total*100:.1f}%)")

print(f"\n5-context sign distribution:")
for pat in sorted(type_f4_5sign.keys()):
    cnt = type_f4_5sign[pat]
    print(f"  {str(pat).replace('1','+').replace('-1','-')}: {cnt} ({cnt/type_f4_total*100:.1f}%)")

print(f"\nTotal time: {time.time()-t0:.1f}s")
