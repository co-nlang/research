#!/usr/bin/env python3
"""P2: Type B analysis — collinearity constraint vs KS sign pattern."""

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
    ncols = len(rows[0]) if rows else 0
    for col in range(ncols):
        pivot = None
        for r in range(rank, len(rows)):
            if rows[r][col] == 1:
                pivot = r
                break
        if pivot is not None:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for r in range(len(rows)):
                if r != rank and rows[r][col] == 1:
                    rows[r] = [(rows[r][c] + rows[rank][c]) % 2 for c in range(ncols)]
            rank += 1
    return rank

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
V_POINTS = [p for p in ALL_POINTS if p[3] == 0 and p[4] == 0 and p[5] == 0]
V_SET = set(V_POINTS)

FANO_LABEL = {
    (1,0,0): 1, (0,1,0): 2, (0,0,1): 3,
    (1,1,0): 4, (1,0,1): 5, (0,1,1): 6, (1,1,1): 7
}
FANO_LABEL_REV = {v: k for k, v in FANO_LABEL.items()}

def span3(basis):
    a, b, c = basis
    return frozenset([
        a, b, c, add(a, b), add(a, c), add(b, c), add(a, add(b, c))
    ])

def find_lagrangians():
    lagrangians = []
    seen = set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3:
            continue
        ti = all(symplectic_form(u, v) == 0 for u, v in itertools.combinations(basis, 2))
        if not ti:
            continue
        subspace = span3(basis)
        if subspace not in seen:
            seen.add(subspace)
            lagrangians.append(subspace)
    return lagrangians

def get_fano_lines_in_lagrangian(lag_points):
    pts = list(lag_points)
    lines = set()
    for i in range(7):
        for j in range(i+1, 7):
            s = add(pts[i], pts[j])
            if s in lag_points:
                lines.add(frozenset([pts[i], pts[j], s]))
    return list(lines)

I2 = np.array([[1, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}

PAULI3_CACHE = {}

def vector_to_pauli_string(v):
    chars = []
    for q in range(3):
        x, z = v[q], v[q + 3]
        if x == 0 and z == 0:
            chars.append('I')
        elif x == 1 and z == 0:
            chars.append('X')
        elif x == 1 and z == 1:
            chars.append('Y')
        elif x == 0 and z == 1:
            chars.append('Z')
    return ''.join(chars)

def get_pauli3(v):
    if v not in PAULI3_CACHE:
        s = vector_to_pauli_string(v)
        M = PAULI[s[0]]
        for c in s[1:]:
            M = np.kron(M, PAULI[c])
        PAULI3_CACHE[v] = M
    return PAULI3_CACHE[v]

def context_product_sign(ops):
    P = np.eye(8, dtype=complex)
    for v in ops:
        P = P @ get_pauli3(v)
    return int(round(P[0, 0].real))

FANO_LINES = [
    {1, 2, 4}, {1, 3, 5}, {1, 6, 7},
    {2, 3, 6}, {2, 5, 7}, {3, 4, 7}, {4, 5, 6}
]

def find_collinear_triple(fano_labels):
    """Find which 3 of the 4 distinct Fano points are collinear."""
    pts = set(fano_labels)
    for line in FANO_LINES:
        inter = sorted(line & pts)
        if len(inter) == 3:
            return tuple(inter)
    return None

t0 = time.time()

print("[1/5] Finding 135 Lagrangians...")
lagrangians = find_lagrangians()
print(f"  Done ({time.time()-t0:.1f}s)")

print("\n[2/5] Extracting 945 contexts...")
contexts = []
for lag_idx, L in enumerate(lagrangians):
    lines = get_fano_lines_in_lagrangian(L)
    for line_idx, line in enumerate(lines):
        context_ops = tuple(p for p in L if p not in line)
        contexts.append((context_ops, lag_idx, line_idx))

print("\n[3/5] Precomputing product signs...")
signs = []
for i, (ops, _, _) in enumerate(contexts):
    s = context_product_sign(ops)
    signs.append(s)

print("\n[4/5] Building adjacency...")
n = len(contexts)
adj = [[] for _ in range(n)]
ctx_sets = [set(ctx[0]) for ctx in contexts]
for i in range(n):
    for j in range(i + 1, n):
        if len(ctx_sets[i] & ctx_sets[j]) == 1:
            adj[i].append(j)
            adj[j].append(i)

print(f"\n[5/5] Finding Type B Mermin pentagrams and analyzing collinearity...")
t1 = time.time()

adj_sets = [set(a) for a in adj]

type_b_count = 0
collinear_match = 0  # collinear triple product = -1
collinear_no_match = 0  # collinear triple product = +1
non_collinear = 0  # no collinear triple found (shouldn't happen for Type B)

# Track: for each collinear line, how many pentagrams have that line
line_counts = defaultdict(int)
# Track: for each collinear line, how many have product = -1
line_minus_counts = defaultdict(int)

# Sample data for first few Type B
samples = []

for i in range(n):
    si = adj_sets[i]
    for j_pos in range(len(adj[i])):
        j = adj[i][j_pos]
        sj = adj_sets[j]
        parity_ij = (1 if signs[i] == -1 else 0) + (1 if signs[j] == -1 else 0)

        common_k = si & sj
        for k in common_k:
            if k <= j:
                continue
            sk = adj_sets[k]
            parity_ijk = parity_ij + (1 if signs[k] == -1 else 0)

            common_m = common_k & sk
            for m in common_m:
                if m <= k:
                    continue
                sm = adj_sets[m]
                parity_ijkm = parity_ijk + (1 if signs[m] == -1 else 0)

                common_p = common_m & sm
                for p in common_p:
                    if p <= m:
                        continue

                    # Check distinct shared operators
                    shared = []
                    clique_list = [i, j, k, m, p]
                    valid_mermin = True
                    for a_pos in range(5):
                        for b_pos in range(a_pos+1, 5):
                            ia = clique_list[a_pos]
                            ib = clique_list[b_pos]
                            inter = ctx_sets[ia] & ctx_sets[ib]
                            if len(inter) != 1:
                                valid_mermin = False
                                break
                            shared.append(next(iter(inter)))
                        if not valid_mermin:
                            break
                    if not valid_mermin:
                        continue
                    if len(set(shared)) != 10:
                        continue

                    # Parity check
                    parity = parity_ijkm + (1 if signs[p] == -1 else 0)
                    if parity % 2 == 0:
                        continue

                    # Classify
                    fano_points = []
                    for idx in clique_list:
                        _, lag_idx, _ = contexts[idx]
                        L = lagrangians[lag_idx]
                        inter = L & V_SET
                        if len(inter) == 1:
                            v = next(iter(inter))
                            fano_points.append(FANO_LABEL[(v[0], v[1], v[2])])
                        elif len(inter) == 0:
                            fano_points.append(0)
                        else:
                            fano_points.append(-1)

                    nonzero = [x for x in fano_points if x > 0]
                    distinct = len(set(nonzero))
                    transverse = fano_points.count(0)

                    if transverse == 0 and distinct == 4:
                        # Type B
                        type_b_count += 1

                        clique_signs = [signs[idx] for idx in clique_list]
                        coll = find_collinear_triple(nonzero)

                        if coll is not None:
                            # Find which contexts correspond to the collinear points
                            coll_indices = [idx_in_clique for idx_in_clique, fp in enumerate(fano_points) if fp in coll]
                            coll_product = 1
                            for ci in coll_indices:
                                coll_product *= clique_signs[ci]

                            if coll_product == -1:
                                collinear_match += 1
                            else:
                                collinear_no_match += 1

                            line_key = tuple(sorted(coll))
                            line_counts[line_key] += 1
                            if coll_product == -1:
                                line_minus_counts[line_key] += 1

                            if len(samples) < 5:
                                samples.append({
                                    'fano_points': fano_points,
                                    'signs': clique_signs,
                                    'collinear': coll,
                                    'coll_product': coll_product,
                                    'minus_count': sum(1 for s in clique_signs if s == -1),
                                })
                        else:
                            non_collinear += 1

                    if type_b_count % 1000 == 0:
                        elapsed = time.time() - t1
                        print(f"  Type B: {type_b_count} ({elapsed:.1f}s)")

print(f"\n  Total Type B: {type_b_count} ({time.time()-t1:.1f}s)")

# Results
print(f"\n{'='*70}")
print("Type B Collinearity Analysis")
print(f"{'='*70}")
print(f"\nCollinear triple found: {collinear_match + collinear_no_match}")
print(f"  Collinear product = -1 (match): {collinear_match} ({collinear_match/type_b_count*100:.1f}%)")
print(f"  Collinear product = +1 (no match): {collinear_no_match} ({collinear_no_match/type_b_count*100:.1f}%)")
print(f"  No collinear triple: {non_collinear}")

print(f"\nCollinear line distribution:")
for line_key in sorted(line_counts.keys(), key=lambda x: -line_counts[x]):
    total = line_counts[line_key]
    minus = line_minus_counts.get(line_key, 0)
    line_str = str(line_key)
    print(f"  {line_str}: {total} pentagrams, {minus} with -1 product ({minus/total*100:.1f}%)")

print(f"\nSample Type B pentagrams:")
for idx, s in enumerate(samples):
    print(f"\n  Sample {idx+1}:")
    print(f"    Fano points: {s['fano_points']}")
    print(f"    Signs: {s['signs']} ({s['minus_count']} minus)")
    print(f"    Collinear triple: {s['collinear']}")
    print(f"    Collinear product: {s['coll_product']}")

print(f"\nTotal time: {time.time()-t0:.1f}s")
