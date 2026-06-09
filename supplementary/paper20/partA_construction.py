"""Closing Part A's n>=5 direction: an EXPLICIT proper K5 with odd N_anti for every n>=5.

Spread-stabilization lemma:  if (L_0..L_4) is a proper K5 in Sp(2n,F2) and (U_0..U_4)
are 5 pairwise-transverse Lagrangians in Sp(2m,F2), then (L_i (+) U_i) is a proper K5 in
Sp(2(n+m),F2) with the SAME ray Gram matrix -> same N_anti and every n_m.  Pairwise:
(L_i(+)U_i) cap (L_j(+)U_j) = (L_i cap L_j) (+) (U_i cap U_j) = <v_ij> (+) 0 (dim 1); rays
stay in the Sp(2n) block so the form between them is unchanged.  5 pairwise-transverse
Lagrangians exist in Sp(2m,F2) for all m>=2 (spreads, size 2^m+1).

So: explicit odd-N_anti witnesses at n=5 and n=6, stabilized by m>=2, give an explicit
proper K5 with the same odd N_anti at every n>=5.  This script verifies all of it.

Vectors are (x,z) pairs of bitmasks; the symplectic form is block-diagonal under direct
sum, so symp is width-independent:  symp((x,z),(x',z')) = <x,z'> + <z,x'> (mod 2).
"""
import random
from itertools import combinations

def symp(a, b):
    return (bin(a[0] & b[1]).count('1') + bin(a[1] & b[0]).count('1')) & 1

# ---- F2 symmetric-matrix machinery (chart Lagrangians L_S = {(x, Sx)}) ----
def parity(z): return bin(z).count('1') & 1
def matvec(rows, x, n):
    r = 0
    for i in range(n):
        if parity(rows[i] & x): r |= 1 << i
    return r
def ker_size(rows, n): return sum(1 for x in range(1 << n) if matvec(rows, x, n) == 0)
def rank(rows, n): return n - (ker_size(rows, n).bit_length() - 1)
def ker_vec(rows, n):
    for x in range(1, 1 << n):
        if matvec(rows, x, n) == 0: return x
def rand_sym(n, rng):
    rows = [0]*n
    for i in range(n):
        for j in range(i, n):
            if rng.getrandbits(1): rows[i] |= 1 << j; rows[j] |= 1 << i
    return rows
def diffm(A, B): return [A[i] ^ B[i] for i in range(len(A))]
def lag_chart(rows, n):
    """L_S as a list of (x,z) pairs, z = Sx."""
    return [(x, matvec(rows, x, n)) for x in range(1 << n)]
def lag_inf(n):
    """L_inf = {(0,z)} as (x,z) list."""
    return [(0, z) for z in range(1 << n)]

# ---- proper K5 with odd N_anti at dim n, via the symmetric chart ----
def find_oddK5(n, rng, tries=20000):
    for _ in range(tries):
        mats = []
        for _ in range(4000):
            if len(mats) == 5: break
            S = rand_sym(n, rng)
            if all(rank(diffm(S, T), n) == n-1 for T in mats): mats.append(S)
        if len(mats) != 5: continue
        ray = {}
        for i in range(5):
            for j in range(i+1, 5):
                k = ker_vec(diffm(mats[i], mats[j]), n)
                ray[(i, j)] = (k, matvec(mats[i], k, n))
        if len(set(ray.values())) != 10: continue  # need 10 distinct rays
        Nanti = nanti(ray)
        if Nanti % 2 == 1:
            return [lag_chart(S, n) for S in mats], ray, Nanti
    return None

def nanti(ray):
    pairs = []
    for (i, j) in combinations(range(5), 2):
        for (k, l) in combinations(range(5), 2):
            if (i, j) < (k, l) and len({i, j, k, l}) == 4:
                pairs.append(((i, j), (k, l)))
    return sum(symp(ray[p], ray[q]) for (p, q) in pairs)

# ---- 5 pairwise-transverse Lagrangians (a partial spread) in Sp(2m,F2) ----
def transverse_set(m, rng, need=5, tries=20000):
    """L_inf plus chart Lagrangians whose pairwise differences are nonsingular."""
    for _ in range(tries):
        mats = []
        for _ in range(6000):
            if len(mats) == need - 1: break
            S = rand_sym(m, rng)
            if all(rank(diffm(S, T), m) == m for T in mats): mats.append(S)
        if len(mats) == need - 1:
            Us = [lag_inf(m)] + [lag_chart(S, m) for S in mats]
            return Us
    return None

# ---- direct-sum stabilization ----
def combine(Li, Ui, n):
    """L_i (+) U_i over n+m coords: L uses bits 0..n-1, U uses bits n.. ."""
    return [((lx | (ux << n)), (lz | (uz << n))) for (lx, lz) in Li for (ux, uz) in Ui]

def proper_and_nanti(lags):
    """verify pairwise dim-1 (intersection = exactly {0, ray}) and return rays + N_anti."""
    ray = {}
    for (i, j) in combinations(range(5), 2):
        inter = set(map(tuple, lags[i])) & set(map(tuple, lags[j]))
        inter.discard((0, 0))
        if len(inter) != 1:
            return None, None  # not proper (dim != 1)
        ray[(i, j)] = next(iter(inter))
    if len(set(ray.values())) != 10:
        return None, None
    return ray, nanti(ray)

def stabilize(baseL, n, m, rng):
    Us = transverse_set(m, rng)
    assert Us is not None, f"no 5 pairwise-transverse Lagrangians in Sp({2*m})"
    return [combine(baseL[i], Us[i], n) for i in range(5)]

if __name__ == "__main__":
    rng = random.Random(20260609)
    print("=== explicit odd-N_anti proper K5 witnesses ===")
    bases = {}
    for n in (5, 6):
        res = find_oddK5(n, rng)
        assert res is not None, f"no odd witness at n={n}"
        baseL, ray, Na = res
        bases[n] = baseL
        print(f"  n={n}: found proper K5 with N_anti={Na} (ODD)")

    print("\n=== spread stabilization preserves properness and N_anti ===")
    # n=5 base -> 7,8,9 ; n=6 base -> 8,9,10  (covers all n>=5 together with bases)
    plan = [(5, 2), (5, 3), (5, 4), (6, 2), (6, 3), (6, 4)]
    for (n, m) in plan:
        # recompute base N_anti
        _, Na0 = proper_and_nanti(bases[n])
        lags = stabilize(bases[n], n, m, rng)
        ray, Na = proper_and_nanti(lags)
        ok = ray is not None
        print(f"  n={n} (+) m={m} -> dim {n+m}: proper={ok}, "
              f"N_anti {Na0} -> {Na}  "
              f"[{'PRESERVED, ODD' if ok and Na == Na0 and Na%2==1 else 'MISMATCH'}]")
