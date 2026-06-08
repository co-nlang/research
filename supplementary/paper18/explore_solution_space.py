#!/usr/bin/env python3
"""
Paper XVIII: Explore the 4-element solution space of ω-vectors.

For a proper K₅ in Sp(8,F₂):
- 10 rays satisfy rank=8 → exactly 2 F₂-linear relations R₁, R₂.
- Applying ω(v_k, R_α) = 0 gives 20 linear constraints on 15 cross-context ω values.
- Rank = 13 → 2 free variables → 4 candidate ω-vectors.

Question: Among the 4 candidates, which is realized? What are their Σ_m values?
If ALL Σ_m = 0 is always realized: rank=8 ALGEBRAICALLY selects the Σ=0 solution.
If not always: rank=8 alone is insufficient; more geometric input needed.
"""
import sys, time, random
from itertools import combinations

N_K5 = int(sys.argv[1]) if len(sys.argv) > 1 else 50
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 42

N = 4; DIM = 8; _SZ = 256; _MSK = 15
random.seed(SEED); t0 = time.time()

_PN = [bin(i).count('1') & 1 for i in range(16)]
_XT = [[_PN[i & j] for j in range(16)] for i in range(16)]
def symp(v, w):
    return _XT[v & _MSK][(w >> N) & _MSK] ^ _XT[(v >> N) & _MSK][w & _MSK]

def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)): s ^= basis[i] if (mask >> i) & 1 else 0
        if s: span.add(s)
    return span

ALL_VEC = list(range(1, _SZ))
def random_lagrangian():
    basis = []; span = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands: return None
        v = random.choice(cands); basis.append(v); span = xor_span(basis)
    return frozenset(span)

lag_set = set(); lags = []
while len(lags) < 500:
    lag = random_lagrangian()
    if lag and lag not in lag_set: lag_set.add(lag); lags.append(lag)

adj = [set() for _ in range(len(lags))]
for i in range(len(lags)):
    for j in range(i+1, len(lags)):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)

# All cross-context pairs (15 total), indexed 0..14
PAIRS = []
pair_idx = {}
for m in range(5):
    others = sorted(x for x in range(5) if x != m)
    a,b,c,d = others
    for p1, p2 in [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]:
        if (p1, p2) not in pair_idx and (p2, p1) not in pair_idx:
            pair_idx[(p1, p2)] = len(PAIRS)
            PAIRS.append((p1, p2))

def get_pair_idx(p1, p2):
    if (p1, p2) in pair_idx: return pair_idx[(p1, p2)]
    return pair_idx[(p2, p1)]

# Σ_m as function of ω-vector
def sigma_m(m, omega_vec, shared):
    others = sorted(x for x in range(5) if x != m)
    a,b,c,d = others
    pairs = [((a,b),(c,d)), ((a,c),(b,d)), ((a,d),(b,c))]
    result = 0
    for p1, p2 in pairs:
        idx = get_pair_idx(p1, p2)
        result ^= omega_vec[idx]
    return result

print(f"Solution space explorer  n=4  N_K5={N_K5}  seed={SEED}", flush=True)

# Summary: for each K₅, how many of the 4 candidates have all Σ_m=0?
cand_sigma_patterns = {}   # (pattern of Σ values for each candidate) → count
realized_is_allzero = 0
realized_sigmas = {}

n_k5 = 0; done = False
n_lag = len(lags)

for i in range(n_lag):
    if done: break
    ai = adj[i]
    for j in ai:
        if j<=i or done: continue
        for k in (ai & adj[j]):
            if k<=j or done: continue
            for l in (ai & adj[j] & adj[k]):
                if l<=k or done: continue
                for m in (ai & adj[j] & adj[k] & adj[l]):
                    if m<=l: continue
                    five = [lags[x] for x in (i,j,k,l,m)]
                    shared = {}
                    ok = True
                    for a in range(5):
                        for b in range(a+1, 5):
                            inter = five[a] & five[b]
                            if len(inter) != 1: ok = False; break
                            shared[(a,b)] = next(iter(inter))
                        if not ok: break
                    if not ok or len(set(shared.values())) != 10: continue

                    # Index the 10 rays as a list
                    ray_list = []
                    ray_to_idx = {}
                    for a2 in range(5):
                        for b2 in range(a2+1, 5):
                            ray_to_idx[(a2,b2)] = len(ray_list)
                            ray_list.append(shared[(a2,b2)])

                    # Find the 2 linear relations via null space of 10×8 matrix
                    # Build matrix M: rows = rays as 8-bit vectors
                    # Use Gaussian elimination over F₂
                    rows = [ray_list[r] for r in range(10)]
                    # Each row is an 8-bit integer
                    # Augmented matrix for null space: [M | I_10]
                    # We want to find vectors in null space of M^T (i.e., row relations)

                    # Build 8×10 matrix (columns = rays)
                    mat = [[0]*10 for _ in range(8)]
                    for col, v in enumerate(rows):
                        for bit in range(8):
                            mat[bit][col] = (v >> bit) & 1

                    # Gaussian elimination to find null space (relations among columns)
                    # Work with 10×8 matrix (rows=rays, cols=bits)
                    M = [[( rows[r] >> bit ) & 1 for bit in range(8)] for r in range(10)]
                    # Augmented: M | I_10
                    aug = [M[r][:] + [1 if c==r else 0 for c in range(10)] for r in range(10)]

                    pivot_cols = []
                    row_ptr = 0
                    for col in range(8):
                        # Find pivot
                        pivot = None
                        for r in range(row_ptr, 10):
                            if aug[r][col] == 1:
                                pivot = r; break
                        if pivot is None: continue
                        aug[row_ptr], aug[pivot] = aug[pivot], aug[row_ptr]
                        for r in range(10):
                            if r != row_ptr and aug[r][col] == 1:
                                aug[r] = [(aug[r][c] ^ aug[row_ptr][c]) for c in range(18)]
                        pivot_cols.append(col)
                        row_ptr += 1

                    # rank should be 8; null space rows are aug[8] and aug[9]
                    relations = []
                    for r in range(row_ptr, 10):
                        rel = aug[r][8:]  # the identity part = coefficients of relation
                        if any(rel): relations.append(rel)

                    if len(relations) != 2:
                        continue  # skip degenerate cases

                    # Now build the constraint matrix for the 15 ω values.
                    # For each relation rel, for each ray v_k (not in rel or any):
                    # sum_{j: rel[j]=1} ω(v_k, v_j) = 0
                    # where same-context ω = 0 (automatically)

                    # Enumerate cross-context pairs with their indices
                    # pair_to_xidx maps (pair_ab, pair_cd) → index in 0..14
                    xpairs = []
                    xpair_idx = {}
                    for a2 in range(5):
                        for b2 in range(a2+1, 5):
                            for c2 in range(5):
                                for d2 in range(c2+1, 5):
                                    if {a2,b2} & {c2,d2}: continue
                                    key = ((a2,b2),(c2,d2))
                                    rkey = ((c2,d2),(a2,b2))
                                    if key not in xpair_idx and rkey not in xpair_idx:
                                        xpair_idx[key] = len(xpairs)
                                        xpairs.append(key)
                    # 15 cross-context pairs

                    # For each relation × each ray: generate constraint row (length 15)
                    constraints = []
                    for rel in relations:
                        rel_support = [ri for ri in range(10) if rel[ri] == 1]
                        # For each ray v_k:
                        for k in range(10):
                            ab_k = [(a2,b2) for a2 in range(5) for b2 in range(a2+1,5)
                                    if ray_to_idx[(a2,b2)] == k][0]
                            row = [0]*15
                            for ri in rel_support:
                                if ri == k: continue
                                ab_r = [(a2,b2) for a2 in range(5) for b2 in range(a2+1,5)
                                        if ray_to_idx[(a2,b2)] == ri][0]
                                # Check if cross-context
                                if set(ab_k) & set(ab_r): continue  # same-context → 0
                                key = (ab_k, ab_r) if ab_k < ab_r else (ab_r, ab_k)
                                if key not in xpair_idx:
                                    key2 = (ab_r, ab_k) if ab_r < ab_k else (ab_k, ab_r)
                                    if key2 in xpair_idx: key = key2
                                if key in xpair_idx:
                                    row[xpair_idx[key]] ^= 1
                            if any(row):
                                constraints.append(row)

                    # Gaussian elimination on constraint matrix to find solution space
                    # We want: find all x ∈ F₂^15 satisfying Ax = 0
                    cmat = [row[:] for row in constraints]
                    pivots = []
                    rp = 0
                    for col in range(15):
                        piv = None
                        for r in range(rp, len(cmat)):
                            if cmat[r][col]: piv = r; break
                        if piv is None: continue
                        cmat[rp], cmat[piv] = cmat[piv], cmat[rp]
                        for r in range(len(cmat)):
                            if r != rp and cmat[r][col]:
                                cmat[r] = [cmat[r][c] ^ cmat[rp][c] for c in range(15)]
                        pivots.append(col)
                        rp += 1

                    free_vars = [c for c in range(15) if c not in pivots]
                    rank_c = len(pivots)

                    # Generate the 4 solutions (2^|free_vars| if |free_vars|=2)
                    n_free = len(free_vars)
                    solutions = []
                    for mask in range(1 << n_free):
                        x = [0]*15
                        for fi, fv in enumerate(free_vars):
                            x[fv] = (mask >> fi) & 1
                        # Back-substitute
                        for pi, pc in reversed(list(enumerate(pivots))):
                            val = 0
                            for c in range(15):
                                if c != pc:
                                    val ^= cmat[pi][c] * x[c]
                            x[pc] = val
                        solutions.append(tuple(x))

                    # The actual ω values for this K₅
                    actual_omega = [0]*15
                    for xi, (p1, p2) in enumerate(xpairs):
                        r1 = shared[p1] if p1 in shared else shared[(p1[1],p1[0])]
                        r2 = shared[p2] if p2 in shared else shared[(p2[1],p2[0])]
                        actual_omega[xi] = symp(r1, r2)
                    actual_omega = tuple(actual_omega)

                    # Compute Σ_m for each solution
                    # Σ_m = XOR of the 3 pairs in matching m
                    matching_pairs = {}
                    for mm in range(5):
                        others = sorted(x for x in range(5) if x != mm)
                        a2,b2,c2,d2 = others
                        pp = [((a2,b2),(c2,d2)), ((a2,c2),(b2,d2)), ((a2,d2),(b2,c2))]
                        matching_pairs[mm] = pp

                    def sigmas_for_sol(sol):
                        s = []
                        for mm in range(5):
                            v = 0
                            for p1, p2 in matching_pairs[mm]:
                                key = (p1, p2) if (p1,p2) in xpair_idx else (p2, p1)
                                v ^= sol[xpair_idx[key]]
                            s.append(v)
                        return tuple(s)

                    sol_sigmas = [sigmas_for_sol(s) for s in solutions]
                    actual_sigmas = sigmas_for_sol(actual_omega)

                    # Check if actual is in solutions
                    actual_in_space = actual_omega in solutions

                    # Record
                    key2 = tuple(sorted(set(sol_sigmas)))
                    cand_sigma_patterns[key2] = cand_sigma_patterns.get(key2, 0) + 1

                    sig_tuple = tuple(actual_sigmas)
                    realized_sigmas[sig_tuple] = realized_sigmas.get(sig_tuple, 0) + 1
                    if all(s == 0 for s in actual_sigmas):
                        realized_is_allzero += 1

                    if n_k5 < 3:
                        print(f"\nK₅ #{n_k5+1}:")
                        print(f"  Constraint rank: {rank_c}  Free vars: {free_vars}")
                        print(f"  {len(solutions)} candidates:")
                        for si, (sol, sigs) in enumerate(zip(solutions, sol_sigmas)):
                            marker = " ← ACTUAL" if sol == actual_omega else ""
                            print(f"    cand {si}: Σ_m = {list(sigs)}{marker}")
                        print(f"  Actual in solution space: {actual_in_space}")

                    n_k5 += 1
                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Summary over {n_k5} K₅s ({time.time()-t0:.1f}s) ──")
print(f"  Realized ω-vector is all-Σ=0: {realized_is_allzero}/{n_k5}")
print(f"\n  Realized Σ patterns:")
for sig, cnt in sorted(realized_sigmas.items(), key=lambda x: -x[1]):
    print(f"    Σ={list(sig)}: {cnt} K₅s")

print(f"\n  Candidate Σ-pattern sets per K₅ (what the 4 candidates look like):")
for pat, cnt in sorted(cand_sigma_patterns.items(), key=lambda x: -x[1]):
    print(f"    {[list(p) for p in pat]}: {cnt} K₅s")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
