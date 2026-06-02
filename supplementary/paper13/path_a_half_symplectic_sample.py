"""
Path A (optimized): Analyze h_i = β(C_i)/2 mod 2 for each context.
Sample 500 pentagrams for speed.
"""

import numpy as np
import itertools
import random
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
    v_points = [p for p in lag if p[3]==0 and p[4]==0 and p[5]==0]
    return len(v_points)

def compute_beta(context_points):
    pts = list(context_points)
    beta = 0
    for j in range(len(pts)):
        for k in range(j+1, len(pts)):
            beta += omega_int(pts[j], pts[k])
    return beta

def main():
    print("Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    print(f"  {len(lagrangians)} Lagrangians")

    all_contexts = []
    ctx_lag_idx = []
    ctx_k_type = []
    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        fano_lines = get_fano_lines(lag)
        kt = k_type(lag)
        for line in fano_lines:
            ctx_pts = frozenset(p for p in pts if p not in line)
            if len(ctx_pts) != 4: continue
            all_contexts.append(ctx_pts)
            ctx_lag_idx.append(li)
            ctx_k_type.append(kt)
    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts")

    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i+1, n_ctx):
            shared = all_contexts[i] & all_contexts[j]
            if len(shared) == 1:
                adj[i].append(j); adj[j].append(i)

    print("Finding Mermin pentagrams (sampling 500)...")
    mermin_pentagrams = []
    found = 0
    for start in range(n_ctx):
        if found >= 500: break
        for c2 in adj[start]:
            if found >= 500: break
            if c2 <= start: continue
            for c3 in adj[c2]:
                if found >= 500: break
                if c3 <= start or c3 == start: continue
                if start not in adj[c3]: continue
                for c4 in adj[c3]:
                    if found >= 500: break
                    if c4 <= start or c4 in (start, c2, c3): continue
                    if start not in adj[c4] or c2 not in adj[c4]: continue
                    for c5 in adj[c4]:
                        if found >= 500: break
                        if c5 <= start or c5 in (start, c2, c3, c4): continue
                        if (start in adj[c5] and c2 in adj[c5] and c3 in adj[c5]):
                            clique = tuple(sorted([start, c2, c3, c4, c5]))
                            all_rays = set()
                            for ci in clique:
                                all_rays |= all_contexts[ci]
                            if len(all_rays) != 10: continue

                            context_betas = {}
                            for ci in clique:
                                beta = compute_beta(all_contexts[ci])
                                context_betas[ci] = beta
                            b_sum = sum(context_betas[ci] for ci in clique)
                            if b_sum % 4 != 2: continue

                            if clique not in mermin_pentagrams:
                                mermin_pentagrams.append(clique)
                                found += 1

    print(f"  {len(mermin_pentagrams)} Mermin pentagrams (sample)")

    print("\n=== Path A: h_i mod 2 vs k-type ===\n")

    h_mod2_by_k = defaultdict(lambda: Counter())
    h_values_by_k = defaultdict(list)

    for pent in mermin_pentagrams:
        for ci in pent:
            li = ctx_lag_idx[ci]
            kt = ctx_k_type[ci]
            beta = compute_beta(all_contexts[ci])
            h = beta // 2
            h_mod2 = h % 2
            h_mod2_by_k[kt][h_mod2] += 1
            h_values_by_k[kt].append(h)

    print("h_i = β(C_i)/2 distribution by k-type:")
    print(f"{'k-type':>8} {'h=0 mod 2':>12} {'h=1 mod 2':>12} {'total':>8} {'P(h=1)':>8}")
    print("-" * 52)
    for kt in sorted(h_mod2_by_k.keys()):
        c = h_mod2_by_k[kt]
        total = c[0] + c[1]
        p1 = c[1] / total if total > 0 else 0
        print(f"{kt:>8} {c[0]:>12} {c[1]:>12} {total:>8} {p1:>8.3f}")

    print("\n=== h_i value range by k-type ===\n")
    for kt in sorted(h_values_by_k.keys()):
        vals = h_values_by_k[kt]
        print(f"k={kt}: min={min(vals)}, max={max(vals)}, "
              f"distinct={len(set(vals))}, mean={np.mean(vals):.1f}")

    print("\n=== Per-pentagram: Σhᵢ by k-profile ===\n")

    kprofile_hsum = defaultdict(lambda: Counter())
    for pent in mermin_pentagrams:
        kprofile = tuple(sorted(ctx_k_type[ci] for ci in pent))
        h_sum = 0
        for ci in pent:
            beta = compute_beta(all_contexts[ci])
            h_sum += beta // 2
        kprofile_hsum[kprofile][h_sum % 2] += 1

    print(f"{'k-profile':>25} {'Σh=0':>8} {'Σh=1':>8} {'total':>8}")
    print("-" * 55)
    for kp in sorted(kprofile_hsum.keys()):
        c = kprofile_hsum[kp]
        total = c[0] + c[1]
        print(f"{str(kp):>25} {c[0]:>8} {c[1]:>8} {total:>8}")

    print("\n=== Is Σhᵢ mod 2 determined by k-profile? ===")
    determined = all(c[0] == 0 or c[1] == 0 for c in kprofile_hsum.values())
    print(f"  {'YES' if determined else 'NO'}")

    if not determined:
        print("\n  Mixed k-profiles (both parities occur):")
        for kp in sorted(kprofile_hsum.keys()):
            c = kprofile_hsum[kp]
            if c[0] > 0 and c[1] > 0:
                print(f"    {kp}: even={c[0]}, odd={c[1]}")

    print("\n=== Per-pentagram h_i pattern ===\n")
    h_pattern_counter = Counter()
    for pent in mermin_pentagrams:
        h_mod2_pattern = tuple(
            (compute_beta(all_contexts[ci]) // 2) % 2
            for ci in pent
        )
        h_pattern_counter[h_mod2_pattern] += 1

    print(f"Distinct (h₁ mod 2, ..., h₅ mod 2) patterns: {len(h_pattern_counter)}")
    print("\nTop 15 patterns:")
    for pat, cnt in h_pattern_counter.most_common(15):
        n_ones = sum(pat)
        print(f"  {pat} (sum={n_ones}): {cnt} pentagrams")

    print("\n=== Sum of h_i mod 2 pattern ===")
    pattern_sum = Counter()
    for pat, cnt in h_pattern_counter.items():
        pattern_sum[sum(pat) % 2] += cnt
    print(f"  Σhᵢ mod 2 = 0: {pattern_sum[0]} pentagrams")
    print(f"  Σhᵢ mod 2 = 1: {pattern_sum[1]} pentagrams")

if __name__ == "__main__":
    main()
