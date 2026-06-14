"""n=8 confirmation of the even/odd dichotomy (Paper XXI seed).

Random-Lagrangian search is too slow in Sp(16,F2), so we sample proper K5 via the
symmetric-matrix chart: a Lagrangian transverse to L_inf is L_S = {(x, Sx)} for a
symmetric S over F2.  Then
    L_{S_i} cap L_{S_j} = ker(S_i + S_j)   (over F2, - = +),
so "proper K5" (all pairwise dim-1) <=> five symmetric 8x8 matrices whose ten
pairwise sums S_i+S_j each have rank n-1 = 7.  mu and na are Sp-invariant, so this
chart is a valid sampler (it realises configs sharing the common transversal L_inf).

EXPECTATION if the dichotomy holds at n=8 (even):
  - Part B: mu == 1 on all 10 triples (rank-parity theorem, even n).
  - Part A: FAILS -> odd n_m present, N_anti both parities.
"""
import random
from itertools import combinations
from collections import Counter
from nerve_cochain import build

N = 8
MSK = (1 << N) - 1
symp, _gen, _k5s, mu_triple = build(N)

def parity(z): return bin(z).count('1') & 1

def matvec(rows, x):
    """(M x)_i = parity(row_i & x), returned as a bitmask over output coords."""
    r = 0
    for i in range(N):
        if parity(rows[i] & x): r |= (1 << i)
    return r

def kernel_size(rows):
    return sum(1 for x in range(1 << N) if matvec(rows, x) == 0)

def rank(rows):
    k = kernel_size(rows)                 # = 2^(N-rank)
    return N - (k.bit_length() - 1)

def ker_vector(rows):
    """unique nonzero kernel vector when rank == N-1."""
    for x in range(1, 1 << N):
        if matvec(rows, x) == 0: return x
    return None

def rand_sym(rng):
    rows = [0] * N
    for i in range(N):
        for j in range(i, N):
            if rng.getrandbits(1):
                rows[i] |= (1 << j); rows[j] |= (1 << i)
    return rows

def diff(A, B): return [A[i] ^ B[i] for i in range(N)]

def lift(rows):
    """L_S as a frozenset of nonzero encoded vectors: x in low N bits, Sx in high N bits."""
    return frozenset((x | (matvec(rows, x) << N)) for x in range(1, 1 << N))

def build_config(rng, max_attempts=4000):
    mats = []
    for _ in range(max_attempts):
        if len(mats) == 5: break
        S = rand_sym(rng)
        if all(rank(diff(S, T)) == N - 1 for T in mats):
            mats.append(S)
    if len(mats) != 5: return None
    # rays v_ij = ker(S_i+S_j) lifted; require all 10 distinct (proper)
    sh = {}
    for i in range(5):
        for j in range(i + 1, 5):
            k = ker_vector(diff(mats[i], mats[j]))
            sh[(i, j)] = k | (matvec(mats[i], k) << N)
    if len(set(sh.values())) != 10: return None
    return [lift(S) for S in mats], sh

def run(nconfig, seed0=4242):
    rng = random.Random(seed0)
    tot = 0; mu_all_one = 0; na_eq_dmu = 0
    na_dist = Counter(); nanti_vals = Counter(); nanti_parity = Counter()
    attempts = 0
    while tot < nconfig and attempts < nconfig * 50:
        attempts += 1
        cfg = build_config(rng)
        if cfg is None: continue
        five, sh = cfg
        tot += 1
        ray = {(a, b): sh[(a, b)] for a in range(5) for b in range(a + 1, 5)}
        na = []
        for m in range(5):
            rest = [x for x in range(5) if x != m]; a, b, c, dd = rest
            prs = [((a, b), (c, dd)), ((a, c), (b, dd)), ((a, dd), (b, c))]
            na.append(sum(1 for (p, q) in prs
                          if symp(ray[tuple(sorted(p))], ray[tuple(sorted(q))])))
        for v in na: na_dist[v] += 1
        Nanti = sum(na); nanti_vals[Nanti] += 1; nanti_parity[Nanti % 2] += 1
        mu = {t: mu_triple(five[t[0]], five[t[1]], five[t[2]])
              for t in combinations(range(5), 3)}
        if all(v == 1 for v in mu.values()): mu_all_one += 1
        dmu = [sum(mu[f] for f in combinations(tuple(x for x in range(5) if x != m), 3)) % 2
               for m in range(5)]
        if all((na[m] % 2) == dmu[m] for m in range(5)): na_eq_dmu += 1
    print(f"  n={N}: proper K5 sampled = {tot}  (from {attempts} attempts)")
    print(f"    Part B  -- mu==1 on all 10 triples: {mu_all_one}/{tot}")
    print(f"    per-matching na value distribution: {dict(sorted(na_dist.items()))}")
    print(f"    N_anti value distribution: {dict(sorted(nanti_vals.items()))}")
    print(f"    N_anti parity (0=even,1=odd): {dict(nanti_parity)}")
    print(f"    na_m == (delta mu)_m for all m: {na_eq_dmu}/{tot}")
    print(f"    => Part A (n_m even per matching): "
          f"{'HOLDS' if set(na_dist) <= {0,2} else 'FAILS (odd na_m present)'}")

if __name__ == "__main__":
    print("=== n=8 confirmation: even/odd dichotomy at the next even dimension ===")
    run(nconfig=150)
