#!/usr/bin/env python3
"""
Prove: for equiangular K₅, dim(L_k ∩ (L_i + L_j)) = 2 for all distinct i,j,k.

If dim = 2, then L_k ∩ (L_i + L_j) = span(r_{ik}, r_{jk}).
Since the 10 rays form a cap (no 3 collinear), r_{kl} ∉ span(r_{ik}, r_{jk}).
Therefore r_{kl} ∉ L_i + L_j = r_{ij}^⊥, so ω(r_{ij}, r_{kl}) = 1.
"""

import sys
sys.path.insert(0, '/mnt/d/Workspace/ai_ai/nlang/research/supplementary/paper10')
import numpy as np
from itertools import combinations
from g2_orbits import find_lagrangians, enumerate_pentagrams, gf2_rank

def gf2_span_dim(vectors):
    if not vectors: return 0
    return gf2_rank(vectors)

def gf2_intersection_dim(basis1, basis2):
    """Compute dimension of intersection of two subspaces given by spanning sets."""
    # dim(V ∩ W) = dim(V) + dim(W) - dim(V + W)
    dim_V = gf2_rank(basis1)
    dim_W = gf2_rank(basis2)
    combined = list(basis1) + list(basis2)
    dim_sum = gf2_rank(combined)
    return dim_V + dim_W - dim_sum

print("Loading pentagrams...")
lagrangians = find_lagrangians()
pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(lagrangians)

# For each pentagram, extract the 5 Lagrangians and check dim(L_k ∩ (L_i + L_j))
dim_counts = {}
checked = 0

for pidx, pent in enumerate(pentagrams[:1000]):  # Check first 1000
    # Get the 5 Lagrangian indices
    lag_indices = [context_lag_idx[ci] for ci in pent]
    lags = [lagrangians[li] for li in lag_indices]
    
    # For each triple (i,j,k) with i < j, check dim(L_k ∩ (L_i + L_j))
    for i in range(5):
        for j in range(i+1, 5):
            for k in range(5):
                if k == i or k == j:
                    continue
                # L_i + L_j: need a basis
                Li_Lj = list(lags[i]) + list(lags[j])
                # Find intersection with L_k
                dim_int = gf2_intersection_dim(list(lags[k]), Li_Lj)
                
                key = dim_int
                dim_counts[key] = dim_counts.get(key, 0) + 1
                checked += 1

print(f"\nChecked {checked} triples from first 1000 pentagrams")
print(f"dim(L_k ∩ (L_i + L_j)) distribution:")
for dim in sorted(dim_counts.keys()):
    print(f"  dim = {dim}: {dim_counts[dim]} ({100*dim_counts[dim]/checked:.1f}%)")

# Now check: for each pentagram, verify that r_{kl} ∉ L_i + L_j for disjoint {i,j}, {k,l}
print("\n\nVerifying r_{kl} ∉ L_i + L_j for disjoint pairs...")
edges = list(combinations(range(5), 2))
disjoint_pairs = []
for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        e1, e2 = set(edges[i]), set(edges[j])
        if not (e1 & e2):
            disjoint_pairs.append((edges[i], edges[j]))

in_count = 0
out_count = 0

for pidx, pent in enumerate(pentagrams[:1000]):
    lag_indices = [context_lag_idx[ci] for ci in pent]
    lags = [lagrangians[li] for li in lag_indices]
    
    # Extract rays
    rays = {}
    for i in range(5):
        for j in range(i+1, 5):
            shared = all_contexts[pent[i]] & all_contexts[pent[j]]
            rays[(i,j)] = list(shared)[0]
    
    for (e1, e2) in disjoint_pairs:
        i, j = e1
        k, l = e2
        # Check if r_{kl} ∈ L_i + L_j
        Li_Lj = list(lags[i]) + list(lags[j])
        r_kl = rays[(k,l)]
        
        # r_kl ∈ L_i + L_j iff rank(L_i + L_j + [r_kl]) = rank(L_i + L_j)
        rank_without = gf2_rank(Li_Lj)
        rank_with = gf2_rank(Li_Lj + [r_kl])
        
        if rank_with == rank_without:
            in_count += 1
        else:
            out_count += 1

print(f"r_{{kl}} ∈ L_i + L_j: {in_count}")
print(f"r_{{kl}} ∉ L_i + L_j: {out_count}")
print(f"Total: {in_count + out_count}")
