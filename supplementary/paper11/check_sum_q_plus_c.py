#!/usr/bin/env python3
"""
Quick check: is ∑Q + c_sharing always even?
(Modify verify_conditions.py output)
"""

import itertools
import numpy as np
from collections import defaultdict
import time


def symplectic_form_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def Q_form(v):
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]

def correction(a, b):
    return sum(a[2*k] * a[2*k+1] * b[2*k] * b[2*k+1] for k in range(3))

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
    pts = list(context_points)
    beta = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            beta += omega_int(pts[j], pts[k])
    return beta


def main():
    t0 = time.time()
    print("Enumerating...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    all_contexts = []
    context_signs_pauli = []
    context_betas = []

    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4: continue
            sign_pauli = context_product_sign(ctx_pts)
            if sign_pauli == 0: continue
            beta = compute_beta(ctx_pts)
            all_contexts.append(frozenset(ctx_pts))
            context_signs_pauli.append(sign_pauli)
            context_betas.append(beta)

    n_ctx = len(all_contexts)
    print(f"  {n_ctx} contexts")

    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    n_pent = 0
    sum_q_plus_c_even = 0
    sum_q_plus_c_odd = 0

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

                        n_pent += 1

                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]] & all_contexts[clique[b]]
                                if shared:
                                    rays[(a,b)] = next(iter(shared))

                        rays_list = list(rays.values())

                        sum_q = sum(Q_form(r) for r in rays_list)

                        c_sum = 0
                        for (a1,b1), r1 in rays.items():
                            for (a2,b2), r2 in rays.items():
                                if (a1,b1) >= (a2,b2): continue
                                if set([a1,b1]) & set([a2,b2]):
                                    c_sum += correction(r1, r2)

                        if (sum_q + c_sum) % 2 == 0:
                            sum_q_plus_c_even += 1
                        else:
                            sum_q_plus_c_odd += 1

        if n_pent > 0 and n_pent % 4000 == 0:
            print(f"  ... {n_pent}")

    print(f"\n{'=' * 70}")
    print(f"Results ({n_pent} pentagrams):")
    print(f"{'=' * 70}")
    print(f"∑Q + c_sharing even: {sum_q_plus_c_even} ({100*sum_q_plus_c_even/n_pent:.1f}%)")
    print(f"∑Q + c_sharing odd:  {sum_q_plus_c_odd} ({100*sum_q_plus_c_odd/n_pent:.1f}%)")

    if sum_q_plus_c_odd == 0:
        print("\n✓ ∑Q + c_sharing ≡ 0 (mod 2) for ALL pentagrams!")
        print("\nProof complete:")
        print("  ∑h ≡ ∑Q + ω_ns + c_sharing")
        print("     ≡ (∑Q + c_sharing) + ω_ns")
        print("     ≡ 0 + 1 = 1 (mod 2)")
    else:
        print("\n✗ ∑Q + c_sharing is NOT always even")

    print(f"\nTime: {time.time() - t0:.1f}s")


if __name__ == '__main__':
    main()
