#!/usr/bin/env python3
"""
Paper XIII: Maslov Index Computation for Equiangular Lagrangian Cycles
Optimized version with precomputation and sampling.
"""

import itertools
import numpy as np
from collections import Counter, defaultdict

# ─── GF(2) Linear Algebra ───

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

# ─── Symplectic Forms ───

def omega_mod2(u, v):
    return (u[0]*v[3] + u[1]*v[4] + u[2]*v[5] +
            u[3]*v[0] + u[4]*v[1] + u[5]*v[2]) % 2

def omega_int(a, b):
    return (a[0]*b[3] + a[1]*b[4] + a[2]*b[5] -
            a[3]*b[0] - a[4]*b[1] - a[5]*b[2])

# ─── Lagrangian Enumeration ───

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

# ─── Kashiwara Triple Index (optimized) ───

def kashiwara_triple_fast(L_a, L_b, L_c, L_sum_ab=None):
    """Kashiwara index for triple (L_a, L_b, L_c). Precomputed L_sum_ab optional."""
    if L_sum_ab is None:
        L_sum_ab = frozenset(add_mod2(a, b) for a in L_a for b in L_b)
    W = L_sum_ab & L_c
    W_list = [w for w in W if w != (0,)*6]
    if not W_list:
        return 0, 0, []
    
    # Compute Q on W
    Q = {}
    for w in W_list:
        for u in L_a:
            v = add_mod2(w, u)
            if v in L_b:
                Q[w] = omega_int(u, v)
                break
    
    # Find basis
    basis = []
    spanned = {(0,)*6}
    for w in W_list:
        if w not in spanned:
            basis.append(w)
            spanned = spanned | {add_mod2(s, w) for s in spanned}
            if len(basis) >= 3: break
    
    n = len(basis)
    if n == 0: return 0, 0, []
    
    # Build integer matrix M
    M = np.zeros((n, n), dtype=float)
    for i in range(n):
        M[i, i] = Q.get(basis[i], 0)
        for j in range(i+1, n):
            s = add_mod2(basis[i], basis[j])
            cross = Q.get(s, 0) - Q.get(basis[i], 0) - Q.get(basis[j], 0)
            M[i, j] = cross / 2.0
            M[j, i] = cross / 2.0
    
    eigenvalues = np.linalg.eigvalsh(M)
    sig = sum(1 for e in eigenvalues if e > 1e-10) - sum(1 for e in eigenvalues if e < -1e-10)
    return sig, n, [Q.get(b, 0) for b in basis]


def kashiwara_ref_fast(L_a, L_b, L_ref, L_sum_bref=None):
    """μ(L_a, L_b, L_ref): W = L_a ∩ (L_b + L_ref)."""
    if L_sum_bref is None:
        L_sum_bref = frozenset(add_mod2(b, r) for b in L_b for r in L_ref)
    W = L_a & L_sum_bref
    W_list = [w for w in W if w != (0,)*6]
    if not W_list: return 0
    
    Q = {}
    for w in W_list:
        for u in L_b:
            v = add_mod2(w, u)
            if v in L_ref:
                Q[w] = omega_int(u, v)
                break
    
    basis = []
    spanned = {(0,)*6}
    for w in W_list:
        if w not in spanned:
            basis.append(w)
            spanned = spanned | {add_mod2(s, w) for s in spanned}
    
    n = len(basis)
    if n == 0: return 0
    M = np.zeros((n, n), dtype=float)
    for i in range(n):
        M[i, i] = Q.get(basis[i], 0)
        for j in range(i+1, n):
            s = add_mod2(basis[i], basis[j])
            cross = Q.get(s, 0) - Q.get(basis[i], 0) - Q.get(basis[j], 0)
            M[i, j] = cross / 2.0; M[j, i] = cross / 2.0
    eigenvalues = np.linalg.eigvalsh(M)
    return sum(1 for e in eigenvalues if e > 1e-10) - sum(1 for e in eigenvalues if e < -1e-10)


# ─── Main ───

def main():
    import time
    t0 = time.time()
    print("=" * 70)
    print("Paper XIII: Maslov Index for Equiangular Lagrangian Cycles")
    print("=" * 70)
    
    print("\n[1/5] Enumerating Lagrangians...")
    lagrangians = find_lagrangians()
    n_lag = len(lagrangians)
    print(f"  {n_lag} Lagrangians ({time.time()-t0:.1f}s)")
    
    print("[2/5] Generating contexts...")
    all_contexts = generate_contexts(lagrangians)
    n_ctx = len(all_contexts)
    print(f"  {n_ctx} proper contexts ({time.time()-t0:.1f}s)")
    
    # Precompute context β values
    print("[3/5] Precomputing context β values...")
    context_betas = []
    for ci in range(n_ctx):
        pts = list(all_contexts[ci][1])
        beta = 0
        for j in range(4):
            for k in range(j+1, 4):
                beta += omega_int(pts[j], pts[k])
        context_betas.append(beta)
    print(f"  Done ({time.time()-t0:.1f}s)")
    
    # Precompute pairwise Lagrangian sums (for Kashiwara)
    print("[4/5] Precomputing Lagrangian pairwise sums...")
    lag_sums = {}
    for i in range(n_lag):
        for j in range(i, n_lag):
            s = frozenset(add_mod2(a, b) for a in lagrangians[i] for b in lagrangians[j])
            lag_sums[(i, j)] = s
            lag_sums[(j, i)] = s
    print(f"  {len(lag_sums)//2} pairs ({time.time()-t0:.1f}s)")
    
    # Build pentagrams (optimized 5-nested-loop)
    print("[5/5] Building pentagrams and computing Maslov candidates...")
    adj = defaultdict(list)
    for i in range(n_ctx):
        for j in range(i + 1, n_ctx):
            if len(all_contexts[i][1] & all_contexts[j][1]) == 1:
                adj[i].append(j); adj[j].append(i)
    
    SAMPLE_SIZE = 500
    results = []
    pent_count = 0
    seen_pents = set()
    
    for i in range(n_ctx):
        if pent_count >= SAMPLE_SIZE: break
        for j in adj[i]:
            if j <= i or pent_count >= SAMPLE_SIZE: continue
            for k in adj[j]:
                if k <= j or k not in adj[i] or pent_count >= SAMPLE_SIZE: continue
                for m in adj[k]:
                    if m <= k or m not in adj[i] or m not in adj[j] or pent_count >= SAMPLE_SIZE: continue
                    for p in adj[m]:
                        if p <= m or p not in adj[i] or p not in adj[j] or p not in adj[k]: continue
                        if pent_count >= SAMPLE_SIZE: break
                        clique = [i, j, k, m, p]
                        all_ops = set()
                        for ci in clique: all_ops |= all_contexts[ci][1]
                        if len(all_ops) != 10: continue
                        
                        pent_key = tuple(sorted(clique))
                        if pent_key in seen_pents: continue
                        seen_pents.add(pent_key)
                        
                        lag_idx = [all_contexts[c][0] for c in clique]
                        if len(set(lag_idx)) != 5: continue
                        
                        pent_count += 1
                        Ls = [lagrangians[li] for li in lag_idx]
                        
                        # β_sum
                        beta_sum = sum(context_betas[ci] for ci in clique)
                        
                        # Extract intersection rays
                        rays = {}
                        for a in range(5):
                            for b in range(a+1, 5):
                                shared = all_contexts[clique[a]][1] & all_contexts[clique[b]][1]
                                if shared: rays[(a,b)] = next(iter(shared))
                        
                        # Σ_all_rays: sum of ω_int over all 45 ray pairs
                        rays_list = list(rays.values())
                        sigma_all = 0
                        for ri in range(10):
                            for rj in range(ri+1, 10):
                                sigma_all += omega_int(rays_list[ri], rays_list[rj])
                        
                        # Σ_sharing: sum of ω_int over 30 sharing pairs (= β_sum)
                        # Σ_disjoint: sum of ω_int over 15 disjoint pairs
                        sigma_disjoint = sigma_all - beta_sum
                        
                        # Σ_consec_intersection: ω_int between consecutive intersection rays
                        sigma_consec = 0
                        for ci in range(5):
                            cj = (ci + 1) % 5
                            ck = (ci + 2) % 5
                            r_ij = rays.get((min(ci,cj), max(ci,cj)), rays.get((min(cj,ci), max(cj,ci))))
                            r_jk = rays.get((min(cj,ck), max(cj,ck)), rays.get((min(ck,cj), max(ck,cj))))
                            if r_ij and r_jk:
                                sigma_consec += omega_int(r_ij, r_jk)
                        
                        # Kashiwara consecutive triples
                        kash_sigs = []
                        for ci in range(5):
                            a, b, c = ci, (ci+1)%5, (ci+2)%5
                            la, lb, lc = lag_idx[a], lag_idx[b], lag_idx[c]
                            ls_ab = lag_sums.get((la, lb))
                            sig, wdim, qvals = kashiwara_triple_fast(Ls[a], Ls[b], Ls[c], ls_ab)
                            kash_sigs.append(sig)
                        kash_sum = sum(kash_sigs)
                        
                        # Kashiwara with reference = L_1
                        kash_ref_sum = 0
                        ref_idx = lag_idx[0]
                        for ci in range(5):
                            cj = (ci + 1) % 5
                            la, lb = lag_idx[ci], lag_idx[cj]
                            ls = lag_sums.get((lb, ref_idx))
                            sig = kashiwara_ref_fast(Ls[ci], Ls[cj], Ls[0], ls)
                            kash_ref_sum += sig
                        
                        # Kashiwara with reference = lagrangians[0] (V)
                        kash_V_sum = 0
                        V = lagrangians[0]
                        for ci in range(5):
                            cj = (ci + 1) % 5
                            la, lb = lag_idx[ci], lag_idx[cj]
                            ls = lag_sums.get((lb, 0))
                            sig = kashiwara_ref_fast(Ls[ci], Ls[cj], V, ls)
                            kash_V_sum += sig
                        
                        # Candidate: Σ ω_int / 2 over Lagrangian intersection rays
                        sigma_lag_rays = 0
                        for a in range(5):
                            for b in range(a+1, 5):
                                r = rays.get((a, b))
                                if r:
                                    # Sum ω_int between this ray and all other intersection rays
                                    pass
                        # Actually: sum of ω_int(r_ab, r_cd) for all pairs of Lagrangian pairs
                        sigma_lag_pairs = 0
                        ray_keys = list(rays.keys())
                        for ri in range(len(ray_keys)):
                            for rj in range(ri+1, len(ray_keys)):
                                r1 = rays[ray_keys[ri]]
                                r2 = rays[ray_keys[rj]]
                                sigma_lag_pairs += omega_int(r1, r2)
                        # This is the same as sigma_all
                        
                        # Half-integer candidates
                        half_beta = beta_sum // 2
                        half_sigma_disjoint = sigma_disjoint  # always odd
                        
                        results.append({
                            'beta_sum': beta_sum,
                            'sigma_all': sigma_all,
                            'sigma_disjoint': sigma_disjoint,
                            'sigma_consec': sigma_consec,
                            'kash_consec': kash_sum,
                            'kash_sigs': kash_sigs,
                            'kash_ref': kash_ref_sum,
                            'kash_V': kash_V_sum,
                            'lag_idx': lag_idx,
                        })
    
    N = len(results)
    print(f"  {N} pentagrams sampled ({time.time()-t0:.1f}s)")
    
    # ─── Results ───
    print("\n" + "=" * 70)
    print(f"RESULTS ({N} pentagrams)")
    print("=" * 70)
    
    print(f"\n--- β_sum distribution ---")
    bc = Counter(r['beta_sum'] for r in results)
    for val, cnt in sorted(bc.items()):
        print(f"  β_sum = {val:4d} (mod4={val%4}): {cnt} ({100*cnt/N:.1f}%)")
    
    print(f"\n--- σ_disjoint (= σ_all - β_sum, 15 disjoint pairs) ---")
    dc = Counter(r['sigma_disjoint'] for r in results)
    for val, cnt in sorted(dc.items())[:10]:
        print(f"  σ_disj = {val:4d}: {cnt}")
    if len(dc) > 10: print(f"  ... ({len(dc)} distinct values)")
    
    print(f"\n--- σ_consec (5 consecutive intersection ray pairs) ---")
    cc = Counter(r['sigma_consec'] for r in results)
    for val, cnt in sorted(cc.items())[:10]:
        print(f"  σ_consec = {val:4d}: {cnt}")
    if len(cc) > 10: print(f"  ... ({len(cc)} distinct values)")
    
    print(f"\n--- Kashiwara consecutive triples (sum of 5) ---")
    kc = Counter(r['kash_consec'] for r in results)
    for val, cnt in sorted(kc.items()):
        print(f"  Σμ = {val:4d}: {cnt} ({100*cnt/N:.1f}%)")
    
    print(f"\n--- Kashiwara with ref = L_1 ---")
    kr = Counter(r['kash_ref'] for r in results)
    for val, cnt in sorted(kr.items())[:15]:
        print(f"  Σμ_ref = {val:4d}: {cnt} ({100*cnt/N:.1f}%)")
    if len(kr) > 15: print(f"  ... ({len(kr)} distinct values)")
    
    print(f"\n--- Kashiwara with ref = V ---")
    kv = Counter(r['kash_V'] for r in results)
    for val, cnt in sorted(kv.items())[:15]:
        print(f"  Σμ_V = {val:4d}: {cnt} ({100*cnt/N:.1f}%)")
    if len(kv) > 15: print(f"  ... ({len(kv)} distinct values)")
    
    # Match checks
    print(f"\n--- Match: β_sum = 2μ? ---")
    for name, key in [("Consec triples", 'kash_consec'), ("Ref L_1", 'kash_ref'), ("Ref V", 'kash_V')]:
        n_match = sum(1 for r in results if r['beta_sum'] == 2 * r[key])
        print(f"  {name:20s}: {n_match}/{N} ({100*n_match/N:.1f}%)")
    
    # Additional: check β_sum = 2μ + constant
    print(f"\n--- β_sum - 2μ distribution ---")
    for name, key in [("Consec triples", 'kash_consec'), ("Ref L_1", 'kash_ref'), ("Ref V", 'kash_V')]:
        diff = Counter(r['beta_sum'] - 2*r[key] for r in results)
        print(f"  {name}: {dict(sorted(diff.items())[:8])}")
        if len(diff) > 8: print(f"    ... ({len(diff)} distinct values)")
    
    # Check if σ_disjoint relates to β_sum
    print(f"\n--- β_sum + σ_disjoint = σ_all ---")
    sa = Counter(r['sigma_all'] for r in results)
    for val, cnt in sorted(sa.items())[:10]:
        print(f"  σ_all = {val:4d}: {cnt}")
    if len(sa) > 10: print(f"  ... ({len(sa)} distinct values)")
    
    # Individual Kashiwara triple signatures
    print(f"\n--- Individual triple signature distribution ---")
    all_sigs = []
    for r in results:
        all_sigs.extend(r['kash_sigs'])
    sc = Counter(all_sigs)
    for val, cnt in sorted(sc.items()):
        print(f"  μ = {val:4d}: {cnt} ({100*cnt/len(all_sigs):.1f}%)")
    
    # Detailed standard pentagram analysis
    print(f"\n--- First pentagram detailed ---")
    if results:
        r = results[0]
        print(f"  β_sum = {r['beta_sum']}")
        print(f"  σ_all = {r['sigma_all']}")
        print(f"  σ_disjoint = {r['sigma_disjoint']}")
        print(f"  σ_consec = {r['sigma_consec']}")
        print(f"  Kashiwara consec: sigs={r['kash_sigs']}, sum={r['kash_consec']}")
        print(f"  Kashiwara ref L_1: {r['kash_ref']}")
        print(f"  Kashiwara ref V: {r['kash_V']}")
        print(f"  Lagrangian indices: {r['lag_idx']}")
    
    print(f"\nTotal time: {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
