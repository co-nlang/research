#!/usr/bin/env python3
"""
Paper XVIII: corrected ground-truth recheck (review pass).

Fixes three defects found in the cited scripts:
  (A) check_k5_random_n.py never enforced properness (distinct rays) -> reported
      MIXED N_anti for n=4. Here ALL K5s are filtered to proper (10 distinct rays).
  (B) explore_solution_space.py never computed Gram ranks -> the "Gram rank
      selection" Key Lemma was never actually verified. Here we build G_x for
      each of the 4 candidates and compute its F2 rank, then test
      rank(G_x) in {0,8}  <->  Sigma_m = 0 for all m.
  (C) check_lower_bound.py counted all-ANTI matchings (0 commuting), which is
      vacuous under Sigma_m=0. The real failure mode for N_anti<10 is an
      all-COMMUTING matching (0 anti). Here we count both and report the
      per-matching commuting-count distribution.

Usage: python3 recheck_paper18.py
"""
import sys, time, random
from itertools import combinations
from collections import Counter


def make_symp(n):
    msk = (1 << n) - 1
    PN = [bin(i).count('1') & 1 for i in range(1 << n)]
    XT = [[PN[i & j] for j in range(1 << n)] for i in range(1 << n)]
    def symp(v, w):
        return XT[v & msk][(w >> n) & msk] ^ XT[(v >> n) & msk][w & msk]
    return symp


def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)):
            if (mask >> i) & 1:
                s ^= basis[i]
        if s:
            span.add(s)
    return span


def f2_rank(rows, ncols):
    rows = list(rows)
    rank = 0
    for col in range(ncols):
        piv = None
        for i in range(rank, len(rows)):
            if (rows[i] >> col) & 1:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and (rows[i] >> col) & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def gen_lagrangians(n, n_lag, symp, rng, hard_cap_attempts=2_000_000):
    SZ = 1 << (2 * n)
    ALL = list(range(1, SZ))
    def random_lagrangian():
        basis = []
        span = set()
        for _ in range(n):
            cands = [v for v in ALL if v not in span
                     and all(symp(v, b) == 0 for b in basis)]
            if not cands:
                return None
            v = rng.choice(cands)
            basis.append(v)
            span = xor_span(basis)
        return frozenset(span)
    seen = set()
    lags = []
    attempts = 0
    while len(lags) < n_lag and attempts < hard_cap_attempts:
        attempts += 1
        L = random_lagrangian()
        if L and L not in seen:
            seen.add(L)
            lags.append(L)
    return lags


def build_adj(lags):
    adj = [set() for _ in lags]
    for i in range(len(lags)):
        for j in range(i + 1, len(lags)):
            if len(lags[i] & lags[j]) == 1:
                adj[i].add(j)
                adj[j].add(i)
    return adj


def iter_proper_k5(lags, adj, max_k5):
    """Yield 'shared' dicts {(a,b): ray} for proper K5s (10 distinct rays)."""
    n_lag = len(lags)
    count = 0
    for i in range(n_lag):
        ai = adj[i]
        for j in ai:
            if j <= i:
                continue
            aij = ai & adj[j]
            for k in aij:
                if k <= j:
                    continue
                aijk = aij & adj[k]
                for l in aijk:
                    if l <= k:
                        continue
                    for m in (aijk & adj[l]):
                        if m <= l:
                            continue
                        five = [lags[x] for x in (i, j, k, l, m)]
                        shared = {}
                        ok = True
                        for a in range(5):
                            for b in range(a + 1, 5):
                                inter = five[a] & five[b]
                                if len(inter) != 1:
                                    ok = False
                                    break
                                shared[(a, b)] = next(iter(inter))
                            if not ok:
                                break
                        if not ok or len(set(shared.values())) != 10:
                            continue  # PROPERNESS enforced here
                        yield shared
                        count += 1
                        if count >= max_k5:
                            return


def matchings():
    out = {}
    for mm in range(5):
        others = sorted(x for x in range(5) if x != mm)
        a, b, c, d = others
        out[mm] = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
    return out
MATCH = matchings()


def cross_pairs():
    xs = []
    idx = {}
    for a in range(5):
        for b in range(a + 1, 5):
            for c in range(5):
                for d in range(c + 1, 5):
                    if {a, b} & {c, d}:
                        continue
                    key = ((a, b), (c, d))
                    if key in idx or ((c, d), (a, b)) in idx:
                        continue
                    idx[key] = len(xs)
                    xs.append(key)
    return xs, idx
XPAIRS, XIDX = cross_pairs()  # 15


def xkey(p1, p2):
    return (p1, p2) if (p1, p2) in XIDX else (p2, p1)


def omega_vec(shared, symp):
    x = [0] * 15
    for (p1, p2), e in XIDX.items():
        x[e] = symp(shared[p1], shared[p2])
    return tuple(x)


def sigmas(xvec):
    out = []
    for mm in range(5):
        v = 0
        for p1, p2 in MATCH[mm]:
            v ^= xvec[XIDX[xkey(p1, p2)]]
        out.append(v)
    return tuple(out)


def n_anti(xvec):
    return sum(xvec)


# ---------------------------------------------------------------------------
# Part 1: corrected landscape  (proper K5, n = 3,4,5,6)
# ---------------------------------------------------------------------------
def landscape(n, n_lag, max_k5, seed):
    rng = random.Random(seed)
    symp = make_symp(n)
    t0 = time.time()
    lags = gen_lagrangians(n, n_lag, symp, rng)
    adj = build_adj(lags)
    anti_dist = Counter()
    uniform = 0
    total = 0
    sig0 = 0
    for shared in iter_proper_k5(lags, adj, max_k5):
        x = omega_vec(shared, symp)
        s = sigmas(x)
        anti_dist[n_anti(x)] += 1
        total += 1
        if len(set(s)) == 1:
            uniform += 1
        if all(si == 0 for si in s):
            sig0 += 1
    return {
        "n": n, "lags": len(lags), "k5": total,
        "anti_dist": dict(sorted(anti_dist.items())),
        "uniform": uniform, "sigma0": sig0,
        "secs": time.time() - t0,
    }


# ---------------------------------------------------------------------------
# Part 2: REAL Key Lemma  (compute Gram ranks of the 4 candidates)
# ---------------------------------------------------------------------------
def candidate_omega_vectors(shared, n, symp):
    """Return (4 candidate xvecs, constraint_rank). Mirrors explore_solution_space."""
    ray_idx = {}
    rays = []
    for a in range(5):
        for b in range(a + 1, 5):
            ray_idx[(a, b)] = len(rays)
            rays.append(shared[(a, b)])
    dim = 2 * n
    # null space (relations among the 10 rays) via [M | I_10]
    aug = [[(rays[r] >> bit) & 1 for bit in range(dim)]
           + [1 if c == r else 0 for c in range(10)] for r in range(10)]
    rp = 0
    width = dim + 10
    for col in range(dim):
        piv = None
        for r in range(rp, 10):
            if aug[r][col] == 1:
                piv = r
                break
        if piv is None:
            continue
        aug[rp], aug[piv] = aug[piv], aug[rp]
        for r in range(10):
            if r != rp and aug[r][col] == 1:
                aug[r] = [aug[r][c] ^ aug[rp][c] for c in range(width)]
        rp += 1
    relations = [aug[r][dim:] for r in range(rp, 10) if any(aug[r][dim:])]
    if len(relations) != 2:
        return None, None
    # constraints on 15 omega values: for each relation, each ray k
    pos_of = {v: k for k, v in ray_idx.items()}
    constraints = []
    for rel in relations:
        supp = [ri for ri in range(10) if rel[ri] == 1]
        for k in range(10):
            ab_k = pos_of[k]
            row = [0] * 15
            for ri in supp:
                if ri == k:
                    continue
                ab_r = pos_of[ri]
                if set(ab_k) & set(ab_r):
                    continue
                row[XIDX[xkey(ab_k, ab_r)]] ^= 1
            if any(row):
                constraints.append(row)
    cmat = [r[:] for r in constraints]
    pivots = []
    rp2 = 0
    for col in range(15):
        piv = None
        for r in range(rp2, len(cmat)):
            if cmat[r][col]:
                piv = r
                break
        if piv is None:
            continue
        cmat[rp2], cmat[piv] = cmat[piv], cmat[rp2]
        for r in range(len(cmat)):
            if r != rp2 and cmat[r][col]:
                cmat[r] = [cmat[r][c] ^ cmat[rp2][c] for c in range(15)]
        pivots.append(col)
        rp2 += 1
    free = [c for c in range(15) if c not in pivots]
    sols = []
    for mask in range(1 << len(free)):
        x = [0] * 15
        for fi, fv in enumerate(free):
            x[fv] = (mask >> fi) & 1
        for pi, pc in reversed(list(enumerate(pivots))):
            val = 0
            for c in range(15):
                if c != pc:
                    val ^= cmat[pi][c] * x[c]
            x[pc] = val
        sols.append(tuple(x))
    return sols, len(pivots)


def gram_rank(xvec):
    """F2 rank of the 10x10 alternating matrix built from the candidate omega."""
    G = [0] * 10
    rid = {}
    rays = []
    for a in range(5):
        for b in range(a + 1, 5):
            rid[(a, b)] = len(rays)
            rays.append((a, b))
    for (p1, p2), e in XIDX.items():
        i, j = rid[p1], rid[p2]
        if xvec[e]:
            G[i] |= (1 << j)
            G[j] |= (1 << i)
    return f2_rank(G, 10)


def key_lemma(n, n_lag, max_k5, seed):
    rng = random.Random(seed)
    symp = make_symp(n)
    t0 = time.time()
    lags = gen_lagrangians(n, n_lag, symp, rng)
    adj = build_adj(lags)
    total_inst = 0
    exceptions = 0
    rankset_dist = Counter()
    pairs_seen = Counter()       # (rank, all_sigma_zero) -> count
    actual_rank_dist = Counter()
    k5 = 0
    for shared in iter_proper_k5(lags, adj, max_k5):
        sols, crank = candidate_omega_vectors(shared, n, symp)
        if sols is None or len(sols) != 4:
            continue
        actual = omega_vec(shared, symp)
        ranks = tuple(sorted(gram_rank(s) for s in sols))
        rankset_dist[ranks] += 1
        actual_rank_dist[gram_rank(actual)] += 1
        for s in sols:
            r = gram_rank(s)
            sig0 = all(si == 0 for si in sigmas(s))
            pairs_seen[(r, sig0)] += 1
            total_inst += 1
            # Key Lemma claim: (r in {0,8}) <-> sig0
            if (r in (0, 8)) != sig0:
                exceptions += 1
        k5 += 1
    return {
        "k5": k5, "instances": total_inst, "exceptions": exceptions,
        "rankset_dist": dict(rankset_dist),
        "actual_rank_dist": dict(sorted(actual_rank_dist.items())),
        "pairs": dict(pairs_seen),
        "secs": time.time() - t0,
    }


# ---------------------------------------------------------------------------
# Part 3: REAL value pinning  (per-matching commuting-count distribution)
# ---------------------------------------------------------------------------
def value_pin(n, n_lag, max_k5, seed):
    rng = random.Random(seed)
    symp = make_symp(n)
    t0 = time.time()
    lags = gen_lagrangians(n, n_lag, symp, rng)
    adj = build_adj(lags)
    comm_count_dist = Counter()      # commuting pairs per matching
    all_commuting = 0                # matchings with 0 anti (the real failure mode)
    all_anti = 0                     # matchings with 0 commuting (vacuous-under-sigma0)
    anti_dist = Counter()
    k5 = 0
    for shared in iter_proper_k5(lags, adj, max_k5):
        x = omega_vec(shared, symp)
        anti_dist[n_anti(x)] += 1
        for mm in range(5):
            na = sum(x[XIDX[xkey(p1, p2)]] for p1, p2 in MATCH[mm])
            nc = 3 - na
            comm_count_dist[nc] += 1
            if na == 0:
                all_commuting += 1
            if nc == 0:
                all_anti += 1
        k5 += 1
    return {
        "k5": k5, "anti_dist": dict(sorted(anti_dist.items())),
        "comm_per_matching": dict(sorted(comm_count_dist.items())),
        "all_commuting_matchings": all_commuting,
        "all_anti_matchings": all_anti,
        "secs": time.time() - t0,
    }


if __name__ == "__main__":
    print("=" * 70)
    print("PART 1 — Corrected landscape (PROPER K5 only)")
    print("=" * 70)
    cfg = [(3, 200, 200), (4, 800, 300), (5, 3000, 200), (6, 3000, 30)]
    for n, n_lag, max_k5 in cfg:
        r = landscape(n, n_lag, max_k5, 42)
        upct = 100 * r["uniform"] / r["k5"] if r["k5"] else 0
        print(f"  n={n}: K5={r['k5']:>4}  N_anti={r['anti_dist']}")
        print(f"        Sigma uniform={r['uniform']}/{r['k5']} ({upct:.0f}%)  "
              f"Sigma=0 (all m)={r['sigma0']}/{r['k5']}  ({r['secs']:.1f}s)")

    print()
    print("=" * 70)
    print("PART 2 — REAL Key Lemma: Gram rank of 4 candidates vs Sigma")
    print("=" * 70)
    r = key_lemma(4, 800, 210, 42)
    print(f"  K5={r['k5']}  instances={r['instances']}  "
          f"EXCEPTIONS to [rank in {{0,8}} <-> Sigma=0]: {r['exceptions']}")
    print(f"  actual omega Gram-rank dist: {r['actual_rank_dist']}")
    print(f"  candidate rank-multiset dist:")
    for rk, c in sorted(r["rankset_dist"].items(), key=lambda kv: -kv[1]):
        print(f"      {rk}: {c}")
    print(f"  (rank, all-Sigma-zero) -> count:")
    for k, c in sorted(r["pairs"].items()):
        print(f"      rank={k[0]:>2}  sigma0={k[1]!s:<5}: {c}")
    print(f"  ({r['secs']:.1f}s)")

    print()
    print("=" * 70)
    print("PART 3 — REAL value pinning (proper n=4)")
    print("=" * 70)
    r = value_pin(4, 800, 500, 42)
    print(f"  K5={r['k5']}  direct N_anti dist: {r['anti_dist']}")
    print(f"  commuting pairs PER MATCHING dist: {r['comm_per_matching']}")
    print(f"  all-COMMUTING matchings (0 anti, REAL failure mode): "
          f"{r['all_commuting_matchings']}")
    print(f"  all-ANTI matchings (0 comm, what check_lower_bound counted): "
          f"{r['all_anti_matchings']}")
    print(f"  ({r['secs']:.1f}s)")
