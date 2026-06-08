#!/usr/bin/env python3
"""
Paper XVIII: K₅ parity sampling in Sp(10, F₂) via RANDOM Lagrangians.

Eliminates the lexicographic bias of check_k5_5qubit.py.
Randomly generates Lagrangians by choosing isotropic basis vectors uniformly
at each extension step, then searches for K₅ configurations among them.

Usage: python3 check_k5_5qubit_random.py [n_lag=2000] [max_k5=500] [seed=42]
"""
import sys, time, random
from collections import Counter

N      = 5
DIM    = 2 * N      # 10
_SZ    = 2**DIM     # 1024

N_LAG  = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
MAX_K5 = int(sys.argv[2]) if len(sys.argv) > 2 else 500
SEED   = int(sys.argv[3]) if len(sys.argv) > 3 else 42

random.seed(SEED)
t0 = time.time()
print(f"Sp(10,F₂) K₅ parity sampler (RANDOM)  "
      f"n_lag={N_LAG}  max_k5={MAX_K5}  seed={SEED}", flush=True)

# ── Precomputed symplectic form ω(v,w) ──────────────────────────────────────
# ω(v,w) = parity(v_lo & w_hi) XOR parity(v_hi & w_lo)
# where v = (v_lo | v_hi<<5) in F₂^5 × F₂^5
print("[init] Precomputing ω table (1024×1024)...", flush=True)
_P5 = [bin(i).count('1') & 1 for i in range(32)]
_OMEGA = bytearray(_SZ * _SZ)
for v in range(_SZ):
    vlo = v & 31; vhi = (v >> N) & 31
    for w in range(_SZ):
        wlo = w & 31; whi = (w >> N) & 31
        _OMEGA[v * _SZ + w] = _P5[vlo & whi] ^ _P5[vhi & wlo]

def symp(v, w):
    return _OMEGA[v * _SZ + w]

# ── XOR span ─────────────────────────────────────────────────────────────────
def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)):
            if (mask >> i) & 1: s ^= basis[i]
        if s: span.add(s)
    return span

# ── Random Lagrangian generation ─────────────────────────────────────────────
# At each step k, valid candidates = {v ∉ span : ω(v,bᵢ)=0 for all i<k}.
# The set of such v has size 2^{N+1-k} - 2^{k-1} for k = 1..N.
# We pick uniformly from the candidate list (O(1024) scan per step).

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
print(f"[1] Generating {N_LAG} random Lagrangians in Sp(10,F₂)...", flush=True)
lag_set  = set()
lags     = []
attempts = 0
while len(lags) < N_LAG:
    attempts += 1
    lag = random_lagrangian()
    if lag is None or lag in lag_set:
        continue
    lag_set.add(lag)
    lags.append(lag)
    if len(lags) % 200 == 0:
        print(f"     {len(lags)}/{N_LAG}  ({time.time()-t0:.1f}s)", flush=True)

n_lag = len(lags)
print(f"     {n_lag} Lagrangians in {attempts} attempts  ({time.time()-t0:.1f}s)", flush=True)

# ── Adjacency graph (dim-1 intersection) ─────────────────────────────────────
print("[2] Building adjacency graph (dim(Lᵢ∩Lⱼ)=1)...", flush=True)
adj    = [set() for _ in range(n_lag)]
n_edges = 0
for i in range(n_lag):
    for j in range(i + 1, n_lag):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)
            n_edges += 1

deg = [len(adj[i]) for i in range(n_lag)]
if deg:
    print(f"     {n_edges} edges  |  deg min={min(deg)} max={max(deg)} "
          f"mean={sum(deg)/n_lag:.0f}  ({time.time()-t0:.1f}s)", flush=True)

# ── K₅ parity via Lemma 4.2 (interleaving anticommuting pairs) ───────────────
def k5_parity(idx5):
    five = [lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a + 1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1:
                return None
            shared[(a, b)] = next(iter(inter))
    # N_I = interleaving anticommuting pairs: for each {a<b<c<d}, check (v_{ac}, v_{bd})
    n_i = sum(
        1
        for a in range(5) for b in range(a+1, 5)
        for c in range(b+1, 5) for d in range(c+1, 5)
        if symp(shared[(a, c)], shared[(b, d)]) == 1
    )
    # N_anti = all anticommuting cross-context pairs (for reporting)
    n_anti = sum(
        1 for (a, b), vab in shared.items()
          for (c, d), vcd in shared.items()
          if (c, d) > (a, b) and not ({a, b} & {c, d}) and symp(vab, vcd) == 1
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
                    if result is None: continue
                    p, na = result
                    parity_dist[p] += 1
                    anti_dist[na]  += 1
                    n_k5 += 1
                    if n_k5 % 50 == 0:
                        print(f"     {n_k5:>5} K₅s  parity={dict(parity_dist)}  "
                              f"N_anti={dict(anti_dist)}  ({time.time()-t0:.1f}s)", flush=True)
                    if n_k5 >= MAX_K5:
                        done = True; break
                if done: break
            if done: break
        if done: break

# ── Report ────────────────────────────────────────────────────────────────────
print(f"\n[4] Results  ({time.time()-t0:.1f}s)")
print(f"     Lagrangians sampled : {n_lag}  (out of 75735 total)")
print(f"     K₅s found          : {n_k5}")
print(f"     Parity distribution : {dict(parity_dist)}")
print(f"     N_anti distribution : {dict(anti_dist)}")

if n_k5 == 0:
    print("\n>>> No K₅s found. Try increasing n_lag.")
elif parity_dist.get(-1, 0) > 0 and parity_dist.get(+1, 0) == 0:
    print("\n>>> All K₅s parity -1.  Alternating pattern n=3(-1)→n=4(+1)→n=5(-1) SUPPORTED.")
elif parity_dist.get(+1, 0) > 0 and parity_dist.get(-1, 0) == 0:
    print(f"\n>>> All K₅s parity +1.  Pattern is even for n≥4.")
    if anti_dist.get(0, 0) == n_k5:
        print("    ALL have N_anti=0 — the 10 shared rays form a mutually isotropic set.")
        print("    Hypothesis: the 10 rays span a totally isotropic subspace (≤ a Lagrangian).")
    elif 0 in anti_dist:
        print(f"    Mixed N_anti: some have N_anti=0, others have N_anti>0.")
else:
    print("\n>>> MIXED parities.  K₅ parity is not universal for n=5.")
