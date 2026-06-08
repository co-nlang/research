#!/usr/bin/env python3
"""
Paper XVIII: K₅ parity sampler for Sp(2n, F₂), general n.
Random Lagrangian sampling — eliminates lexicographic bias.

Tracks:
  parity distribution  (via N_I: interleaving anticommuting pairs)
  N_anti distribution  (total anticommuting cross-context pairs)

Usage: python3 check_k5_random_n.py [n=5] [n_lag=2000] [max_k5=500] [seed=42]

Lagrangian counts:  n=3→135  n=4→2295  n=5→75735  n=6→4922775
"""
import sys, time, random
from collections import Counter

N      = int(sys.argv[1]) if len(sys.argv) > 1 else 5
N_LAG  = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
MAX_K5 = int(sys.argv[3]) if len(sys.argv) > 3 else 500
SEED   = int(sys.argv[4]) if len(sys.argv) > 4 else 42

DIM  = 2 * N
_SZ  = 2**DIM
_MSK = (1 << N) - 1

random.seed(SEED)
t0 = time.time()

lag_count = 1
for i in range(1, N+1): lag_count *= (2**i + 1)

print(f"Sp({DIM},F₂) K₅ parity sampler  n={N}  n_lag={N_LAG}  "
      f"max_k5={MAX_K5}  seed={SEED}", flush=True)
print(f"  Lagrangian count={lag_count}  size={2**N - 1}", flush=True)

# ── Symplectic form via (2^N × 2^N) parity XOR table ─────────────────────────
# ω(v,w) = parity(v_lo & w_hi) XOR parity(v_hi & w_lo)
# _XT[a][b] = parity(a & b)  for a,b ∈ {0,...,2^N-1}
_PN = [bin(i).count('1') & 1 for i in range(1 << N)]
_XT = [[_PN[i & j] for j in range(1 << N)] for i in range(1 << N)]

def symp(v, w):
    vlo = v & _MSK; vhi = (v >> N) & _MSK
    wlo = w & _MSK; whi = (w >> N) & _MSK
    return _XT[vlo][whi] ^ _XT[vhi][wlo]

# ── XOR span ─────────────────────────────────────────────────────────────────
def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)):
            if (mask >> i) & 1: s ^= basis[i]
        if s: span.add(s)
    return span

# ── Random Lagrangian ────────────────────────────────────────────────────────
# At step k, valid candidates = {v ∉ span : ω(v,bᵢ)=0 ∀i<k}.
# Size = 2^{N+1-k} - 2^{k-1}  (complement minus span).
ALL_VEC = list(range(1, _SZ))

def random_lagrangian():
    basis = []
    span  = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands:
            return None
        v = random.choice(cands)
        basis.append(v)
        span = xor_span(basis)
    return frozenset(span)

# ── Collect N_LAG distinct random Lagrangians ─────────────────────────────────
print(f"[1] Generating {N_LAG} random Lagrangians...", flush=True)
lag_set  = set()
lags     = []
attempts = 0
report_every = max(1, N_LAG // 10)
while len(lags) < N_LAG:
    attempts += 1
    lag = random_lagrangian()
    if lag is None or lag in lag_set:
        continue
    lag_set.add(lag)
    lags.append(lag)
    if len(lags) % report_every == 0:
        print(f"   {len(lags)}/{N_LAG}  ({time.time()-t0:.1f}s)", flush=True)

n_lag = len(lags)
print(f"   {n_lag} Lagrangians in {attempts} attempts  ({time.time()-t0:.1f}s)", flush=True)

# ── Adjacency graph (dim-1 intersection) ─────────────────────────────────────
print("[2] Building adjacency graph...", flush=True)
adj     = [set() for _ in range(n_lag)]
n_edges = 0
report_every_row = max(1, n_lag // 4)
for i in range(n_lag):
    for j in range(i + 1, n_lag):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)
            n_edges += 1
    if (i + 1) % report_every_row == 0:
        print(f"   row {i+1}/{n_lag}  edges={n_edges}  ({time.time()-t0:.1f}s)", flush=True)

deg = [len(adj[i]) for i in range(n_lag)]
print(f"   {n_edges} edges  deg=[{min(deg)},{max(deg)}] mean={sum(deg)/n_lag:.0f}  "
      f"({time.time()-t0:.1f}s)", flush=True)

if n_edges == 0:
    print("No edges — increase N_LAG.")
    sys.exit(1)

# ── K₅ parity ────────────────────────────────────────────────────────────────
# parity = (-1)^{N_I}  where N_I = interleaving anticommuting cross-context pairs.
# For 4-element subset {a<b<c<d}, the interleaving pair is (v_{ac}, v_{bd}).
def k5_parity(idx5):
    five = [lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a + 1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1:
                return None
            shared[(a, b)] = next(iter(inter))
    n_i = sum(
        1
        for a in range(5) for b in range(a+1, 5)
        for c in range(b+1, 5) for d in range(c+1, 5)
        if symp(shared[(a, c)], shared[(b, d)]) == 1
    )
    n_anti = sum(
        1 for (a,b),vab in shared.items()
          for (c,d),vcd in shared.items()
          if (c,d) > (a,b) and not ({a,b} & {c,d}) and symp(vab, vcd) == 1
    )
    return (-1)**n_i, n_anti

# ── K₅ search ─────────────────────────────────────────────────────────────────
print(f"[3] Searching K₅ configurations (up to {MAX_K5})...", flush=True)
parity_dist = Counter()
anti_dist   = Counter()
n_k5 = 0
done = False

for i in range(n_lag):
    if done: break
    ai = adj[i]
    for j in ai:
        if j <= i or done: continue
        aij = ai & adj[j]
        for k in aij:
            if k <= j or done: continue
            aijk = aij & adj[k]
            for l in aijk:
                if l <= k or done: continue
                aijkl = aijk & adj[l]
                for m in aijkl:
                    if m <= l: continue
                    result = k5_parity((i, j, k, l, m))
                    if result is None:
                        continue
                    p, na = result
                    parity_dist[p] += 1
                    anti_dist[na]  += 1
                    n_k5 += 1
                    if n_k5 % 50 == 0:
                        print(f"   {n_k5:>5} K₅s  parity={dict(parity_dist)}  "
                              f"N_anti={dict(anti_dist)}  ({time.time()-t0:.1f}s)", flush=True)
                    if n_k5 >= MAX_K5:
                        done = True; break
                if done: break
            if done: break
        if done: break

# ── Report ────────────────────────────────────────────────────────────────────
print(f"\n[4] Results  n={N}  ({time.time()-t0:.1f}s)")
print(f"   Lagrangians : {n_lag}/{lag_count}  ({100*n_lag/lag_count:.3f}%)")
print(f"   K₅s found  : {n_k5}")
print(f"   Parity dist : {dict(sorted(parity_dist.items()))}")
print(f"   N_anti dist : {dict(sorted(anti_dist.items()))}")

if n_k5 == 0:
    print("\n>>> No K₅s found — increase N_LAG.")
elif len(parity_dist) == 1:
    p = next(iter(parity_dist))
    sign = "+1" if p == 1 else "-1"
    print(f"\n>>> UNIVERSAL parity {sign} for n={N}.")
    if p == 1 and anti_dist.get(0, 0) == n_k5:
        print("    All N_anti=0 — 10 shared rays mutually isotropic (sampling artifact).")
else:
    neg = parity_dist.get(-1, 0)
    pos = parity_dist.get(+1, 0)
    frac = neg / (neg + pos)
    print(f"\n>>> MIXED parity for n={N}.  -1: {neg}  +1: {pos}  ({frac*100:.1f}% negative)")
    if abs(frac - 0.5) < 0.05:
        print("    ~50/50 — involution symmetry suspected.")
