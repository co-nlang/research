"""Ladder vs truncation: does the anticommutation obstruction reach H^4 on K6?

Nerve of N Lagrangians = boundary of (N-1)-simplex ~ S^{N-2}, with nontrivial
cohomology only in degree 0 and N-2.  K5 -> S^3 (H^3); K6 -> S^4 (H^4).

But anticommutation is a 4-INDEX datum (a disjoint pair {v_ij,v_kl} uses 4 indices),
hence intrinsically a 3-COCHAIN on the nerve, whatever N is.  On S^3 (K5) degree 3 is
TOP -> genuine H^3 (= N_anti mod 2).  On S^4 (K6) degree 3 is SUB-top -> H^3(S^4)=0 ->
forced exact.  The natural degree-4 cochain assembled from the six sub-K5 classes,
c_m = N_anti(face_m) mod 2, pairs with [S^4] as  sum_m c_m  = sum over disjoint pairs
of (#faces containing the pair) = 2 * (...) = 0.  So [c]=0 in H^4 always: the six
sub-pentagram H^3 classes cancel and never build an H^4 obstruction => TRUNCATION.

This script tests, via the symmetric-matrix chart sampler (6 symmetric NxN matrices,
pairwise sum rank N-1, 15 distinct rays):
  (1) proper K6 exist;
  (2) the sub-face classes c_m individually VARY (degree-3 obstruction alive);
  (3) A4 = sum_m c_m == 0 ALWAYS (no degree-4 obstruction).
"""
import random
from itertools import combinations
from collections import Counter

def parity(z): return bin(z).count('1') & 1
def symp(a, b):  # a=(x,z), b=(x',z')
    return (parity(a[0] & b[1]) ^ parity(a[1] & b[0]))

def make(N):
    def matvec(rows, x):
        r = 0
        for i in range(N):
            if parity(rows[i] & x): r |= 1 << i
        return r
    def ker_size(rows): return sum(1 for x in range(1 << N) if matvec(rows, x) == 0)
    def rank(rows): return N - (ker_size(rows).bit_length() - 1)
    def ker_vec(rows):
        for x in range(1, 1 << N):
            if matvec(rows, x) == 0: return x
    def rand_sym(rng):
        rows = [0]*N
        for i in range(N):
            for j in range(i, N):
                if rng.getrandbits(1): rows[i] |= 1 << j; rows[j] |= 1 << i
        return rows
    def dm(A, B): return [A[i] ^ B[i] for i in range(N)]
    return matvec, rank, ker_vec, rand_sym, dm

def k6(N, rng, tries=8000):
    matvec, rank, ker_vec, rand_sym, dm = make(N)
    mats = []
    for _ in range(tries):
        if len(mats) == 6: break
        S = rand_sym(rng)
        if all(rank(dm(S, T)) == N-1 for T in mats): mats.append(S)
    if len(mats) != 6: return None
    ray = {}
    for i in range(6):
        for j in range(i+1, 6):
            k = ker_vec(dm(mats[i], mats[j]))
            ray[(i, j)] = (k, matvec(mats[i], k))      # (x, S_i x)
    if len(set(ray.values())) != 15: return None
    return ray

def disjoint_pairs(idxset):
    out = []
    s = sorted(idxset)
    for a, b, c, d in combinations(s, 4):
        out += [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
    return out

def nanti(ray, idxset):
    tot = 0
    for (p, q) in disjoint_pairs(idxset):
        tot += symp(ray[p], ray[q])
    return tot

def run(N, target, seed):
    rng = random.Random(seed)
    found = 0; att = 0
    A4 = Counter(); cvec = Counter(); cm_vals = Counter(); Mtot = Counter()
    while found < target and att < target*80:
        att += 1
        ray = k6(N, rng)
        if ray is None: continue
        found += 1
        faces = [tuple(x for x in range(6) if x != m) for m in range(6)]
        c = [nanti(ray, f) % 2 for f in faces]
        for v in c: cm_vals[v] += 1
        A4[sum(c) % 2] += 1
        cvec[tuple(c)] += 1
        Mtot[nanti(ray, range(6)) % 2] += 1
    if found == 0:
        print(f"  n={N}: NO proper K6 found in {att} attempts")
        return
    print(f"  n={N}: proper K6 sampled = {found} (from {att} attempts)  -> EXIST")
    print(f"    per-face class c_m values: {dict(sorted(cm_vals.items()))} "
          f"(both values present => degree-3 obstruction ALIVE on faces)")
    print(f"    A4 = sum_m c_m  (the H^4 pairing): {dict(sorted(A4.items()))} "
          f"{'=> ALWAYS 0: H^4 TRIVIAL (truncation)' if set(A4)=={0} else '=> NONZERO H^4!'}")
    print(f"    #distinct c-vectors seen: {len(cvec)} (sub-obstructions vary, but constrained to sum=0)")
    print(f"    total K6 anti-count parity M: {dict(sorted(Mtot.items()))} (lower-degree info, varies)")

if __name__ == "__main__":
    print("=== K6 / H^4 test: does the anticommutation obstruction climb past H^3? ===")
    for N in (4, 5, 6):
        run(N, target=200, seed=70+N)
