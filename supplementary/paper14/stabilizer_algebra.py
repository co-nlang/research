#!/usr/bin/env python3
"""
Stabilizer algebra computation — v4, generator-only BFS.

Key optimization: BFS uses only 2 generators (4 with inverses),
not all 12,096 group elements. This reduces orbit BFS from
O(|orbit| × |G|) to O(|orbit| × 4).

Stabilizer check: apply each group element to 5 contexts only.
"""

import itertools
import numpy as np
from collections import defaultdict, Counter, deque

# ============================================================
# G₂(2) generators (ATLAS basis)
# ============================================================

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
                            row[idx[(min(c,d), max(c,d))]] ^= 1
                row[idx[(a, b)]] ^= 1
                equations.append(row)
    equations = np.array(equations, dtype=int)
    m, ncols = equations.shape
    mat = equations.copy(); pivot_cols = []; row_idx = 0
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
        if int(round(np.linalg.det(Omega.astype(float)))) % 2 == 1: return Omega
    for combo in range(1, 2 ** len(null_vectors)):
        nv = [0] * ncols
        for bit in range(len(null_vectors)):
            if combo & (1 << bit):
                nv = [(a + b) % 2 for a, b in zip(nv, null_vectors[bit])]
        Omega = np.zeros((n, n), dtype=int)
        for k, (i, j) in enumerate(unknowns):
            Omega[i][j] = nv[k]; Omega[j][i] = nv[k]
        if int(round(np.linalg.det(Omega.astype(float)))) % 2 == 1: return Omega
    return None


def find_change_of_basis(Omega):
    n = 6
    ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
    def symplectic_omega(u, v):
        return int(np.dot(u, Omega @ np.array(v))) % 2
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
    basis = []
    for step in range(3):
        found = False
        for e in ALL_POINTS:
            if any(symplectic_omega(e, b) != 0 for b in basis): continue
            if basis and gf2_rank(basis + [e]) <= len(basis): continue
            for f in ALL_POINTS:
                if f == e: continue
                if symplectic_omega(e, f) != 1: continue
                if any(symplectic_omega(f, b) != 0 for b in basis): continue
                if gf2_rank(basis + [e, f]) != len(basis) + 2: continue
                basis.extend([e, f]); found = True; break
            if found: break
    reordered = [basis[0], basis[2], basis[4], basis[1], basis[3], basis[5]]
    P = np.zeros((6, 6), dtype=int)
    for j in range(6):
        for i in range(6): P[i][j] = reordered[j][i]
    return P


# ============================================================
# Symplectic geometry
# ============================================================

def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

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
# G₂(2) group generation
# ============================================================

def generate_g2_elements(generators):
    identity = tuple(tuple(int(x) for x in row) for row in np.eye(6, dtype=int))
    gens = [tuple(tuple(int(x) for x in row) for row in g) for g in generators]
    gen_inverses = []
    for g in generators:
        m = g.copy(); order = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g) % 2; order += 1
        inv = np.eye(6, dtype=int)
        for _ in range(order - 1): inv = (inv @ g) % 2
        gen_inverses.append(tuple(tuple(int(x) for x in row) for row in inv))
    all_elements = {identity}; queue = deque([identity])
    all_gens = gens + gen_inverses
    while queue:
        elem = queue.popleft()
        for g in all_gens:
            prod = tuple(tuple(int(x) for x in row)
                        for row in (np.array(elem) @ np.array(g)) % 2)
            if prod not in all_elements:
                all_elements.add(prod); queue.append(prod)
    return all_elements


def apply_matrix_to_context(g_mat, ctx):
    """Apply matrix to context (frozenset of vectors)."""
    return frozenset(tuple((g_mat @ np.array(v)) % 2) for v in ctx)


def find_orbit_reps_gen_bfs(pentagrams, all_contexts, ctx_to_idx, gen_mats, n_expected=4):
    """BFS using only generator matrices (not all group elements)."""
    pent_to_idx = {p: i for i, p in enumerate(pentagrams)}
    visited = [False] * len(pentagrams)
    reps = []; orbit_sizes = []

    for start_idx in range(len(pentagrams)):
        if visited[start_idx]: continue
        reps.append(start_idx)
        queue = deque([start_idx])
        visited[start_idx] = True
        orbit_size = 0
        while queue:
            pidx = queue.popleft()
            orbit_size += 1
            pent = pentagrams[pidx]
            # Apply each generator
            for g_mat in gen_mats:
                new_ctx = []
                valid = True
                for ci in pent:
                    new_pts = apply_matrix_to_context(g_mat, all_contexts[ci])
                    if new_pts not in ctx_to_idx:
                        valid = False; break
                    new_ctx.append(ctx_to_idx[new_pts])
                if not valid: continue
                new_pent = tuple(sorted(new_ctx))
                if new_pent in pent_to_idx:
                    ni = pent_to_idx[new_pent]
                    if not visited[ni]:
                        visited[ni] = True; queue.append(ni)
        orbit_sizes.append(orbit_size)
        if len(reps) >= n_expected: break

    return reps, orbit_sizes


def compute_stabilizer(rep_idx, pentagrams, all_contexts, ctx_to_idx, g2_elements):
    """Check each group element against the representative's 5 contexts."""
    pent = pentagrams[rep_idx]
    stabilizer = []
    for g_tuple in g2_elements:
        g_mat = np.array(g_tuple)
        new_ctx = []
        valid = True
        for ci in pent:
            new_pts = apply_matrix_to_context(g_mat, all_contexts[ci])
            if new_pts not in ctx_to_idx:
                valid = False; break
            new_ctx.append(ctx_to_idx[new_pts])
        if not valid: continue
        if tuple(sorted(new_ctx)) == pent:
            stabilizer.append(g_tuple)
    return stabilizer


def analyze_group(stabilizer):
    order = len(stabilizer)
    orders = []
    for g in stabilizer:
        g_mat = np.array(g); m = g_mat.copy(); o = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g_mat) % 2; o += 1
        orders.append(o)
    order_counts = Counter(orders)

    is_abelian = True
    for i in range(len(stabilizer)):
        for j in range(i+1, len(stabilizer)):
            a = np.array(stabilizer[i]); b = np.array(stabilizer[j])
            if not np.array_equal((a @ b) % 2, (b @ a) % 2):
                is_abelian = False; break
        if not is_abelian: break

    return {
        'order': order, 'element_orders': dict(order_counts),
        'is_abelian': is_abelian,
        'n_order2': order_counts.get(2, 0),
        'n_order3': order_counts.get(3, 0),
        'n_order6': order_counts.get(6, 0),
    }


# ============================================================
# k-profile
# ============================================================

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
    print("Paper XIV: Stabilizer Algebra (v4, generator-only BFS)")
    print("=" * 70)

    # Setup
    print("\n[1/6] Change of basis...")
    Omega = find_symplectic_form([G2_GEN1_ATLAS, G2_GEN2_ATLAS])
    P = find_change_of_basis(Omega)
    P_inv = np.array(np.round(np.linalg.inv(P.astype(float)))).astype(int) % 2

    g2_gens_std = []
    for g in [G2_GEN1_ATLAS, G2_GEN2_ATLAS]:
        g_std = (P_inv @ g @ P) % 2
        g2_gens_std.append(g_std)

    # Compute generator inverses for BFS
    gen_mats_with_inv = list(g2_gens_std)
    for g in g2_gens_std:
        m = g.copy(); order = 1
        while not np.array_equal(m, np.eye(6, dtype=int)):
            m = (m @ g) % 2; order += 1
        inv = np.eye(6, dtype=int)
        for _ in range(order - 1): inv = (inv @ g) % 2
        gen_mats_with_inv.append(inv)

    # Enumerate
    print("\n[2/6] Enumerating Lagrangians and pentagrams...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(lagrangians)
    print(f"  {len(pentagrams)} pentagrams")
    ctx_to_idx = {ctx: i for i, ctx in enumerate(all_contexts)}

    # Generate group
    print("\n[3/6] Generating G₂(2)...")
    # Convert generators to tuple form for group generation
    gen_tuples = [tuple(tuple(int(x) for x in row) for row in g) for g in g2_gens_std[:2]]
    g2_elements = generate_g2_elements([np.array(g) for g in gen_tuples])
    print(f"  |G₂(2)| = {len(g2_elements)}")

    # Find orbit representatives (generator-only BFS)
    print("\n[4/6] Finding orbit representatives (generator BFS)...")
    rep_indices, orbit_sizes = find_orbit_reps_gen_bfs(
        pentagrams, all_contexts, ctx_to_idx, gen_mats_with_inv)

    print(f"  Found {len(rep_indices)} orbits:")
    for i, (ri, sz) in enumerate(zip(rep_indices, orbit_sizes)):
        stab_size = len(g2_elements) // sz
        print(f"    Orbit {i+1}: size={sz}, |Stab|={stab_size}")

    # Compute stabilizers
    print("\n[5/6] Computing stabilizer algebras...")
    for i, ri in enumerate(rep_indices):
        stab = compute_stabilizer(ri, pentagrams, all_contexts, ctx_to_idx, g2_elements)
        info = analyze_group(stab)
        if info['order'] == 2:
            group_type = "Z₂"
        elif info['order'] == 6:
            group_type = "Z₆" if info['is_abelian'] else "S₃"
        else:
            group_type = f"Unknown(order={info['order']})"

        print(f"\n  Orbit {i+1} stabilizer:")
        print(f"    Group: {group_type}")
        print(f"    Abelian: {info['is_abelian']}")
        print(f"    Element orders: {info['element_orders']}")
        print(f"    Order-2 elements: {info['n_order2']}")
        print(f"    Order-3 elements: {info['n_order3']}")

    # Label all pentagrams by orbit (BFS from each rep)
    print("\n[5b/6] Labeling all pentagrams by orbit...")
    pent_to_idx = {p: i for i, p in enumerate(pentagrams)}
    orbit_labels = [-1] * len(pentagrams)
    for orbit_num, rep_idx in enumerate(rep_indices):
        orbit_labels[rep_idx] = orbit_num
        queue = deque([rep_idx])
        while queue:
            pidx = queue.popleft()
            pent = pentagrams[pidx]
            for g_mat in gen_mats_with_inv:
                new_ctx = []
                valid = True
                for ci in pent:
                    new_pts = apply_matrix_to_context(g_mat, all_contexts[ci])
                    if new_pts not in ctx_to_idx:
                        valid = False; break
                    new_ctx.append(ctx_to_idx[new_pts])
                if not valid: continue
                new_pent = tuple(sorted(new_ctx))
                if new_pent in pent_to_idx:
                    ni = pent_to_idx[new_pent]
                    if orbit_labels[ni] == -1:
                        orbit_labels[ni] = orbit_num
                        queue.append(ni)
    unlabeled = sum(1 for x in orbit_labels if x == -1)
    print(f"  Unlabeled: {unlabeled} (should be 0)")

    # k-Profile
    print("\n[6/6] k-Profile exhaustiveness + orbit cross-table...")
    k_profile_counts = Counter()
    k_profile_parity = defaultdict(lambda: Counter())
    cross_table = defaultdict(lambda: defaultdict(int))

    for pi, pent in enumerate(pentagrams):
        kp = compute_k_profile(pent, context_lag_idx, lagrangians)
        k_profile_counts[kp] += 1
        parity = sum(1 for ci in pent if context_signs[ci] == -1)
        k_profile_parity[kp][parity] += 1
        cross_table[orbit_labels[pi]][kp] += 1
        if (pi + 1) % 2000 == 0:
            print(f"  {pi+1}/{len(pentagrams)}...")

    print(f"\n  k-Profile distribution:")
    total = sum(k_profile_counts.values())
    for kp, count in sorted(k_profile_counts.items(), key=lambda x: -x[1]):
        parity_info = dict(k_profile_parity[kp])
        odd = sum(v for k, v in parity_info.items() if k % 2 == 1)
        even = sum(v for k, v in parity_info.items() if k % 2 == 0)
        print(f"    {kp}: {count} ({100*count/total:.1f}%) (odd={odd}, even={even})")

    print(f"\n  Orbit × k-profile cross-table (counts):")
    all_kps = sorted(k_profile_counts.keys(), key=lambda x: -k_profile_counts[x])
    header = f"  {'':>10}" + "".join(f"  {str(kp):>16}" for kp in all_kps)
    print(header)
    for orb in range(len(rep_indices)):
        row = f"  O{orb+1}({orbit_sizes[orb]:>5})" + "".join(
            f"  {cross_table[orb].get(kp, 0):>16}" for kp in all_kps)
        print(row)
    print(f"  {'Total':>10}" + "".join(
        f"  {k_profile_counts[kp]:>16}" for kp in all_kps))

    print(f"\n  Orbit × k-profile cross-table (%):")
    for orb in range(len(rep_indices)):
        sz = orbit_sizes[orb]
        row = f"  O{orb+1}({sz:>5})" + "".join(
            f"  {100*cross_table[orb].get(kp,0)/sz:>15.1f}%" for kp in all_kps)
        print(row)

    print(f"\n{'=' * 70}")
    print(f"Total time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
