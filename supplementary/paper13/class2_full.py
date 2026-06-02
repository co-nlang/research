#!/usr/bin/env python3
"""
Class II geometric characterization (full enumeration).

Enumerates all 12,096 pentagrams, computes G₂(2) orbits,
then analyzes geometric invariants to distinguish Class I vs Class II.
"""

import numpy as np
import itertools
from collections import defaultdict, Counter, deque
import time
import sys
sys.path.insert(0, '/mnt/d/Workspace/ai_ai/nlang/research/supplementary/paper10')

# G₂(2) generators (standard basis, from g2_orbits.py)
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


def mat_vec_mod2(A, v):
    return tuple((A @ np.array(v)) % 2)


def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2


def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])


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
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            s = add(pts[i], pts[j])
            if s in lag_points and s != (0,0,0,0,0,0):
                lines.add(frozenset([pts[i], pts[j], s]))
    return list(lines)


def k_type(lag):
    return sum(1 for p in lag if p[3]==0 and p[4]==0 and p[5]==0)


def Q_form(v):
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]


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


def enumerate_pentagrams(lagrangians):
    all_contexts = []
    context_signs = []
    context_k_type = []
    context_lag_idx = []

    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        kt = k_type(lag)
        for line in fano_lines:
            ctx_pts = [p for p in pts if p not in line]
            if len(ctx_pts) != 4:
                continue
            sign = pauli_product_sign(ctx_pts)
            if sign == 0:
                continue
            all_contexts.append(frozenset(ctx_pts))
            context_signs.append(sign)
            context_k_type.append(kt)
            context_lag_idx.append(li)

    n_ctx = len(all_contexts)

    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            shared = all_contexts[i] & all_contexts[j]
            if len(shared) == 1:
                adj[i].append(j)
                adj[j].append(i)

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

    return list(set(pentagrams)), all_contexts, context_signs, context_k_type, context_lag_idx, lagrangians


def generate_g2_elements(generators):
    identity = tuple(tuple(row) for row in np.eye(6, dtype=int))
    gens = [tuple(tuple(row) for row in g) for g in generators]
    gen_inverses = []
    for g in generators:
        m = g.copy()
        order = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g) % 2
            order += 1
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
            e_mat = np.array(elem)
            g_mat = np.array(g)
            prod = tuple(tuple(int(x) for x in row) for row in (e_mat @ g_mat) % 2)
            if prod not in all_elements:
                all_elements.add(prod)
                queue.append(prod)

    return all_elements


def main():
    t0 = time.time()
    print("=" * 70)
    print("Class II Geometric Characterization")
    print("=" * 70)

    print("\n[1/5] Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    print("\n[2/5] Enumerating all pentagrams...")
    pentagrams, all_contexts, context_signs, context_k_type, context_lag_idx, lags = enumerate_pentagrams(lagrangians)
    print(f"  {len(pentagrams)} pentagrams")
    print(f"  {len(all_contexts)} contexts")

    print("\n[3/5] Computing G₂(2) orbits...")
    
    # Find symplectic form preserved by ATLAS generators
    from g2_orbits import find_symplectic_form, find_change_of_basis
    Omega = find_symplectic_form([G2_GEN1, G2_GEN2])
    P = find_change_of_basis(Omega)
    P_inv = np.array(np.round(np.linalg.inv(P.astype(float)))).astype(int) % 2
    
    # Transform generators to standard basis
    g2_gens = []
    for g in [G2_GEN1, G2_GEN2]:
        g_std = (P_inv @ g @ P) % 2
        g2_gens.append(g_std)
    print(f"  G₂(2) generators transformed to standard basis")
    
    # Generate G₂(2) elements
    g2_elements = generate_g2_elements(g2_gens)
    print(f"  |G₂(2)| = {len(g2_elements)}")

    # Build context lookup
    ctx_to_idx = {ctx: i for i, ctx in enumerate(all_contexts)}

    # Precompute generator actions on contexts
    gen_inv_mats = []
    for g in g2_gens:
        inv = np.eye(6, dtype=int)
        m = g.copy()
        order = 1
        while not np.array_equal(m % 2, np.eye(6, dtype=int)):
            m = (m @ g) % 2
            order += 1
        for _ in range(order - 1):
            inv = (inv @ g) % 2
        gen_inv_mats.append(inv)

    all_gens = g2_gens + gen_inv_mats

    ctx_action = []
    for g_mat in all_gens:
        action = {}
        for i, ctx in enumerate(all_contexts):
            new_pts = frozenset(mat_vec_mod2(g_mat, v) for v in ctx)
            if new_pts in ctx_to_idx:
                action[i] = ctx_to_idx[new_pts]
        ctx_action.append(action)

    # BFS to find orbits
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

    orbits = sorted(orbits, key=len, reverse=True)
    print(f"  {len(orbits)} orbits: {[len(o) for o in orbits]}")

    # Classify: Class I = orbit 0 (6048) + orbit 1 (2016), Class II = orbits 2+3 (2016 each)
    orbit_of_pent = {}
    for oi, orbit in enumerate(orbits):
        for pidx in orbit:
            orbit_of_pent[pidx] = oi

    class1_orbits = [0, 1]
    class2_orbits = [2, 3]

    print(f"\n  Class I (orbits {class1_orbits}): {sum(len(orbits[i]) for i in class1_orbits)} pentagrams")
    print(f"  Class II (orbits {class2_orbits}): {sum(len(orbits[i]) for i in class2_orbits)} pentagrams")

    print("\n[4/5] Computing geometric invariants...")
    
    class1_data = []
    class2_data = []
    
    for pidx, pent in enumerate(pentagrams):
        orbit_idx = orbit_of_pent[pidx]
        is_class1 = orbit_idx in class1_orbits
        
        # Get Lagrangians for this pentagram
        pent_lags = [lags[context_lag_idx[ci]] for ci in pent]
        
        # k-profile
        k_profile = tuple(sorted(context_k_type[ci] for ci in pent))
        
        # T-vector
        rays = list(set().union(*[all_contexts[ci] for ci in pent]))
        T = [0] * 6
        for r in rays:
            T = [(T[k] + r[k]) % 2 for k in range(6)]
        T = tuple(T)
        
        q_T = Q_form(T)
        T_in_any_lag = any(T in lag for lag in pent_lags)
        
        # Triple intersection dimensions
        triple_dims = []
        for i, j, k in itertools.combinations(range(5), 3):
            inter = pent_lags[i] & pent_lags[j] & pent_lags[k]
            triple_dims.append(len(inter))
        triple_profile = tuple(sorted(triple_dims))
        
        # Parity distribution (number of -1 contexts)
        n_minus = sum(1 for ci in pent if context_signs[ci] == -1)
        
        data = {
            'orbit': orbit_idx,
            'k_profile': k_profile,
            'q_T': q_T,
            'T_in_lag': T_in_any_lag,
            'triple_profile': triple_profile,
            'n_minus': n_minus,
        }
        
        if is_class1:
            class1_data.append(data)
        else:
            class2_data.append(data)
    
    print(f"  Computed invariants for {len(class1_data)} Class I + {len(class2_data)} Class II pentagrams")

    print("\n[5/5] Comparing distributions...")
    print("\n" + "=" * 70)
    print("INVARIANT COMPARISON: Class I vs Class II")
    print("=" * 70)
    
    # k-profile
    print("\n1. k-profile distribution:")
    k1 = Counter(d['k_profile'] for d in class1_data)
    k2 = Counter(d['k_profile'] for d in class2_data)
    for kp in sorted(set(k1.keys()) | set(k2.keys())):
        c1 = k1.get(kp, 0)
        c2 = k2.get(kp, 0)
        pct1 = 100*c1/len(class1_data) if class1_data else 0
        pct2 = 100*c2/len(class2_data) if class2_data else 0
        print(f"  {kp}: Class I {c1} ({pct1:.1f}%), Class II {c2} ({pct2:.1f}%)")
    
    # q(T)
    print("\n2. q(T) distribution:")
    q1 = Counter(d['q_T'] for d in class1_data)
    q2 = Counter(d['q_T'] for d in class2_data)
    for qv in sorted(set(q1.keys()) | set(q2.keys())):
        c1 = q1.get(qv, 0)
        c2 = q2.get(qv, 0)
        pct1 = 100*c1/len(class1_data) if class1_data else 0
        pct2 = 100*c2/len(class2_data) if class2_data else 0
        print(f"  q(T)={qv}: Class I {c1} ({pct1:.1f}%), Class II {c2} ({pct2:.1f}%)")
    
    # T in Lagrangian
    print("\n3. T ∈ ∪Lᵢ:")
    t1 = Counter(d['T_in_lag'] for d in class1_data)
    t2 = Counter(d['T_in_lag'] for d in class2_data)
    print(f"  Class I: {dict(t1)}")
    print(f"  Class II: {dict(t2)}")
    
    # Triple intersection
    print("\n4. Triple intersection profile:")
    trip1 = Counter(d['triple_profile'] for d in class1_data)
    trip2 = Counter(d['triple_profile'] for d in class2_data)
    print(f"  Class I: {dict(trip1)}")
    print(f"  Class II: {dict(trip2)}")
    
    # Parity (n_minus)
    print("\n5. Parity distribution (number of -1 contexts):")
    p1 = Counter(d['n_minus'] for d in class1_data)
    p2 = Counter(d['n_minus'] for d in class2_data)
    for nv in sorted(set(p1.keys()) | set(p2.keys())):
        c1 = p1.get(nv, 0)
        c2 = p2.get(nv, 0)
        pct1 = 100*c1/len(class1_data) if class1_data else 0
        pct2 = 100*c2/len(class2_data) if class2_data else 0
        print(f"  {nv}-minus: Class I {c1} ({pct1:.1f}%), Class II {c2} ({pct2:.1f}%)")
    
    # Per-orbit breakdown
    print("\n6. Per-orbit breakdown:")
    for oi in range(4):
        orbit_data = [d for d in class1_data + class2_data if d['orbit'] == oi]
        kp = Counter(d['k_profile'] for d in orbit_data)
        qt = Counter(d['q_T'] for d in orbit_data)
        nm = Counter(d['n_minus'] for d in orbit_data)
        print(f"  Orbit {oi} ({len(orbit_data)} pentagrams):")
        print(f"    k-profiles: {dict(kp)}")
        print(f"    q(T): {dict(qt)}")
        print(f"    parity: {dict(nm)}")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
