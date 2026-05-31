#!/usr/bin/env python3
"""P7: Analyze the 10 intersection rays of equiangular Lagrangian configuration."""

import itertools
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

print("[1/4] Finding 135 Lagrangians...")
lagrangians = find_lagrangians()

print("\n[2/4] Extracting 945 contexts...")
contexts = []
for lag_idx, L in enumerate(lagrangians):
    lines = get_fano_lines_in_lagrangian(L)
    for line in lines:
        context_ops = tuple(p for p in L if p not in line)
        contexts.append((context_ops, lag_idx))

print("\n[3/4] Precomputing product signs...")
signs = [context_product_sign(ops) for ops,_ in contexts]

print("\n[4/4] Finding a sample Mermin pentagram and analyzing its 10 rays...")

nn = len(contexts)
ctx_sets = [set(ctx[0]) for ctx in contexts]
adj = [[] for _ in range(nn)]
for i in range(nn):
    for j in range(i+1,nn):
        if len(ctx_sets[i] & ctx_sets[j])==1:
            adj[i].append(j); adj[j].append(i)
adj_sets = [set(a) for a in adj]

# Find first Mermin pentagram (any type)
found = None
for i in range(nn):
    si = adj_sets[i]
    for j in adj[i]:
        sj = adj_sets[j]
        common_k = si & sj
        for k in common_k:
            if k<=j: continue
            sk = adj_sets[k]
            common_m = common_k & sk
            for m in common_m:
                if m<=k: continue
                sm = adj_sets[m]
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
                    parity = sum(1 for idx in clique if signs[idx]==-1)
                    if parity%2==0: continue

                    lag_indices = [contexts[idx][1] for idx in clique]
                    found = (clique, lag_indices, shared)
                    break
                if found: break
            if found: break
        if found: break
    if found: break

clique, lag_indices, shared = found
Ls = [lagrangians[li] for li in lag_indices]

print(f"\nFound Mermin pentagram:")
print(f"  Context indices: {clique}")
print(f"  Lagrangian indices: {lag_indices}")
print(f"  Context signs: {[signs[idx] for idx in clique]}")

# Get the 10 intersection rays
print(f"\n--- 10 Intersection Rays ---")
rays = {}
ray_list = []
ray_keys = []
for a in range(5):
    for b in range(a+1,5):
        # Find intersection: check which vector in Ls[a] is also in Ls[b]
        for v in Ls[a]:
            if v in Ls[b]:
                rays[(a,b)] = v
                ray_list.append(v)
                ray_keys.append((a,b))
                pauli = vector_to_pauli_string(v)
                print(f"  R_{a}{b} = {v} -> {pauli}")
                break

# Compare with shared operators
shared_set = set(shared)
ray_set = set(ray_list)
print(f"\n  Shared operators == Intersection rays? {shared_set == ray_set}")

# Span of 10 rays
span_rank = gf2_rank(ray_list)
print(f"\n--- Span of 10 Rays ---")
print(f"  Dimension of span: {span_rank} (out of 6)")

# Linear dependencies: each Lagrangian has 4 rays summing to 0
print(f"\n--- Dependencies Within Each Lagrangian ---")
for i in range(5):
    lag_rays = []
    lag_names = []
    for j in range(5):
        if i != j:
            key = (min(i,j), max(i,j))
            lag_rays.append(rays[key])
            lag_names.append(f"R_{key[0]}{key[1]}")
    s = (0,0,0,0,0,0)
    for v in lag_rays:
        s = add(s, v)
    print(f"  L{i}: {' + '.join(lag_names)} = {s}")

# Collinearity: which triples of rays sum to a third ray in the set?
print(f"\n--- Collinearity Among 10 Rays ---")
collinear = []
for i in range(10):
    for j in range(i+1, 10):
        s = add(ray_list[i], ray_list[j])
        if s in ray_list:
            k = ray_list.index(s)
            if k > j:
                collinear.append((i,j,k))

print(f"  Number of collinear triples: {len(collinear)}")
for triple in collinear:
    names = [f"R_{ray_keys[i][0]}{ray_keys[i][1]}" for i in triple]
    print(f"    {names[0]}, {names[1]}, {names[2]}")

# Symplectic orthogonality pattern
print(f"\n--- Symplectic Orthogonality ---")
orthogonal_pairs = []
for i in range(10):
    for j in range(i+1, 10):
        if symplectic_form(ray_list[i], ray_list[j]) == 0:
            orthogonal_pairs.append((i,j))

print(f"  Orthogonal pairs: {len(orthogonal_pairs)} out of 45")
for pair in orthogonal_pairs[:15]:
    names = [f"R_{ray_keys[i][0]}{ray_keys[i][1]}" for i in pair]
    print(f"    {names[0]} ⟂ {names[1]}")

# Check: is this the Desargues configuration?
# Desargues: 10 points, 10 lines, 3 points per line, 3 lines per point
# Here: 10 points (rays), collinear triples form "lines"
print(f"\n--- Configuration Type ---")
print(f"  10 points (rays)")
print(f"  {len(collinear)} collinear triples (lines)")
# Count how many lines each point is on
point_lines = defaultdict(list)
for idx, triple in enumerate(collinear):
    for p in triple:
        point_lines[p].append(idx)

print(f"  Lines per point: {[len(point_lines[i]) for i in range(10)]}")
