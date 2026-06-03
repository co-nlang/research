#!/usr/bin/env python3
"""
Weil cocycle verification: β(C)/2 mod 2 = c(g_C, g_C^{-1}) mod 2.

For each context C ⊂ L (Lagrangian), construct g_C ∈ Sp(6, F₂) with g_C(V) = L,
then verify that the metaplectic cocycle c(g_C, g_C^{-1}) equals (-1)^{β(C)/2}.

This connects the β-formula (Paper XI) to the Weil representation cocycle.
"""

import numpy as np
from collections import defaultdict, deque, Counter
import itertools
import time

# ============================================================
# GF(2) linear algebra
# ============================================================

def gf2_inv(M):
    n = M.shape[0]
    aug = np.hstack([M.copy() % 2, np.eye(n, dtype=int)])
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if aug[r, col] == 1: pivot = r; break
        if pivot is None: return None
        if pivot != col: aug[[col, pivot]] = aug[[pivot, col]]
        for r in range(n):
            if r != col and aug[r, col] == 1:
                aug[r] = (aug[r] + aug[col]) % 2
    return aug[:, n:] % 2


def gf2_rank(M):
    M = M.copy() % 2
    rows, cols = M.shape; rank = 0
    for col in range(cols):
        pivot = None
        for r in range(rank, rows):
            if M[r, col] == 1: pivot = r; break
        if pivot is not None:
            M[[rank, pivot]] = M[[pivot, rank]]
            for r in range(rows):
                if r != rank and M[r, col] == 1:
                    M[r] = (M[r] + M[rank]) % 2
            rank += 1
    return rank


def gf2_nullspace(M):
    """Find null space of M over GF(2)."""
    M = M.copy() % 2
    rows, cols = M.shape
    aug = M.copy()
    pivot_cols = []
    row_idx = 0
    for col in range(cols):
        pivot = None
        for r in range(row_idx, rows):
            if aug[r, col] == 1: pivot = r; break
        if pivot is None: continue
        if pivot != row_idx: aug[[row_idx, pivot]] = aug[[pivot, row_idx]]
        for r in range(rows):
            if r != row_idx and aug[r, col] == 1:
                aug[r] = (aug[r] + aug[row_idx]) % 2
        pivot_cols.append(col)
        row_idx += 1
    free_cols = [c for c in range(cols) if c not in pivot_cols]
    null_vecs = []
    for fc in free_cols:
        v = np.zeros(cols, dtype=int)
        v[fc] = 1
        for i, pc in enumerate(pivot_cols):
            for r in range(len(pivot_cols)):
                if aug[r][pc] == 1:
                    v[pc] = aug[r][fc]; break
        null_vecs.append(v)
    return null_vecs


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


def gf2_rank_vectors(vectors):
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
        if gf2_rank_vectors(basis) < 3: continue
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


def find_complementary_lagrangian(L):
    """Find a Lagrangian L' such that L ∩ L' = {0} (complementary)."""
    L_list = list(L)
    for other in all_lagrangians:
        if len(L & other) == 1:  # only 0 in common (but 0 not in our set, so empty intersection)
            # Actually our Lagrangians don't include 0, so intersection should be empty
            if len(L & other) == 0:
                return other
    return None


def construct_symplectic_matrix(L, L_prime):
    """
    Construct g ∈ Sp(6, F₂) such that g(V) = L and g(V^⊥) = L_prime.
    V = span{e1, e2, e3}, V^⊥ = span{f1, f2, f3}.
    """
    # Get basis for L
    L_pts = list(L)
    # Find a basis of 3 independent vectors
    for basis in itertools.combinations(L_pts, 3):
        if gf2_rank_vectors(basis) == 3:
            L_basis = [np.array(v) for v in basis]
            break

    # Get basis for L_prime
    Lp_pts = list(L_prime)
    for basis in itertools.combinations(Lp_pts, 3):
        if gf2_rank_vectors(basis) == 3:
            Lp_basis = [np.array(v) for v in basis]
            break

    # Standard basis: V = span{e1,e2,e3}, V^⊥ = span{f1,f2,f3}
    # e1=(1,0,0,0,0,0), e2=(0,1,0,0,0,0), e3=(0,0,1,0,0,0)
    # f1=(0,0,0,1,0,0), f2=(0,0,0,0,1,0), f3=(0,0,0,0,0,1)
    std_basis = [np.array([1,0,0,0,0,0]), np.array([0,1,0,0,0,0]), np.array([0,0,1,0,0,0]),
                 np.array([0,0,0,1,0,0]), np.array([0,0,0,0,1,0]), np.array([0,0,0,0,0,1])]

    # g maps e_i → L_basis[i], f_i → Lp_basis[i]
    # g = [L_basis[0] L_basis[1] L_basis[2] Lp_basis[0] Lp_basis[1] Lp_basis[2]]
    g = np.zeros((6, 6), dtype=int)
    for i in range(3):
        g[:, i] = L_basis[i]
        g[:, i+3] = Lp_basis[i]

    # Verify symplectic
    J = np.zeros((6, 6), dtype=int)
    for i in range(3): J[i][i+3] = 1; J[i+3][i] = 1
    test = (g.T @ J @ g) % 2
    if not np.array_equal(test, J):
        # Try different pairing of L_prime basis vectors
        for perm in itertools.permutations(range(3)):
            g2 = np.zeros((6, 6), dtype=int)
            for i in range(3):
                g2[:, i] = L_basis[i]
                g2[:, i+3] = Lp_basis[perm[i]]
            test2 = (g2.T @ J @ g2) % 2
            if np.array_equal(test2, J):
                return g2
        return None
    return g


# ============================================================
# Pauli and β computation
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


def compute_beta(context_pts):
    pts = list(context_pts)
    beta = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            beta += omega_int(pts[j], pts[k])
    return beta


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
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

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
# Weil representation
# ============================================================

def int_vec(v):
    return int(v[0]) * 4 + int(v[1]) * 2 + int(v[2])

def all_vecs():
    return [np.array([int(b) for b in format(i, '03b')]) for i in range(8)]

def weil_gl(A):
    rho = np.zeros((8, 8), dtype=complex)
    for x in all_vecs():
        y = (A @ x) % 2
        rho[int_vec(y), int_vec(x)] = 1
    return rho

def weil_sym(B):
    rho = np.zeros((8, 8), dtype=complex)
    for x in all_vecs():
        phase = int(x @ B @ x) % 2
        rho[int_vec(x), int_vec(x)] = (-1) ** phase
    return rho

def weil_fourier():
    rho = np.zeros((8, 8), dtype=complex)
    factor = 2 ** (-1.5)
    for x in all_vecs():
        for y in all_vecs():
            phase = int(x @ y) % 2
            rho[int_vec(y), int_vec(x)] = factor * ((-1) ** phase)
    return rho

def weil_decompose(g):
    n = 3
    A = g[:n, :n] % 2; B = g[:n, n:] % 2
    C = g[n:, :n] % 2; D = g[n:, n:] % 2
    ops = []

    if np.array_equal(C, np.zeros((n, n))):
        ops.append(('sym', (B @ A.T) % 2))
        ops.append(('gl', A))
    else:
        D_inv = gf2_inv(D)
        if D_inv is not None:
            BD_inv = (B @ D_inv) % 2
            D_inv_C = (D_inv @ C) % 2
            A_mid = (A - B @ D_inv @ C) % 2
            ops.append(('sym', BD_inv))
            ops.append(('gl', A_mid))
            ops.append(('fourier',))
            ops.append(('sym', D_inv_C))
            ops.append(('fourier',))
        else:
            gF = np.zeros((6, 6), dtype=int)
            gF[:n, :n] = B; gF[:n, n:] = A
            gF[n:, :n] = D; gF[n:, n:] = C
            D2 = gF[n:, n:] % 2; D2_inv = gf2_inv(D2)
            if D2_inv is not None:
                B2 = gF[:n, n:] % 2; A2 = gF[:n, :n] % 2; C2 = gF[n:, :n] % 2
                BD2_inv = (B2 @ D2_inv) % 2
                D2_inv_C2 = (D2_inv @ C2) % 2
                A2_mid = (A2 - B2 @ D2_inv @ C2) % 2
                ops.append(('sym', BD2_inv))
                ops.append(('gl', A2_mid))
                ops.append(('fourier',))
                ops.append(('sym', D2_inv_C2))
                ops.append(('fourier',))
                ops.append(('fourier',))
            else:
                gS = np.zeros((6, 6), dtype=int)
                gS[:n, :n] = A; gS[:n, n:] = (A + B) % 2
                gS[n:, :n] = C; gS[n:, n:] = (C + D) % 2
                D3 = gS[n:, n:] % 2; D3_inv = gf2_inv(D3)
                if D3_inv is not None:
                    B3 = gS[:n, n:] % 2; A3 = gS[:n, :n] % 2; C3 = gS[n:, :n] % 2
                    BD3_inv = (B3 @ D3_inv) % 2
                    D3_inv_C3 = (D3_inv @ C3) % 2
                    A3_mid = (A3 - B3 @ D3_inv @ C3) % 2
                    ops.append(('sym', BD3_inv))
                    ops.append(('gl', A3_mid))
                    ops.append(('fourier',))
                    ops.append(('sym', D3_inv_C3))
                    ops.append(('fourier',))
                    ops.append(('sym', np.eye(n, dtype=int)))
                else:
                    raise ValueError(f"Cannot decompose g=\n{g}")
    return ops

def weil_from_ops(ops):
    rho = np.eye(8, dtype=complex)
    for op in ops:
        if op[0] == 'gl': rho = rho @ weil_gl(op[1])
        elif op[0] == 'sym': rho = rho @ weil_sym(op[1])
        elif op[0] == 'fourier': rho = rho @ weil_fourier()
    return rho

def weil_representation(g):
    ops = weil_decompose(g)
    return weil_from_ops(ops)


def compute_cocycle(g, h, weil_mats):
    """Compute c(g, h) from ρ(g)ρ(h) = c(g,h) ρ(gh)."""
    g_tuple = tuple(tuple(int(x) for x in row) for row in g)
    h_tuple = tuple(tuple(int(x) for x in row) for row in h)
    rho_g = weil_mats[g_tuple]
    rho_h = weil_mats[h_tuple]
    gh = (g @ h) % 2
    gh_tuple = tuple(tuple(int(x) for x in row) for row in gh)
    rho_gh = weil_mats[gh_tuple]
    prod = rho_g @ rho_h @ rho_gh.conj().T
    c = np.trace(prod).real / 8.0
    return 1 if c > 0 else -1


# ============================================================
# G₂(2) group generation with Weil representation
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
    ALL_PTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
    def symplectic_omega(u, v):
        return int(np.dot(u, Omega @ np.array(v))) % 2
    def gf2_r(vectors):
        if not vectors: return 0
        rows = [list(v) for v in vectors]; nc = len(rows[0]); rk = 0
        for col in range(nc):
            pivot = None
            for r in range(rk, len(rows)):
                if rows[r][col] == 1: pivot = r; break
            if pivot is not None:
                rows[rk], rows[pivot] = rows[pivot], rows[rk]
                for r in range(len(rows)):
                    if r != rk and rows[r][col] == 1:
                        rows[r] = [(rows[r][c] + rows[rk][c]) % 2 for c in range(nc)]
                rk += 1
        return rk
    basis = []
    for step in range(3):
        found = False
        for e in ALL_PTS:
            if any(symplectic_omega(e, b) != 0 for b in basis): continue
            if basis and gf2_r(basis + [e]) <= len(basis): continue
            for f in ALL_PTS:
                if f == e: continue
                if symplectic_omega(e, f) != 1: continue
                if any(symplectic_omega(f, b) != 0 for b in basis): continue
                if gf2_r(basis + [e, f]) != len(basis) + 2: continue
                basis.extend([e, f]); found = True; break
            if found: break
    reordered = [basis[0], basis[2], basis[4], basis[1], basis[3], basis[5]]
    P = np.zeros((6, 6), dtype=int)
    for j in range(6):
        for i in range(6): P[i][j] = reordered[j][i]
    return P


def generate_g2_with_weil(generators):
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

    all_elements = {identity}
    weil_mats = {identity: np.eye(8, dtype=complex)}
    queue = deque([identity])
    all_gens = gens + gen_inverses

    gen_weil = {}
    for g_tuple in all_gens:
        g_mat = np.array(g_tuple)
        gen_weil[g_tuple] = weil_representation(g_mat)

    while queue:
        elem = queue.popleft()
        elem_weil = weil_mats[elem]
        for g in all_gens:
            prod = tuple(tuple(int(x) for x in row)
                        for row in (np.array(elem) @ np.array(g)) % 2)
            if prod not in all_elements:
                all_elements.add(prod)
                weil_mats[prod] = elem_weil @ gen_weil[g]
                queue.append(prod)

    return all_elements, weil_mats


# ============================================================
# Main
# ============================================================

def main():
    t0 = time.time()

    print("=" * 70)
    print("Paper XV: Weil Cocycle Verification (β = cocycle)")
    print("=" * 70)

    # Setup
    print("\n[1/6] Change of basis...")
    Omega = find_symplectic_form([G2_GEN1_ATLAS, G2_GEN2_ATLAS])
    P = find_change_of_basis(Omega)
    P_inv = np.array(np.round(np.linalg.inv(P.astype(float)))).astype(int) % 2
    g2_gens_std = [(P_inv @ g @ P) % 2 for g in [G2_GEN1_ATLAS, G2_GEN2_ATLAS]]

    # Enumerate
    print("\n[2/6] Enumerating Lagrangians and contexts...")
    global all_lagrangians
    all_lagrangians = find_lagrangians()
    print(f"  {len(all_lagrangians)} Lagrangians")

    pentagrams, all_contexts, context_signs, context_lag_idx = enumerate_pentagrams(all_lagrangians)
    print(f"  {len(all_contexts)} contexts, {len(pentagrams)} pentagrams")

    # Generate G₂(2) with Weil representation
    print("\n[3/6] Generating G₂(2) with Weil representation...")
    g2_elements, weil_mats = generate_g2_with_weil(g2_gens_std)
    print(f"  |G₂(2)| = {len(g2_elements)}")

    # Precompute: for each Lagrangian, find g ∈ G₂(2) such that g(V) = L
    print("\n[4/6] Finding g_C ∈ G₂(2) for each Lagrangian...")
    lag_to_g = {}

    # V = {(1,0,0,0,0,0), (0,1,0,0,0,0), (0,0,1,0,0,0), (1,1,0,0,0,0), (1,0,1,0,0,0), (0,1,1,0,0,0), (1,1,1,0,0,0)}
    V_pts = frozenset([
        (1,0,0,0,0,0), (0,1,0,0,0,0), (0,0,1,0,0,0),
        (1,1,0,0,0,0), (1,0,1,0,0,0), (0,1,1,0,0,0), (1,1,1,0,0,0)
    ])

    # Sample G₂(2) elements and track which Lagrangians they map V to
    print(f"  Searching {len(g2_elements)} G₂(2) elements...")
    found_count = 0
    for gi, g_tuple in enumerate(g2_elements):
        if found_count >= len(all_lagrangians):
            break
        g_mat = np.array(g_tuple)
        # Compute g(V)
        gV = frozenset(tuple((g_mat @ np.array(v)) % 2) for v in V_pts)
        # Find which Lagrangian this is
        for li, lag in enumerate(all_lagrangians):
            if li in lag_to_g:
                continue
            if lag == gV:
                lag_to_g[li] = g_tuple
                found_count += 1
                break
        if (gi + 1) % 2000 == 0:
            print(f"  {gi+1}/{len(g2_elements)}, found {found_count}/{len(all_lagrangians)}")

    print(f"  {len(lag_to_g)}/{len(all_lagrangians)} Lagrangians have g_C ∈ G₂(2)")

    # Verify β = cocycle for each context
    print("\n[5/6] Verifying β(C)/2 mod 2 = c(g_C, g_C^{-1}) mod 2...")
    match_count = 0
    total_count = 0
    mismatches = []

    for ci, ctx in enumerate(all_contexts):
        li = context_lag_idx[ci]
        if li not in lag_to_g:
            continue

        g_tuple = lag_to_g[li]
        g = np.array(g_tuple)

        # Compute β(C)
        beta = compute_beta(ctx)
        beta_half_mod2 = (beta // 2) % 2

        # Compute cocycle c(g, g^{-1}) where g ∈ G₂(2)
        g_inv_tuple = tuple(tuple(int(x) for x in row) for row in gf2_inv(g))
        c_val = compute_cocycle(g, np.array(g_inv_tuple), weil_mats)
        cocycle_phase = 0 if c_val == 1 else 1

        total_count += 1
        if beta_half_mod2 == cocycle_phase:
            match_count += 1
        else:
            mismatches.append((ci, li, beta, c_val, beta_half_mod2, cocycle_phase))

        if total_count % 200 == 0:
            print(f"  {total_count}/{len(all_contexts)} contexts checked, {match_count} matches")

    print(f"\n  Results: {match_count}/{total_count} matches ({100*match_count/total_count:.1f}%)")
    if mismatches:
        print(f"  First 5 mismatches:")
        for ci, li, beta, c_val, bhm, cp in mismatches[:5]:
            print(f"    ctx {ci}, lag {li}: β={beta}, β/2 mod 2={bhm}, c(g,g⁻¹)={c_val}, cocycle phase={cp}")

    # Per k-type analysis
    print("\n[5b/6] Per k-type analysis...")
    k_type_matches = defaultdict(lambda: {'match': 0, 'total': 0})
    for ci, ctx in enumerate(all_contexts):
        li = context_lag_idx[ci]
        if li not in lag_to_g: continue
        lag = all_lagrangians[li]
        k = sum(1 for v in lag if v[3] == 0 and v[4] == 0 and v[5] == 0)

        g_tuple = lag_to_g[li]
        g = np.array(g_tuple)
        beta = compute_beta(ctx)
        beta_half_mod2 = (beta // 2) % 2
        g_inv = gf2_inv(g)
        g_inv_tuple = tuple(tuple(int(x) for x in row) for row in g_inv)
        c_val = compute_cocycle(g, np.array(g_inv_tuple), weil_mats)
        cocycle_phase = 0 if c_val == 1 else 1

        k_type_matches[k]['total'] += 1
        if beta_half_mod2 == cocycle_phase:
            k_type_matches[k]['match'] += 1

    for k in sorted(k_type_matches.keys()):
        d = k_type_matches[k]
        print(f"  k={k}: {d['match']}/{d['total']} ({100*d['match']/d['total']:.1f}%)")

    print(f"\n{'=' * 70}")
    print(f"Total time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
