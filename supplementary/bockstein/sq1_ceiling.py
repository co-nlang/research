#!/usr/bin/env python3
"""
Does the Z/4 Bockstein leak the H^3 obstruction to H^4?  (a sharp objection)

The Pauli group is the central extension  0 -> Z/4 -> P_n -> V=(Z/2)^{2n} -> 0
(phases +1,-1,+i,-i).  The Bockstein of the *sub*-sequence  0 -> Z/2 -> Z/4 -> Z/2 -> 0
is, on mod-2 cohomology, exactly the Steenrod square  beta = Sq^1.  The framework's
family-A source is  Sq^1(omega)  (omega = the symplectic 2-cocycle, family B); i.e. the
H^3 class is *already* the Z/4-Bockstein of the H^2 class.

Objection: doesn't  beta: H^3(V;Z/2) -> H^4(V;Z/2)  leak it further, breaking the
"H^3 ceiling"?

Two decisive facts, verified here on V = (Z/2)^8  (n=4):
  (A) Sq^1 . Sq^1 = 0  (Adem)  =>  beta(Sq^1 omega) = Sq^1(Sq^1 omega) = 0.   (no leak)
  (B) On V=(Z/2)^{2n}, H^*(V;F_2)=F_2[x_1..x_{2n}] is Sq^1-ACYCLIC in positive degrees
      (ker Sq^1 = im Sq^1), because H^*(V;Z) has exponent 2 (no Z/4 torsion) so the
      Bockstein spectral sequence collapses at E_2.  => the Bockstein has NO ROOM to
      manufacture a new obstruction in H^3 or H^4.

Pure F2 (Python-int bitsets); no deps.
"""
from itertools import combinations_with_replacement

NV = 8  # 2n with n=4

def monomials(d):
    """degree-d monomials in NV vars as exponent tuples."""
    out = []
    for combo in combinations_with_replacement(range(NV), d):
        e = [0]*NV
        for i in combo: e[i] += 1
        out.append(tuple(e))
    return out

def sq1_mono(m):
    """Sq^1 (derivation, Sq^1 x_i = x_i^2): m -> { m+e_i : m[i] odd }."""
    res = []
    for i in range(NV):
        if m[i] % 2 == 1:
            mm = list(m); mm[i] += 1; res.append(tuple(mm))
    return res

def sq1_poly(poly):
    """poly = set of monomials (F2 coeffs). Returns Sq^1(poly) as a set (xor)."""
    acc = set()
    for m in poly:
        for t in sq1_mono(m):
            acc ^= {t}
    return acc

# ---------- (A) Sq^1 . Sq^1 (omega) = 0 ----------
omega = {tuple(1 if j in (i, i+4) else 0 for j in range(NV)) for i in range(4)}
s1 = sq1_poly(omega)
s2 = sq1_poly(s1)
print("(A) beta = Sq^1 on the symplectic class omega = sum x_i x_{i+4}:")
print(f"    Sq^1(omega):     {len(s1)} monomials (all degree 3)   [the family-A source n_a]")
print(f"    Sq^1(Sq^1 omega): {len(s2)} monomials   => beta(n_a) = beta(beta(omega)) = {'0' if not s2 else s2}")
print(f"    beta^2 = 0 confirmed: {s2 == set()}   (Adem Sq^1 Sq^1 = 0)\n")

# ---------- (B) Sq^1-cohomology of F_2[x_1..x_8] in degrees 3, 4 ----------
def f2_rank(cols):
    """rank over F2 of a set of bit-vectors (Python ints)."""
    basis = []
    for v in cols:
        for b in basis:
            v = min(v, v ^ b)
        if v: basis.append(v); basis.sort(reverse=True)
    return len(basis)

def sq1_rank(d):
    """rank of Sq^1 : C^d -> C^{d+1}."""
    src = monomials(d); tgt = monomials(d+1)
    idx = {m: k for k, m in enumerate(tgt)}
    cols = []
    for m in src:
        v = 0
        for t in sq1_mono(m):
            v |= 1 << idx[t]
        cols.append(v)
    return f2_rank(cols), len(src), len(tgt)

print("(B) Sq^1-cohomology of H^*(V;F_2)=F_2[x_1..x_8], V=(Z/2)^8:")
dims = {d: len(monomials(d)) for d in range(2, 6)}
r = {}
for d in (2, 3, 4):
    r[d], _, _ = sq1_rank(d)
    print(f"    dim C^{d} = {dims[d]:3d};  rank(Sq^1: C^{d}->C^{d+1}) = {r[d]}")

# H^d(Sq^1) = dim C^d - rank(C^d->C^{d+1}) - rank(C^{d-1}->C^d)
H3 = dims[3] - r[3] - r[2]
H4 = dims[4] - r[4] - r[3]
print(f"\n    Sq^1-cohomology  H^3 = {H3}    H^4 = {H4}")
print(f"    => acyclic in degrees 3,4: {H3 == 0 and H4 == 0}")
print("""
CONCLUSION
  (A) The H^3 class is itself the Z/4-Bockstein of the H^2 class (n_a = Sq^1 omega), and
      Sq^1.Sq^1 = 0, so the very Bockstein the objection invokes ANNIHILATES it:
      beta(n_a) = 0. It does not reach H^4.
  (B) H^*(V;F_2) is Sq^1-acyclic in positive degrees (H^3 = H^4 = 0 above): H^*(V;Z) has
      exponent 2 (no Z/4 torsion), so the Bockstein spectral sequence collapses at E_2 and
      the Bockstein has no room to create a NEW obstruction in H^3 or H^4.

  => The H^3 ceiling is NOT an F_2 artifact. It is controlled by beta^2 = 0 -- a fact about
     the Z/4 structure itself. The leak-to-H^4 mechanism self-annihilates.

  Honest residue:
  - "no leak" is contingent on n_a being Sq^1-CLOSED -- i.e. on n_a = Sq^1 omega, which is
    exactly Direction D (the open comparison map, item 23). If n_a were NOT Sq^1-closed,
    beta(n_a) != 0 and the objection would bite. So the objection sharpens precisely to the
    framework's own open capstone, not to a coefficient-ring mistake.
  - A genuinely non-bilinear, non-Bockstein arity-5 invariant is separately open (item 21).
""")
