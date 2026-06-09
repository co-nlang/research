"""Part A (n_m even per matching) is n=4-EXCLUSIVE: verifying the B1/B2 hinges.

Part A at n=4 = XVIII B1 (<=1 commuting pairing) AND B2 (>=1 commuting pairing),
so every matching has exactly 1 commuting pairing (n_m = 2 anti).  Both lemmas hinge
on 2n=8:
  B1: S={v_ab,v_ac,v_bd,v_cd} isotropic dim 4 is LAGRANGIAN  <=>  n=4.
  B2: W=span(6 rays) non-degenerate dim 6 has W^perp of dim 2 (3 nonzero) <=> n=4.

This script, over proper K4 (4 symmetric NxN matrices, pairwise sum rank N-1):
 1. tabulates #commuting pairings per matching by N  (expect: N=4 -> always 1;
    N>=5 -> 0,1,2,3 all occur, i.e. B1 AND B2 both fail);
 2. on an N>=5 witness with >=2 commuting pairings, checks the B1 hinge directly:
    span(S) is isotropic of dim 4 but NOT Lagrangian, and the escaping rays
    v_ad,v_bc lie in S^perp \\ S.
"""
import random
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def parity(z): return bin(z).count('1') & 1

def make(N):
    MSK = (1 << N) - 1
    symp, *_ = build(N)
    def matvec(rows, x):
        r = 0
        for i in range(N):
            if parity(rows[i] & x): r |= (1 << i)
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
    def diff(A, B): return [A[i] ^ B[i] for i in range(N)]
    def encode(x, rows): return x | (matvec(rows, x) << N)

    def k4(rng, tries=4000):
        mats = []
        for _ in range(tries):
            if len(mats) == 4: break
            S = rand_sym(rng)
            if all(rank(diff(S, T)) == N-1 for T in mats): mats.append(S)
        if len(mats) != 4: return None
        ray = {}
        for i in range(4):
            for j in range(i+1, 4):
                k = ker_vec(diff(mats[i], mats[j]))
                ray[(i, j)] = encode(k, mats[i])
        if len(set(ray.values())) != 6: return None
        return mats, ray

    # F2 span dim of a set of vectors (ints)
    def spandim(vs):
        basis = []
        for v in vs:
            for b in basis: v = min(v, v ^ b)
            if v: basis.append(v); basis.sort(reverse=True)
        return len(basis)
    return symp, k4, spandim

def tabulate(N, nconfig, seed0=7):
    symp, k4, _ = make(N)
    rng = random.Random(seed0 + N)
    comm = Counter(); tot = 0; att = 0
    while tot < nconfig and att < nconfig*60:
        att += 1
        r = k4(rng)
        if r is None: continue
        _, ray = r; tot += 1
        pairings = [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]
        c = sum(1 for (p,q) in pairings if symp(ray[p], ray[q]) == 0)
        comm[c] += 1
    print(f"  N={N}: proper K4 sampled={tot}  #commuting-pairings dist={dict(sorted(comm.items()))}"
          f"   B1-fail(>=2):{sum(v for k,v in comm.items() if k>=2)}"
          f"  B2-fail(=0):{comm.get(0,0)}")

def hinge_witness(N, seed0=7):
    """find a K4 with >=2 commuting pairings and check the B1 hinge."""
    symp, k4, spandim = make(N)
    rng = random.Random(100 + seed0 + N)
    for _ in range(20000):
        r = k4(rng)
        if r is None: continue
        _, ray = r
        pairings = [((0,1),(2,3)), ((0,2),(1,3)), ((0,3),(1,2))]
        comm = [(p,q) for (p,q) in pairings if symp(ray[p], ray[q]) == 0]
        if len(comm) >= 2:
            # S = the four rays in the two commuting pairings (they coincide on indices)
            Svecs = set()
            for (p,q) in comm[:2]: Svecs |= {ray[p], ray[q]}
            Svecs = list(Svecs)
            d = spandim(Svecs)
            iso = all(symp(u, w) == 0 for u in Svecs for w in Svecs)
            # the two "escaping" rays = the rays NOT in S
            escaping = [ray[k] for k in ray if ray[k] not in set(Svecs)]
            # membership of escaping rays in span(S):  in-span iff spandim(S+v)==spandim(S)
            in_S = [spandim(Svecs + [v]) == d for v in escaping]
            # perp-membership: v in S^perp iff ω(v, s)=0 for all s in S
            in_perp = [all(symp(v, s) == 0 for s in Svecs) for v in escaping]
            print(f"  N={N} witness: {len(comm)} commuting pairings; |S|={len(Svecs)}, "
                  f"dim span(S)={d}, isotropic={iso}")
            print(f"    Lagrangian(dim==n)? {d == N}    (n={N})")
            print(f"    escaping rays in span(S)? {in_S}   in S^perp? {in_perp}")
            print(f"    => escaping rays are in S^perp \\ S: "
                  f"{all(p and not s for p, s in zip(in_perp, in_S))}")
            return
    print(f"  N={N}: no >=2-commuting K4 found in budget")

if __name__ == "__main__":
    print("=== Part A is n=4-exclusive: #commuting pairings per matching ===")
    for N in (3, 4, 5, 6):
        tabulate(N, nconfig=300 if N <= 5 else 200)
    print("\n=== B1 hinge on an n>=5 witness (>=2 commuting pairings) ===")
    for N in (5, 6):
        hinge_witness(N)
