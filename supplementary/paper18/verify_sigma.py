#!/usr/bin/env python3
"""
Paper XVIII: Verify Theorem B — matching sum uniformity.

For each K₅ of Lagrangians in Sp(2n,F₂), define 5 matching sums:
  Σ_m = ω(v_{ab},v_{cd}) + ω(v_{ac},v_{bd}) + ω(v_{ad},v_{bc})  (mod 2)
where {a,b,c,d} = {0,1,2,3,4} \ {m}.

Theorem B conjecture: all 5 Σ_m are equal for every K₅.

Corollary B1: N_anti=14 is impossible (would need 4 matchings with Σ=1, 1 with Σ=0).
Theorem C conjecture: for n=4, Σ_m = 0 always (hence N_anti is always even).

Usage: python3 verify_sigma.py [n=4] [n_lag=500] [max_k5=200] [seed=42]
"""
import sys, time, random
from collections import Counter

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 4
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 500
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 200
SEED   = int(sys.argv[4]) if len(sys.argv) > 4 else 42

DIM  = 2 * N
_SZ  = 2**DIM
_MSK = (1 << N) - 1

random.seed(SEED)
t0 = time.time()

lag_count = 1
for i in range(1, N+1): lag_count *= (2**i + 1)
print(f"Sp({DIM},F₂) Σ_m uniformity check  n={N}  n_lag={N_LAG}  "
      f"max_k5={MAX_K5}  seed={SEED}", flush=True)
print(f"  Lagrangian count={lag_count}  size={2**N-1}", flush=True)

# ── Symplectic form ──────────────────────────────────────────────────────────
_PN = [bin(i).count('1') & 1 for i in range(1 << N)]
_XT = [[_PN[i & j] for j in range(1 << N)] for i in range(1 << N)]

def symp(v, w):
    vlo = v & _MSK; vhi = (v >> N) & _MSK
    wlo = w & _MSK; whi = (w >> N) & _MSK
    return _XT[vlo][whi] ^ _XT[vhi][wlo]

def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)):
            if (mask >> i) & 1: s ^= basis[i]
        if s: span.add(s)
    return span

ALL_VEC = list(range(1, _SZ))

def random_lagrangian():
    basis = []; span = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands: return None
        v = random.choice(cands)
        basis.append(v); span = xor_span(basis)
    return frozenset(span)

# ── Generate Lagrangians ──────────────────────────────────────────────────────
print(f"[1] Generating {N_LAG} random Lagrangians...", flush=True)
lag_set = set(); lags = []; attempts = 0
while len(lags) < N_LAG:
    attempts += 1
    lag = random_lagrangian()
    if lag is None or lag in lag_set: continue
    lag_set.add(lag); lags.append(lag)
n_lag = len(lags)
print(f"    {n_lag} Lagrangians  ({time.time()-t0:.1f}s)", flush=True)

# ── Adjacency ─────────────────────────────────────────────────────────────────
print("[2] Building adjacency graph...", flush=True)
adj = [set() for _ in range(n_lag)]
for i in range(n_lag):
    for j in range(i+1, n_lag):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)
print(f"    done  ({time.time()-t0:.1f}s)", flush=True)

# ── Sigma computation ─────────────────────────────────────────────────────────
# For each K₅, compute all 5 matching sums Σ_m.
# Missing index m ∈ {0,1,2,3,4}; {a,b,c,d} = {0..4}\{m} in sorted order.
# Matching: (v_{ab},v_{cd}), (v_{ac},v_{bd}), (v_{ad},v_{bc}).

def k5_sigmas(idx5):
    five = [lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a+1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1: return None
            shared[(a,b)] = next(iter(inter))

    # Degenerate K₅s (some rays coincide) excluded.
    if len(set(shared.values())) != 10:
        return None

    # Fano zero-sum check: v_{i,j1}⊕v_{i,j2}⊕v_{i,j3}⊕v_{i,j4} = 0 within each L_i.
    from functools import reduce
    import operator
    fano_ok = all(
        reduce(operator.xor, [shared[(min(i,j),max(i,j))] for j in range(5) if j!=i]) == 0
        for i in range(5)
    )

    sigmas = []
    for m in range(5):
        a, b, c, d = sorted(x for x in range(5) if x != m)
        s = (symp(shared[(a,b)], shared[(c,d)]) ^
             symp(shared[(a,c)], shared[(b,d)]) ^
             symp(shared[(a,d)], shared[(b,c)]))
        sigmas.append(s)

    n_anti = sum(
        1 for (i,j),vij in shared.items()
          for (k,l),vkl in shared.items()
          if (k,l)>(i,j) and not ({i,j}&{k,l}) and symp(vij,vkl)==1
    )
    return tuple(sigmas), n_anti, fano_ok

# ── K₅ search ─────────────────────────────────────────────────────────────────
print(f"[3] Checking K₅s (up to {MAX_K5})...", flush=True)

# Track separately for Fano-OK and Fano-FAIL K₅s
# fano_unif[fok][sigma_val] = count of K₅s with that Fano status and uniform sigma
fano_unif    = {True: Counter(), False: Counter()}
fano_anti    = {True: {0: Counter(), 1: Counter()}, False: {0: Counter(), 1: Counter()}}
fano_nonunif = {True: 0, False: 0}
fano_total   = {True: 0, False: 0}
n_k5 = 0; done = False

for i in range(n_lag):
    if done: break
    ai = adj[i]
    for j in ai:
        if j<=i or done: continue
        aij = ai & adj[j]
        for k in aij:
            if k<=j or done: continue
            aijk = aij & adj[k]
            for l in aijk:
                if l<=k or done: continue
                aijkl = aijk & adj[l]
                for m in aijkl:
                    if m<=l: continue
                    result = k5_sigmas((i,j,k,l,m))
                    if result is None: continue
                    sigs, na, fok = result
                    n_k5 += 1
                    fano_total[fok] += 1
                    if len(set(sigs)) == 1:
                        sv = sigs[0]
                        fano_unif[fok][sv] += 1
                        fano_anti[fok][sv][na] += 1
                    else:
                        fano_nonunif[fok] += 1
                    if n_k5 >= MAX_K5:
                        done = True; break
                if done: break
            if done: break
        if done: break

# ── Report ────────────────────────────────────────────────────────────────────
print(f"\n[4] Results  n={N}  ({time.time()-t0:.1f}s)")
print(f"    K₅s (distinct rays) : {n_k5}")

for fok, label in [(True, "Fano zero-sum OK"), (False, "Fano zero-sum FAIL")]:
    tot = fano_total[fok]
    if tot == 0: continue
    nu = sum(fano_unif[fok].values())
    nn = fano_nonunif[fok]
    print(f"\n  [{label}]  {tot} K₅s")
    print(f"    Σ_m uniform   : {nu}  ({100*nu/tot:.1f}%)")
    print(f"    Σ_m non-unif  : {nn}  ({100*nn/tot:.1f}%)")
    for sv in [0, 1]:
        c = fano_unif[fok].get(sv, 0)
        if c:
            print(f"    Σ={sv}: {c}  N_anti={dict(sorted(fano_anti[fok][sv].items()))}")
