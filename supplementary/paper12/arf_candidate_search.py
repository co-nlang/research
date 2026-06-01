#!/usr/bin/env python3
"""
Paper XII: Search for the geometrically natural u with q(u)=1
that corresponds to the [f₃] obstruction class.

1. Enumerate all 36 vectors u with q(u) = 1
2. Compute G₂(2) orbits on these 36 vectors
3. For each u, analyze relationship to all 12,096 pentagrams:
   - u ∈ L_i membership
   - ω(u, r_ij) pattern
   - Correlation with pentagram type (B/F2/F4) and orbit
4. Check for G₂(2)-fixed points
5. Standard pentagram: which u gives correct [f₃]?
"""

import itertools
import numpy as np
from collections import defaultdict, Counter
import time

# G₂(2) generators (standard symplectic basis)
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

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def Q_form(v):
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]

def q_mod2(v):
    return (v[0]*v[3] + v[1]*v[4] + v[2]*v[5]) % 2

def add(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))

def mat_vec_mod2(A, v):
    return tuple(int(x) for x in (A @ np.array(v)) % 2)

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


def generate_g2_orbit(v):
    """BFS to find the full G₂(2) orbit of vector v."""
    orbit = set()
    queue = [v]
    orbit.add(v)
    while queue:
        curr = queue.pop()
        for gen in [G2_GEN1, G2_GEN2]:
            nxt = mat_vec_mod2(gen, curr)
            if nxt not in orbit and nxt != (0,0,0,0,0,0):
                orbit.add(nxt)
                queue.append(nxt)
            inv = mat_vec_mod2(np.linalg.inv(gen).astype(int) % 2, curr)
    # Redo properly with inverse generators
    orbit2 = set()
    queue2 = [v]
    orbit2.add(v)
    gens_and_inv = []
    for gen in [G2_GEN1, G2_GEN2]:
        inv = np.array(np.round(np.linalg.inv(gen)), dtype=int) % 2
        gens_and_inv.extend([gen, inv])
    while queue2:
        curr = queue2.pop()
        for g in gens_and_inv:
            nxt = mat_vec_mod2(g, curr)
            if nxt != (0,0,0,0,0,0) and nxt not in orbit2:
                orbit2.add(nxt)
                queue2.append(nxt)
    return orbit2


def generate_g2_group():
    """Generate all elements of G₂(2) by BFS on generators."""
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


def main():
    t0 = time.time()
    print("=" * 70)
    print("Paper XII: Arf Invariant Candidate Search")
    print("=" * 70)

    # Step 1: Enumerate q(u)=1 vectors
    print("\n[1/5] Enumerating q(u)=1 vectors...")
    q1_vectors = [v for v in ALL_POINTS if q_mod2(v) == 1]
    q0_vectors = [v for v in ALL_POINTS if q_mod2(v) == 0]
    print(f"  q(u)=1: {len(q1_vectors)} vectors")
    print(f"  q(u)=0 (nonzero): {len(q0_vectors)} vectors")

    # Step 2: G₂(2) orbits on q=1 vectors
    print("\n[2/5] Computing G₂(2) orbits on q=1 vectors...")
    remaining = set(q1_vectors)
    orbits = []
    while remaining:
        seed = next(iter(remaining))
        orbit = generate_g2_orbit(seed)
        orbit = orbit & set(q1_vectors)  # restrict to q=1
        orbits.append(orbit)
        remaining -= orbit
        print(f"  Orbit {len(orbits)}: size {len(orbit)}, seed {seed}")

    print(f"  Total: {len(orbits)} orbits, sizes: {sorted([len(o) for o in orbits], reverse=True)}")
    print(f"  Sum: {sum(len(o) for o in orbits)}")

    # Check: any fixed points? (orbit of size 1)
    fixed = [o for o in orbits if len(o) == 1]
    print(f"  Fixed points (orbit size 1): {len(fixed)}")
    if fixed:
        for o in fixed:
            print(f"    u = {next(iter(o))}")

    # Step 3: Enumerate Lagrangians and pentagrams
    print("\n[3/5] Enumerating Lagrangians and pentagrams...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    all_contexts = []
    context_signs = []
    context_lag_idx = []

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

    # Build pentagrams
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

                        # Extract rays and Lagrangians
                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]] & all_contexts[clique[b]]
                                if shared:
                                    rays[(a,b)] = next(iter(shared))

                        lag_indices = [context_lag_idx[ci] for ci in clique]
                        lag_sets = [lagrangians[li] for li in lag_indices]

                        # V-intersection type
                        k_vals = []
                        for ls in lag_sets:
                            k = len(ls & V_SET)
                            k_vals.append(k)

                        # Fano points (contexts ∩ V)
                        fano_pts = set()
                        for ci in clique:
                            for v in all_contexts[ci]:
                                if v in V_SET:
                                    fano_pts.add(v)
                        n_fano = len(fano_pts)

                        # Type classification
                        if n_fano == 4:
                            ptype = 'B'
                        elif n_fano == 3:
                            ptype = 'F2'
                        elif n_fano <= 1:
                            ptype = 'F4'
                        else:
                            ptype = '?'

                        pentagrams.append(pent)
                        pent_data.append({
                            'rays': rays,
                            'lag_indices': lag_indices,
                            'lag_sets': lag_sets,
                            'k_vals': k_vals,
                            'fano_pts': fano_pts,
                            'n_fano': n_fano,
                            'type': ptype,
                            'clique': clique,
                        })

    n_pent = len(pentagrams)
    print(f"  {n_pent} Mermin pentagrams")

    # Step 4: For each q=1 vector u, analyze relationship to pentagrams
    print(f"\n[4/5] Analyzing u-pentagram relationships...")

    # Sample pentagrams for speed (full analysis on all 12096 is expensive)
    # But let's try full first
    SAMPLE = min(n_pent, 2000)
    sample_indices = list(range(0, n_pent, n_pent // SAMPLE))[:SAMPLE]

    for u in q1_vectors[:3]:  # Show first 3 in detail
        print(f"\n  --- u = {u}, q(u) = {Q_form(u)} ---")

        # How many pentagrams have u in some Lagrangian?
        in_lag_count = 0
        in_lag_positions = Counter()
        omega_patterns = Counter()

        for pi in sample_indices:
            d = pent_data[pi]
            u_in_lag = False
            for idx, ls in enumerate(d['lag_sets']):
                if u in ls:
                    u_in_lag = True
                    in_lag_positions[idx] += 1
            if u_in_lag:
                in_lag_count += 1

            # ω(u, r) for each ray
            pattern = tuple(omega_int(u, r) % 2 for r in d['rays'].values())
            omega_patterns[pattern] += 1

        print(f"    u ∈ some L_i: {in_lag_count}/{SAMPLE} pentagrams")
        print(f"    Position distribution: {dict(in_lag_positions)}")
        print(f"    Top 3 ω-patterns: {omega_patterns.most_common(3)}")

    # Step 5: Global analysis — for each u, count how many pentagrams have u ∈ ∪L_i
    print(f"\n[5/5] Global u-pentagram analysis (all {n_pent} pentagrams)...")

    # Precompute: for each Lagrangian, which q=1 vectors does it contain?
    lag_q1 = []
    for lag in lagrangians:
        lag_q1.append(set(v for v in lag if q_mod2(v) == 1))

    # For each u, count pentagrams where u ∈ ∪L_i
    u_pent_membership = {}
    for u in q1_vectors:
        # Which Lagrangians contain u?
        lags_with_u = set()
        for li, lag in enumerate(lagrangians):
            if u in lag:
                lags_with_u.add(li)

        # Count pentagrams where at least one Lagrangian contains u
        count = 0
        type_dist = Counter()
        for pi in range(n_pent):
            d = pent_data[pi]
            if any(li in lags_with_u for li in d['lag_indices']):
                count += 1
                type_dist[d['type']] += 1

        u_pent_membership[u] = {
            'n_lags': len(lags_with_u),
            'n_pents': count,
            'pct': count / n_pent * 100,
            'type_dist': type_dist,
        }

    # Summary
    print(f"\n{'='*70}")
    print("RESULTS")
    print(f"{'='*70}")

    print(f"\n--- G₂(2) orbits on q=1 vectors ---")
    for i, orbit in enumerate(orbits):
        print(f"  Orbit {i+1}: size {len(orbit)}")
        rep = next(iter(orbit))
        info = u_pent_membership[rep]
        print(f"    Representative: {rep}")
        print(f"    Lagrangians containing u: {info['n_lags']}")
        print(f"    Pentagrams with u ∈ ∪L_i: {info['n_pents']}/{n_pent} ({info['pct']:.1f}%)")
        print(f"    Type distribution: {dict(info['type_dist'])}")

    # Check: is there a u that belongs to ALL pentagrams' Lagrangian unions?
    print(f"\n--- Universal u candidates ---")
    for u in q1_vectors:
        info = u_pent_membership[u]
        if info['n_pents'] == n_pent:
            print(f"  UNIVERSAL: u={u}, in all {n_pent} pentagrams")

    # Check: is there a u in NO pentagram's Lagrangian union?
    for u in q1_vectors:
        info = u_pent_membership[u]
        if info['n_pents'] == 0:
            print(f"  ABSENT: u={u}, in 0 pentagrams")

    # Distribution of membership percentages
    print(f"\n--- Membership distribution across q=1 vectors ---")
    pcts = [u_pent_membership[u]['pct'] for u in q1_vectors]
    pct_counter = Counter(round(p, 1) for p in pcts)
    for pct, cnt in sorted(pct_counter.items()):
        print(f"  {pct}%: {cnt} vectors")

    # For standard pentagram (first one), which u's are "natural"?
    print(f"\n--- Standard pentagram analysis ---")
    d0 = pent_data[0]
    print(f"  Pentagram 0: type={d0['type']}, k_vals={d0['k_vals']}")
    print(f"  Rays: {dict(list(d0['rays'].items())[:3])}...")

    # T-vector for pentagram 0
    T = [0] * 6
    for r in d0['rays'].values():
        for i in range(6):
            T[i] ^= r[i]
    T = tuple(T)
    print(f"  T = {T}, q(T) = {q_mod2(T)}")

    # Which q=1 vectors have special relationship to pentagram 0?
    # Check: u such that ω(u, r) = 1 for ALL 10 rays
    for u in q1_vectors:
        omega_all = [omega_int(u, r) % 2 for r in d0['rays'].values()]
        if all(w == 1 for w in omega_all):
            print(f"  u={u}: ω(u,r)=1 for ALL 10 rays")
        if all(w == 0 for w in omega_all):
            print(f"  u={u}: ω(u,r)=0 for ALL 10 rays (u ∈ span(rays)⊥)")

    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
