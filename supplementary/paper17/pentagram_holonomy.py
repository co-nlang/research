#!/usr/bin/env python3
"""
Paper XVII (exploratory): Pentagram K₅ structure and Weyl holonomy.

A Mermin pentagram has 5 contexts C₁,...,C₅ that are PAIRWISE adjacent
(every pair shares exactly 1 ray). The 10 rays are vᵢⱼ = Cᵢ ∩ Cⱼ.
This is a K₅ structure, NOT a pentagon.

Key computation: the full product W_{C₁}...W_{C₅} = -I₈.
Expanding: 20 Pauli operators, each ray vᵢⱼ appearing exactly twice.
If we bring each pair W(vᵢⱼ)·W(vᵢⱼ) together → I₈, the sign picked up is:

  (-1)^N  where N = # anticommuting cross-context pairs

Hypothesis: N is always ODD for any Mermin pentagram.

If N odd → product = -I₈ → proves the KS obstruction algebraically
(no 12,096 enumeration needed once N-odd is shown combinatorially).

Also checks:
  (A) Distribution of N
  (B) β_sum vs N (both must be ≡ 2 mod 4, but are they equal?)
  (C) β_sum vs cross-context ω_int sum
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../paper16'))

import numpy as np
from collections import defaultdict
import itertools
import time

from displacement_operator import (
    find_lagrangians, enumerate_pentagrams,
    symplectic_form, omega_int, xor_vec, compute_beta,
)


def build_k5_structure(five_ctxs):
    """
    Given 5 pairwise-adjacent contexts (a K₅), return the shared-ray matrix:
      shared[i][j] = the ray in Cᵢ ∩ Cⱼ  (i≠j)
    """
    five = list(five_ctxs)
    shared = [[None]*5 for _ in range(5)]
    for i in range(5):
        for j in range(i+1, 5):
            inter = list(five[i] & five[j])
            assert len(inter) == 1, f"|Cᵢ∩Cⱼ|={len(inter)}, expected 1"
            shared[i][j] = inter[0]
            shared[j][i] = inter[0]
    return five, shared


def sign_from_anticommutations(five_ctxs, shared):
    """
    Compute the sign of W_{C₁}...W_{C₅} by counting anticommutations.

    Strategy: within the full 20-op product (ordered C₁,C₂,C₃,C₄,C₅,
    within each context in index order), bring each pair W(vᵢⱼ) together.

    Each time W(vᵢⱼ) passes W(vₖₗ), it picks up (-1)^{ω(vᵢⱼ,vₖₗ)}.

    We do this for all 10 pairs, accumulating the total sign.

    Returns: (total_sign, N_anticomm, anticomm_pairs)
    where N_anticomm = # pairs with ω(vᵢⱼ,vₖₗ)=1.
    """
    five = list(five_ctxs)

    # Build ordered list of all 20 operators: (context_index, ray)
    # Within each context, order rays by the OTHER context index they belong to.
    ops = []
    for i in range(5):
        ctx_rays = []
        for j in range(5):
            if j != i:
                ctx_rays.append((j, shared[i][j]))   # (other_ctx, ray)
        ctx_rays.sort(key=lambda x: x[0])
        ops.extend([(i, r) for (_, r) in ctx_rays])

    # ops is a list of 20 (context_index, ray) tuples

    # For each ray v = shared[i][j], it appears in ops at two positions:
    #   position p1 (in context i's block)
    #   position p2 (in context j's block, with i<j since j>i in sorted order)
    # We bring the second occurrence past all ops between p1 and p2.

    # Identify the two positions of each ray in ops:
    ray_positions = defaultdict(list)
    for pos, (ctx_idx, ray) in enumerate(ops):
        ray_positions[ray].append(pos)

    # For each pair of rays vᵢⱼ and vₖₗ (cross-context), count anticommutations
    # "Cross-context pair": the two rays are NOT in the same context
    # i.e., {context of vᵢⱼ's shared contexts} ∩ {context of vₖₗ's shared contexts} = ∅

    # Build ray → (ctx_a, ctx_b) mapping
    ray_owners = {}   # ray → frozenset({i,j})
    for i in range(5):
        for j in range(i+1, 5):
            ray_owners[shared[i][j]] = frozenset({i,j})

    unique_rays = list(ray_owners.keys())

    # Compute total anticommutation sign
    # When we bring the second W(v) leftward past W(w) between them,
    # we get (-1)^{ω(v,w)}.
    # We need to carefully track the "current" positions of operators
    # as earlier moves shift things around.
    #
    # Simpler: since all operators are Pauli strings (Hermitian),
    # the sign from moving W(v₁₂) past W(v₁₃) etc. is just
    # (-1)^{ω(v₁₂, w)} for each w it passes.
    #
    # But order of moves matters! Use a bubble-sort-like approach:
    # bring each ray pair together by moving the rightmost occurrence leftward,
    # accumulating signs.

    ops_list = list(ops)   # (ctx, ray)
    total_sign = 1

    processed_rays = set()
    for i in range(5):
        for j in range(i+1, 5):
            v = shared[i][j]
            if v in processed_rays:
                continue
            # Find current positions of v in ops_list
            pos_v = [k for k, (_, r) in enumerate(ops_list) if r == v]
            assert len(pos_v) == 2
            p_left, p_right = pos_v[0], pos_v[1]
            # Move the right occurrence leftward past everything until adjacent to left
            while p_right > p_left + 1:
                w = ops_list[p_right - 1][1]
                sign_flip = (-1) ** symplectic_form(v, w)
                total_sign *= sign_flip
                # Swap ops_list[p_right] and ops_list[p_right-1]
                ops_list[p_right], ops_list[p_right-1] = \
                    ops_list[p_right-1], ops_list[p_right]
                p_right -= 1
            # Now ops_list[p_left] and ops_list[p_right] = ops_list[p_left+1] are W(v)W(v)
            # Remove both (they cancel to I)
            ops_list.pop(p_right)
            ops_list.pop(p_left)
            # Update positions for remaining ops
            processed_rays.add(v)

    assert len(ops_list) == 0, f"Expected empty ops_list, got {len(ops_list)}"

    # Count anticommuting cross-context pairs for statistics
    n_anti = 0
    anti_pairs = []
    for a in range(len(unique_rays)):
        for b in range(a+1, len(unique_rays)):
            va, vb = unique_rays[a], unique_rays[b]
            owners_a = ray_owners[va]
            owners_b = ray_owners[vb]
            if owners_a & owners_b:  # same-context pair → skip
                continue
            if symplectic_form(va, vb):
                n_anti += 1
                anti_pairs.append((va, vb))

    return total_sign, n_anti, anti_pairs


def main():
    t0 = time.time()

    print("[1/3] Enumerating...")
    lagrangians = find_lagrangians()
    pentagrams, all_contexts, context_signs, _ = enumerate_pentagrams(lagrangians)
    ctx_beta = {c: compute_beta(list(c)) for c in all_contexts}
    print(f"      {len(pentagrams)} pentagrams  ({time.time()-t0:.1f}s)")

    print("\n[2/3] K₅ structure + anticommutation analysis...")

    sign_dist     = defaultdict(int)   # total_sign → count
    n_anti_dist   = defaultdict(int)   # N_anticomm → count
    beta_vs_nanti = defaultdict(int)   # (β_sum mod 4, N mod 2) → count

    errors = []
    sample = []

    for pent_idx in pentagrams:
        five = [all_contexts[i] for i in pent_idx]
        beta_sum = sum(ctx_beta[c] for c in five)

        try:
            five_list, shared = build_k5_structure(five)
        except AssertionError as e:
            errors.append(str(e)); continue

        total_sign, n_anti, _ = sign_from_anticommutations(
            frozenset(five), shared)

        sign_dist[total_sign] += 1
        n_anti_dist[n_anti] += 1
        beta_vs_nanti[(beta_sum % 4, n_anti % 2)] += 1

        if len(sample) < 5:
            sample.append({
                'beta_sum': beta_sum,
                'total_sign': total_sign,
                'n_anti': n_anti,
            })

    print(f"      Errors: {len(errors)}")
    print(f"      Product sign distribution: {dict(sign_dist)}")
    print(f"      N_anticomm distribution:   {dict(n_anti_dist)}")
    print(f"      (β_sum mod 4, N mod 2) co-distribution:")
    for k, v in sorted(beta_vs_nanti.items()):
        print(f"        {k}: {v}")

    print("\n[3/3] Sample:")
    for d in sample:
        parity = "ODD" if d['n_anti'] % 2 == 1 else "EVEN"
        print(f"      β_sum={d['beta_sum']:+3d}  sign={d['total_sign']:+d}  "
              f"N_anti={d['n_anti']} ({parity})")

    # Key check: is N_anticomm always odd?
    all_odd = all(n % 2 == 1 for n in n_anti_dist.keys())
    print(f"\n>>> N_anticomm always odd? {all_odd}")
    print(f"    (If yes: proves ∏W_C = -I₈ algebraically!)")

    print(f"\nTotal: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
