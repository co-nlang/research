#!/usr/bin/env python3
"""
Paper XII: Test T-vector (sum of 10 rays) as the natural u candidate.

Check for all 12,096 pentagrams:
1. q(T) mod 2
2. ω_int(T, r) for all 10 rays
3. T ∈ L_i membership
4. Relationship between T and pentagram type
"""

import itertools
import numpy as np
from collections import defaultdict, Counter
import time

def symplectic_form_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def Q_form(v):
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]

def q_mod2(v):
    return (v[0]*v[3] + v[1]*v[4] + v[2]*v[5]) % 2

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


def main():
    t0 = time.time()
    print("=" * 70)
    print("Paper XII: T-vector Analysis")
    print("=" * 70)

    print("\n[1/2] Enumerating...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    I2 = np.array([[1, 0], [0, 1]], dtype=complex)
    XM = np.array([[0, 1], [1, 0]], dtype=complex)
    YM = np.array([[0, -1j], [1j, 0]], dtype=complex)
    ZM = np.array([[1, 0], [0, -1]], dtype=complex)
    PAULI = {'I': I2, 'X': XM, 'Y': YM, 'Z': ZM}

    def vec_to_pauli(v):
        chars = []
        for qubit in range(3):
            x, z = v[qubit], v[qubit + 3]
            if x == 0 and z == 0: chars.append('I')
            elif x == 1 and z == 0: chars.append('X')
            elif x == 1 and z == 1: chars.append('Y')
            else: chars.append('Z')
        return ''.join(chars)

    def pauli_matrix(s):
        mat = PAULI[s[0]]
        for ch in s[1:]: mat = np.kron(mat, PAULI[ch])
        return mat

    def context_product_sign(ctx_pts):
        mat = np.eye(8, dtype=complex)
        for v in ctx_pts:
            mat = mat @ pauli_matrix(vec_to_pauli(v))
        return int(round(mat[0, 0].real))

    all_contexts = []
    context_signs = []
    context_lag_idx = []

    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4: continue
            sign = context_product_sign(ctx_pts)
            if sign == 0: continue
            all_contexts.append(frozenset(ctx_pts))
            context_signs.append(sign)
            context_lag_idx.append(li)

    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts")

    print("  Building pentagrams...")
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    pentagrams = []
    pent_data = []
    seen_pents = set()

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
                        parity = sum(1 for ci in clique if context_signs[ci] == -1)
                        if parity % 2 == 0: continue
                        pent = tuple(sorted(clique))
                        if pent in seen_pents: continue
                        seen_pents.add(pent)

                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]] & all_contexts[clique[b]]
                                if shared:
                                    rays[(a,b)] = next(iter(shared))

                        lag_indices = [context_lag_idx[ci] for ci in clique]
                        lag_sets = [lagrangians[li] for li in lag_indices]

                        # Compute T = XOR sum of all 10 rays
                        T = [0] * 6
                        for r in rays.values():
                            for idx in range(6):
                                T[idx] ^= r[idx]
                        T = tuple(T)

                        # ω_int(T, r) for each ray
                        omega_T_rays = [omega_int(T, r) for r in rays.values()]

                        # T ∈ L_i?
                        T_in_lag = [T in ls for ls in lag_sets]

                        pentagrams.append(pent)
                        pent_data.append({
                            'rays': rays,
                            'lag_sets': lag_sets,
                            'lag_indices': lag_indices,
                            'T': T,
                            'q_T': q_mod2(T),
                            'Q_T': Q_form(T),
                            'omega_T_rays': omega_T_rays,
                            'T_in_lag': T_in_lag,
                        })

    n_pent = len(pentagrams)
    print(f"  {n_pent} Mermin pentagrams")

    print(f"\n[2/2] Analysis...")
    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")

    # q(T) distribution
    q_T_dist = Counter(d['q_T'] for d in pent_data)
    print(f"\n--- q(T) mod 2 distribution ---")
    for v, cnt in sorted(q_T_dist.items()):
        print(f"  q(T)={v}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # Q(T) integer distribution
    Q_T_dist = Counter(d['Q_T'] for d in pent_data)
    print(f"\n--- Q(T) integer distribution ---")
    for v, cnt in sorted(Q_T_dist.items()):
        print(f"  Q(T)={v}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # ω_int(T, r) for all rays
    print(f"\n--- ω_int(T, r) for all 10 rays ---")
    all_omega_1 = 0
    all_omega_odd = 0
    omega_mod2_patterns = Counter()
    for d in pent_data:
        mods = tuple(w % 2 for w in d['omega_T_rays'])
        omega_mod2_patterns[mods] += 1
        if all(w % 2 == 1 for w in d['omega_T_rays']):
            all_omega_1 += 1
        if all(w % 2 == 1 for w in d['omega_T_rays']):
            all_omega_odd += 1

    print(f"  All ω_int(T,r) odd: {all_omega_1}/{n_pent} ({all_omega_1/n_pent*100:.1f}%)")
    print(f"  Distinct ω mod 2 patterns: {len(omega_mod2_patterns)}")
    top_patterns = omega_mod2_patterns.most_common(5)
    for pat, cnt in top_patterns:
        print(f"    {pat}: {cnt} ({cnt/n_pent*100:.1f}%)")

    # T ∈ L_i membership
    print(f"\n--- T ∈ L_i membership ---")
    T_in_any = sum(1 for d in pent_data if any(d['T_in_lag']))
    T_in_none = sum(1 for d in pent_data if not any(d['T_in_lag']))
    T_in_count = Counter(sum(d['T_in_lag']) for d in pent_data)
    print(f"  T ∈ at least one L_i: {T_in_any}/{n_pent} ({T_in_any/n_pent*100:.1f}%)")
    print(f"  T ∈ no L_i: {T_in_none}/{n_pent} ({T_in_none/n_pent*100:.1f}%)")
    for cnt, num in sorted(T_in_count.items()):
        print(f"    T in {cnt} Lagrangians: {num} pentagrams")

    # T distinct values
    T_values = Counter(d['T'] for d in pent_data)
    print(f"\n--- T distinct values ---")
    print(f"  {len(T_values)} distinct T vectors")
    print(f"  Top 5: {T_values.most_common(5)}")

    # For pentagrams where q(T)=1: is T a q=1 vector?
    q1_T = [d for d in pent_data if d['q_T'] == 1]
    print(f"\n--- Pentagrams with q(T)=1: {len(q1_T)} ---")
    if q1_T:
        omega_all_odd = sum(1 for d in q1_T if all(w % 2 == 1 for w in d['omega_T_rays']))
        print(f"  All ω_int(T,r) odd: {omega_all_odd}/{len(q1_T)} ({omega_all_odd/len(q1_T)*100:.1f}%)")

    # Integer ω_int(T, r) values
    print(f"\n--- Integer ω_int(T, r) values ---")
    all_omega_vals = Counter()
    for d in pent_data:
        for w in d['omega_T_rays']:
            all_omega_vals[w] += 1
    for v, cnt in sorted(all_omega_vals.items()):
        print(f"  ω_int={v}: {cnt}")

    # Check: T = 0?
    T_zero = sum(1 for d in pent_data if d['T'] == (0,0,0,0,0,0))
    print(f"\n--- T = 0: {T_zero}/{n_pent} ---")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
