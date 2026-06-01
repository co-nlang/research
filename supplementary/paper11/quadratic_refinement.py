#!/usr/bin/env python3
"""
Paper XI: Quadratic refinement approach to Conjecture 9.1.

For a context C = {v₁, v₂, v₃, v₄} with ∑vᵢ = 0 in F₂⁶:
  s(C) = (-1)^S  where S = ∑_{j<k} B(vⱼ, vₖ)
  B(a,b) = a_x · b_z  (integer dot product, NOT mod 2)

Total parity = ∏ sᵢ = (-1)^{∑ Sᵢ}

We verify:
1. s(C) matches pauli_product_sign for all contexts
2. ∑ Sᵢ is always odd for all 12,096 pentagrams
3. Decompose ∑ Sᵢ into ray-level and cross-context contributions
"""

import itertools
import numpy as np
from collections import defaultdict, Counter, deque
import time


def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

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
        if not all(symplectic_form(u, v) == 0
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


def B_form(a, b):
    """B(a,b) = a_x · b_z (INTEGER dot product, not mod 2)."""
    return a[0]*b[3] + a[1]*b[4] + a[2]*b[5]


def Q_form(v):
    """Q(v) = x₁z₁ + x₂z₂ + x₃z₃ (INTEGER)."""
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]


def context_S(context_points):
    """S = ∑_{j<k} B(vⱼ, vₖ) for ordered context."""
    pts = list(context_points)
    S = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            S += B_form(pts[j], pts[k])
    return S


def main():
    t0 = time.time()
    print("=" * 70)
    print("Paper XI: Quadratic Refinement Parity Proof")
    print("=" * 70)

    print("\n[1/4] Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    print("\n[2/4] Building contexts with sign verification...")
    all_contexts = []
    context_signs_pauli = []
    context_signs_B = []
    context_S_vals = []
    context_lag_idx = []
    n_mismatch = 0

    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4: continue

            sign_pauli = context_product_sign(ctx_pts)
            if sign_pauli == 0: continue

            S = context_S(ctx_pts)
            sign_B = (-1) ** (S % 2)

            if sign_pauli != sign_B:
                n_mismatch += 1

            all_contexts.append(frozenset(ctx_pts))
            context_signs_pauli.append(sign_pauli)
            context_signs_B.append(sign_B)
            context_S_vals.append(S)
            context_lag_idx.append(li)

    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts")
    print(f"  Sign formula mismatch: {n_mismatch}/{n_ctx}")

    # Verify formula on all contexts
    if n_mismatch == 0:
        print("  ✓ s(C) = (-1)^S verified for ALL contexts")
    else:
        print(f"  ✗ {n_mismatch} mismatches found!")

    print("\n[3/4] Enumerating pentagrams...")
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    pentagrams = []
    pent_parity_S = []
    pent_parity_pauli = []
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

                        # Pauli parity
                        parity_pauli = sum(1 for ci in clique if context_signs_pauli[ci] == -1)
                        if parity_pauli % 2 == 0: continue

                        pent = tuple(sorted(clique))
                        if pent in pentagrams: continue

                        # S-sum parity
                        S_sum = sum(context_S_vals[ci] for ci in clique)
                        parity_S = S_sum % 2

                        # Extract rays and their Q-values
                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]] & all_contexts[clique[b]]
                                if shared:
                                    r = next(iter(shared))
                                    rays[(a,b)] = r

                        ray_Q = {key: Q_form(r) for key, r in rays.items()}
                        total_ray_Q = sum(ray_Q.values())

                        pentagrams.append(pent)
                        pent_parity_S.append(parity_S)
                        pent_parity_pauli.append(parity_pauli % 2)
                        pent_ray_data.append({
                            'S_sum': S_sum,
                            'total_ray_Q': total_ray_Q,
                            'ray_Q': ray_Q,
                            'rays': rays,
                        })

    n_pent = len(pentagrams)
    print(f"  {n_pent} Mermin pentagrams")

    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")

    # Check 1: S-sum always odd?
    S_odd = sum(1 for p in pent_parity_S if p == 1)
    S_even = sum(1 for p in pent_parity_S if p == 0)
    print(f"\n--- S-sum parity ---")
    print(f"  Odd (parity = -1):  {S_odd} ({S_odd/n_pent*100:.1f}%)")
    print(f"  Even (parity = +1): {S_even} ({S_even/n_pent*100:.1f}%)")
    if S_odd == n_pent:
        print(f"  ✓ ALL pentagrams have odd S-sum → parity = -1")
    else:
        print(f"  ✗ {S_even} pentagrams have even S-sum!")

    # Check 2: Pauli parity always odd?
    P_odd = sum(1 for p in pent_parity_pauli if p == 1)
    print(f"\n--- Pauli parity ---")
    print(f"  Odd:  {P_odd} ({P_odd/n_pent*100:.1f}%)")

    # Check 3: S-sum parity matches Pauli parity?
    match = sum(1 for i in range(n_pent) if pent_parity_S[i] == pent_parity_pauli[i])
    print(f"\n--- S-parity vs Pauli parity match ---")
    print(f"  Match: {match}/{n_pent} ({match/n_pent*100:.1f}%)")

    # Check 4: Total ray Q distribution
    print(f"\n--- Total ray Q = ∑ Q(R_r) ---")
    Q_dist = Counter(d['total_ray_Q'] for d in pent_ray_data)
    for q, cnt in sorted(Q_dist.items()):
        print(f"  Q_total={q}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # Check 5: S_sum distribution
    print(f"\n--- S_sum distribution ---")
    S_dist = Counter(d['S_sum'] for d in pent_ray_data)
    for s, cnt in sorted(S_dist.items()):
        print(f"  S_sum={s}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # Check 6: Relationship between S_sum and total_ray_Q
    print(f"\n--- S_sum mod 2 vs total_ray_Q mod 2 ---")
    cross = Counter()
    for d in pent_ray_data:
        cross[(d['S_sum'] % 2, d['total_ray_Q'] % 2)] += 1
    for (sm, qm), cnt in sorted(cross.items()):
        print(f"  S_sum%2={sm}, Q_total%2={qm}: {cnt}")

    # Check 7: Decompose S_sum into ray-level and cross-context terms
    print(f"\n--- Decomposition analysis ---")
    # For each pentagram, compute:
    #   S_sum = ∑_i S_i = ∑_i ∑_{j<k, j,k≠i} B(R_{ij}, R_{ik})
    # Each pair of rays (R_{ab}, R_{cd}) appears in S_i iff i ∉ {a,b,c,d}
    # i.e., iff i is the 5th vertex not in {a,b,c,d}
    # So B(R_{ab}, R_{cd}) appears in S_i where i ∉ {a,b,c,d}
    # This means i = the unique vertex in {1,2,3,4,5} \ {a,b,c,d}
    # But {a,b} and {c,d} are edges sharing vertex i, so a=i or b=i, c=i or d=i
    # Wait, the rays in context i are R_{ij} for j≠i
    # So the pairs in S_i are (R_{ij}, R_{ik}) for j<k, j,k≠i
    # These are pairs of rays sharing vertex i

    # Let's compute the "B-matrix" for a representative pentagram
    print("  Representative pentagram B-matrix analysis:")
    d = pent_ray_data[0]
    rays = d['rays']
    print(f"  Rays:")
    for (a,b), r in sorted(rays.items()):
        print(f"    R_{{{a+1},{b+1}}} = {r}, Q={Q_form(r)}")

    # For each context i, the 4 rays are R_{i,j} for j≠i
    # S_i = sum of B(R_{i,j}, R_{i,k}) for j<k, j,k≠i
    print(f"\n  Context-level S decomposition:")
    for i in range(5):
        ctx_rays = []
        for j in range(5):
            if j == i: continue
            key = (min(i,j), max(i,j))
            ctx_rays.append(rays[key])
        S_i = 0
        for a in range(4):
            for b in range(a+1, 4):
                S_i += B_form(ctx_rays[a], ctx_rays[b])
        Q_sum_i = sum(Q_form(r) for r in ctx_rays)
        print(f"    Context {i+1}: S={S_i}, Q_sum={Q_sum_i}, S%2={S_i%2}, sign={(-1)**(S_i%2)}")

    # Global: S_sum = ∑ S_i
    # Each B(R_{ij}, R_{ik}) appears in exactly one S_i
    # Total number of B-terms: 5 × C(4,2) = 30
    # These are all ordered pairs of rays sharing a vertex

    # Key identity: for context i with rays summing to 0:
    #   Q(∑ rays) = 0 = ∑Q + ∑_{j<k} ω(r_j, r_k)
    #   ∑Q = -∑ω (as integers, but this is mod 2 identity)
    # Actually: Q(∑r) = ∑Q(r) + ∑_{j<k} [B(r_j,r_k) + B(r_k,r_j)]
    #          0       = ∑Q(r) + ∑_{j<k} ω(r_j,r_k)  (in F₂)
    # So ∑Q(r) ≡ ∑_{j<k} ω(r_j,r_k) (mod 2)

    # But S_i = ∑_{j<k} B(r_j, r_k) (ORDERED sum, not symmetric)
    # S_i ≠ ∑Q/2 in general

    # Let's check: is there a formula relating S_sum to ray Q-values?
    print(f"\n--- Formula search: S_sum vs ray Q-values ---")
    # For each pentagram, compute various ray-level invariants
    formula_match = 0
    for pi in range(min(n_pent, 1000)):
        d = pent_ray_data[pi]
        S_sum = d['S_sum']

        # Try: S_sum ≡ ∑ Q(R_r) + correction (mod 2)
        # The correction involves cross-terms between contexts

        # Compute: for each pair of rays NOT sharing a context vertex
        # i.e., R_{ab} and R_{cd} where {a,b} ∩ {c,d} = ∅
        # These are "opposite" edges of K₅
        # There are 15 pairs of edges in K₅, 5×C(4,2)=30 share a vertex
        # Wait: C(10,2) = 45 pairs of rays total. 30 share a vertex. 15 don't.
        # The 15 non-sharing pairs correspond to pairs of disjoint edges in K₅

        cross_B = 0
        rays_list = list(d['rays'].items())
        for idx1 in range(len(rays_list)):
            for idx2 in range(idx1+1, len(rays_list)):
                (a1,b1), r1 = rays_list[idx1]
                (a2,b2), r2 = rays_list[idx2]
                # Check if they share a vertex
                if len({a1,b1} & {a2,b2}) == 0:
                    # Disjoint edges: these appear in cross-context terms
                    cross_B += B_form(r1, r2)

        # Try formula: S_sum + cross_B ≡ ? (mod 2)
        total = (S_sum + cross_B) % 2
        # This should give us something

        # Also try: S_sum ≡ ∑Q + cross_ω (mod 2)
        total_Q = d['total_ray_Q']
        cross_omega = 0
        for idx1 in range(len(rays_list)):
            for idx2 in range(idx1+1, len(rays_list)):
                (a1,b1), r1 = rays_list[idx1]
                (a2,b2), r2 = rays_list[idx2]
                if len({a1,b1} & {a2,b2}) == 0:
                    cross_omega += symplectic_form(r1, r2)

        formula = (total_Q + cross_omega) % 2
        if formula == S_sum % 2:
            formula_match += 1

    print(f"  Formula S_sum ≡ ∑Q + ∑ω_cross (mod 2): {formula_match}/1000 match")

    # Try another formula
    formula_match2 = 0
    for pi in range(min(n_pent, 1000)):
        d = pent_ray_data[pi]
        S_sum = d['S_sum']
        total_Q = d['total_ray_Q']

        # Compute ALL pairwise ω between rays
        all_omega = 0
        rays_list = list(d['rays'].items())
        for idx1 in range(len(rays_list)):
            for idx2 in range(idx1+1, len(rays_list)):
                (_, _), r1 = rays_list[idx1]
                (_, _), r2 = rays_list[idx2]
                all_omega += symplectic_form(r1, r2)

        formula2 = (total_Q + all_omega) % 2
        if formula2 == S_sum % 2:
            formula_match2 += 1

    print(f"  Formula S_sum ≡ ∑Q + ∑ω_all (mod 2): {formula_match2}/1000 match")

    # Direct: S_sum ≡ ∑Q (mod 2)?
    formula_match3 = 0
    for pi in range(min(n_pent, 1000)):
        d = pent_ray_data[pi]
        if d['S_sum'] % 2 == d['total_ray_Q'] % 2:
            formula_match3 += 1
    print(f"  Formula S_sum ≡ ∑Q (mod 2): {formula_match3}/1000 match")

    # Try: S_sum ≡ ∑ B(R_{ab}, R_{cd}) over ALL ordered pairs (mod 2)
    formula_match4 = 0
    for pi in range(min(n_pent, 1000)):
        d = pent_ray_data[pi]
        S_sum = d['S_sum']
        rays_list = list(d['rays'].items())

        all_B = 0
        for idx1 in range(len(rays_list)):
            for idx2 in range(len(rays_list)):
                if idx1 == idx2: continue
                (_, _), r1 = rays_list[idx1]
                (_, _), r2 = rays_list[idx2]
                all_B += B_form(r1, r2)

        if all_B % 2 == S_sum % 2:
            formula_match4 += 1
    print(f"  Formula S_sum ≡ ∑B_all (mod 2): {formula_match4}/1000 match")

    # The key: total_B = ∑_{all ordered pairs} B(r_a, r_b)
    # = ∑_{a<b} [B(r_a,r_b) + B(r_b,r_a)]
    # = ∑_{a<b} ω(r_a, r_b)
    # So all_B = ∑_{a<b} ω(r_a, r_b) = all_omega

    # Let's try: S_sum mod 2 = ?
    # S_sum = ∑_i ∑_{j<k, j,k≠i} B(R_{ij}, R_{ik})
    # This is a sum of 30 B-terms (6 per context × 5 contexts)
    # Each B-term is B(R_{ij}, R_{ik}) where i,j,k are distinct

    # Let's enumerate all 30 terms and check which are always odd
    print(f"\n--- Per-term analysis of S_sum ---")
    term_parity = Counter()
    for pi in range(min(n_pent, 100)):
        d = pent_ray_data[pi]
        rays = d['rays']
        terms = []
        for i in range(5):
            ctx_rays = []
            for j in range(5):
                if j == i: continue
                key = (min(i,j), max(i,j))
                ctx_rays.append((j, rays[key]))
            for a in range(4):
                for b in range(a+1, 4):
                    ja, ra = ctx_rays[a]
                    jb, rb = ctx_rays[b]
                    terms.append(B_form(ra, rb) % 2)
        term_parity[tuple(terms)] += 1

    print(f"  {len(term_parity)} distinct term-parity patterns in 100 pentagrams")

    # Count how many of the 30 terms are always 1
    if term_parity:
        patterns = list(term_parity.keys())
        always_one = 0
        always_zero = 0
        for t_idx in range(30):
            vals = set(p[t_idx] for p in patterns)
            if vals == {1}: always_one += 1
            elif vals == {0}: always_zero += 1
        print(f"  Terms always 1: {always_one}")
        print(f"  Terms always 0: {always_zero}")
        print(f"  Terms variable: {30 - always_one - always_zero}")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
