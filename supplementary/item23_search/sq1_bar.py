#!/usr/bin/env python3
"""
THE LAST STEP (V-side convention pin): verify, in the bar complex of V = F_2^{2n}, that the
Steenrod cup-1 self-product of the extension cocycle equals Sq^1(omega) -- i.e. that the explicit
quadratic-refinement object we use IS the standard lowest Steenrod square, with NO hand-waving.

  - extension cocycle (cup cocycle of the Heisenberg / extra-special 2-group):
        c(g1,g2) = X_{g1} . Z_{g2}   (mod 2)          [a 2-cochain; [c] = omega = sum_i a_i b_i]
        q(v)     = c(v,v) = X_v . Z_v                   [the diagonal = quadratic refinement]
  - Steenrod cup-1 (the chain-level Sq^1 of a 2-cocycle), Steenrod's simplicial formula:
        (c cup_1 c)(g1,g2,g3) = c(g1, g2+g3) c(g2,g3)  +  c(g1+g2, g3) c(g1,g2)
  - the target class, Sq^1(omega) as a polynomial in H^3(BV;F_2)= F_2[a_i,b_i]:
        Sq^1(omega) = Sq^1(sum_i a_i b_i) = sum_i a_i b_i (a_i + b_i)   (Cartan + Sq^1 a = a^2)
    as an Alexander-Whitney 3-cochain:
        P(g1,g2,g3) = sum_i X_{g1}[i] (X_{g2}[i] + Z_{g2}[i]) Z_{g3}[i]

We verify:
  (1) c cup_1 c is a 3-COCYCLE (delta = 0)        -- it represents a class in H^3.
  (2) P is a 3-cocycle and is NONZERO              -- Sq^1 omega != 0.
  (3) [c cup_1 c] = [P] in H^3(V;F_2)             -- i.e. (c cup_1 c) + P = delta(r) is solvable.
That triple is exactly  "the quadratic-refinement defect cochain = the standard Sq^1 omega."

Combined with the PROVEN configuration-side identity (n_a)_m = q(S_m) (+) XOR q(rays)
(closed_form.py, 123,000/123,000) and the Kudo transgression tau(t^2)=Sq^1 omega of the
Heisenberg LHS spectral sequence, this closes the Direction-D bridge n_a = <Sq^1 omega,[K_5]>.

Pure Python; F_2 Gaussian elimination via Python ints as bit-vectors.
"""
import sys
from itertools import product

def bits(x, n):           # low n bits as list
    return [(x >> i) & 1 for i in range(n)]

def run(n):
    N = 2 * n
    SZ = 1 << N
    def X(g): return g & ((1 << n) - 1)
    def Z(g): return (g >> n) & ((1 << n) - 1)
    def c(g1, g2):        # X_{g1} . Z_{g2} mod 2
        return bin(X(g1) & Z(g2)).count('1') & 1
    def cup1(g1, g2, g3): # Steenrod cup-1 of c with itself
        return (c(g1, g2 ^ g3) & c(g2, g3)) ^ (c(g1 ^ g2, g3) & c(g1, g2))
    def P(g1, g2, g3):    # Sq^1 omega = sum_i X1[i](X2[i]+Z2[i])Z3[i]
        x1, x2, z2, z3 = X(g1), X(g2), Z(g2), Z(g3)
        return bin(x1 & (x2 ^ z2) & z3).count('1') & 1

    # delta of a 3-cochain f -> 4-cochain (should be 0 for a cocycle)
    def is_cocycle3(f):
        for g1, g2, g3, g4 in product(range(SZ), repeat=4):
            v = (f(g2, g3, g4) ^ f(g1 ^ g2, g3, g4) ^ f(g1, g2 ^ g3, g4)
                 ^ f(g1, g2, g3 ^ g4) ^ f(g1, g2, g3))
            if v: return False
        return True

    cocy_cup1 = is_cocycle3(cup1)
    cocy_P = is_cocycle3(P)
    nz_P = any(P(g1, g2, g3) for g1, g2, g3 in product(range(SZ), repeat=3))
    nz_cup1 = any(cup1(g1, g2, g3) for g1, g2, g3 in product(range(SZ), repeat=3))

    # cohomologous?  solve delta(r) = cup1 + P  for a 2-cochain r : V^2 -> F_2.
    # unknowns: r[(a,b)] indexed 0..SZ^2-1 ; equations: one per (g1,g2,g3).
    def idx2(a, b): return a * SZ + b
    NV2 = SZ * SZ
    rows = []  # each row: (set of unknown indices, rhs bit)
    for g1, g2, g3 in product(range(SZ), repeat=3):
        # (delta r)(g1,g2,g3) = r(g2,g3)+r(g1+g2,g3)+r(g1,g2+g3)+r(g1,g2)
        terms = [idx2(g2, g3), idx2(g1 ^ g2, g3), idx2(g1, g2 ^ g3), idx2(g1, g2)]
        acc = 0
        for t in terms: acc ^= (1 << t)
        rhs = cup1(g1, g2, g3) ^ P(g1, g2, g3)
        rows.append((acc, rhs))
    # Gaussian elimination over F_2 (augmented bit = bit at position NV2)
    AUG = NV2
    mat = [(a | (rhs << AUG)) for (a, rhs) in rows]
    pivots = {}
    for r in mat:
        cur = r
        # reduce by existing pivots
        for col, prow in pivots.items():
            if (cur >> col) & 1:
                cur ^= prow
        # find leading column in [0, NV2)
        body = cur & ((1 << NV2) - 1)
        if body == 0:
            if (cur >> AUG) & 1:
                print(f"  n={n}: INCONSISTENT row -> NOT cohomologous"); return
            continue
        col = (body & -body).bit_length() - 1
        # normalize other stored pivots against this one
        for pc in list(pivots):
            if (pivots[pc] >> col) & 1:
                pivots[pc] ^= cur
        pivots[col] = cur
    cohomologous = True  # no inconsistent row found
    print(f"  n={n}: cup1 cocycle={cocy_cup1}, P cocycle={cocy_P}, "
          f"P!=0={nz_P}, cup1!=0={nz_cup1}, "
          f"[cup1]==[Sq^1 omega]: {'YES' if cohomologous else 'NO'} "
          f"(solved delta r = cup1+P, {len(pivots)} pivots / {NV2} unknowns)", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(1)   # V = F_2^2, |V|=4
    run(2)   # V = F_2^4, |V|=16
