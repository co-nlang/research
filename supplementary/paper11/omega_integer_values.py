#!/usr/bin/env python3
"""
Analyze integer ω values for disjoint pairs in equiangular K₅.
Check if ω_int = ±1 always, or can be ±3, ±5, etc.
"""

import sys
sys.path.insert(0, '/mnt/d/Workspace/ai_ai/nlang/research/supplementary/paper10')
import numpy as np
from itertools import combinations
from collections import Counter
from g2_orbits import (find_lagrangians, enumerate_pentagrams)

def omega_int(a, b):
    a, b = np.array(a, dtype=int), np.array(b, dtype=int)
    return int(a[0]*b[3] + a[1]*b[4] + a[2]*b[5] - a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

edges = list(combinations(range(5), 2))
disjoint_pairs = []
for i in range(len(edges)):
    for j in range(i+1, len(edges)):
        e1, e2 = set(edges[i]), set(edges[j])
        if not (e1 & e2):
            disjoint_pairs.append((i, j))

print("Loading pentagrams...")
lagrangians = find_lagrangians()
pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(lagrangians)

# Analyze integer ω values for disjoint pairs
all_omega_values = Counter()
per_pentagram_omega = []

for pidx, pent in enumerate(pentagrams):
    rays = []
    for i in range(5):
        for j in range(i+1, 5):
            shared = all_contexts[pent[i]] & all_contexts[pent[j]]
            rays.append(list(shared)[0])
    
    omega_vals = []
    for (i, j) in disjoint_pairs:
        w = omega_int(rays[i], rays[j])
        omega_vals.append(w)
        all_omega_values[w] += 1
    
    per_pentagram_omega.append(omega_vals)
    
    if pidx < 3:
        print(f"\nPentagram {pidx} disjoint pair ω_int values:")
        for k, (i, j) in enumerate(disjoint_pairs):
            print(f"  r_{edges[i]} × r_{edges[j]}: ω = {omega_vals[k]}")

print(f"\n=== Integer ω value distribution (all {len(disjoint_pairs) * len(pentagrams)} pairs) ===")
for val in sorted(all_omega_values.keys()):
    count = all_omega_values[val]
    pct = 100 * count / sum(all_omega_values.values())
    print(f"  ω = {val:+d}: {count} ({pct:.1f}%)")

# Check: is ω always ±1?
pm1 = all_omega_values.get(1, 0) + all_omega_values.get(-1, 0)
total = sum(all_omega_values.values())
print(f"\nω ∈ {{+1, -1}}: {pm1}/{total} ({100*pm1/total:.1f}%)")

# Check sum of ω_disjoint (integer) per pentagram
sums = [sum(vals) for vals in per_pentagram_omega]
print(f"\nω_disjoint sum distribution:")
sum_counter = Counter(sums)
for val in sorted(sum_counter.keys()):
    print(f"  sum = {val}: {sum_counter[val]} pentagrams")
