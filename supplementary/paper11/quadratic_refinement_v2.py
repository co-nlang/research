#!/usr/bin/env python3
"""
Paper XI: Corrected quadratic refinement.

For a context C = (v₁, v₂, v₃, v₄) with ∑vᵢ = 0 in F₂⁶:
  P(v₁)P(v₂)P(v₃)P(v₄) = i^β · I
  β = ∑_{j<k} ω(vⱼ, vₖ)  where ω(a,b) = a_x·b_z - a_z·b_x (INTEGER)

For Lagrangian: ω(vⱼ,vₖ) = 0 for all pairs, so:
  β = ∑_{j<k} [B(j,k) - B(k,j)] ... WRONG, ω=0 means B(j,k)=B(k,j)

Actually: β = ∑_{j<k} (xⱼzₖ - zⱼxₖ) = ∑_{j<k} ω_int(j,k)
where ω_int is the INTEGER symplectic form (not mod 2).

For Lagrangian: ω_int(j,k) is EVEN for all pairs.
So β = ∑ (even numbers) = even.
sign = i^β = i^{2m} = (-1)^m where m = β/2.

This script computes β correctly and verifies.
"""

import itertools
import numpy as np
from collections import defaultdict, Counter
import time


def symplectic_form_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def omega_int(a, b):
    """Integer symplectic form: x_a·z_b - z_a·x_b (NOT mod 2)."""
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def B_form(a, b):
    """B(a,b) = a_x · b_z (integer)."""
    return a[0]*b[3] + a[1]*b[4] + a[2]*b[5]

def Q_form(v):
    """Q(v) = x₁z₁ + x₂z₂ + x₃z₃ (integer)."""
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]

def add(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))

def gf2_rank(vectors):
    if not vectors: return 0
    rows = [list(v) for v in vectors]
    ncols = len(rows[0]); rank = 0
    for col in range(ncols):
        pivot = None
        for r in range(rank, len(rows)):
            if rows[r][col] == 1: pivot = r; break
        if pivot is not None:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for r in range(len(rows)):
                if r != rank and rows[r][col] == 1:
                    rows[r] = [(rows[r][c] + rows[rank][c]) % 2 for c in range(ncols)]
            rank += 1
    return rank

def span_subspace(basis):
    pts = set()
    for mask in range(1, 1 << len(basis)):
        v = [0] * 6
        for i in range(len(basis)):
            if mask & (1 << i):
                v = [(a + b) % 2 for a, b in zip(v, basis[i])]
        pts.add(tuple(v))
    return frozenset(pts)

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
V_SET = set(p for p in ALL_POINTS if p[3] == 0 and p[4] == 0 and p[5] == 0)


def find_lagrangians():
    lagrangians, seen = [], set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3: continue
        if not all(symplectic_form_mod2(u, v) == 0
                   for u, v in itertools.combinations(basis, 2)): continue
        subspace = span_subspace(basis)
        if subspace not in seen:
            seen.add(subspace); lagrangians.append(subspace)
    return lagrangians

def get_fano_lines(lag_points):
    pts = list(lag_points); lines = set()
    for i in range(7):
        for j in range(i + 1, 7):
            s = add(pts[i], pts[j])
            if s in lag_points:
                lines.add(frozenset([pts[i], pts[j], s]))
    return list(lines)

I2 = np.array([[1, 0], [0, 1]], dtype=complex)
XM = np.array([[0, 1], [1, 0]], dtype=complex)
YM = np.array([[0, -1j], [1j, 0]], dtype=complex)
ZM = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {'I': I2, 'X': XM, 'Y': YM, 'Z': ZM}

def vec_to_pauli(v):
    chars = []
    for q in range(3):
        x, z = v[q], v[q + 3]
        if x == 0 and z == 0: chars.append('I')
        elif x == 1 and z == 0: chars.append('X')
        elif x == 1 and z == 1: chars.append('Y')
        else: chars.append('Z')
    return ''.join(chars)

def pauli_matrix(s):
    mat = PAULI[s[0]]
    for ch in s[1:]: mat = np.kron(mat, PAULI[ch])
    return mat

def context_product_sign(context_points):
    mat = np.eye(8, dtype=complex)
    for v in context_points:
        mat = mat @ pauli_matrix(vec_to_pauli(v))
    return int(round(mat[0, 0].real))


def compute_beta(context_points):
    """β = ∑_{j<k} ω_int(vⱼ, vₖ) for the given ordering."""
    pts = list(context_points)
    beta = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            beta += omega_int(pts[j], pts[k])
    return beta


def compute_S(context_points):
    """S = ∑_{j<k} B(vⱼ, vₖ) for the given ordering."""
    pts = list(context_points)
    S = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            S += B_form(pts[j], pts[k])
    return S


def main():
    t0 = time.time()
    print("=" * 70)
    print("Paper XI: Corrected Quadratic Refinement")
    print("=" * 70)

    print("\n[1/3] Enumerating Lagrangians and contexts...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    all_contexts = []
    context_signs_pauli = []
    context_betas = []
    context_S_vals = []
    context_lag_idx = []
    n_mismatch_beta = 0
    n_mismatch_S = 0

    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4: continue

            sign_pauli = context_product_sign(ctx_pts)
            if sign_pauli == 0: continue

            beta = compute_beta(ctx_pts)
            S = compute_S(ctx_pts)

            # β should be even for Lagrangian contexts
            # sign = i^β: if β ≡ 0 (mod 4) → +1, if β ≡ 2 (mod 4) → -1
            sign_beta = 1 if beta % 4 == 0 else (-1 if beta % 4 == 2 else 0)

            # S formula: sign = (-1)^S
            sign_S = (-1) ** (S % 2)

            if sign_pauli != sign_beta:
                n_mismatch_beta += 1
            if sign_pauli != sign_S:
                n_mismatch_S += 1

            all_contexts.append(frozenset(ctx_pts))
            context_signs_pauli.append(sign_pauli)
            context_betas.append(beta)
            context_S_vals.append(S)
            context_lag_idx.append(li)

    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts")
    print(f"  β formula mismatches: {n_mismatch_beta}/{n_ctx}")
    print(f"  S formula mismatches: {n_mismatch_S}/{n_ctx}")

    # Check: is β always even?
    beta_odd = sum(1 for b in context_betas if b % 2 != 0)
    print(f"  β odd count: {beta_odd}/{n_ctx}")

    # Check: β mod 4 distribution
    beta_mod4 = Counter(b % 4 for b in context_betas)
    print(f"  β mod 4 distribution: {dict(sorted(beta_mod4.items()))}")

    # Check: β/2 mod 2 vs S mod 2
    match_half_beta_S = sum(1 for i in range(n_ctx)
                           if (context_betas[i] // 2) % 2 == context_S_vals[i] % 2)
    print(f"  (β/2) mod 2 == S mod 2: {match_half_beta_S}/{n_ctx}")

    # Check: β vs 2S
    match_beta_2S = sum(1 for i in range(n_ctx) if context_betas[i] == 2 * context_S_vals[i])
    print(f"  β == 2S: {match_beta_2S}/{n_ctx}")

    # Check: β mod 4 vs 2*(S mod 2)
    match_mod = sum(1 for i in range(n_ctx)
                    if context_betas[i] % 4 == (2 * (context_S_vals[i] % 2)))
    print(f"  β mod 4 == 2*(S mod 2): {match_mod}/{n_ctx}")

    # Diagnostic: show some mismatches
    if n_mismatch_S > 0:
        print(f"\n  First 5 S-formula mismatches:")
        shown = 0
        for i in range(n_ctx):
            sign_p = context_signs_pauli[i]
            sign_s = (-1) ** (context_S_vals[i] % 2)
            if sign_p != sign_s and shown < 5:
                ctx = list(all_contexts[i])
                beta = context_betas[i]
                S = context_S_vals[i]
                print(f"    ctx={ctx}")
                print(f"    pauli={sign_p}, S={S}, (-1)^S={sign_s}, β={beta}, β%4={beta%4}")
                # Show ω_int for all pairs
                for j in range(4):
                    for k in range(j+1, 4):
                        w = omega_int(ctx[j], ctx[k])
                        b = B_form(ctx[j], ctx[k])
                        print(f"      ω({j},{k})={w}, B({j},{k})={b}, B({k},{j})={B_form(ctx[k], ctx[j])}")
                shown += 1

    print(f"\n[2/3] Enumerating pentagrams with corrected formula...")
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    pentagrams = []
    pent_beta_sum = []
    pent_S_sum = []
    pent_parity = []
    pent_ray_data = []

    for i in range(n_ctx):
        for j in adj[i]:
            if j <= i: continue
            for k in adj[j]:
                if k <= j or k not in adj[i]: continue
                for m in adj[k]:
                    if m <= k or m not in adj[i] or m not in adj[j]: continue
                    for p in adj[m]:
                        if p <= m or p not in adj[i] or p not in adj[j] or p not in adj[k]: continue
                        clique = [i, j, k, m, p]
                        all_ops = set()
                        for ci in clique: all_ops |= all_contexts[ci]
                        if len(all_ops) != 10: continue

                        parity = sum(1 for ci in clique if context_signs_pauli[ci] == -1)
                        if parity % 2 == 0: continue

                        pent = tuple(sorted(clique))
                        if pent in pentagrams: continue

                        b_sum = sum(context_betas[ci] for ci in clique)
                        s_sum = sum(context_S_vals[ci] for ci in clique)

                        # Extract rays
                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]] & all_contexts[clique[b]]
                                if shared:
                                    rays[(a,b)] = next(iter(shared))

                        ray_Q = {key: Q_form(r) for key, r in rays.items()}
                        total_ray_Q = sum(ray_Q.values())

                        # Compute all pairwise ω between rays
                        rays_list = list(rays.values())
                        total_omega = 0
                        for ri in range(len(rays_list)):
                            for rj in range(ri+1, len(rays_list)):
                                total_omega += omega_int(rays_list[ri], rays_list[rj])

                        pentagrams.append(pent)
                        pent_beta_sum.append(b_sum)
                        pent_S_sum.append(s_sum)
                        pent_parity.append(parity)
                        pent_ray_data.append({
                            'beta_sum': b_sum,
                            'S_sum': s_sum,
                            'total_ray_Q': total_ray_Q,
                            'total_omega': total_omega,
                            'ray_Q': ray_Q,
                            'rays': rays,
                        })

    n_pent = len(pentagrams)
    print(f"  {n_pent} Mermin pentagrams")

    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")

    # β-sum parity
    print(f"\n--- β-sum = ∑βᵢ ---")
    beta_sum_mod4 = Counter(d['beta_sum'] % 4 for d in pent_ray_data)
    print(f"  β_sum mod 4: {dict(sorted(beta_sum_mod4.items()))}")

    # β-sum always ≡ 2 (mod 4)?
    beta_sum_2mod4 = sum(1 for d in pent_ray_data if d['beta_sum'] % 4 == 2)
    print(f"  β_sum ≡ 2 (mod 4): {beta_sum_2mod4}/{n_pent} ({beta_sum_2mod4/n_pent*100:.1f}%)")

    # S-sum parity
    S_sum_odd = sum(1 for d in pent_ray_data if d['S_sum'] % 2 == 1)
    print(f"\n--- S-sum parity ---")
    print(f"  S_sum odd: {S_sum_odd}/{n_pent} ({S_sum_odd/n_pent*100:.1f}%)")

    # Key identity: β_sum = 2*S_sum + correction?
    print(f"\n--- β vs 2S relationship ---")
    beta_eq_2S = sum(1 for d in pent_ray_data if d['beta_sum'] == 2 * d['S_sum'])
    print(f"  β_sum == 2·S_sum: {beta_eq_2S}/{n_pent}")

    # β_sum mod 4
    print(f"\n--- β_sum mod 4 distribution ---")
    for m, cnt in sorted(beta_sum_mod4.items()):
        print(f"  {m}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # Key formula: ∏ sign_i = ∏ (-1)^{βᵢ/2} = (-1)^{∑ βᵢ/2}
    # Since βᵢ is always even, βᵢ/2 is an integer
    half_beta_sum_parity = Counter()
    for d in pent_ray_data:
        half_beta = d['beta_sum'] // 2
        half_beta_sum_parity[half_beta % 2] += 1
    print(f"\n--- (∑ βᵢ/2) mod 2 ---")
    for p, cnt in sorted(half_beta_sum_parity.items()):
        print(f"  {p}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # Relationship: ∑(βᵢ/2) ≡ ∑Q(rays) + correction (mod 2)?
    print(f"\n--- Formula search for ∑(β/2) mod 2 ---")
    f1 = sum(1 for d in pent_ray_data if (d['beta_sum']//2) % 2 == d['total_ray_Q'] % 2)
    print(f"  ∑(β/2) ≡ ∑Q(rays) (mod 2): {f1}/{n_pent}")

    f2 = sum(1 for d in pent_ray_data
             if (d['beta_sum']//2) % 2 == (d['total_ray_Q'] + d['total_omega']) % 2)
    print(f"  ∑(β/2) ≡ ∑Q + ∑ω (mod 2): {f2}/{n_pent}")

    # total_omega should be 0 for cap rays... check
    omega_dist = Counter(d['total_omega'] for d in pent_ray_data)
    print(f"\n--- Total ω between ray pairs ---")
    for w, cnt in sorted(omega_dist.items())[:10]:
        print(f"  ω_total={w}: {cnt}")

    # ∑Q + ∑ω/2 ?
    # Since rays are NOT in the same Lagrangian, ω can be nonzero
    # But ω is always an integer (could be odd or even)
    omega_mod2 = Counter(d['total_omega'] % 2 for d in pent_ray_data)
    print(f"\n--- ω_total mod 2 ---")
    for m, cnt in sorted(omega_mod2.items()):
        print(f"  {m}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # Try: ∑(β/2) ≡ ∑Q + ∑ω (mod 2) where ∑ω is over CROSS-context pairs only
    print(f"\n--- Cross-context ω ---")
    cross_match = 0
    for pi in range(min(n_pent, 1000)):
        d = pent_ray_data[pi]
        rays_list = list(d['rays'].items())
        cross_omega = 0
        for i1 in range(len(rays_list)):
            for i2 in range(i1+1, len(rays_list)):
                (a1,b1), r1 = rays_list[i1]
                (a2,b2), r2 = rays_list[i2]
                if len({a1,b1} & {a2,b2}) == 0:  # disjoint edges
                    cross_omega += omega_int(r1, r2)
        formula = (d['total_ray_Q'] + cross_omega) % 2
        if formula == (d['beta_sum'] // 2) % 2:
            cross_match += 1
    print(f"  ∑(β/2) ≡ ∑Q + ∑ω_cross (mod 2): {cross_match}/1000")

    # The master formula:
    # For each context i: βᵢ = ∑_{j<k} ω_int(rⱼ, rₖ) where rⱼ,rₖ are in context i
    # ∑ᵢ βᵢ = ∑ᵢ ∑_{j<k in ctx i} ω_int(rⱼ, rₖ)
    # Each pair of rays sharing a vertex appears in exactly one context
    # So ∑βᵢ = ∑_{sharing pairs} ω_int(r_a, r_b)
    #
    # Now: ω_int(a,b) = B(a,b) - B(b,a)
    # For sharing pairs in context i: both a,b ∈ L_i, so ω_mod2(a,b) = 0
    # But ω_int can be ±2, ±4, etc (even but nonzero)
    #
    # Total: ∑βᵢ = ∑_{sharing pairs} ω_int(r_a, r_b)
    # Since each ω_int is even, ∑βᵢ is even.
    # ∑βᵢ/2 = ∑_{sharing pairs} ω_int(r_a, r_b)/2

    # Let's compute ∑βᵢ/2 mod 2 directly
    print(f"\n--- Direct computation: ∑(βᵢ/2) mod 2 ---")
    half_beta_parity = sum(1 for d in pent_ray_data if (d['beta_sum'] // 2) % 2 == 1)
    print(f"  ∑(β/2) odd: {half_beta_parity}/{n_pent} ({half_beta_parity/n_pent*100:.1f}%)")

    # The answer: ∑(βᵢ/2) mod 2 should ALWAYS be 1 (= odd parity)
    if half_beta_parity == n_pent:
        print(f"  ✓ ALL pentagrams have ∑(β/2) odd → parity = -1")
        print(f"  ✓ CONJECTURE 9.1 PROVEN COMPUTATIONALLY!")
    else:
        print(f"  ✗ {n_pent - half_beta_parity} pentagrams have ∑(β/2) even!")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
