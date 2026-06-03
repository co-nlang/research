#!/usr/bin/env python3
"""Check: are there K₅ of Lagrangians with parity +1 (even parity)?"""
import sys, os
sys.path.insert(0, '../paper16')

from displacement_operator import find_lagrangians, symplectic_form, omega_int, xor_vec
from collections import defaultdict
import itertools, time

def gf2_rank_vectors(vectors):
    if not vectors: return 0
    rows = [list(v) for v in vectors]; ncols = len(rows[0]); rank = 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
        if pivot is not None:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for r in range(len(rows)):
                if r != rank and rows[r][col]:
                    rows[r] = [(rows[r][c]^rows[rank][c]) for c in range(ncols)]
            rank += 1
    return rank

def get_fano_lines(lag):
    pts = list(lag); lines = set()
    for i in range(7):
        for j in range(i+1,7):
            s = tuple(a^b for a,b in zip(pts[i],pts[j]))
            if s in lag: lines.add(frozenset([pts[i],pts[j],s]))
    return list(lines)

def compute_beta(pts):
    b = 0
    for j in range(len(pts)):
        for k in range(j+1,len(pts)):
            b += omega_int(pts[j], pts[k])
    return b

t0 = time.time()
print("Enumerating Lagrangians and contexts...")
lagrangians = find_lagrangians()

all_contexts = []; context_signs = []
for lag in lagrangians:
    pts = list(lag)
    for line in get_fano_lines(lag):
        ctx = frozenset(p for p in pts if p not in line)
        if len(ctx) != 4: continue
        beta = compute_beta(list(ctx))
        all_contexts.append(ctx)
        context_signs.append((-1)**(beta//2))

print(f"  {len(lagrangians)} Lagrangians, {len(all_contexts)} contexts")

# Build adjacency (share exactly 1 ray)
n = len(all_contexts)
adj = defaultdict(list)
for i in range(n):
    for j in range(i+1,n):
        if len(all_contexts[i] & all_contexts[j]) == 1:
            adj[i].append(j); adj[j].append(i)

print("Finding ALL K₅s (no parity filter)...")
k5_parity = defaultdict(int)  # parity → count
for i in range(n):
    for j in adj[i]:
        if j<=i: continue
        common_ij = set(adj[i]) & set(adj[j])
        for k in common_ij:
            if k<=j: continue
            common_ijk = common_ij & set(adj[k])
            for m in common_ijk:
                if m<=k: continue
                common_ijkm = common_ijk & set(adj[m])
                for p in common_ijkm:
                    if p<=m: continue
                    clique = [i,j,k,m,p]
                    rays = set()
                    for ci in clique: rays |= all_contexts[ci]
                    if len(rays) != 10: continue
                    n_minus = sum(1 for ci in clique if context_signs[ci]==-1)
                    parity = (-1)**n_minus
                    k5_parity[parity] += 1

print(f"\nK₅ parity distribution: {dict(k5_parity)}")
print(f"Total K₅s: {sum(k5_parity.values())}")
print(f"All K₅s have parity -1? {set(k5_parity.keys()) == {-1}}")
print(f"Time: {time.time()-t0:.1f}s")
