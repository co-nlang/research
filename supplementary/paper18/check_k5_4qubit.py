#!/usr/bin/env python3
"""
Paper XVIII (exploratory): Even K₅ search in Sp(8, F₂).

Tests the Cross-Context Anticommutation Theorem (Paper XVII, Thm 3.1)
for the 4-qubit case n=4.

Paper XVII proves: for any K₅ of Lagrangians in Sp(6,F₂), all 15 cross-context
ray pairs satisfy ω(vᵢⱼ, vₖₗ) = 1.  The proof uses a size argument:
10 rays cannot be mutually isotropic because any totally isotropic subspace
of F₂⁶ has at most 2³-1 = 7 nonzero vectors, and 10 > 7.

For n=4 (Sp(8,F₂)): a Lagrangian has 2⁴-1 = 15 nonzero vectors, so 10 ≤ 15
and the size argument FAILS.

This script asks: does the theorem still hold for n=4?
  - If all K₅s have all 15 cross-context pairs anticommuting → theorem extends
  - If any K₅ has a commuting cross-context pair → "even K₅" found, theorem fails

Run modes:
  python check_k5_4qubit.py          # early-exit on first even K₅
  python check_k5_4qubit.py full     # enumerate all K₅s (may be slow)
"""

import sys
import time
from collections import defaultdict

N = 4        # qubits
DIM = 2 * N  # 8
LAG_DIM = N  # Lagrangian dimension
LAG_SIZE = 2**N - 1  # 15 nonzero elements per Lagrangian

FULL_ENUM = (len(sys.argv) > 1 and sys.argv[1] == 'full')

t0 = time.time()

def elapsed():
    return f"({time.time()-t0:.1f}s)"

# ── Symplectic form ω(v,w) = Σᵢ (vᵢwᵢ₊ₙ + vᵢ₊ₙwᵢ) mod 2 ─────────────────

print("[init] Precomputing symplectic form table...", flush=True)
OMEGA = bytearray(256 * 256)
for v in range(256):
    vb = [(v >> i) & 1 for i in range(DIM)]
    for w in range(v + 1, 256):
        wb = [(w >> i) & 1 for i in range(DIM)]
        o = sum(vb[i]*wb[i+N] + vb[i+N]*wb[i] for i in range(N)) % 2
        OMEGA[v*256 + w] = o
        OMEGA[w*256 + v] = o

def symp(v, w):
    return OMEGA[v*256 + w]

# ── XOR span ─────────────────────────────────────────────────────────────────

def xor_span(basis):
    """All nonzero XOR-combinations of integer basis vectors."""
    result = set()
    n = len(basis)
    for mask in range(1, 1 << n):
        s = 0
        for i in range(n):
            if (mask >> i) & 1:
                s ^= basis[i]
        if s:
            result.add(s)
    return result

# ── Find all Lagrangians ──────────────────────────────────────────────────────
# Enumerate 4-dim totally isotropic subspaces of (F₂⁸, ω).
# Canonical form: basis vectors b₁ < b₂ < b₃ < b₄ (as integers),
# deduplicated by frozenset of 15 nonzero elements.

def find_lagrangians():
    seen = set()
    result = []

    def search(basis, span):
        if len(basis) == N:
            key = frozenset(span)
            if key not in seen:
                seen.add(key)
                result.append(key)
            return
        start = basis[-1] + 1 if basis else 1
        for v in range(start, 256):
            if v in span:
                continue
            if all(symp(v, b) == 0 for b in basis):
                search(basis + [v], span | xor_span(basis + [v]))

    search([], set())
    return result

print("[1/4] Finding Lagrangians in Sp(8,F₂)...", flush=True)
lagrangians = find_lagrangians()
n_lag = len(lagrangians)
print(f"      {n_lag} Lagrangians  {elapsed()}", flush=True)

# Expected: (2+1)(4+1)(8+1)(16+1) = 3·5·9·17 = 2295
if n_lag != 2295:
    print(f"  WARNING: expected 2295, got {n_lag}")

# ── Build adjacency graph (dim-1 intersections) ───────────────────────────────

print("[2/4] Building adjacency graph (dim(Lᵢ∩Lⱼ)=1)...", flush=True)
lag_list = lagrangians
adj = [[] for _ in range(n_lag)]
n_edges = 0
for i in range(n_lag):
    for j in range(i + 1, n_lag):
        if len(lag_list[i] & lag_list[j]) == 1:
            adj[i].append(j)
            adj[j].append(i)
            n_edges += 1

degrees = [len(adj[i]) for i in range(n_lag)]
print(f"      {n_edges} edges  |  degree min={min(degrees)} max={max(degrees)} "
      f"mean={sum(degrees)/n_lag:.1f}  {elapsed()}", flush=True)

# ── K₅ search ────────────────────────────────────────────────────────────────

print(f"\n[3/4] Searching K₅ configurations {'(full enum)' if FULL_ENUM else '(early-exit on even K₅)'}...",
      flush=True)

adj_set = [set(a) for a in adj]

n_k5 = 0
n_odd = 0
n_even = 0
first_even = None

class EvenK5Found(Exception):
    pass

def check_k5(five_indices):
    """Check all 15 cross-context ω values for this K₅.
    Returns True if all anticommute (ω=1), False if any commute (ω=0)."""
    five = [lag_list[x] for x in five_indices]
    # Get shared rays: shared[(a,b)] = unique ray in Lₐ ∩ L_b
    shared = {}
    for a in range(5):
        for b in range(a + 1, 5):
            inter = five[a] & five[b]
            assert len(inter) == 1, f"dim intersection ≠ 1: {len(inter)}"
            shared[(a, b)] = next(iter(inter))
    # Check cross-context pairs
    for (a, b), vab in shared.items():
        for (c, d), vcd in shared.items():
            if (c, d) <= (a, b):
                continue
            if {a, b} & {c, d}:
                continue  # same-context pair, skip
            if symp(vab, vcd) == 0:
                return False  # commuting cross-context pair found
    return True

try:
    for i in range(n_lag):
        ai = adj_set[i]
        for j in ai:
            if j <= i:
                continue
            aij = ai & adj_set[j]
            for k in aij:
                if k <= j:
                    continue
                aijk = aij & adj_set[k]
                for l in aijk:
                    if l <= k:
                        continue
                    aijkl = aijk & adj_set[l]
                    for m in aijkl:
                        if m <= l:
                            continue
                        n_k5 += 1
                        if check_k5((i, j, k, l, m)):
                            n_odd += 1
                        else:
                            n_even += 1
                            if first_even is None:
                                first_even = (i, j, k, l, m)
                            if not FULL_ENUM:
                                raise EvenK5Found()
                        if n_k5 % 50000 == 0:
                            print(f"      {n_k5:>9} K₅s  |  odd={n_odd}  even={n_even}  {elapsed()}",
                                  flush=True)
except EvenK5Found:
    pass

# ── Report ────────────────────────────────────────────────────────────────────

print(f"\n[4/4] Results  {elapsed()}")
print(f"      K₅ configurations checked : {n_k5}")
print(f"      All-anticommuting (odd)   : {n_odd}")
print(f"      Has commuting pair (even) : {n_even}")

if n_k5 == 0:
    print("\n>>> No K₅ configurations found in Sp(8,F₂).")
    print("    (K₅ geometry may not exist for n=4)")
elif n_even == 0:
    if FULL_ENUM:
        print(f"\n>>> FULL ENUMERATION: no even K₅ found.")
        print("    Cross-Context Anticommutation Theorem EXTENDS to n=4.")
        print("    (But the Paper XVII size-argument proof does not — a new proof is needed.)")
    else:
        print(f"\n>>> No even K₅ found in {n_k5} K₅s checked.")
        print("    Run with 'full' argument for complete enumeration.")
else:
    print(f"\n>>> EVEN K₅ FOUND: {first_even}")
    print("    Cross-Context Anticommutation Theorem does NOT extend to n=4.")
    # Print details of the even K₅
    five = [lag_list[x] for x in first_even]
    shared = {}
    for a in range(5):
        for b in range(a+1, 5):
            inter = five[a] & five[b]
            shared[(a,b)] = next(iter(inter))
    print("\n    Cross-context ω values:")
    for (a,b), vab in shared.items():
        for (c,d), vcd in shared.items():
            if (c,d) <= (a,b): continue
            if {a,b} & {c,d}: continue
            o = symp(vab, vcd)
            mark = "" if o == 1 else "  ← COMMUTES (ω=0)"
            print(f"      ω(v{a}{b}, v{c}{d}) = {o}{mark}")
