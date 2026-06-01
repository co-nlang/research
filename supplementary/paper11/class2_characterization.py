#!/usr/bin/env python3
"""
Paper XI warmup: Geometric characterization of Class I vs Class II pentagrams.

Computes detailed invariants per pentagram:
1. Lagrangian V-intersection profile (sorted k-values)
2. Ray V-membership (how many of 10 rays lie in V)
3. Parity breakdown (1-minus vs 3-minus vs 5-minus)
4. Quadratic form values on rays
5. Context sign pattern vs Lagrangian geometry
"""

import itertools
import numpy as np
from collections import defaultdict, Counter, deque
import time

G2_GEN1_ATLAS = np.array([
    [1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0], [1, 1, 1, 0, 0, 1],
], dtype=int)
G2_GEN2_ATLAS = np.array([
    [0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1],
], dtype=int)


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


def find_symplectic_form_matrix(generators):
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


def enumerate_pentagrams_full(lagrangians):
    """Enumerate pentagrams with full geometric data."""
    lag_types = [len(lag & V_SET) for lag in lagrangians]

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

    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    print(f"  Searching K₅ cliques...")
    pentagrams = []
    pent_data = []

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
                                # Compute detailed invariants
                                lag_indices = [context_lag_idx[ci] for ci in clique]
                                k_profile = tuple(sorted(lag_types[li] for li in lag_indices))

                                # Rays: shared operators between context pairs
                                rays = {}
                                for a in range(5):
                                    for b in range(a+1, 5):
                                        shared = all_contexts[clique[a]] & all_contexts[clique[b]]
                                        if shared:
                                            rays[(a,b)] = next(iter(shared))

                                rays_in_V = sum(1 for r in rays.values() if r in V_SET)

                                # Quadratic form values on rays
                                # Q(v) = x·z (standard quadratic refinement of ω)
                                ray_Q = {}
                                for key, r in rays.items():
                                    Q_val = (r[0]*r[3] + r[1]*r[4] + r[2]*r[5]) % 2
                                    ray_Q[key] = Q_val
                                Q_sum = sum(ray_Q.values()) % 2

                                pentagrams.append(pent)
                                pent_data.append({
                                    'k_profile': k_profile,
                                    'parity': parity,
                                    'rays_in_V': rays_in_V,
                                    'Q_sum': Q_sum,
                                    'lag_indices': lag_indices,
                                    'rays': rays,
                                    'ray_Q': ray_Q,
                                    'context_signs': tuple(context_signs[ci] for ci in clique),
                                })

    return pentagrams, pent_data, all_contexts, context_signs, context_lag_idx


def compute_orbits(pentagrams, all_contexts, g2_gens_std):
    """Compute G₂(2) orbits."""
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
    return orbits


def main():
    t0 = time.time()
    print("=" * 70)
    print("Paper XI: Class I vs Class II Geometric Characterization")
    print("=" * 70)

    print("\n[1/5] Setting up G₂(2)...")
    Omega = find_symplectic_form_matrix([G2_GEN1_ATLAS, G2_GEN2_ATLAS])
    P = find_change_of_basis(Omega)
    P_inv = np.array(np.round(np.linalg.inv(P.astype(float)))).astype(int) % 2
    g2_gens_std = [(P_inv @ g @ P) % 2 for g in [G2_GEN1_ATLAS, G2_GEN2_ATLAS]]

    print("\n[2/5] Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    print("\n[3/5] Enumerating pentagrams with full invariants...")
    pentagrams, pent_data, all_contexts, context_signs, context_lag_idx = \
        enumerate_pentagrams_full(lagrangians)
    print(f"  {len(pentagrams)} pentagrams")

    print("\n[4/5] Computing orbits...")
    orbits = compute_orbits(pentagrams, all_contexts, g2_gens_std)
    orbits_sorted = sorted(orbits, key=len, reverse=True)
    print(f"  {len(orbits)} orbits: {[len(o) for o in orbits_sorted]}")

    # Assign orbit labels
    orbit_class = {}
    for oi, orbit in enumerate(orbits_sorted):
        for pidx in orbit:
            orbit_class[pidx] = oi

    # Class I = orbits 0,1 (6048 + 2016); Class II = orbits 2,3 (2016 + 2016)
    # But we need to check which orbits form which class
    # From Paper X: Class I = O1∪O2, Class II = O3∪O4
    # O1 has 61.1% F2, O2 also 61.1% F2 → Class I
    # O3, O4 have 55.6% F2 → Class II

    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")

    # --- Invariant 1: k-profile distribution ---
    print("\n--- Invariant 1: Lagrangian V-intersection profile (k-profile) ---")
    for oi, orbit in enumerate(orbits_sorted):
        kprof_counts = Counter()
        for pidx in orbit:
            kprof_counts[pent_data[pidx]['k_profile']] += 1
        print(f"\n  Orbit {oi+1} ({len(orbit)} pentagrams):")
        for kp, cnt in sorted(kprof_counts.items(), key=lambda x: -x[1]):
            print(f"    k={kp}: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Invariant 2: Rays in V ---
    print("\n--- Invariant 2: Number of rays in V ---")
    for oi, orbit in enumerate(orbits_sorted):
        rv_counts = Counter()
        for pidx in orbit:
            rv_counts[pent_data[pidx]['rays_in_V']] += 1
        print(f"\n  Orbit {oi+1}:")
        for rv, cnt in sorted(rv_counts.items()):
            print(f"    {rv} rays in V: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Invariant 3: Parity distribution ---
    print("\n--- Invariant 3: Parity (number of -1 contexts) ---")
    for oi, orbit in enumerate(orbits_sorted):
        par_counts = Counter()
        for pidx in orbit:
            par_counts[pent_data[pidx]['parity']] += 1
        print(f"\n  Orbit {oi+1}:")
        for p, cnt in sorted(par_counts.items()):
            print(f"    {p}-minus: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Invariant 4: Q-sum on rays ---
    print("\n--- Invariant 4: Sum of Q(ray) mod 2 ---")
    for oi, orbit in enumerate(orbits_sorted):
        qs_counts = Counter()
        for pidx in orbit:
            qs_counts[pent_data[pidx]['Q_sum']] += 1
        print(f"\n  Orbit {oi+1}:")
        for qs, cnt in sorted(qs_counts.items()):
            print(f"    Q_sum={qs}: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Invariant 5: Q-ray pattern (detailed) ---
    print("\n--- Invariant 5: Q-ray pattern distribution ---")
    for oi, orbit in enumerate(orbits_sorted):
        qpat_counts = Counter()
        for pidx in orbit:
            rq = pent_data[pidx]['ray_Q']
            pattern = tuple(rq[(a,b)] for a in range(5) for b in range(a+1,5))
            qpat_counts[pattern] += 1
        print(f"\n  Orbit {oi+1}: {len(qpat_counts)} distinct Q-patterns")
        for pat, cnt in sorted(qpat_counts.items(), key=lambda x: -x[1])[:10]:
            print(f"    {pat}: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Invariant 6: Context sign pattern ---
    print("\n--- Invariant 6: Context sign pattern ---")
    for oi, orbit in enumerate(orbits_sorted):
        sp_counts = Counter()
        for pidx in orbit:
            signs = pent_data[pidx]['context_signs']
            n_minus = signs.count(-1)
            sp_counts[n_minus] += 1
        print(f"\n  Orbit {oi+1}:")
        for nm, cnt in sorted(sp_counts.items()):
            print(f"    {nm} minus signs: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Cross-invariant: k-profile × parity ---
    print("\n--- Cross-invariant: k-profile × parity ---")
    for oi, orbit in enumerate(orbits_sorted):
        cross = Counter()
        for pidx in orbit:
            cross[(pent_data[pidx]['k_profile'], pent_data[pidx]['parity'])] += 1
        print(f"\n  Orbit {oi+1}:")
        for (kp, par), cnt in sorted(cross.items(), key=lambda x: -x[1])[:15]:
            print(f"    k={kp}, {par}-minus: {cnt}")

    # --- Class-level summary ---
    print(f"\n{'='*70}")
    print("CLASS-LEVEL SUMMARY")
    print(f"{'='*70}")

    # Determine class membership from type distribution
    # Compute B/F2/F4 per orbit to identify classes
    for oi, orbit in enumerate(orbits_sorted):
        type_counts = Counter()
        for pidx in orbit:
            kp = pent_data[pidx]['k_profile']
            # Count k=0 Lagrangians (transverse) and distinct k=1 Fano points
            k_vals = list(kp)
            n_transverse = k_vals.count(0)
            # For Fano points, need actual V-intersection points
            # Approximate: k=1 Lagrangians contribute Fano points
            n_fano_lags = k_vals.count(1)
            n_special = sum(1 for k in k_vals if k >= 3)

            if n_transverse == 0 and n_fano_lags == 5:
                type_name = 'A_or_B'  # Need more detail
            elif n_transverse == 0:
                type_name = f'F0_special{n_special}'
            else:
                type_name = f'F{n_transverse}'
            type_counts[type_name] += 1
        stab = 12096 // len(orbit)
        print(f"\n  Orbit {oi+1} (size {len(orbit)}, |Stab|={stab}):")
        for tn, cnt in sorted(type_counts.items(), key=lambda x: -x[1]):
            print(f"    {tn}: {cnt} ({cnt/len(orbit)*100:.1f}%)")

    # --- Quadratic refinement deep dive ---
    print(f"\n{'='*70}")
    print("QUADRATIC REFINEMENT ANALYSIS")
    print(f"{'='*70}")

    # For a representative from each orbit, print full details
    for oi, orbit in enumerate(orbits_sorted):
        pidx = orbit[0]
        d = pent_data[pidx]
        print(f"\n  Orbit {oi+1} representative:")
        print(f"    k-profile: {d['k_profile']}")
        print(f"    parity: {d['parity']}-minus")
        print(f"    rays in V: {d['rays_in_V']}")
        print(f"    context signs: {d['context_signs']}")
        print(f"    ray Q-values:")
        for (a,b), q in sorted(d['ray_Q'].items()):
            r = d['rays'][(a,b)]
            in_V = "∈V" if r in V_SET else "∉V"
            print(f"      R_{{{a+1},{b+1}}} = {r}, Q={q} {in_V}")
        print(f"    Q_sum mod 2 = {d['Q_sum']}")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
