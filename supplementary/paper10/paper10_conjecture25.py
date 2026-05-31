#!/usr/bin/env python3
"""
Paper X: Conjecture 2.5 — Context-Level Computation (Optimized v2)
Uses early parity pruning and efficient K5 search.
"""

import itertools
from collections import defaultdict
import numpy as np
import time

def symplectic_form(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def add(u, v):
    return tuple((a + b) % 2 for a, b in zip(u, v))

def gf2_rank(vectors):
    rows = [list(v) for v in vectors]
    rank = 0
    ncols = len(rows[0]) if rows else 0
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

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]
V_POINTS = [p for p in ALL_POINTS if p[3] == 0 and p[4] == 0 and p[5] == 0]
V_SET = set(V_POINTS)

FANO_LABEL = {
    (1,0,0): 1, (0,1,0): 2, (0,0,1): 3,
    (1,1,0): 4, (1,0,1): 5, (0,1,1): 6, (1,1,1): 7
}

def span3(basis):
    a, b, c = basis
    return frozenset([
        a, b, c, add(a, b), add(a, c), add(b, c), add(a, add(b, c))
    ])

def find_lagrangians():
    lagrangians = []
    seen = set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3:
            continue
        ti = all(symplectic_form(u, v) == 0 for u, v in itertools.combinations(basis, 2))
        if not ti:
            continue
        subspace = span3(basis)
        if subspace not in seen:
            seen.add(subspace)
            lagrangians.append(subspace)
    return lagrangians

def get_fano_lines_in_lagrangian(lag_points):
    pts = list(lag_points)
    lines = set()
    for i in range(7):
        for j in range(i+1, 7):
            s = add(pts[i], pts[j])
            if s in lag_points:
                lines.add(frozenset([pts[i], pts[j], s]))
    return list(lines)

# ============================================================
# Pauli matrices (precomputed)
# ============================================================

I2 = np.array([[1, 0], [0, 1]], dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}

PAULI3_CACHE = {}

def vector_to_pauli_string(v):
    chars = []
    for q in range(3):
        x, z = v[q], v[q + 3]
        if x == 0 and z == 0:
            chars.append('I')
        elif x == 1 and z == 0:
            chars.append('X')
        elif x == 1 and z == 1:
            chars.append('Y')
        elif x == 0 and z == 1:
            chars.append('Z')
    return ''.join(chars)

def get_pauli3(v):
    if v not in PAULI3_CACHE:
        s = vector_to_pauli_string(v)
        M = PAULI[s[0]]
        for c in s[1:]:
            M = np.kron(M, PAULI[c])
        PAULI3_CACHE[v] = M
    return PAULI3_CACHE[v]

def context_product_sign(ops):
    P = np.eye(8, dtype=complex)
    for v in ops:
        P = P @ get_pauli3(v)
    return int(round(P[0, 0].real))

# ============================================================
# Fano lines for collinearity check
# ============================================================

FANO_LINES = [
    {1, 2, 4}, {1, 3, 5}, {1, 6, 7},
    {2, 3, 6}, {2, 5, 7}, {3, 4, 7}, {4, 5, 6}
]

def analyze_collinearity(fano_points):
    pts = set(fano_points)
    collinear_triples = []
    for line in FANO_LINES:
        pts_in_line = sorted([p for p in pts if p in line])
        if len(pts_in_line) == 3:
            collinear_triples.append(tuple(pts_in_line))
    return collinear_triples

# ============================================================
# Main
# ============================================================

def main():
    t0 = time.time()

    print("[1/6] Finding 135 Lagrangians...")
    lagrangians = find_lagrangians()
    assert len(lagrangians) == 135
    print(f"  Done ({time.time()-t0:.1f}s)")

    print("\n[2/6] Extracting 945 contexts...")
    contexts = []
    for lag_idx, L in enumerate(lagrangians):
        lines = get_fano_lines_in_lagrangian(L)
        for line_idx, line in enumerate(lines):
            context_ops = tuple(p for p in L if p not in line)
            contexts.append((context_ops, lag_idx, line_idx))
    assert len(contexts) == 945

    print("\n[3/6] Precomputing product signs...")
    signs = []
    for i, (ops, _, _) in enumerate(contexts):
        s = context_product_sign(ops)
        signs.append(s)
    n_minus = sum(1 for s in signs if s == -1)
    print(f"  {n_minus} contexts with -I, {945-n_minus} with +I")

    print("\n[4/6] Building adjacency...")
    n = len(contexts)
    adj = [[] for _ in range(n)]
    for i in range(n):
        set_i = set(contexts[i][0])
        for j in range(i + 1, n):
            if len(set_i & set(contexts[j][0])) == 1:
                adj[i].append(j)
                adj[j].append(i)
    avg_deg = sum(len(a) for a in adj) / n
    print(f"  Done. Degree = {avg_deg:.0f} (regular graph)")

    print(f"\n[5/6] Finding Mermin pentagrams...")
    t1 = time.time()
    mermin_count = 0
    type_counts = defaultdict(int)
    type_a_data = []

    # Precompute sets for fast intersection
    ctx_sets = [set(ctx[0]) for ctx in contexts]

    # Precompute adjacency as sets for fast intersection
    adj_sets = [set(a) for a in adj]

    for i in range(n):
        si = adj_sets[i]
        for j_pos in range(len(adj[i])):
            j = adj[i][j_pos]
            sj = adj_sets[j]
            # Parity pruning: signs[i] + signs[j] so far
            parity_ij = (1 if signs[i] == -1 else 0) + (1 if signs[j] == -1 else 0)

            common_k = si & sj
            for k in common_k:
                if k <= j:
                    continue
                sk = adj_sets[k]
                parity_ijk = parity_ij + (1 if signs[k] == -1 else 0)

                common_m = common_k & sk
                for m in common_m:
                    if m <= k:
                        continue
                    sm = adj_sets[m]
                    parity_ijkm = parity_ijk + (1 if signs[m] == -1 else 0)

                    common_p = common_m & sm
                    for p in common_p:
                        if p <= m:
                            continue

                        # Mermin pentagram: 10 shared operators must be distinct
                        shared = []
                        clique_list = [i, j, k, m, p]
                        valid_mermin = True
                        for a_pos in range(5):
                            for b_pos in range(a_pos+1, 5):
                                ia = clique_list[a_pos]
                                ib = clique_list[b_pos]
                                inter = ctx_sets[ia] & ctx_sets[ib]
                                if len(inter) != 1:
                                    valid_mermin = False
                                    break
                                shared.append(next(iter(inter)))
                            if not valid_mermin:
                                break
                        if not valid_mermin:
                            continue
                        if len(set(shared)) != 10:
                            continue

                        # Final parity check
                        parity = parity_ijkm + (1 if signs[p] == -1 else 0)
                        if parity % 2 == 0:
                            continue

                        mermin_count += 1

                        # Classify
                        clique = (i, j, k, m, p)
                        fano_points = []
                        for idx in clique:
                            _, lag_idx, _ = contexts[idx]
                            L = lagrangians[lag_idx]
                            inter = L & V_SET
                            if len(inter) == 1:
                                v = next(iter(inter))
                                fano_points.append(FANO_LABEL[(v[0], v[1], v[2])])
                            elif len(inter) == 0:
                                fano_points.append(0)
                            else:
                                fano_points.append(-1)

                        nonzero = [x for x in fano_points if x > 0]
                        distinct = len(set(nonzero))
                        transverse = fano_points.count(0)

                        if transverse == 0 and distinct == 5:
                            type_str = "A"
                        elif transverse == 0 and distinct == 4:
                            type_str = "B"
                        elif transverse == 0 and distinct == 3:
                            type_str = "C"
                        elif transverse == 0 and distinct == 2:
                            type_str = "D"
                        elif transverse == 0 and distinct == 1:
                            type_str = "E"
                        elif transverse > 0:
                            type_str = f"F{transverse}"
                        else:
                            type_str = "X"

                        type_counts[type_str] += 1

                        if type_str == "A" and len(type_a_data) < 100:
                            coll = analyze_collinearity(fano_points)
                            clique_signs = [signs[idx] for idx in clique]
                            type_a_data.append({
                                'fano_points': fano_points,
                                'signs': clique_signs,
                                'collinear_triples': coll,
                            })

                        if mermin_count % 2000 == 0:
                            elapsed = time.time() - t1
                            print(f"  {mermin_count} found ({elapsed:.1f}s)")

    print(f"\n  Total: {mermin_count} Mermin pentagrams ({time.time()-t1:.1f}s)")

    # Results
    print(f"\n{'='*70}")
    print("Mermin Pentagram Type Classification")
    print(f"{'='*70}")
    print(f"{'Type':<20} {'Count':>8} {'Fraction':>10}")
    print("-" * 40)
    total = mermin_count
    for t in sorted(type_counts.keys()):
        count = type_counts[t]
        frac = count / total * 100
        print(f"{t:<20} {count:>8} {frac:>9.2f}%")
    print(f"{'TOTAL':<20} {total:>8}")

    # Type A analysis
    print(f"\n{'='*70}")
    print(f"Type A Mermin Pentagrams: {len(type_a_data)} samples")
    print(f"{'='*70}")

    if type_a_data:
        coll_groups = defaultdict(list)
        for d in type_a_data:
            coll_groups[len(d['collinear_triples'])].append(d)

        print(f"\nCollinear triple distribution (sample):")
        for nc in sorted(coll_groups.keys()):
            print(f"  {nc} collinear triples: {len(coll_groups[nc])} samples")

        # Show one example from each collinear group
        for nc in sorted(coll_groups.keys()):
            group = coll_groups[nc]
            print(f"\n  Example ({nc} collinear triple(s)):")
            d = group[0]
            print(f"    Fano points: {d['fano_points']}")
            print(f"    Signs: {d['signs']} ({sum(1 for s in d['signs'] if s == -1)} minus)")
            print(f"    Collinear triples: {d['collinear_triples']}")

            # Check: do the collinear contexts correspond to the -I signs?
            # Map Fano points to context indices
            fp_to_ctx = {}
            for idx_in_clique, fp in enumerate(d['fano_points']):
                fp_to_ctx[fp] = idx_in_clique

            print(f"    Collinear context signs:")
            for triple in d['collinear_triples']:
                ctx_indices = [fp_to_ctx[p] for p in triple]
                ctx_signs = [d['signs'][ci] for ci in ctx_indices]
                print(f"      {triple} -> signs {ctx_signs} (product: {ctx_signs[0]*ctx_signs[1]*ctx_signs[2]})")

    print(f"\nTotal time: {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
