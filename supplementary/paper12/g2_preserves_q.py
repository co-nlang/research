#!/usr/bin/env python3
"""
Paper XII: Check if G₂(2) preserves q, and q(T) distribution per orbit.
Optimized with hash-based pentagram lookup.
"""

import itertools
import numpy as np
from collections import defaultdict, Counter
import time

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


def symplectic_form_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def q_mod2(v):
    return (v[0]*v[3] + v[1]*v[4] + v[2]*v[5]) % 2

def mat_vec_mod2(A, v):
    return tuple(int(x) for x in (A @ np.array(v)) % 2)

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


def generate_g2_group():
    identity = tuple(tuple(row) for row in np.eye(6, dtype=int))
    group = set()
    group.add(identity)
    queue = [np.eye(6, dtype=int)]
    gens = [G2_GEN1, G2_GEN2]
    while queue:
        curr = queue.pop()
        for g in gens:
            nxt = (curr @ g) % 2
            nxt_t = tuple(tuple(row) for row in nxt)
            if nxt_t not in group:
                group.add(nxt_t)
                queue.append(nxt)
    return [np.array(m) for m in group]


def pentagram_hash(context_set):
    """Canonical hash for a pentagram (set of 5 contexts)."""
    sorted_ctxs = tuple(sorted(tuple(sorted(ctx)) for ctx in context_set))
    return hash(sorted_ctxs)


def main():
    t0 = time.time()
    print("=" * 70)
    print("Paper XII: G₂(2) preserves q? + q(T) per orbit")
    print("=" * 70)

    # Step 1: Check if G₂(2) preserves q
    print("\n[1/3] Checking if G₂(2) preserves q...")
    g2_elements = generate_g2_group()
    print(f"  |G₂(2)| = {len(g2_elements)}")

    preserves_q = True
    violations = 0
    for v in ALL_POINTS:
        q_v = q_mod2(v)
        for g in g2_elements:
            gv = mat_vec_mod2(g, v)
            if q_mod2(gv) != q_v:
                violations += 1
                if violations <= 3:
                    print(f"  ✗ v={v}, q={q_v} → g·v={gv}, q={q_mod2(gv)}")
                preserves_q = False

    if preserves_q:
        print(f"  ✓ G₂(2) PRESERVES q (all {len(g2_elements)} × 63 checks passed)")
    else:
        print(f"  ✗ G₂(2) does NOT preserve q ({violations} violations)")

    # Step 2: Enumerate pentagrams
    print("\n[2/3] Enumerating pentagrams...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    I2 = np.eye(2, dtype=complex)
    XM = np.array([[0,1],[1,0]], dtype=complex)
    YM = np.array([[0,-1j],[1j,0]], dtype=complex)
    ZM = np.array([[1,0],[0,-1]], dtype=complex)
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
        return int(round(mat[0,0].real))

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
    pent_hash_to_idx = {}

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

                        T = [0] * 6
                        for r in rays.values():
                            for idx in range(6):
                                T[idx] ^= r[idx]
                        T = tuple(T)

                        pi = len(pentagrams)
                        pentagrams.append(pent)
                        pent_data.append({
                            'rays': rays,
                            'T': T,
                            'q_T': q_mod2(T),
                            'context_set': frozenset(all_contexts[ci] for ci in clique),
                        })
                        h = pentagram_hash(frozenset(all_contexts[ci] for ci in clique))
                        pent_hash_to_idx[h] = pi

    n_pent = len(pentagrams)
    print(f"  {n_pent} Mermin pentagrams")

    # Step 3: Compute orbits using BFS with hash lookup
    print("  Computing G₂(2) orbits via BFS...")
    pent_orbit = [-1] * n_pent
    orbit_id = 0
    orbit_sizes = []

    gens_inv = []
    for gen in [G2_GEN1, G2_GEN2]:
        inv = np.array(np.round(np.linalg.inv(gen)), dtype=int) % 2
        gens_inv.extend([gen, inv])

    for start_pi in range(n_pent):
        if pent_orbit[start_pi] >= 0:
            continue
        orbit_id += 1
        orbit_members = set()
        queue = [start_pi]
        orbit_members.add(start_pi)
        pent_orbit[start_pi] = orbit_id

        while queue:
            curr_pi = queue.pop()
            curr_ctx_set = pent_data[curr_pi]['context_set']

            for g in gens_inv:
                new_ctx_set = frozenset(
                    frozenset(mat_vec_mod2(g, v) for v in ctx)
                    for ctx in curr_ctx_set
                )
                h = pentagram_hash(new_ctx_set)
                if h in pent_hash_to_idx:
                    target_pi = pent_hash_to_idx[h]
                    if pent_orbit[target_pi] < 0:
                        pent_orbit[target_pi] = orbit_id
                        orbit_members.add(target_pi)
                        queue.append(target_pi)

        orbit_sizes.append(len(orbit_members))
        print(f"    Orbit {orbit_id}: size {len(orbit_members)}")

    # Step 4: q(T) per orbit
    print(f"\n[3/3] q(T) distribution per orbit...")
    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")

    print(f"\n  G₂(2) preserves q: {preserves_q}")
    print(f"  Orbits: {orbit_sizes}")

    for oid in range(1, orbit_id + 1):
        members = [pi for pi in range(n_pent) if pent_orbit[pi] == oid]
        q_dist = Counter(pent_data[pi]['q_T'] for pi in members)
        print(f"\n  Orbit {oid} (size {len(members)}):")
        print(f"    q(T)=0: {q_dist[0]} ({q_dist[0]/len(members)*100:.1f}%)")
        print(f"    q(T)=1: {q_dist[1]} ({q_dist[1]/len(members)*100:.1f}%)")

    # Class I vs II
    if orbit_id >= 4:
        class_I = [pi for pi in range(n_pent) if pent_orbit[pi] in (1, 2)]
        class_II = [pi for pi in range(n_pent) if pent_orbit[pi] in (3, 4)]
        cI_q = Counter(pent_data[pi]['q_T'] for pi in class_I)
        cII_q = Counter(pent_data[pi]['q_T'] for pi in class_II)
        print(f"\n  Class I (O₁+O₂, size {len(class_I)}):")
        print(f"    q(T)=0: {cI_q[0]} ({cI_q[0]/len(class_I)*100:.1f}%)")
        print(f"    q(T)=1: {cI_q[1]} ({cI_q[1]/len(class_I)*100:.1f}%)")
        print(f"  Class II (O₃+O₄, size {len(class_II)}):")
        print(f"    q(T)=0: {cII_q[0]} ({cII_q[0]/len(class_II)*100:.1f}%)")
        print(f"    q(T)=1: {cII_q[1]} ({cII_q[1]/len(class_II)*100:.1f}%)")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
