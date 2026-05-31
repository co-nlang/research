#!/usr/bin/env python3
"""Verify: Are all Type F2 pentagrams collinear?"""

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

def span3(basis):
    a, b, c = basis
    return frozenset([a, b, c, add(a,b), add(a,c), add(b,c), add(a,add(b,c))])

def find_lagrangians():
    lagrangians = []
    seen = set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3: continue
        if not all(symplectic_form(u,v) == 0 for u,v in itertools.combinations(basis,2)): continue
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

FANO_LINES = [
    {1, 2, 4}, {1, 3, 5}, {1, 6, 7},
    {2, 3, 6}, {2, 5, 7}, {3, 4, 7}, {4, 5, 6}
]

def is_collinear(p1, p2, p3):
    for line in FANO_LINES:
        if p1 in line and p2 in line and p3 in line:
            return True
    return False

lagrangians = find_lagrangians()
contexts = []
for lag_idx, L in enumerate(lagrangians):
    lines = get_fano_lines_in_lagrangian(L)
    for line_idx, line in enumerate(lines):
        context_ops = tuple(p for p in L if p not in line)
        contexts.append((context_ops, lag_idx))

# Sample some Type F2 pentagrams and check their Fano points
# Type F2: 3 distinct Fano points, 2 transverse
# We need to find pentagrams first

print("Checking: Can 3 Fano points from k=1 MASAs be non-collinear?")
print()

# Get all k=1 MASA Fano points
k1_fano_points = set()
for L in lagrangians:
    inter = L & V_SET
    if len(inter) == 1:
        v = next(iter(inter))
        k1_fano_points.add(FANO_LABEL[(v[0], v[1], v[2])])

print(f"k=1 MASA Fano points: {sorted(k1_fano_points)}")
print(f"Total: {len(k1_fano_points)}")

# Check: what are the possible triples from k=1 MASAs?
# A Type F2 pentagram uses 3 non-transverse contexts, each from some MASA
# Each non-transverse context contributes 1 Fano point

# Let's check: in Type F2, which MASAs contribute the 3 Fano points?
# We need to actually find Type F2 pentagrams

print("\nFinding Type F2 pentagrams to check Fano point sources...")

# Quick search for first few Type F2
ctx_sets = [set(ctx[0]) for ctx in contexts]
n = len(contexts)

# Build adjacency
adj = [[] for _ in range(n)]
for i in range(n):
    for j in range(i+1, n):
        if len(ctx_sets[i] & ctx_sets[j]) == 1:
            adj[i].append(j)
            adj[j].append(i)

found_f2 = 0
f2_triples = []

for i in range(n):
    for j in adj[i]:
        for k in adj[j]:
            if k <= j: continue
            if i not in adj[k]: continue
            # i,j,k form a triangle
            # Check if they can be part of a K5
            common = set(adj[i]) & set(adj[j]) & set(adj[k])
            if len(common) < 2: continue

            # Get Fano points
            fano_pts = []
            for idx in [i, j, k]:
                _, lag_idx = contexts[idx]
                L = lagrangians[lag_idx]
                inter = L & V_SET
                if len(inter) == 1:
                    v = next(iter(inter))
                    fano_pts.append(FANO_LABEL[(v[0], v[1], v[2])])
                else:
                    fano_pts.append(0)

            nonzero = [x for x in fano_pts if x > 0]
            if len(nonzero) == 3 and len(set(nonzero)) == 3:
                # 3 distinct Fano points from these 3 contexts
                coll = is_collinear(nonzero[0], nonzero[1], nonzero[2])
                if not coll:
                    f2_triples.append(tuple(sorted(nonzero)))
                    if len(f2_triples) >= 20:
                        break
            if len(f2_triples) >= 20:
                break
        if len(f2_triples) >= 20:
            break
    if len(f2_triples) >= 20:
        break

if f2_triples:
    print(f"\nFound {len(f2_triples)} non-collinear triples from context triangles:")
    for t in f2_triples[:10]:
        print(f"  {t}")
else:
    print("\nNo non-collinear triples found in context triangles.")
    print("This suggests that the K5 structure + Type F2 constraint")
    print("forces the 3 Fano points to be collinear.")
