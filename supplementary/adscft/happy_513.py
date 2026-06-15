#!/usr/bin/env python3
"""
HaPPY building block: the [[5,1,3]] perfect code as a stabilizer code,
read in the framework's symplectic-F2 language (S = isotropic subspace,
logical = S^perp / S, boundary region = coordinate subspace).

Goal (step 1 of insight/adscft_holographic_codes.md):
  - put the perfect tensor into Sp(2n,F2) form,
  - compute, for every boundary region A subset {0..4}, whether the bulk
    (logical) operator is reconstructable on A,
  - locate the reconstruction threshold and check entanglement-wedge
    *complementarity* (exactly one of A, A-complement reconstructs).

This is the QEC "boundary underdetermines bulk" transition made concrete and
finite, in framework-native terms. Pure F2; no dependencies.
"""

from itertools import combinations, product

N = 5  # physical qubits

# A Pauli (mod phase) on N qubits = (x, z), x,z in F2^N.  Vector in F2^{2N}.
# Symplectic form: omega((x,z),(x',z')) = sum_i x_i z'_i + z_i x'_i  (mod 2).
# Two Paulis commute iff omega = 0.

def pauli(s):
    """Build (x,z) from a length-N string over {I,X,Y,Z}."""
    x = [0]*N; z = [0]*N
    for i, c in enumerate(s):
        if c in 'XY': x[i] = 1
        if c in 'ZY': z[i] = 1
    return (tuple(x), tuple(z))

def omega(a, b):
    (xa, za), (xb, zb) = a, b
    return sum(xa[i]*zb[i] + za[i]*xb[i] for i in range(N)) % 2

def xor(a, b):
    (xa, za), (xb, zb) = a, b
    return (tuple((xa[i]^xb[i]) for i in range(N)),
            tuple((za[i]^zb[i]) for i in range(N)))

def support(a):
    (x, z) = a
    return frozenset(i for i in range(N) if x[i] or z[i])

# --- the standard cyclic [[5,1,3]] generators (cyclic shifts of XZZXI) ---
GENS = [pauli(s) for s in ("XZZXI", "IXZZX", "XIXZZ", "ZXIXZ")]
Xbar = pauli("XXXXX")
Zbar = pauli("ZZZZZ")

# Stabilizer group S = all 2^4 F2-combinations of the 4 generators.
def stabilizer_group(gens):
    elems = []
    for bits in product([0,1], repeat=len(gens)):
        acc = (tuple([0]*N), tuple([0]*N))
        for b, g in zip(bits, gens):
            if b: acc = xor(acc, g)
        elems.append(acc)
    return elems

S = stabilizer_group(GENS)

# --- sanity checks ---
assert all(omega(gi, gj) == 0 for gi in GENS for gj in GENS), "S not isotropic"
assert len(set(S)) == 16, "S not rank-4"
assert all(omega(Xbar, g) == 0 for g in GENS), "Xbar not in S^perp"
assert all(omega(Zbar, g) == 0 for g in GENS), "Zbar not in S^perp"
assert Xbar not in set(S) and Zbar not in set(S), "logical in S (trivial)"
assert omega(Xbar, Zbar) == 1, "logical X,Z must anticommute"

def reconstructable(L, A):
    """Is logical L reconstructable on region A?  I.e. does some coset rep
    L + s  (s in S) have support contained in A?"""
    Aset = frozenset(A)
    return any(support(xor(L, s)) <= Aset for s in S)

def bulk_recon(A):
    return reconstructable(Xbar, A) and reconstructable(Zbar, A)

# --- sweep all regions ---
print(f"[[5,1,3]] perfect code in Sp({2*N},F2):  S isotropic dim 4, "
      f"logical = S^perp/S (dim 2), omega(Xbar,Zbar)=1.\n")

by_size = {k: {"recon": 0, "total": 0} for k in range(N+1)}
detail_threshold = None
for k in range(N+1):
    for A in combinations(range(N), k):
        r = bulk_recon(A)
        by_size[k]["total"] += 1
        by_size[k]["recon"] += int(r)

print("region size |A| | regions reconstructing bulk / total")
print("-"*48)
for k in range(N+1):
    d = by_size[k]
    mark = ""
    if d["recon"] == d["total"] and d["recon"] > 0:
        mark = "  <- ALL reconstruct"
    if d["recon"] == 0:
        mark = "  <- NONE reconstruct"
    print(f"      {k}        |   {d['recon']:2d} / {d['total']:2d}{mark}")

# threshold = smallest k where all regions reconstruct
thr = min(k for k in range(N+1)
          if by_size[k]["recon"] == by_size[k]["total"] and by_size[k]["recon"] > 0)
print(f"\nSharp reconstruction threshold: bulk recoverable  <=>  |A| >= {thr}")
print(f"(= code distance d=3 corrects |A^c| <= 2 erasures; {thr} = ceil(N/2)+? )")

# --- entanglement-wedge complementarity: exactly one of A, A^c reconstructs ---
full = frozenset(range(N))
viol = 0
ties = 0
for k in range(N+1):
    for A in combinations(range(N), k):
        Ac = tuple(sorted(full - frozenset(A)))
        rA, rAc = bulk_recon(A), bulk_recon(Ac)
        if rA == rAc:
            # only legitimate when |A|==|Ac| (impossible for odd N) -> a tie
            ties += 1
            if len(A) != len(Ac):
                viol += 1
print(f"\nEntanglement-wedge complementarity check over all {2**N} regions:")
print(f"  cases where A and A^c agree on reconstruction: {ties} "
      f"(all are exact ties |A|=|A^c|, impossible for odd N={N})")
print(f"  genuine complementarity violations: {viol}")
print("  => for every bipartition, EXACTLY ONE side owns the bulk "
      "(the entanglement wedge), with a sharp |A|>=3 wall.")
