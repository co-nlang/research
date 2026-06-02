"""
Analyze correlation between h_i values in pentagrams.
Check if h-pattern is determined by k-profile.
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

def main():
    print("Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    all_contexts = []
    ctx_k_type = []
    ctx_beta = []
    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        kt = k_type(lag)
        for line in fano_lines:
            ctx_pts = frozenset(p for p in pts if p not in line)
            if len(ctx_pts) != 4: continue
            beta = 0
            cp = list(ctx_pts)
            for j in range(4):
                for k in range(j+1, 4):
                    beta += omega_int(cp[j], cp[k])
            all_contexts.append(ctx_pts)
            ctx_k_type.append(kt)
            ctx_beta.append(beta)
    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts\n")

    from collections import defaultdict
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i+1, n_ctx):
            if len(all_contexts[i] & all_contexts[j]) == 1:
                adj[i].append(j); adj[j].append(i)

    print("Finding Mermin pentagrams (sampling 500)...")
    import random
    random.seed(42)
    mermin_pentagrams = []
    seen_cliques = set()
    attempts = 0
    while len(mermin_pentagrams) < 500 and attempts < 100000:
        attempts += 1
        start = random.randint(0, n_ctx-1)
        if len(adj[start]) < 4: continue
        clique = [start]
        candidates = adj[start]
        for _ in range(4):
            if not candidates: break
            c = random.choice(candidates)
            clique.append(c)
            candidates = [x for x in candidates if x in adj[c] and x not in clique]
        if len(clique) != 5: continue
        clique_tuple = tuple(sorted(clique))
        if clique_tuple in seen_cliques: continue
        all_rays = set()
        for ci in clique:
            all_rays |= all_contexts[ci]
        if len(all_rays) != 10: continue
        b_sum = sum(ctx_beta[ci] for ci in clique)
        if b_sum % 4 != 2: continue
        seen_cliques.add(clique_tuple)
        mermin_pentagrams.append(clique_tuple)
    print(f"  {len(mermin_pentagrams)} pentagrams\n")

    print("=== h-pattern analysis by k-profile ===\n")

    kprofile_hpattern = defaultdict(lambda: Counter())
    for pent in mermin_pentagrams:
        kprofile = tuple(sorted(ctx_k_type[ci] for ci in pent))
        h_pattern = tuple(ctx_beta[ci] // 2 % 2 for ci in pent)
        kprofile_hpattern[kprofile][h_pattern] += 1

    for kp in sorted(kprofile_hpattern.keys()):
        patterns = kprofile_hpattern[kp]
        total = sum(patterns.values())
        print(f"k-profile {kp}: {total} pentagrams, {len(patterns)} distinct h-patterns")
        for pat, count in sorted(patterns.items(), key=lambda x: -x[1])[:5]:
            print(f"  {pat} (sum={sum(pat)}): {count}")
        if len(patterns) > 5:
            print(f"  ... and {len(patterns)-5} more")
        print()

if __name__ == "__main__":
    main()
