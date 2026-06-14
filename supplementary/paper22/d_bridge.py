"""Direction D, first strike: the algebraic skeleton of the A<->B bridge.

Unifying machine: LHS spectral sequence of the Heisenberg extension
  1 -> Z_2 -> P_n -> V=F_2^{2n} -> 1.
Base H*(V;F_2) = F_2[x_1..x_{2n}] (elementary abelian 2-group; polynomial ring,
deg x_i = 1).  Transgression of the fiber generator = the symplectic 2-cocycle
  omega = sum_{i=1}^{n} x_i x_{i+n}  in  H^2(V)   (= family-B / KS central-extension /
Mermin-square class).  Candidate family-A (H^3) source: the Steenrod square Sq^1 omega.

Steenrod action on the polynomial ring (Cartan + Sq^1 x = x^2):
  Sq^1 is a derivation, Sq^1(x_i) = x_i^2.
This script computes omega, Sq^1 omega, omega^2 (= Sq^2 omega) over F_2 for small n,
verifies Sq^1 omega is a nonzero H^3(V) class and prints its monomials -- the algebraic
candidate that must restrict to the pentagram's n_a (N_anti mod 2).
"""
from itertools import combinations

# polynomial over F2 = set of monomials; monomial = tuple of exponents (length 2n)
def mono_mul(a, b): return tuple(x + y for x, y in zip(a, b))
def poly_add(P, Q): return P ^ Q                     # symmetric difference (F2)
def poly_mul(P, Q):
    R = set()
    for a in P:
        for b in Q:
            m = mono_mul(a, b)
            R ^= {m}
    return R
def sq1(P, m2n):
    """Sq^1 as a derivation with Sq^1 x_i = x_i^2."""
    R = set()
    for mono in P:
        for i in range(m2n):
            if mono[i] % 2 == 1:                     # d/dx_i nonzero mod 2
                nm = list(mono); nm[i] += 1
                R ^= {tuple(nm)}
    return R
def deg(mono): return sum(mono)
def show(P, names):
    if not P: return "0"
    terms = []
    for mono in sorted(P):
        s = "".join(f"{names[i]}{'^'+str(e) if e>1 else ''}" for i, e in enumerate(mono) if e)
        terms.append(s or "1")
    return " + ".join(terms)

def run(n):
    m = 2 * n
    names = [f"x{i+1}" for i in range(m)]
    e = lambda i: tuple(1 if k == i else 0 for k in range(m))
    omega = set()
    for i in range(n):
        omega ^= {mono_mul(e(i), e(i + n))}          # x_i x_{i+n}
    s1 = sq1(omega, m)
    s2 = poly_mul(omega, omega)                       # omega^2 = Sq^2 omega
    print(f"  n={n} (V=F_2^{m}):")
    print(f"    omega (H^2) = {show(omega, names)}   [{len(omega)} terms]")
    print(f"    Sq^1 omega (H^3) = {show(s1, names)}")
    print(f"      -> {len(s1)} monomials, all degree { {deg(x) for x in s1} }, nonzero={len(s1)>0}")
    print(f"    omega^2 (H^4) = {len(s2)} terms (deg { {deg(x) for x in s2} })")

if __name__ == "__main__":
    print("=== D bridge skeleton: omega, Sq^1 omega in H*(V;F_2) ===")
    for n in (2, 3, 4):
        run(n)
    print("\n  Sq^1 omega = sum_i (x_i^2 x_{i+n} + x_i x_{i+n}^2): a nonzero H^3(V) class,")
    print("  the candidate source whose restriction to the pentagram nerve must equal n_a.")
