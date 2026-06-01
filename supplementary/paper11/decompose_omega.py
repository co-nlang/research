#!/usr/bin/env python3
"""
Decompose ω_total into sharing/non-sharing pairs and prove ω_total ≡ 1.

Key insight: 
- Sharing pairs (r_{ij}, r_{ik}) are both in L_i → ω = 0 (Lagrangian)
- So ω_total = ω_nonsharing = sum over 15 disjoint edge pairs in K₅
- Need to show ω_nonsharing ≡ 1 (mod 2)
"""

import sys
sys.path.insert(0, '/mnt/d/Workspace/ai_ai/nlang/research/supplementary/paper10')
import numpy as np
from itertools import combinations
from g2_orbits import (generate_g2_elements, find_lagrangians, 
                        enumerate_pentagrams, find_change_of_basis,
                        G2_GEN1, G2_GEN2, symplectic_form_omega)

def omega_int(a, b):
    """Integer symplectic form: ω(a,b) = a_x·b_z - a_z·b_x (block convention)."""
    a, b = np.array(a, dtype=int), np.array(b, dtype=int)
    # Block convention: v = (x₁,x₂,x₃,z₁,z₂,z₃)
    return int(a[0]*b[3] + a[1]*b[4] + a[2]*b[5] - a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def omega_mod2(a, b):
    """Mod-2 symplectic form."""
    return omega_int(a, b) % 2

# Enumerate all 15 disjoint edge pairs in K₅
edges = list(combinations(range(5), 2))
disjoint_pairs = []
sharing_pairs = []
for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        e1, e2 = set(edges[i]), set(edges[j])
        if e1 & e2:
            sharing_pairs.append((i, j))
        else:
            disjoint_pairs.append((i, j))

print(f"Total pairs: {len(sharing_pairs) + len(disjoint_pairs)} = {len(sharing_pairs)} sharing + {len(disjoint_pairs)} disjoint")

# Group disjoint pairs by uncovered vertex
by_vertex = {v: [] for v in range(5)}
for (i, j) in disjoint_pairs:
    e1, e2 = set(edges[i]), set(edges[j])
    covered = e1 | e2
    uncovered = (set(range(5)) - covered).pop()
    by_vertex[uncovered].append((edges[i], edges[j], i, j))

print("\nDisjoint pairs by uncovered vertex:")
for v in range(5):
    print(f"  Vertex {v}: {[(e1,e2) for e1,e2,_,_ in by_vertex[v]]}")

# Now run on all pentagrams
print("\nLoading pentagrams...")
lagrangians = find_lagrangians()
pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(lagrangians)
print(f"Loaded {len(pentagrams)} pentagrams")

# Analyze disjoint pair ω values
omega_sharing_total = []
omega_disjoint_total = []
omega_by_vertex = {v: [] for v in range(5)}

for pidx, pent in enumerate(pentagrams):
    # pent is a tuple of 5 context indices
    # Extract the 10 rays (shared operators between pairs of contexts)
    rays = []
    ray_map = {}  # (i,j) -> ray index
    for i in range(5):
        for j in range(i+1, 5):
            shared = all_contexts[pent[i]] & all_contexts[pent[j]]
            if len(shared) == 1:
                ray = list(shared)[0]
                rays.append(ray)
                ray_map[(i,j)] = len(rays) - 1
            else:
                print(f"ERROR: pentagram {pidx} contexts {i},{j} share {len(shared)} operators")
                rays.append(None)
    
    # Compute sharing ω (mod 2)
    ws = 0
    for (i, j) in sharing_pairs:
        if rays[i] and rays[j]:
            ws += omega_mod2(rays[i], rays[j])
    
    # Compute disjoint ω (mod 2)
    wd = 0
    wd_by_v = {v: 0 for v in range(5)}
    for v in range(5):
        for (e1, e2, i, j) in by_vertex[v]:
            if rays[i] and rays[j]:
                w = omega_mod2(rays[i], rays[j])
                wd += w
                wd_by_v[v] += w
    
    omega_sharing_total.append(ws % 2)
    omega_disjoint_total.append(wd % 2)
    for v in range(5):
        omega_by_vertex[v].append(wd_by_v[v] % 2)
    
    if pidx < 5:
        print(f"\nPentagram {pidx}:")
        print(f"  ω_sharing = {ws} ≡ {ws%2} (mod 2)")
        print(f"  ω_disjoint = {wd} ≡ {wd%2} (mod 2)")
        for v in range(5):
            print(f"    vertex {v}: ω = {wd_by_v[v]} ≡ {wd_by_v[v]%2}")

# Summary statistics
print(f"\n=== SUMMARY ({len(pentagrams)} pentagrams) ===")
print(f"ω_sharing ≡ 0: {sum(1 for x in omega_sharing_total if x == 0)}/{len(pentagrams)}")
print(f"ω_sharing ≡ 1: {sum(1 for x in omega_sharing_total if x == 1)}/{len(pentagrams)}")
print(f"ω_disjoint ≡ 0: {sum(1 for x in omega_disjoint_total if x == 0)}/{len(pentagrams)}")
print(f"ω_disjoint ≡ 1: {sum(1 for x in omega_disjoint_total if x == 1)}/{len(pentagrams)}")

print("\nPer-vertex ω_disjoint parity distribution:")
for v in range(5):
    vals = omega_by_vertex[v]
    print(f"  Vertex {v}: 0={vals.count(0)}, 1={vals.count(1)}")

# Check: does each vertex contribute a fixed parity?
print("\nVertex parity patterns (first 10 pentagrams):")
for pidx in range(10):
    pattern = tuple(omega_by_vertex[v][pidx] for v in range(5))
    print(f"  Pentagram {pidx}: {pattern} (sum={sum(pattern)%2})")
