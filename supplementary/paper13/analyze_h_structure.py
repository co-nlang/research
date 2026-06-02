"""
Analyze h(C) mod 2 structure for each k-type.
Break down contributions from V-points vs non-V points.
"""

import numpy as np
import itertools
from collections import Counter, defaultdict

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def symplectic_form_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def gf2_rank(vectors):
    if not vectors: return 0
    mat = np.array(vectors, dtype=int)
    rows, cols = mat.shape
    r = 0
    for c in range(cols):
        pivot = None
        for row in range(r, rows):
            if mat[row, c] == 1:
                pivot = row
                break
        if pivot is None: continue
        mat[[r, pivot]] = mat[[pivot, r]]
        for row in range(r+1, rows):
            if mat[row, c] == 1:
                mat[row] = (mat[row] + mat[r]) % 2
        r += 1
    return r

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
    for i in range(len(pts)):
        for j in range(i+1, len(pts)):
            s = tuple((pts[i][k] + pts[j][k]) % 2 for k in range(6))
            if s in lag_points and s != (0,0,0,0,0,0):
                lines.add(frozenset([pts[i], pts[j], s]))
    return list(lines)

def k_type(lag):
    return sum(1 for p in lag if p[3]==0 and p[4]==0 and p[5]==0)

def is_v_point(p):
    return p[3]==0 and p[4]==0 and p[5]==0

def main():
    print("Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians\n")

    print("=== Context structure by k-type ===\n")

    for kt in [0, 1, 3, 7]:
        lags_of_type = [lag for lag in lagrangians if k_type(lag) == kt]
        if not lags_of_type: continue
        print(f"k={kt}: {len(lags_of_type)} Lagrangians")

        h_values = []
        v_in_context = Counter()
        for lag in lags_of_type:
            pts = list(lag)
            v_pts = [p for p in pts if is_v_point(p)]
            fano_lines = get_fano_lines(lag)
            for line in fano_lines:
                ctx_pts = [p for p in pts if p not in line]
                if len(ctx_pts) != 4: continue
                n_v_in_ctx = sum(1 for p in ctx_pts if is_v_point(p))
                v_in_context[n_v_in_ctx] += 1

                beta = 0
                for j in range(4):
                    for k in range(j+1, 4):
                        beta += omega_int(ctx_pts[j], ctx_pts[k])
                h = beta // 2
                h_values.append((h, h % 2, n_v_in_ctx))

        print(f"  Contexts: {len(h_values)}")
        print(f"  V-points in context: {dict(v_in_context)}")

        h_mod2_by_v = defaultdict(Counter)
        for h, hmod2, nv in h_values:
            h_mod2_by_v[nv][hmod2] += 1

        print(f"  h mod 2 by V-count:")
        for nv in sorted(h_mod2_by_v.keys()):
            c = h_mod2_by_v[nv]
            print(f"    {nv} V-points: h=0:{c[0]}, h=1:{c[1]}, P(h=1)={c[1]/(c[0]+c[1]):.3f}")

        h_range = [h for h, _, _ in h_values]
        print(f"  h range: min={min(h_range)}, max={max(h_range)}, distinct={len(set(h_range))}")
        print()

if __name__ == "__main__":
    main()
