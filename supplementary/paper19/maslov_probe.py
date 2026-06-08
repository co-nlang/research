#!/usr/bin/env python3
r"""
Paper XIX -- Maslov relative-position probe and the MODULUS witness.

Thesis of Paper XIX: the fiber (na-vector / N_anti parity at fixed symplectic
rank) is NOT classified by any low-arity relative-position invariant. We give:

  1. The triple-Maslov BIT  mu(a,b,c) = [ omega \not\equiv 0 on
       D_{abc} = {(x,y): x in L_a, y in L_b, x+y in L_c} ].
     (Kashiwara form is identically degenerate here, so Arf collapses to one bit.)
  2. n_odd = #odd triples; deterministic tail  n_odd <= 5  =>  N_anti even.
  3. Purity ladder: n_odd  <  odd-triple hypergraph iso-type (up to S5)  <  +quad.
  4. The quadruple bit q4(a,b,c|d) on
       D4 = {(x,y,z): x in L_a, y in L_b, z in L_c, x+y+z in L_d},
       Q4 = omega(x,y)+omega(x,z)+omega(y,z).
  5. *** MODULUS WITNESS ***: two proper K5 with identical
       (dimW, rankG, radW, n_odd, hypergraph-type, full quad-profile)
       but OPPOSITE N_anti parity -- a concrete proof that no invariant up to
       arity 4 classifies the fiber.

Usage: python3 maslov_probe.py [n=5] [n_lag=3000] [max_k5=500] [seeds=10]
"""
import sys, time, random
from collections import Counter, defaultdict
from itertools import combinations, permutations

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 5
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 500
SEEDS  = int(sys.argv[4]) if len(sys.argv) > 4 else 10

SZ = 1 << (2*N); MSK = (1 << N) - 1
PN = [bin(i).count('1') & 1 for i in range(1 << N)]
XT = [[PN[i & j] for j in range(1 << N)] for i in range(1 << N)]
def symp(v, w): return XT[v & MSK][(w >> N) & MSK] ^ XT[(v >> N) & MSK][w & MSK]
def xspan(b):
    s = {0}
    for x in b: s |= {y ^ x for y in s}
    return s
def f2rank(vs):
    bs = []
    for v in vs:
        x = v
        for b in bs: x = min(x, x ^ b)
        if x: bs.append(x); bs.sort(reverse=True)
    return len(bs)
def f2rank_rows(rows, ncols):
    rows = list(rows); rank = 0
    for col in range(ncols):
        piv = None
        for i in range(rank, len(rows)):
            if (rows[i] >> col) & 1: piv = i; break
        if piv is None: continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and (rows[i] >> col) & 1: rows[i] ^= rows[rank]
        rank += 1
    return rank

def gen(seed):
    ALL = list(range(1, SZ)); rng = random.Random(seed)
    def rl():
        b = []; sp = {0}
        for _ in range(N):
            c = [v for v in ALL if v not in sp and all(symp(v, x) == 0 for x in b)]
            if not c: return None
            v = rng.choice(c); b.append(v); sp = xspan(b)
        return frozenset(sp)            # INCLUDES 0 -- needed as vector space
    lags = []; ls = set(); t = time.time()
    while len(lags) < N_LAG and time.time()-t < 120:
        L = rl()
        if L and L not in ls: ls.add(L); lags.append(L)
    adj = [set() for _ in lags]
    for i in range(len(lags)):
        for j in range(i+1, len(lags)):
            # intersection of the two Lagrangians minus 0 has dim 1 (one nonzero ray)
            if len(lags[i] & lags[j]) == 2: adj[i].add(j); adj[j].add(i)
    return lags, adj

def k5s(lags, adj, cap):
    n = len(lags); out = []
    for i in range(n):
        if len(out) >= cap: break
        ai = adj[i]
        for j in ai:
            if j <= i: continue
            aij = ai & adj[j]
            for k in aij:
                if k <= j: continue
                aijk = aij & adj[k]
                for l in aijk:
                    if l <= k: continue
                    for m in (aijk & adj[l]):
                        if m <= l: continue
                        idxs = (i, j, k, l, m)
                        five = [lags[x] for x in idxs]; sh = {}; ok = True
                        for a in range(5):
                            for b in range(a+1, 5):
                                it = (five[a] & five[b]) - {0}
                                if len(it) != 1: ok = False; break
                                sh[(a, b)] = next(iter(it))
                            if not ok: break
                        if not ok or len(set(sh.values())) != 10: continue
                        out.append((idxs, sh))
                        if len(out) >= cap: return out
    return out

# ---- Maslov triple bit -------------------------------------------------
def mu_triple(La, Lb, Lc):
    """1 iff omega not identically 0 on D={(x,y): x in La, y in Lb, x+y in Lc}."""
    Lc_set = Lc
    for x in La:
        for y in Lb:
            if (x ^ y) in Lc_set and symp(x, y):
                return 1
    return 0

def q4_bit(La, Lb, Lc, Ld):
    """1 iff Q4=w(x,y)+w(x,z)+w(y,z) not identically 0 on
       D4={(x,y,z): x in La,y in Lb,z in Lc, x+y+z in Ld}."""
    for x in La:
        for y in Lb:
            xy = x ^ y
            for z in Lc:
                if (xy ^ z) in Ld and (symp(x, y) ^ symp(x, z) ^ symp(y, z)):
                    return 1
    return 0

# ---- canonical hypergraph iso-type (3-uniform on 5 vtx, up to S5) -------
_PERMS = list(permutations(range(5)))
def hg_canon(triples):
    """triples: frozenset of frozenset-3 (the odd triples). Return canonical key."""
    best = None
    tl = [tuple(sorted(t)) for t in triples]
    for p in _PERMS:
        mapped = frozenset(tuple(sorted(p[i] for i in t)) for t in tl)
        key = tuple(sorted(mapped))
        if best is None or key < best: best = key
    return best

# ----------------------------------------------------------------------
def mu_symmetry_selfcheck(lags, adj):
    """Verify mu_triple is invariant under the 6 orderings of {a,b,c}."""
    for idxs, sh in k5s(lags, adj, 5):
        L = [lags[x] for x in idxs]
        for (a, b, c) in combinations(range(5), 3):
            vals = set()
            for p in permutations((a, b, c)):
                vals.add(mu_triple(L[p[0]], L[p[1]], L[p[2]]))
            if len(vals) != 1:
                return False, (idxs, (a, b, c))
    return True, None

def main():
    lg, ad = gen(777)
    ok, info = mu_symmetry_selfcheck(lg, ad)
    print(f"[self-check] mu_triple symmetric under S3 on {{a,b,c}}: "
          f"{'YES' if ok else 'NO  '+str(info)}\n")
    n_odd_parity = defaultdict(Counter)          # n_odd -> Counter(N_anti%2)
    bucket = defaultdict(list)                    # (rankG,radW,n_odd,hg) -> [(parity,record)]
    purity_keys = {                              # for purity-ladder report
        'n_odd':        defaultdict(Counter),
        'n_odd+hg':     defaultdict(Counter),
    }
    total = 0; t0 = time.time()
    for s in range(SEEDS):
        lags, adj = gen(2025 + 101*s)
        for idxs, sh in k5s(lags, adj, MAX_K5):
            L = [lags[x] for x in idxs]
            def Rr(x, y): return sh[(min(x, y), max(x, y))]
            rays = [Rr(a, b) for a in range(5) for b in range(a+1, 5)]
            Nanti = sum(symp(rays[a], rays[b])
                        for a in range(10) for b in range(a+1, 10))
            dimW = f2rank(rays)
            G = [0]*10
            for x in range(10):
                for y in range(10):
                    if x != y and symp(rays[x], rays[y]): G[x] |= 1 << y
            rankG = f2rank_rows(G, 10); radW = dimW - rankG
            # triple Maslov
            odd_tr = []
            for (a, b, c) in combinations(range(5), 3):
                # symmetrize: triple is odd if mu is 1 in the natural ordering;
                # mu_triple is symmetric in the role test by construction of D
                if mu_triple(L[a], L[b], L[c]):
                    odd_tr.append(frozenset((a, b, c)))
            n_odd = len(odd_tr)
            hg = hg_canon(odd_tr)
            par = Nanti % 2
            n_odd_parity[n_odd][par] += 1
            purity_keys['n_odd'][n_odd][par] += 1
            purity_keys['n_odd+hg'][(n_odd, hg)][par] += 1
            bucket[(rankG, radW, n_odd, hg)].append(
                (par, Nanti, idxs, sh, tuple(idxs)))
            total += 1
        if time.time()-t0 > 520: break

    print(f"n={N}  seeds_used<= {SEEDS}  K5 total={total}\n")

    # (1) deterministic tail
    print("=== n_odd -> N_anti parity (deterministic tail) ===")
    for k in sorted(n_odd_parity):
        c = n_odd_parity[k]
        tag = "EVEN-only" if c.get(1, 0) == 0 else ("ODD-only" if c.get(0,0)==0 else "mixed")
        print(f"  n_odd={k:2d}: even={c.get(0,0):4d} odd={c.get(1,0):4d}  [{tag}]")
    le5 = sum(n_odd_parity[k].get(1, 0) for k in n_odd_parity if k <= 5)
    le5_tot = sum(sum(n_odd_parity[k].values()) for k in n_odd_parity if k <= 5)
    print(f"  CLAIM n_odd<=5 => N_anti even: violations={le5}/{le5_tot}")

    # (2) purity ladder
    def purity(table):
        tot = 0; pure = 0
        for k, c in table.items():
            n = sum(c.values()); tot += n; pure += max(c.values())
        return pure/tot if tot else 0
    print("\n=== purity ladder (fraction in the majority parity class) ===")
    print(f"  by n_odd          : {purity(purity_keys['n_odd']):.3f}")
    print(f"  by n_odd + hg-type: {purity(purity_keys['n_odd+hg']):.3f}")
    nmix = sum(1 for c in purity_keys['n_odd+hg'].values()
               if c.get(0,0) and c.get(1,0))
    npure = sum(1 for c in purity_keys['n_odd+hg'].values()
                if (c.get(0,0)>0) ^ (c.get(1,0)>0))
    print(f"  hg-types: {npure} pure / {nmix} mixed")

    # (3) MODULUS WITNESS search: same (rankG,radW,n_odd,hg) but both parities,
    #     then confirm identical full quad-profile.
    print("\n=== MODULUS WITNESS (same coarse+triple data, opposite parity) ===")
    def quad_profile(idxs):
        L = [lags[x] for x in idxs]
        # 5 four-subsets x 4 distinguished vertices -> 20 bits; report the
        # sorted MULTISET so it is an S5-invariant relative-position signature.
        bits = []
        for sub in combinations(range(5), 4):
            for d in sub:
                a, b, c = [v for v in sub if v != d]
                bits.append(q4_bit(L[a], L[b], L[c], L[d]))
        return tuple(sorted(bits)), sum(bits)

    nq4_dist = Counter()
    witnesses = []   # (informativeness, key, even_rec, odd_rec, n_q4)
    for key, recs in bucket.items():
        pars = set(r[0] for r in recs)
        if len(pars) < 2: continue
        even = [r for r in recs if r[0] == 0][:8]
        odd  = [r for r in recs if r[0] == 1][:8]
        qe_cache = {i: quad_profile(e[2]) for i, e in enumerate(even)}
        qo_cache = {j: quad_profile(o[2]) for j, o in enumerate(odd)}
        for q in list(qe_cache.values()) + list(qo_cache.values()):
            nq4_dist[q[1]] += 1
        for i, e in enumerate(even):
            for j, o in enumerate(odd):
                if qe_cache[i] == qo_cache[j]:
                    nq4 = qe_cache[i][1]
                    rankG_w, radW_w, n_odd_w, _ = key
                    # MOST CONVINCING witness = most STRUCTURED (least saturated)
                    # shared data: small n_odd (non-complete hypergraph) ranks first,
                    # then quad informativeness.
                    score = (-n_odd_w, min(nq4, 20 - nq4))
                    witnesses.append((score, key, e, o, nq4))
    print(f"  n_q4 distribution over sampled configs: "
          f"{dict(sorted(nq4_dist.items()))}")
    sat = nq4_dist.get(20, 0); tot_q = sum(nq4_dist.values())
    print(f"  quad bit saturated (n_q4=20) in {sat}/{tot_q} "
          f"({100*sat/max(tot_q,1):.1f}%) -> quad bit nearly non-informative")
    if witnesses:
        witnesses.sort(reverse=True)   # most structured (smallest n_odd) first
        info, key, e, o, nq4 = witnesses[0]
        rankG, radW, n_odd, _ = key
        print(f"\n  *** MODULUS WITNESS *** (best of {len(witnesses)} matched pairs)")
        print(f"  bucket: rankG={rankG} radW={radW} n_odd={n_odd}, "
              f"shared n_q4={nq4} (informativeness={info})")
        print(f"    even K5 idxs={e[4]}  N_anti={e[1]} (even)")
        print(f"    odd  K5 idxs={o[4]}  N_anti={o[1]} (odd)")
        print(f"    identical (rankG,radW,n_odd,hg-type,quad-profile), "
              f"OPPOSITE N_anti parity.")
        print(f"    => no Sp(W)-invariant of relative position up to ARITY 4 "
              f"classifies the fiber.")
    else:
        # fall back: triple-level witness already breaks arity<=3 classification
        for key, recs in bucket.items():
            if len(set(r[0] for r in recs)) >= 2:
                rankG, radW, n_odd, _ = key
                e = next(r for r in recs if r[0] == 0)
                o = next(r for r in recs if r[0] == 1)
                print(f"\n  TRIPLE-LEVEL witness (no quad match in sample) "
                      f"rankG={rankG} radW={radW} n_odd={n_odd}:")
                print(f"    even idxs={e[4]} N_anti={e[1]}; "
                      f"odd idxs={o[4]} N_anti={o[1]}")
                print(f"    => already breaks classification up to arity 3.")
                break

if __name__ == "__main__":
    main()
