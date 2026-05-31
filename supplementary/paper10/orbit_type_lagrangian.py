#!/usr/bin/env python3
"""
Orbit-Type Analysis using LAGRANGIAN V-intersection profile.
Matches the old classification from paper10_conjecture25.py:
  - For each context, look at its Lagrangian's intersection with V
  - k=0 Lagrangian → label 0 (transverse)
  - k=1 Lagrangian → label = Fano point
  - k=3/k=7 Lagrangian → label -1
  - Type = (transverse count, distinct Fano point count)
"""

import itertools
import numpy as np
from collections import defaultdict, deque
import time

G2_GEN1_ATLAS = np.array([
    [1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1],
], dtype=int)
G2_GEN2_ATLAS = np.array([
    [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1],
], dtype=int)


def find_symplectic_form(generators):
    n = 6
    unknowns = [(i, j) for i in range(n) for j in range(i + 1, n)]
    idx = {pair: k for k, pair in enumerate(unknowns)}
    equations = []
    for M in generators:
        for a in range(n):
            for b in range(a + 1, n):
                row = [0] * 15
                for c in range(n):
                    for d in range(n):
                        if c == d: continue
                        if M[c][a] == 1 and M[d][b] == 1:
                            pair = (min(c, d), max(c, d))
                            row[idx[pair]] ^= 1
                row[idx[(a, b)]] ^= 1
                equations.append(row)
    equations = np.array(equations, dtype=int)
    m, ncols = equations.shape
    mat = equations.copy()
    pivot_cols, row_idx = [], 0
    for col in range(ncols):
        found = -1
        for r in range(row_idx, m):
            if mat[r][col] == 1: found = r; break
        if found == -1: continue
        mat[[row_idx, found]] = mat[[found, row_idx]]
        for r in range(m):
            if r != row_idx and mat[r][col] == 1:
                mat[r] = (mat[r] + mat[row_idx]) % 2
        pivot_cols.append(col); row_idx += 1
    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    null_vectors = []
    for fc in free_cols:
        v = [0] * ncols; v[fc] = 1
        for i, pc in enumerate(pivot_cols):
            for r in range(len(pivot_cols)):
                if mat[r][pc] == 1: v[pc] = mat[r][fc]; break
        null_vectors.append(v)
    for nv in null_vectors:
        Omega = np.zeros((n, n), dtype=int)
        for k, (i, j) in enumerate(unknowns):
            Omega[i][j] = nv[k]; Omega[j][i] = nv[k]
        det = int(round(np.linalg.det(Omega.astype(float)))) % 2
        if det == 1: return Omega
    return None


def symplectic_form_omega(Omega, u, v):
    return int(np.dot(u, Omega @ np.array(v))) % 2

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
    n = len(basis)
    for mask in range(1, 1 << n):
        v = [0] * len(basis[0])
        for i in range(n):
            if mask & (1 << i):
                v = [(a + b) % 2 for a, b in zip(v, basis[i])]
        pts.add(tuple(v))
    return frozenset(pts)

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
V_SET = set(p for p in ALL_POINTS if p[3] == 0 and p[4] == 0 and p[5] == 0)

# Fano point labels (x-part only)
FANO_LABEL = {}
for p in V_SET:
    FANO_LABEL[(p[0], p[1], p[2])] = p[0]*4 + p[1]*2 + p[2]


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
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}

def vec_to_pauli(v):
    chars = []
    for q in range(3):
        x, z = v[q], v[q + 3]
        if x == 0 and z == 0: chars.append('I')
        elif x == 1 and z == 0: chars.append('X')
        elif x == 1 and z == 1: chars.append('Y')
        else: chars.append('Z')
    return ''.join(chars)

def context_product_sign(context_points):
    mat = np.eye(8, dtype=complex)
    for v in context_points:
        s = vec_to_pauli(v)
        op_mat = PAULI[s[0]]
        for ch in s[1:]: op_mat = np.kron(op_mat, PAULI[ch])
        mat = mat @ op_mat
    return int(round(mat[0, 0].real))


def find_change_of_basis(Omega):
    n = 6
    J = np.zeros((n, n), dtype=int)
    for i in range(3): J[i][i + 3] = 1; J[i + 3][i] = 1
    basis = []
    for step in range(3):
        found = False
        for e in ALL_POINTS:
            if any(symplectic_form_omega(Omega, e, b) != 0 for b in basis): continue
            if basis and gf2_rank(basis + [e]) <= len(basis): continue
            for f in ALL_POINTS:
                if f == e: continue
                if symplectic_form_omega(Omega, e, f) != 1: continue
                if any(symplectic_form_omega(Omega, f, b) != 0 for b in basis): continue
                if gf2_rank(basis + [e, f]) != len(basis) + 2: continue
                basis.extend([e, f]); found = True; break
            if found: break
        if not found: return None
    reordered = [basis[0], basis[2], basis[4], basis[1], basis[3], basis[5]]
    P = np.zeros((6, 6), dtype=int)
    for j in range(6):
        for i in range(6): P[i][j] = reordered[j][i]
    test = (P.T @ Omega @ P) % 2
    if np.array_equal(test, J): return P
    return None


def mat_vec_mod2(A, v):
    return tuple((A @ np.array(v)) % 2)


def classify_lagrangian_type(lag):
    """Classify Lagrangian by V-intersection: k=7, k=3, k=1, k=0."""
    inter = lag & V_SET
    return len(inter)


def enumerate_pentagrams_with_types(lagrangians):
    """Enumerate pentagrams and classify by Lagrangian V-intersection profile."""
    # Precompute Lagrangian types
    lag_types = [classify_lagrangian_type(lag) for lag in lagrangians]

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
    print(f"  {n_ctx} proper contexts found")

    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            shared = all_contexts[i] & all_contexts[j]
            if len(shared) == 1:
                adj[i].append(j); adj[j].append(i)

    print(f"  Searching for K₅ cliques...")
    pentagrams = []
    pent_types = []

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
                        if parity % 2 == 1:
                            pent = tuple(sorted(clique))
                            if pent not in pentagrams:
                                # Classify using Lagrangian V-intersection profile
                                fano_labels = []
                                for ci in clique:
                                    li = context_lag_idx[ci]
                                    k_type = lag_types[li]
                                    if k_type == 1:
                                        v = next(iter(lagrangians[li] & V_SET))
                                        fano_labels.append(FANO_LABEL[(v[0], v[1], v[2])])
                                    elif k_type == 0:
                                        fano_labels.append(0)
                                    else:
                                        fano_labels.append(-1)

                                nonzero = [x for x in fano_labels if x > 0]
                                distinct = len(set(nonzero))
                                transverse = fano_labels.count(0)

                                if transverse == 0 and distinct == 5:
                                    type_name = 'A'
                                elif transverse == 0 and distinct == 4:
                                    type_name = 'B'
                                elif transverse == 0 and distinct == 3:
                                    type_name = 'C'
                                elif transverse == 0 and distinct == 2:
                                    type_name = 'D'
                                elif transverse == 0 and distinct == 1:
                                    type_name = 'E'
                                elif transverse > 0:
                                    type_name = f'F{transverse}'
                                else:
                                    type_name = 'X'

                                pentagrams.append(pent)
                                pent_types.append((type_name, transverse, distinct, tuple(sorted(fano_labels, reverse=True))))

    return pentagrams, pent_types, all_contexts, context_signs, context_lag_idx


def main():
    t0 = time.time()
    print("=" * 70)
    print("Orbit-Type Analysis (Lagrangian V-intersection profile)")
    print("=" * 70)

    print("\n[1/5] Setting up G₂(2) in standard basis...")
    Omega = find_symplectic_form([G2_GEN1_ATLAS, G2_GEN2_ATLAS])
    P = find_change_of_basis(Omega)
    P_inv = np.array(np.round(np.linalg.inv(P.astype(float)))).astype(int) % 2
    g2_gens_std = [(P_inv @ g @ P) % 2 for g in [G2_GEN1_ATLAS, G2_GEN2_ATLAS]]

    print("\n[2/5] Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    # Lagrangian type distribution
    lag_type_counts = defaultdict(int)
    for lag in lagrangians:
        k = len(lag & V_SET)
        lag_type_counts[k] += 1
    print(f"  Lagrangian V-intersection types: {dict(sorted(lag_type_counts.items()))}")

    print("\n[3/5] Enumerating pentagrams with Lagrangian-type classification...")
    pentagrams, pent_types, all_contexts, context_signs, context_lag_idx = \
        enumerate_pentagrams_with_types(lagrangians)
    print(f"  {len(pentagrams)} Mermin pentagrams")

    # Global type distribution
    type_counts = defaultdict(int)
    for t in pent_types:
        type_counts[t[0]] += 1
    print(f"\n  Global type distribution:")
    for tn in sorted(type_counts.keys()):
        print(f"    {tn}: {type_counts[tn]} ({type_counts[tn]/len(pentagrams)*100:.1f}%)")

    # Detailed signatures
    sig_counts = defaultdict(int)
    for t in pent_types:
        sig_counts[(t[0], t[3])] += 1
    print(f"\n  Detailed signatures (type, labels):")
    for (tn, sig), cnt in sorted(sig_counts.items()):
        print(f"    {tn} {sig}: {cnt}")

    print("\n[4/5] Computing G₂(2) orbits...")
    ctx_to_idx = {ctx: i for i, ctx in enumerate(all_contexts)}
    gen_inv_mats = []
    for g in g2_gens_std:
        inv = np.eye(6, dtype=int); m = g.copy(); order = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g) % 2; order += 1
        for _ in range(order - 1): inv = (inv @ g) % 2
        gen_inv_mats.append(inv)
    all_gens = g2_gens_std + gen_inv_mats

    ctx_action = []
    for g_mat in all_gens:
        action = {}
        for i, ctx in enumerate(all_contexts):
            new_pts = frozenset(mat_vec_mod2(g_mat, v) for v in ctx)
            if new_pts in ctx_to_idx: action[i] = ctx_to_idx[new_pts]
        ctx_action.append(action)

    pent_to_idx = {p: i for i, p in enumerate(pentagrams)}
    visited = [False] * len(pentagrams)
    orbits = []
    for start_idx in range(len(pentagrams)):
        if visited[start_idx]: continue
        orbit = []; queue = deque([start_idx]); visited[start_idx] = True
        while queue:
            pidx = queue.popleft(); orbit.append(pidx)
            pent = pentagrams[pidx]
            for ga in ctx_action:
                new_ctx = []; valid = True
                for ci in pent:
                    if ci not in ga: valid = False; break
                    new_ctx.append(ga[ci])
                if not valid: continue
                new_pent = tuple(sorted(new_ctx))
                if new_pent in pent_to_idx:
                    ni = pent_to_idx[new_pent]
                    if not visited[ni]: visited[ni] = True; queue.append(ni)
        orbits.append(orbit)

    print(f"  {len(orbits)} orbits")

    print(f"\n{'=' * 70}")
    print("RESULTS")
    print(f"{'=' * 70}")

    all_type_names = sorted(type_counts.keys())
    for oi, orbit in enumerate(sorted(orbits, key=len, reverse=True)):
        orbit_type_counts = defaultdict(int)
        for pidx in orbit:
            orbit_type_counts[pent_types[pidx][0]] += 1
        stab = 12096 // len(orbit)
        print(f"\nOrbit {oi+1}: {len(orbit)} pentagrams (|Stab| = {stab})")
        for tn in all_type_names:
            cnt = orbit_type_counts.get(tn, 0)
            if cnt > 0:
                print(f"    {tn}: {cnt} ({cnt/len(orbit)*100:.1f}%)")
        if len(orbit_type_counts) == 1:
            print(f"  ★ PURE {list(orbit_type_counts.keys())[0]} orbit!")

    # Summary table
    print(f"\n{'=' * 70}")
    print("SUMMARY TABLE")
    print(f"{'=' * 70}")
    header = f"{'Orbit':<8} {'Size':<8} {'|Stab|':<8}" + "".join(f" {tn:<8}" for tn in all_type_names)
    print(header)
    print("-" * len(header))
    for oi, orbit in enumerate(sorted(orbits, key=len, reverse=True)):
        orbit_type_counts = defaultdict(int)
        for pidx in orbit:
            orbit_type_counts[pent_types[pidx][0]] += 1
        stab = 12096 // len(orbit)
        row = f"  {oi+1:<6} {len(orbit):<8} {stab:<8}"
        for tn in all_type_names:
            row += f" {orbit_type_counts.get(tn, 0):<8}"
        print(row)

    # 3-fold symmetry check
    small_orbits = [o for o in orbits if len(o) == 2016]
    if len(small_orbits) == 3:
        profiles = []
        for orbit in small_orbits:
            profile = defaultdict(int)
            for pidx in orbit:
                profile[pent_types[pidx][0]] += 1
            profiles.append(dict(profile))
        if profiles[0] == profiles[1] == profiles[2]:
            print(f"\n★ 3-fold symmetry: All three 2016-orbits have IDENTICAL type profiles")
            print(f"    Profile: {profiles[0]}")
        else:
            print(f"\n★ 3-fold BROKEN: Three 2016-orbits have DIFFERENT type profiles")
            for i, p in enumerate(profiles):
                print(f"    Orbit {i+1}: {p}")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
