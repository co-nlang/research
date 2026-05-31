#!/usr/bin/env python3
"""
G₂(2) orbit decomposition of 12,096 Mermin pentagrams.

Uses G₂(2) generators from GAP AtlasRep (6×6 matrices over GF(2)).
"""

import itertools
import numpy as np
from collections import defaultdict, deque

# G₂(2) generators from GAP AtlasGroup("G2(2)", Characteristic, 2)
G2_GEN1 = np.array([
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0, 1],
], dtype=int)

G2_GEN2 = np.array([
    [0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 0, 1],
], dtype=int)


def mat_mul_mod2(A, B):
    return (A @ B) % 2


def mat_vec_mod2(A, v):
    return tuple((A @ np.array(v)) % 2)


def find_symplectic_form(generators):
    """Find the symplectic form Ω preserved by the generators: M^T Ω M = Ω."""
    n = 6
    # Ω is antisymmetric: Ω[i][j] = Ω[j][i] for i<j (over GF(2), antisymmetric = symmetric)
    # 15 unknowns: Ω[i][j] for 0 <= i < j <= 5
    unknowns = [(i, j) for i in range(n) for j in range(i + 1, n)]
    idx = {pair: k for k, pair in enumerate(unknowns)}

    equations = []
    for M in generators:
        MT = M.T % 2
        # (M^T Ω M)[a][b] = Ω[a][b] for all a < b
        for a in range(n):
            for b in range(a + 1, n):
                row = [0] * 15
                # (M^T Ω M)[a][b] = sum_{c,d} M[c][a] * Ω[c][d] * M[d][b]
                for c in range(n):
                    for d in range(n):
                        if c == d:
                            continue
                        if M[c][a] == 1 and M[d][b] == 1:
                            pair = (min(c, d), max(c, d))
                            row[idx[pair]] ^= 1
                # Subtract Ω[a][b]
                row[idx[(a, b)]] ^= 1
                equations.append(row)

    equations = np.array(equations, dtype=int)
    # Find null space over GF(2)
    # Use Gaussian elimination
    m, ncols = equations.shape
    mat = equations.copy()
    pivot_cols = []
    row_idx = 0
    for col in range(ncols):
        found = -1
        for r in range(row_idx, m):
            if mat[r][col] == 1:
                found = r
                break
        if found == -1:
            continue
        mat[[row_idx, found]] = mat[[found, row_idx]]
        for r in range(m):
            if r != row_idx and mat[r][col] == 1:
                mat[r] = (mat[r] + mat[row_idx]) % 2
        pivot_cols.append(col)
        row_idx += 1

    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    print(f"  Rank: {len(pivot_cols)}, Free variables: {len(free_cols)}")

    # Find null space vectors
    null_vectors = []
    for fc in free_cols:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(pivot_cols):
            # Find which row has this pivot
            for r in range(len(pivot_cols)):
                if mat[r][pc] == 1:
                    v[pc] = mat[r][fc]
                    break
        null_vectors.append(v)

    # Build Ω matrices from null space vectors and find non-degenerate one
    for nv in null_vectors:
        Omega = np.zeros((n, n), dtype=int)
        for k, (i, j) in enumerate(unknowns):
            Omega[i][j] = nv[k]
            Omega[j][i] = nv[k]
        det = int(round(np.linalg.det(Omega.astype(float)))) % 2
        if det == 1:
            return Omega

    # If no single vector works, try linear combinations
    print("  Trying linear combinations of null space vectors...")
    for combo in range(1, 2 ** len(null_vectors)):
        nv = [0] * ncols
        for bit in range(len(null_vectors)):
            if combo & (1 << bit):
                nv = [(a + b) % 2 for a, b in zip(nv, null_vectors[bit])]
        Omega = np.zeros((n, n), dtype=int)
        for k, (i, j) in enumerate(unknowns):
            Omega[i][j] = nv[k]
            Omega[j][i] = nv[k]
        det = int(round(np.linalg.det(Omega.astype(float)))) % 2
        if det == 1:
            return Omega

    return None


def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2


def symplectic_form_omega(Omega, u, v):
    return int(np.dot(u, Omega @ np.array(v))) % 2


def add(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))


def gf2_rank(vectors):
    if not vectors:
        return 0
    rows = [list(v) for v in vectors]
    ncols = len(rows[0])
    rank = 0
    for col in range(ncols):
        pivot = None
        for r in range(rank, len(rows)):
            if rows[r][col] == 1:
                pivot = r
                break
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


def find_lagrangians():
    lagrangians, seen = [], set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3:
            continue
        if not all(symplectic_form(u, v) == 0
                   for u, v in itertools.combinations(basis, 2)):
            continue
        subspace = span_subspace(basis)
        if subspace not in seen:
            seen.add(subspace)
            lagrangians.append(subspace)
    return lagrangians


def get_fano_lines(lag_points):
    pts = list(lag_points)
    lines = set()
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
        if x == 0 and z == 0:
            chars.append('I')
        elif x == 1 and z == 0:
            chars.append('X')
        elif x == 1 and z == 1:
            chars.append('Y')
        else:
            chars.append('Z')
    return ''.join(chars)


def pauli_product_sign(operators):
    mat = np.eye(8, dtype=complex)
    for v in operators:
        s = vec_to_pauli(v)
        op_mat = PAULI[s[0]]
        for ch in s[1:]:
            op_mat = np.kron(op_mat, PAULI[ch])
        mat = mat @ op_mat
    return int(round(mat[0, 0].real))


def compute_context_sign(context_points):
    return pauli_product_sign(context_points)


def enumerate_pentagrams(lagrangians):
    print(f"  Finding contexts for {len(lagrangians)} Lagrangians...")
    all_contexts = []
    context_signs = []
    context_lag_idx = []

    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4:
                continue
            sign = compute_context_sign(ctx_pts)
            if sign == 0:
                continue
            all_contexts.append(frozenset(ctx_pts))
            context_signs.append(sign)
            context_lag_idx.append(li)

    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts found")

    # Build adjacency: contexts sharing exactly 1 operator (pentagram vertex)
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            shared = all_contexts[i] & all_contexts[j]
            if len(shared) == 1:
                adj[i].append(j)
                adj[j].append(i)

    print(f"  Searching for K₅ cliques...")
    pentagrams = []
    for i in range(n_ctx):
        for j in adj[i]:
            if j <= i:
                continue
            for k in adj[j]:
                if k <= j or k not in adj[i]:
                    continue
                for m in adj[k]:
                    if m <= k or m not in adj[i] or m not in adj[j]:
                        continue
                    for p in adj[m]:
                        if p <= m or p not in adj[i] or p not in adj[j] or p not in adj[k]:
                            continue
                        clique = [i, j, k, m, p]
                        all_ops = set()
                        for ci in clique:
                            all_ops |= all_contexts[ci]
                        if len(all_ops) != 10:
                            continue
                        parity = sum(1 for ci in clique if context_signs[ci] == -1)
                        if parity % 2 == 1:
                            pentagrams.append(tuple(sorted(clique)))

    return list(set(pentagrams)), all_contexts, context_signs, context_lag_idx


def generate_g2_elements(generators):
    """Generate all G₂(2) elements using BFS."""
    identity = tuple(tuple(row) for row in np.eye(6, dtype=int))
    gens = [tuple(tuple(row) for row in g) for g in generators]
    gen_inverses = []
    for g in generators:
        # Over GF(2), inverse can be found by enumeration
        # But for generators, g^{-1} = g^{ord(g)-1}
        # Compute order
        m = g.copy()
        order = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g) % 2
            order += 1
        # g^{-1} = g^{order-1}
        inv = np.eye(6, dtype=int)
        for _ in range(order - 1):
            inv = (inv @ g) % 2
        gen_inverses.append(tuple(tuple(row) for row in inv))

    all_elements = set()
    all_elements.add(identity)
    queue = deque([identity])
    all_gens = gens + gen_inverses

    while queue:
        elem = queue.popleft()
        for g in all_gens:
            product = tuple(tuple((np.array(elem) @ np.array(g)) % 2) for _ in [0])
            # Fix: proper matrix multiply
            e_mat = np.array(elem)
            g_mat = np.array(g)
            prod = tuple(tuple(int(x) for x in row) for row in (e_mat @ g_mat) % 2)
            if prod not in all_elements:
                all_elements.add(prod)
                queue.append(prod)

    return all_elements


def act_on_pentagram(g, pentagram, all_contexts):
    """Apply group element g to a pentagram."""
    g_mat = np.array(g)
    new_ctx_indices = []
    for ci in pentagram:
        ctx = all_contexts[ci]
        new_pts = frozenset(mat_vec_mod2(g_mat, v) for v in ctx)
        # Find this context in all_contexts
        found = -1
        for j, other_ctx in enumerate(all_contexts):
            if other_ctx == new_pts:
                found = j
                break
        if found == -1:
            return None
        new_ctx_indices.append(found)
    return tuple(sorted(new_ctx_indices))


def find_change_of_basis(Omega):
    """Find P such that P^T Omega P = J (standard symplectic form)."""
    n = 6
    J = np.zeros((n, n), dtype=int)
    for i in range(3):
        J[i][i + 3] = 1
        J[i + 3][i] = 1

    basis = []

    for step in range(3):
        found = False
        for e in ALL_POINTS:
            if any(symplectic_form_omega(Omega, e, b) != 0 for b in basis):
                continue
            if basis and gf2_rank(basis + [e]) <= len(basis):
                continue
            for f in ALL_POINTS:
                if f == e:
                    continue
                if symplectic_form_omega(Omega, e, f) != 1:
                    continue
                if any(symplectic_form_omega(Omega, f, b) != 0 for b in basis):
                    continue
                if gf2_rank(basis + [e, f]) != len(basis) + 2:
                    continue
                basis.extend([e, f])
                found = True
                break
            if found:
                break
        if not found:
            print(f"  ERROR: Could not find symplectic pair {step+1}")
            return None

    # basis = [e1, e2, e3, f1, f2, f3]
    # P has these as columns
    P = np.zeros((6, 6), dtype=int)
    for j in range(6):
        for i in range(6):
            P[i][j] = basis[j][i]

    test = (P.T @ Omega @ P) % 2
    if np.array_equal(test, J):
        return P

    print(f"  P^T Omega P =")
    for row in test:
        print(f"    {list(row)}")
    print(f"  Expected J =")
    for row in J:
        print(f"    {list(row)}")

    # Try different ordering: [e1, f1, e2, f2, e3, f3] -> rearrange to [e1,e2,e3,f1,f2,f3]
    # basis is currently [e1, f1, e2, f2, e3, f3]
    # Rearrange to [e1, e2, e3, f1, f2, f3]
    reordered = [basis[0], basis[2], basis[4], basis[1], basis[3], basis[5]]
    P2 = np.zeros((6, 6), dtype=int)
    for j in range(6):
        for i in range(6):
            P2[i][j] = reordered[j][i]
    test2 = (P2.T @ Omega @ P2) % 2
    if np.array_equal(test2, J):
        print("  Fixed by reordering to [e1,e2,e3,f1,f2,f3]")
        return P2

    print(f"  Reordered P^T Omega P =")
    for row in test2:
        print(f"    {list(row)}")
    return None


def main():
    print("=" * 70)
    print("G₂(2) Orbit Decomposition of 12,096 Mermin Pentagrams")
    print("=" * 70)

    print("\n[1/6] Finding symplectic form preserved by G₂(2)...")
    Omega = find_symplectic_form([G2_GEN1, G2_GEN2])
    if Omega is None:
        print("ERROR: Could not find non-degenerate symplectic form!")
        return
    print(f"  Found symplectic form Ω (ATLAS basis)")

    # Verify generators preserve Ω
    for i, g in enumerate([G2_GEN1, G2_GEN2]):
        test = (g.T @ Omega @ g) % 2
        assert np.array_equal(test, Omega), f"Generator {i+1} does not preserve Ω!"
    print("  Both generators preserve Ω ✓")

    print("\n[1b/6] Change of basis to standard symplectic form...")
    P = find_change_of_basis(Omega)
    if P is None:
        print("ERROR: Could not find change of basis!")
        return
    # P^{-1} over GF(2)
    P_inv = np.array(np.round(np.linalg.inv(P.astype(float)))).astype(int) % 2
    # Verify
    assert np.array_equal((P @ P_inv) % 2, np.eye(6, dtype=int)), "P_inv incorrect"

    # Transform G2 generators to standard basis: g_std = P^{-1} g P
    g2_gens_std = []
    for g in [G2_GEN1, G2_GEN2]:
        g_std = (P_inv @ g @ P) % 2
        g2_gens_std.append(g_std)
        # Verify preserves J
        J = np.zeros((6, 6), dtype=int)
        for i in range(3):
            J[i][i + 3] = 1
            J[i + 3][i] = 1
        test = (g_std.T @ J @ g_std) % 2
        assert np.array_equal(test, J), "Transformed generator doesn't preserve J!"
    print("  G₂(2) generators transformed to standard basis ✓")
    print("  Transformed generators preserve standard J ✓")

    print("\n[2/6] Enumerating Lagrangians (standard basis)...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians found")

    print("\n[3/6] Enumerating pentagrams...")
    pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(lagrangians)
    print(f"  {len(pentagrams)} Mermin pentagrams found")

    print("\n[4/6] Generating G₂(2) elements (standard basis)...")
    g2_elements = generate_g2_elements(g2_gens_std)
    print(f"  |G₂(2)| = {len(g2_elements)} (expected 12096)")

    print("\n[5/6] Computing orbits...")
    # Build context lookup: frozenset -> index
    ctx_to_idx = {ctx: i for i, ctx in enumerate(all_contexts)}

    # For efficiency, precompute the action of each generator on all contexts
    gen_inv_mats = []
    for g in g2_gens_std:
        inv = np.eye(6, dtype=int)
        m = g.copy()
        order = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g) % 2
            order += 1
        for _ in range(order - 1):
            inv = (inv @ g) % 2
        gen_inv_mats.append(inv)

    all_gens = g2_gens_std + gen_inv_mats

    # Precompute action of each generator on each context
    print("  Precomputing generator actions on contexts...")
    ctx_action = []
    for g_mat in all_gens:
        action = {}
        for i, ctx in enumerate(all_contexts):
            new_pts = frozenset(mat_vec_mod2(g_mat, v) for v in ctx)
            if new_pts in ctx_to_idx:
                action[i] = ctx_to_idx[new_pts]
        ctx_action.append(action)

    # BFS to find orbits
    pent_set = set(pentagrams)
    pent_to_idx = {p: i for i, p in enumerate(pentagrams)}
    visited = [False] * len(pentagrams)
    orbits = []

    for start_idx in range(len(pentagrams)):
        if visited[start_idx]:
            continue
        orbit = []
        queue = deque([start_idx])
        visited[start_idx] = True
        while queue:
            pidx = queue.popleft()
            orbit.append(pidx)
            pent = pentagrams[pidx]
            for ga in ctx_action:
                new_ctx = []
                valid = True
                for ci in pent:
                    if ci not in ga:
                        valid = False
                        break
                    new_ctx.append(ga[ci])
                if not valid:
                    continue
                new_pent = tuple(sorted(new_ctx))
                if new_pent in pent_to_idx:
                    ni = pent_to_idx[new_pent]
                    if not visited[ni]:
                        visited[ni] = True
                        queue.append(ni)
        orbits.append(orbit)

    print(f"\n{'=' * 70}")
    print(f"RESULTS")
    print(f"{'=' * 70}")
    print(f"Total pentagrams: {len(pentagrams)}")
    print(f"|G₂(2)|: {len(g2_elements)}")
    print(f"Number of orbits: {len(orbits)}")
    print(f"\nOrbit sizes:")
    for i, orbit in enumerate(sorted(orbits, key=len, reverse=True)):
        print(f"  Orbit {i+1}: {len(orbit)} pentagrams")

    # Check orbit structure
    sizes = sorted([len(o) for o in orbits])
    if sizes == [2016, 2016, 2016, 6048]:
        print(f"\n✓ Confirmed: 4 orbits (6048 + 3×2016 = 12,096)")
    else:
        print(f"\n✗ Unexpected orbit sizes: {sizes}")


if __name__ == '__main__':
    import time
    t0 = time.time()
    main()
    print(f"\nTotal time: {time.time()-t0:.1f}s")
