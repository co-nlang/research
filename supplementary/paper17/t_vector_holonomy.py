#!/usr/bin/env python3
"""
Paper XVII (exploratory): T-vector and pentagram holonomy.

For each Mermin pentagram P (5 contexts, 10 rays), find T ∈ F₂⁶ with
ω(T,v) = 1 for all 10 rays, and explore relationships between T and β_sum.

Candidate identities:
  (A) β_sum ≡ Σ ω_int(T,v)²   (mod 4)  [trivially true: each term ≡ 1 mod 4]
  (B) β_sum ≡ Σ ω_int(T,v)    (mod 4)  [non-trivial: odd terms with varying sign]
  (C) s(C)  vs Σ_{v∈C} ω_int(T,v)      [context-level]
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../paper16'))

import numpy as np
from collections import defaultdict
import itertools
import time

# Import enumeration from Paper XVI
from displacement_operator import (
    find_lagrangians, enumerate_pentagrams,
    symplectic_form, omega_int, xor_vec,
)


# ============================================================
# GF(2) linear system solver
# ============================================================

def f2_solve_all(A, b):
    """All solutions to Ax = b over F₂. Returns list of tuples."""
    m, n = A.shape
    A_aug = np.hstack([A % 2, b.reshape(-1, 1) % 2])
    pivot_cols, pivot_row = [], 0
    for col in range(n):
        found = next((r for r in range(pivot_row, m) if A_aug[r, col]), -1)
        if found == -1: continue
        A_aug[[pivot_row, found]] = A_aug[[found, pivot_row]]
        for r in range(m):
            if r != pivot_row and A_aug[r, col]:
                A_aug[r] = (A_aug[r] + A_aug[pivot_row]) % 2
        pivot_cols.append(col); pivot_row += 1
    rank = len(pivot_cols)
    if any(A_aug[r, -1] for r in range(rank, m)):
        return []  # inconsistent
    free_cols = [c for c in range(n) if c not in pivot_cols]
    solutions = []
    for mask in range(1 << len(free_cols)):
        x = np.zeros(n, dtype=int)
        for i, fc in enumerate(free_cols):
            x[fc] = (mask >> i) & 1
        for r, pc in enumerate(pivot_cols):
            val = A_aug[r, -1]
            for fc in free_cols:
                val = (val + A_aug[r, fc] * x[fc]) % 2
            x[pc] = val % 2
        solutions.append(tuple(x.tolist()))
    return solutions


def find_T_vectors(rays_10):
    """Find all T ∈ F₂⁶ with ω(T,v) = 1 for each ray v."""
    # ω(T,v) = T₀v₃+T₁v₄+T₂v₅+T₃v₀+T₄v₁+T₅v₂  (mod 2)
    A = np.array([[v[3],v[4],v[5],v[0],v[1],v[2]] for v in rays_10], dtype=int)
    b = np.ones(10, dtype=int)
    return f2_solve_all(A, b)


def compute_beta(ctx_pts):
    pts = list(ctx_pts); b = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            b += omega_int(pts[j], pts[k])
    return b


# ============================================================
# Main
# ============================================================

def main():
    t0 = time.time()

    print("[1/3] Enumerating Lagrangians, contexts, pentagrams...")
    lagrangians = find_lagrangians()
    pentagrams, all_contexts, context_signs, _ = enumerate_pentagrams(lagrangians)
    print(f"      {len(lagrangians)} Lagrangians, {len(all_contexts)} contexts, "
          f"{len(pentagrams)} pentagrams  ({time.time()-t0:.1f}s)")

    # Build context sign map
    ctx_sign = {c: context_signs[i] for i, c in enumerate(all_contexts)}

    # Precompute β for each context
    ctx_beta = {c: compute_beta(c) for c in all_contexts}

    print("\n[2/3] T-vector analysis over all pentagrams...")

    t_mult_dist   = defaultdict(int)   # distribution of #T solutions
    sum_oint_mod4 = defaultdict(int)   # Σ ω_int(T,v) mod 4
    # Context-level: s(C) → distribution of (Σ_{v∈C} ω_int(T,v)) mod 4
    ctx_level     = {-1: defaultdict(int), +1: defaultdict(int)}

    no_T_count = 0
    checked = 0

    for pent_idx in pentagrams:
        five = [all_contexts[i] for i in pent_idx]
        rays = list({v for c in five for v in c})
        assert len(rays) == 10

        beta_sum = sum(ctx_beta[c] for c in five)
        assert beta_sum % 4 == 2, f"β_sum={beta_sum}"

        T_sols = find_T_vectors(rays)
        t_mult_dist[len(T_sols)] += 1

        if not T_sols:
            no_T_count += 1; continue

        for T in T_sols:
            oints = [omega_int(T, v) for v in rays]
            assert all(o % 2 == 1 for o in oints), "ω(T,v)≠1 mod 2"

            # (A) Σ ω_int² mod 4 — should always be 10 ≡ 2
            sq_sum = sum(o*o for o in oints)
            # (B) Σ ω_int mod 4
            lin_sum = sum(oints)
            sum_oint_mod4[lin_sum % 4] += 1

            # (C) context-level
            for ctx in five:
                s = ctx_sign[ctx]
                ctx_rays = list(ctx)
                ctx_lin = sum(omega_int(T, v) for v in ctx_rays)
                ctx_level[s][ctx_lin % 4] += 1

        checked += 1

    print(f"      Pentagrams processed: {checked}, no-T: {no_T_count}")
    print(f"      T-vector multiplicity: {dict(t_mult_dist)}")
    print(f"      Σ ω_int(T,v) mod 4:   {dict(sum_oint_mod4)}")
    print(f"                              [always 2? parity theorem analog?]")

    print("\n[3/3] Context-level Σ_{v∈C} ω_int(T,v) mod 4, split by s(C):")
    for s_val in [-1, +1]:
        dist = dict(ctx_level[s_val])
        print(f"      s(C)={s_val:+d}: {dist}")

    # Quick sample
    print("\n      Sample pentagram (first 3):")
    for pent_idx in pentagrams[:3]:
        five = [all_contexts[i] for i in pent_idx]
        rays = list({v for c in five for v in c})
        beta_sum = sum(ctx_beta[c] for c in five)
        T_sols = find_T_vectors(rays)
        if T_sols:
            T = T_sols[0]
            oints = sorted(omega_int(T, v) for v in rays)
            lin_sum = sum(omega_int(T, v) for v in rays)
            print(f"        β_sum={beta_sum:+3d}  T={T}  "
                  f"Σω_int={lin_sum:+3d}  ω_int vals={oints}")

    print(f"\nTotal: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
