#!/usr/bin/env python3
"""
β_sum distribution and h-pattern analysis per k-profile.

Computes for all 12,096 pentagrams:
1. β_sum = Σ β(Cᵢ) where β(Cᵢ) = Σ_{j<k} ω_int(rⱼ, rₖ)
2. h(Cᵢ) = β(Cᵢ)/2 mod 2
3. k-profile per pentagram
4. h-pattern per pentagram (tuple of h values)
5. Distribution by k-profile
"""

import itertools
import numpy as np
from collections import defaultdict, Counter

# ============================================================
# Symplectic geometry
# ============================================================

def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def add(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))

def gf2_rank(vectors):
    if not vectors: return 0
    rows = [list(v) for v in vectors]; ncols = len(rows[0]); rank = 0
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
    pts = set(); n = len(basis)
    for mask in range(1, 1 << n):
        v = [0] * len(basis[0])
        for i in range(n):
            if mask & (1 << i):
                v = [(a + b) % 2 for a, b in zip(v, basis[i])]
        pts.add(tuple(v))
    return frozenset(pts)

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]

def find_lagrangians():
    lagrangians, seen = [], set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3: continue
        if not all(symplectic_form(u, v) == 0 for u, v in itertools.combinations(basis, 2)): continue
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


# ============================================================
# Pauli
# ============================================================

PAULI = {
    'I': np.array([[1, 0], [0, 1]], dtype=complex),
    'X': np.array([[0, 1], [1, 0]], dtype=complex),
    'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
    'Z': np.array([[1, 0], [0, -1]], dtype=complex),
}

def vec_to_pauli(v):
    chars = []
    for q in range(3):
        x, z = v[q], v[q + 3]
        if x == 0 and z == 0: chars.append('I')
        elif x == 1 and z == 0: chars.append('X')
        elif x == 1 and z == 1: chars.append('Y')
        else: chars.append('Z')
    return ''.join(chars)

def pauli_product_sign(operators):
    mat = np.eye(8, dtype=complex)
    for v in operators:
        s = vec_to_pauli(v)
        op = PAULI[s[0]]
        for ch in s[1:]: op = np.kron(op, PAULI[ch])
        mat = mat @ op
    return int(round(mat[0, 0].real))


# ============================================================
# Pentagram enumeration
# ============================================================

def enumerate_pentagrams(lagrangians):
    all_contexts = []; context_signs = []; context_lag_idx = []
    for li, lag in enumerate(lagrangians):
        pts = list(lag); fano_lines = get_fano_lines(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4: continue
            sign = pauli_product_sign(ctx_pts)
            if sign == 0: continue
            all_contexts.append(frozenset(ctx_pts))
            context_signs.append(sign)
            context_lag_idx.append(li)

    n_ctx = len(all_contexts)
    print("  Building adjacency...")
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    print("  Finding K₅ cliques...")
    pentagrams = []
    for i in range(n_ctx):
        for j in adj[i]:
            if j <= i: continue
            common_ij = set(adj[i]) & set(adj[j])
            for k in common_ij:
                if k <= j: continue
                common_ijk = common_ij & set(adj[k])
                for m in common_ijk:
                    if m <= k: continue
                    common_ijkm = common_ijk & set(adj[m])
                    for p in common_ijkm:
                        if p <= m: continue
                        clique = [i, j, k, m, p]
                        all_ops = set()
                        for ci in clique: all_ops |= all_contexts[ci]
                        if len(all_ops) != 10: continue
                        parity = sum(1 for ci in clique if context_signs[ci] == -1)
                        if parity % 2 == 1:
                            pentagrams.append(tuple(sorted(clique)))

    return list(set(pentagrams)), all_contexts, context_signs, context_lag_idx


# ============================================================
# β computation
# ============================================================

def compute_beta(context_pts):
    """β = Σ_{j<k} ω_int(rⱼ, rₖ) for ordered context points."""
    pts = list(context_pts)
    beta = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            beta += omega_int(pts[j], pts[k])
    return beta


def compute_k_profile(pentagram, context_lag_idx, lagrangians):
    k_values = []
    for ci in pentagram:
        li = context_lag_idx[ci]
        lag = lagrangians[li]
        k = sum(1 for v in lag if v[3] == 0 and v[4] == 0 and v[5] == 0)
        k_values.append(k)
    return tuple(sorted(k_values, reverse=True))


# ============================================================
# Main
# ============================================================

def main():
    import time
    t0 = time.time()

    print("=" * 70)
    print("Paper XIV: β_sum Distribution and h-Pattern Analysis")
    print("=" * 70)

    print("\n[1/3] Enumerating Lagrangians and pentagrams...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(lagrangians)
    print(f"  {len(pentagrams)} pentagrams")

    print("\n[2/3] Computing β_sum and h-patterns...")
    # Per pentagram data
    beta_sum_dist = Counter()
    beta_sum_mod4_dist = Counter()
    k_profile_data = defaultdict(lambda: {
        'count': 0,
        'beta_sum_dist': Counter(),
        'h_pattern_dist': Counter(),
        'parity_dist': Counter(),
        'beta_per_context': Counter(),  # individual β values
    })

    for pi, pent in enumerate(pentagrams):
        # β per context
        context_betas = []
        context_h = []
        for ci in pent:
            beta = compute_beta(all_contexts[ci])
            context_betas.append(beta)
            context_h.append((beta // 2) % 2)

        beta_sum = sum(context_betas)
        h_pattern = tuple(sorted(context_h))  # sorted for canonical form
        parity = sum(1 for ci in pent if context_signs[ci] == -1)
        kp = compute_k_profile(pent, context_lag_idx, lagrangians)

        beta_sum_dist[beta_sum] += 1
        beta_sum_mod4_dist[beta_sum % 4] += 1

        kd = k_profile_data[kp]
        kd['count'] += 1
        kd['beta_sum_dist'][beta_sum] += 1
        kd['h_pattern_dist'][h_pattern] += 1
        kd['parity_dist'][parity] += 1
        for b in context_betas:
            kd['beta_per_context'][b] += 1

        if (pi + 1) % 2000 == 0:
            print(f"  {pi+1}/{len(pentagrams)}...")

    print("\n[3/3] Results...")

    # Global β_sum distribution
    print(f"\n{'=' * 70}")
    print("GLOBAL β_sum DISTRIBUTION")
    print(f"{'=' * 70}")
    print(f"  Range: [{min(beta_sum_dist.keys())}, {max(beta_sum_dist.keys())}]")
    print(f"  β_sum mod 4: {dict(sorted(beta_sum_mod4_dist.items()))}")
    print(f"  Most common β_sum values:")
    for bs, count in beta_sum_dist.most_common(10):
        print(f"    β_sum = {bs}: {count} ({100*count/len(pentagrams):.1f}%)")

    # β_sum/2 distribution
    beta_half_dist = Counter(bs // 2 for bs in beta_sum_dist.elements())
    print(f"\n  β_sum/2 range: [{min(beta_half_dist.keys())}, {max(beta_half_dist.keys())}]")

    # Per k-profile
    print(f"\n{'=' * 70}")
    print("PER k-PROFILE ANALYSIS")
    print(f"{'=' * 70}")

    for kp in sorted(k_profile_data.keys(), key=lambda x: -k_profile_data[x]['count']):
        kd = k_profile_data[kp]
        print(f"\n  k-profile {kp}: {kd['count']} pentagrams ({100*kd['count']/len(pentagrams):.1f}%)")

        # β_sum range
        bs_values = sorted(kd['beta_sum_dist'].keys())
        print(f"    β_sum range: [{bs_values[0]}, {bs_values[-1]}]")
        print(f"    β_sum mod 4: {dict(sorted(Counter(b % 4 for b in bs_values for _ in range(kd['beta_sum_dist'][b])).items()))}")

        # Top β_sum values
        print(f"    Top β_sum: ", end="")
        for bs, count in kd['beta_sum_dist'].most_common(5):
            print(f"{bs}({count}) ", end="")
        print()

        # h-patterns
        print(f"    h-patterns (sorted): {len(kd['h_pattern_dist'])} distinct")
        for hp, count in sorted(kd['h_pattern_dist'].items(), key=lambda x: -x[1])[:5]:
            print(f"      {hp}: {count} ({100*count/kd['count']:.1f}%)")

        # Parity distribution
        print(f"    Parity: ", end="")
        for p in sorted(kd['parity_dist'].keys()):
            print(f"{p}-minus={kd['parity_dist'][p]} ({100*kd['parity_dist'][p]/kd['count']:.1f}%) ", end="")
        print()

    # Cross-k-profile β_sum comparison
    print(f"\n{'=' * 70}")
    print("β_sum STATISTICS BY k-PROFILE")
    print(f"{'=' * 70}")
    print(f"  {'k-profile':>15} {'Count':>7} {'Mean β':>8} {'Median β':>10} {'Std β':>8} {'Min β':>7} {'Max β':>7}")
    print(f"  {'-'*15} {'-'*7} {'-'*8} {'-'*10} {'-'*8} {'-'*7} {'-'*7}")
    for kp in sorted(k_profile_data.keys(), key=lambda x: -k_profile_data[x]['count']):
        kd = k_profile_data[kp]
        bs_list = []
        for bs, count in kd['beta_sum_dist'].items():
            bs_list.extend([bs] * count)
        bs_arr = np.array(bs_list)
        print(f"  {str(kp):>15} {kd['count']:>7} {bs_arr.mean():>8.1f} {np.median(bs_arr):>10.0f} {bs_arr.std():>8.1f} {bs_arr.min():>7} {bs_arr.max():>7}")

    print(f"\n{'=' * 70}")
    print(f"Total time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
