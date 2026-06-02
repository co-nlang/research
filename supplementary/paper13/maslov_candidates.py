#!/usr/bin/env python3
"""
Paper XIII: Alternative Maslov index candidates.
Tests whether β_sum/2 equals various integer quantities.
"""

import itertools
import numpy as np
from collections import Counter, defaultdict

def add_mod2(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))

def gf2_rank(vectors):
    if not vectors: return 0
    M = np.array(vectors, dtype=int) % 2
    rows, cols = M.shape
    r = 0
    for c in range(cols):
        pivot = -1
        for row in range(r, rows):
            if M[row, c] % 2 == 1: pivot = row; break
        if pivot == -1: continue
        M[[r, pivot]] = M[[pivot, r]]
        for row in range(rows):
            if row != r and M[row, c] % 2 == 1:
                M[row] = (M[row] + M[r]) % 2
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

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

def Q_form(v):
    return v[0]*v[3] + v[1]*v[4] + v[2]*v[5]

def omega_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

ALL_POINTS = [tuple(int(x) for x in format(i, '06b')) for i in range(1, 64)]

def find_lagrangians():
    lagrangians, seen = [], set()
    for basis in itertools.combinations(ALL_POINTS, 3):
        if gf2_rank(basis) < 3: continue
        if not all(omega_mod2(u, v) == 0 for u, v in itertools.combinations(basis, 2)): continue
        subspace = span_subspace(basis)
        if subspace not in seen:
            seen.add(subspace); lagrangians.append(subspace)
    return lagrangians

def get_fano_lines(lag_points):
    pts = list(lag_points); lines = set()
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            s = add_mod2(pts[i], pts[j])
            if s in lag_points:
                lines.add(frozenset([pts[i], pts[j], s]))
    return list(lines)

def generate_contexts(lagrangians):
    all_contexts = []
    for li, lag in enumerate(lagrangians):
        pts = list(lag)
        for line in get_fano_lines(lag):
            ctx_pts = frozenset(p for p in pts if p not in line)
            if len(ctx_pts) == 4:
                all_contexts.append((li, ctx_pts))
    return all_contexts

def main():
    import time
    t0 = time.time()
    
    lagrangians = find_lagrangians()
    all_contexts = generate_contexts(lagrangians)
    n_ctx = len(all_contexts)
    print(f"{len(lagrangians)} Lagrangians, {n_ctx} contexts ({time.time()-t0:.1f}s)")
    
    # Precompute context β values
    context_betas = []
    for ci in range(n_ctx):
        pts = list(all_contexts[ci][1])
        beta = sum(omega_int(pts[j], pts[k]) for j in range(4) for k in range(j+1, 4))
        context_betas.append(beta)
    
    # Precompute Lagrangian sums
    lag_sums = {}
    n_lag = len(lagrangians)
    for i in range(n_lag):
        for j in range(i, n_lag):
            s = frozenset(add_mod2(a, b) for a in lagrangians[i] for b in lagrangians[j])
            lag_sums[(i, j)] = s; lag_sums[(j, i)] = s
    
    # Build adjacency
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i][1] & all_contexts[j][1]) == 1:
                adj[i].append(j); adj[j].append(i)
    
    SAMPLE = 500
    results = []
    seen = set()
    pent_count = 0
    
    for i in range(n_ctx):
        if pent_count >= SAMPLE: break
        for j in adj[i]:
            if j <= i or pent_count >= SAMPLE: continue
            for k in adj[j]:
                if k <= j or k not in adj[i] or pent_count >= SAMPLE: continue
                for m in adj[k]:
                    if m <= k or m not in adj[i] or m not in adj[j] or pent_count >= SAMPLE: continue
                    for p in adj[m]:
                        if p <= m or p not in adj[i] or p not in adj[j] or p not in adj[k]: continue
                        if pent_count >= SAMPLE: break
                        clique = [i, j, k, m, p]
                        all_ops = set()
                        for ci in clique: all_ops |= all_contexts[ci][1]
                        if len(all_ops) != 10: continue
                        pent_key = tuple(sorted(clique))
                        if pent_key in seen: continue
                        seen.add(pent_key)
                        lag_idx = [all_contexts[c][0] for c in clique]
                        if len(set(lag_idx)) != 5: continue
                        pent_count += 1
                        
                        Ls = [lagrangians[li] for li in lag_idx]
                        beta_sum = sum(context_betas[ci] for ci in clique)
                        
                        # Extract rays
                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]][1] & all_contexts[clique[b]][1]
                                if shared: rays[(a,b)] = next(iter(shared))
                        
                        # Q_sum: sum of Q(r) over all 10 rays
                        Q_sum = sum(Q_form(r) for r in rays.values())
                        
                        # Candidate A: sum of ω_int over ALL nonzero w in each W_ijk
                        # using lex-smallest decomposition
                        sum_W_omega = 0
                        for ci in range(5):
                            a, b, c = ci, (ci+1)%5, (ci+2)%5
                            la, lb = lag_idx[a], lag_idx[b]
                            W = lag_sums[(la, lb)] & Ls[c]
                            for w in W:
                                if w == (0,)*6: continue
                                # Find lex-smallest u ∈ L_a with w-u ∈ L_b
                                best_u = None
                                for u in sorted(Ls[a]):
                                    v = add_mod2(w, u)
                                    if v in Ls[b]:
                                        best_u = u; break
                                if best_u is not None:
                                    v = add_mod2(w, best_u)
                                    sum_W_omega += omega_int(best_u, v)
                        
                        # Candidate B: sum of ω_int(r_ac, r_bc) for consecutive triples
                        sum_ray_triple = 0
                        for ci in range(5):
                            a, b, c = ci, (ci+1)%5, (ci+2)%5
                            r_ac = rays.get((min(a,c), max(a,c)))
                            r_bc = rays.get((min(b,c), max(b,c)))
                            if r_ac and r_bc:
                                sum_ray_triple += omega_int(r_ac, r_bc)
                        
                        # Candidate C: sum of ω_int(r_ij, r_jk) for consecutive edges
                        sum_consec_rays = 0
                        for ci in range(5):
                            cj = (ci+1)%5
                            ck = (ci+2)%5
                            r_ij = rays.get((min(ci,cj), max(ci,cj)))
                            r_jk = rays.get((min(cj,ck), max(cj,ck)))
                            if r_ij and r_jk:
                                sum_consec_rays += omega_int(r_ij, r_jk)
                        
                        # Candidate D: sum of ω_int over all 10 disjoint ray pairs
                        sigma_disjoint = 0
                        ray_keys = list(rays.keys())
                        for ri in range(len(ray_keys)):
                            for rj in range(ri+1, len(ray_keys)):
                                k1, k2 = ray_keys[ri], ray_keys[rj]
                                if len(set(k1) & set(k2)) == 0:  # disjoint edges in K5
                                    sigma_disjoint += omega_int(rays[k1], rays[k2])
                        
                        # Candidate E: sum of Q over all 10 rays
                        # (already computed as Q_sum)
                        
                        # Candidate F: β_sum + 2*Q_sum
                        F_val = beta_sum + 2 * Q_sum
                        
                        # Candidate G: (β_sum + σ_disjoint) / 2 = σ_all / 2
                        sigma_all = beta_sum + sigma_disjoint
                        
                        # Candidate H: sum of ω_int(r_ij, r_kl) for ALL pairs of
                        # intersection rays where (ij) and (kl) share exactly one vertex
                        sum_sharing_rays = 0
                        for ri in range(len(ray_keys)):
                            for rj in range(ri+1, len(ray_keys)):
                                k1, k2 = ray_keys[ri], ray_keys[rj]
                                if len(set(k1) & set(k2)) == 1:  # sharing edge in K5
                                    sum_sharing_rays += omega_int(rays[k1], rays[k2])
                        
                        results.append({
                            'beta_sum': beta_sum,
                            'half_beta': beta_sum // 2,
                            'Q_sum': Q_sum,
                            'sum_W_omega': sum_W_omega,
                            'sum_ray_triple': sum_ray_triple,
                            'sum_consec_rays': sum_consec_rays,
                            'sigma_disjoint': sigma_disjoint,
                            'sigma_all': sigma_all,
                            'sum_sharing_rays': sum_sharing_rays,
                            'F_val': F_val,
                        })
    
    N = len(results)
    print(f"{N} pentagrams ({time.time()-t0:.1f}s)")
    
    print("\n" + "=" * 70)
    print("CANDIDATE MATCHES FOR β_sum/2")
    print("=" * 70)
    
    candidates = [
        ('sum_W_omega', 'sum_W_omega'),
        ('sum_ray_triple', 'sum_ray_triple'),
        ('sum_consec_rays', 'sum_consec_rays'),
        ('sigma_disjoint', 'sigma_disjoint'),
        ('sigma_all/2', None),  # special
        ('sum_sharing_rays', 'sum_sharing_rays'),
        ('Q_sum', 'Q_sum'),
        ('(β+2Q)/2', None),  # special
    ]
    
    for name, key in candidates:
        if key:
            n_match = sum(1 for r in results if r['half_beta'] == r[key])
            vals = Counter(r[key] for r in results)
        elif name == 'sigma_all/2':
            n_match = sum(1 for r in results if r['sigma_all'] % 2 == 0 and r['half_beta'] == r['sigma_all'] // 2)
            vals = Counter(r['sigma_all'] // 2 for r in results if r['sigma_all'] % 2 == 0)
        elif name == '(β+2Q)/2':
            n_match = sum(1 for r in results if r['F_val'] % 2 == 0 and r['half_beta'] == r['F_val'] // 2)
            vals = Counter(r['F_val'] // 2 for r in results if r['F_val'] % 2 == 0)
        
        print(f"\n  {name}:")
        print(f"    Match β_sum/2: {n_match}/{N} ({100*n_match/N:.1f}%)")
        top = sorted(vals.items())[:8]
        print(f"    Distribution: {dict(top)}")
        if len(vals) > 8: print(f"    ... ({len(vals)} distinct)")
    
    # Check linear relations
    print("\n" + "=" * 70)
    print("LINEAR RELATIONS WITH β_sum/2")
    print("=" * 70)
    
    half_betas = [r['half_beta'] for r in results]
    for name, key in [('sum_W_omega', 'sum_W_omega'), ('Q_sum', 'Q_sum'),
                       ('sum_ray_triple', 'sum_ray_triple'), ('sigma_disjoint', 'sigma_disjoint')]:
        vals = [r[key] for r in results]
        # Check if half_beta = a*val + b for some a, b
        diffs = [h - v for h, v in zip(half_betas, vals)]
        diff_counter = Counter(diffs)
        print(f"\n  β_sum/2 - {name}:")
        print(f"    Constant? {len(diff_counter) == 1}")
        print(f"    Distribution: {dict(sorted(diff_counter.items())[:8])}")
        if len(diff_counter) > 8: print(f"    ... ({len(diff_counter)} distinct)")
        
        # Check if half_beta ≡ val (mod n) for small n
        for mod in [2, 3, 4]:
            n_mod = sum(1 for h, v in zip(half_betas, vals) if h % mod == v % mod)
            print(f"    ≡ mod {mod}: {n_mod}/{N} ({100*n_mod/N:.1f}%)")
    
    # Detailed first 5 pentagrams
    print("\n" + "=" * 70)
    print("FIRST 5 PENTAGRAMS (detailed)")
    print("=" * 70)
    for i, r in enumerate(results[:5]):
        print(f"\n  Pentagram {i+1}:")
        print(f"    β_sum = {r['beta_sum']}, β/2 = {r['half_beta']}")
        print(f"    Q_sum = {r['Q_sum']}")
        print(f"    sum_W_omega = {r['sum_W_omega']}")
        print(f"    sum_ray_triple = {r['sum_ray_triple']}")
        print(f"    sum_consec_rays = {r['sum_consec_rays']}")
        print(f"    σ_disjoint = {r['sigma_disjoint']}")
        print(f"    σ_all = {r['sigma_all']}")
        print(f"    sum_sharing_rays = {r['sum_sharing_rays']}")
    
    print(f"\nTotal time: {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
