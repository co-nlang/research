#!/usr/bin/env python3
"""
Paper XVIII: K₅ parity sampling in Sp(10, F₂) (n=5, 5-qubit).

Alternating parity conjecture:
  n=3 (Sp(6,F₂))  → all K₅s have parity -1  [Paper XVII: 12,096/12,096]
  n=4 (Sp(8,F₂))  → all K₅s have parity +1  [Paper XVIII: 3B+/3B+]
  n=5 (Sp(10,F₂)) → ?

Usage: python check_k5_5qubit.py [max_lags=4000] [max_k5=500]
"""
import sys, time
from collections import Counter

N = 5
DIM = 2 * N        # 10
_SZ = 2**DIM       # 1024
LAG_SIZE = 2**N - 1  # 31

MAX_LAGS = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
MAX_K5   = int(sys.argv[2]) if len(sys.argv) > 2 else 500

t0 = time.time()
print(f"Sp(10,F₂) K₅ parity sampler  max_lags={MAX_LAGS}  max_k5={MAX_K5}", flush=True)

# ── Symplectic form ω(v,w) via 5-bit parity lookup ────────────────────────────
# ω(v,w) = parity(v_lo & w_hi) XOR parity(v_hi & w_lo)
# where v = (v_lo, v_hi) with v_lo,v_hi ∈ F₂⁵
_P5 = [bin(i).count('1') & 1 for i in range(32)]  # parity of 5-bit int

def symp(v, w):
    vlo = v & 31;  vhi = (v >> N) & 31
    wlo = w & 31;  whi = (w >> N) & 31
    return _P5[vlo & whi] ^ _P5[vhi & wlo]

# ── XOR span ──────────────────────────────────────────────────────────────────
def xor_span(basis):
    span = set()
    n = len(basis)
    for mask in range(1, 1 << n):
        s = 0
        for i in range(n):
            if (mask >> i) & 1: s ^= basis[i]
        if s: span.add(s)
    return span

# ── Find first MAX_LAGS Lagrangians (recursive basis enumeration) ─────────────
print(f"[1] Finding up to {MAX_LAGS} Lagrangians in Sp(10,F₂)...", flush=True)
_seen = set()
_lags = []

def _search(basis, span):
    if len(_lags) >= MAX_LAGS: return
    if len(basis) == N:
        key = frozenset(span)
        if key not in _seen:
            _seen.add(key)
            _lags.append(key)
        return
    start = basis[-1] + 1 if basis else 1
    for v in range(start, _SZ):
        if len(_lags) >= MAX_LAGS: return
        if v in span: continue
        if all(symp(v, b) == 0 for b in basis):
            _search(basis + [v], span | xor_span(basis + [v]))

_search([], set())
n_lag = len(_lags)
print(f"     {n_lag} Lagrangians  ({time.time()-t0:.1f}s)", flush=True)

if n_lag == 0:
    print("No Lagrangians found. Exiting.")
    sys.exit(1)

# ── Adjacency graph ───────────────────────────────────────────────────────────
print("[2] Building adjacency (dim(Lᵢ∩Lⱼ)=1)...", flush=True)
adj = [set() for _ in range(n_lag)]
n_edges = 0
for i in range(n_lag):
    for j in range(i + 1, n_lag):
        if len(_lags[i] & _lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)
            n_edges += 1

deg = [len(adj[i]) for i in range(n_lag)]
print(f"     {n_edges} edges  |  deg min={min(deg)} max={max(deg)} mean={sum(deg)/n_lag:.0f}  "
      f"({time.time()-t0:.1f}s)", flush=True)

if n_edges == 0:
    print("No adjacent Lagrangian pairs. Increase MAX_LAGS.")
    sys.exit(1)

# ── K₅ search ─────────────────────────────────────────────────────────────────
print(f"[3] Searching K₅ configurations (up to {MAX_K5})...", flush=True)

def k5_parity(idx5):
    """
    Parity of K₅ via Paper XVII Lemma 4.2:
    sign = (-1)^{N_I} where N_I = # interleaving cross-context pairs with ω=1.
    Interleaving pair for {a<b<c<d}: (v_{ac}, v_{bd}).
    """
    five = [_lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a + 1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1:
                return None  # not a valid K₅
            shared[(a, b)] = next(iter(inter))
    n_i = sum(
        1
        for a in range(5) for b in range(a+1, 5)
        for c in range(b+1, 5) for d in range(c+1, 5)
        if symp(shared[(a, c)], shared[(b, d)]) == 1
    )
    n_anti = sum(
        1 for (a,b), vab in shared.items()
          for (c,d), vcd in shared.items()
          if (c,d) > (a,b) and not ({a,b} & {c,d}) and symp(vab, vcd) == 1
    )
    return (-1)**n_i, n_anti

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
                    anti_dist[na] += 1
                    n_k5 += 1
                    if n_k5 % 50 == 0:
                        print(f"     {n_k5:>6} K₅s  parity={dict(parity_dist)}  "
                              f"N_anti={dict(anti_dist)}  ({time.time()-t0:.1f}s)", flush=True)
                    if n_k5 >= MAX_K5:
                        done = True; break
                if done: break
            if done: break
        if done: break

# ── Report ────────────────────────────────────────────────────────────────────
print(f"\n[4] Results  ({time.time()-t0:.1f}s)")
print(f"     K₅s sampled       : {n_k5}")
print(f"     Parity distribution: {dict(parity_dist)}")
print(f"     N_anti distribution: {dict(anti_dist)}")

if n_k5 == 0:
    print("\n>>> No K₅s found in the sampled Lagrangians.")
    print("    Try increasing MAX_LAGS (current: {MAX_LAGS}).")
elif parity_dist.get(-1, 0) > 0 and parity_dist.get(+1, 0) == 0:
    print("\n>>> All sampled K₅s have parity -1.")
    print("    Alternating conjecture  n=3(−1) → n=4(+1) → n=5(−1)  SUPPORTED.")
elif parity_dist.get(+1, 0) > 0 and parity_dist.get(-1, 0) == 0:
    print("\n>>> All sampled K₅s have parity +1.")
    print("    Pattern is NOT alternating — may be all even for n≥4.")
else:
    print("\n>>> MIXED parities found for n=5.")
    print("    K₅ parity is not universal; n=5 has both odd and even K₅s.")
