#!/usr/bin/env python3
"""P1: Check if standard pentagram is in the 12,096 set and verify G₂(2) orbit structure."""

import itertools
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

def pauli_to_vector(s):
    x = [0, 0, 0]
    z = [0, 0, 0]
    for q, c in enumerate(s):
        if c == 'X':
            x[q] = 1
        elif c == 'Y':
            x[q] = 1
            z[q] = 1
        elif c == 'Z':
            z[q] = 1
    return tuple(x + z)

# Standard pentagram operators
std_pentagram = {
    'C1': ['XXX', 'XYY', 'YXY', 'YYX'],
    'C2': ['XXX', 'ZZX', 'ZXZ', 'XZZ'],
    'C3': ['YXY', 'ZXZ', 'ZYY', 'YYZ'],
    'C4': ['YYX', 'ZZX', 'ZYY', 'YZY'],
    'C5': ['XYY', 'XZZ', 'YYZ', 'YZY'],
}

t0 = time.time()

print("[1/4] Finding 135 Lagrangians...")
lagrangians = find_lagrangians()
print(f"  Done ({time.time()-t0:.1f}s)")

print("\n[2/4] Extracting 945 contexts...")
contexts = []
for lag_idx, L in enumerate(lagrangians):
    lines = get_fano_lines_in_lagrangian(L)
    for line_idx, line in enumerate(lines):
        context_ops = tuple(p for p in L if p not in line)
        contexts.append((context_ops, lag_idx, line_idx))
print(f"  {len(contexts)} contexts")

# Build set of all context operator sets (as frozensets)
context_frozensets = set()
for ops, _, _ in contexts:
    context_frozensets.add(frozenset(ops))

print("\n[3/4] Checking standard pentagram contexts...")
std_contexts_vecs = []
for name, ops in std_pentagram.items():
    vecs = tuple(pauli_to_vector(op) for op in ops)
    std_contexts_vecs.append((name, vecs))
    fs = frozenset(vecs)
    in_set = fs in context_frozensets
    print(f"  {name}: {ops} -> in 945 contexts? {in_set}")

all_in = all(frozenset(vecs) in context_frozensets for _, vecs in std_contexts_vecs)
print(f"\n  All 5 contexts in our set? {all_in}")

if not all_in:
    print("\n  Standard pentagram is NOT in the 12,096 set.")
    print("  The 945 contexts come from a specific MASA subset.")
    print("  12,096 decomposes into 4 G₂(2)-orbits,")
    print("  and the standard pentagram may belong to a DIFFERENT orbit")
    print("  (constructed from different MASAs).")
else:
    print("\n  Standard pentagram IS in the 12,096 set.")
    # Find its type
    print("\n[4/4] Classifying standard pentagram type...")
    fano_points = []
    for name, vecs in std_contexts_vecs:
        # Find which Lagrangian this context belongs to
        fs = frozenset(vecs)
        lag_idx = None
        for idx, (ops, li, _) in enumerate(contexts):
            if frozenset(ops) == fs:
                lag_idx = li
                break
        if lag_idx is not None:
            L = lagrangians[lag_idx]
            inter = L & V_SET
            if len(inter) == 1:
                v = next(iter(inter))
                fano_points.append((v[0], v[1], v[2]))
            elif len(inter) == 0:
                fano_points.append(None)
        else:
            fano_points.append(None)
    
    print(f"  Fano points: {fano_points}")
    nonzero = [p for p in fano_points if p is not None]
    distinct = len(set(nonzero))
    transverse = fano_points.count(None)
    print(f"  Distinct Fano points: {distinct}")
    print(f"  Transverse contexts: {transverse}")

print(f"\nTotal time: {time.time()-t0:.1f}s")
