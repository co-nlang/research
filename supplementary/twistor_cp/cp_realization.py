#!/usr/bin/env python3
"""
Item 13 (Paper VIII, Sec.3): is there a geometric realization of the n-qubit
obstruction ladder on CP^{2^n - 1}, and what is the target class?

Setup.  H^*(CP^N; F2) = F2[h]/h^{N+1}, |h|=2: concentrated in EVEN degree, and
  Sq^1 h = 0   (h = c_1(O(1)) mod 2 is the reduction of an integral class),
  Sq^2 h = h^2 (top square of a degree-2 class).
So CP^N is Sq^1-ACYCLIC; its entire Steenrod structure is the Sq^2 / cup-power
ladder h, h^2, h^3, ...

Framework side.  H^*(V; F2) = F2[x_1..x_{2n}], |x_i|=1.  The family-B class is the
symplectic form  omega = sum_i x_i x_{i+n}  in H^2 (the Heisenberg/KS extension
class, Paper IV/XXII), and the family-A pentagram class is  n_a = Sq^1(omega)  in
H^3 (Direction D, Paper XXII Outlook; bockstein/).

Paper VIII Thm 2.1 realizes the family-B generator as h (the Peres-Mermin square
IS family B).  This script tests, for n=2 (CP^3) and n=3 (CP^7):

  (1) the cup-power ladder omega^k <-> h^k is the GEOMETRICALLY REALIZED part
      (family B): omega^k != 0, and its Sq^1 behaviour matches CP exactly only on
      even powers;
  (2) the identification h <-> omega is NOT a map of Steenrod modules -- it fails
      already at the generator, with obstruction  Sq^1 omega = n_a != 0  while
      Sq^1 h = 0.  Equivalently, omega does NOT lift to an integral class
      (obstruction = the integral Bockstein beta omega = Sq^1 omega = n_a).
  => The family-A H^3 Borromean class has NO faithful realization on CP^{2^n-1};
     the geometric/twistor side hosts Sq^2 (family B) but is blind to Sq^1
     (family A).  This is the geometric face of items 23/24.

Pure F2 (exponent-tuple monomials, set = F2 coeffs); no deps.
"""

def mul(p, q):
    """Product of two F2 polynomials (sets of exponent tuples) over F2."""
    acc = set()
    for a in p:
        for b in q:
            m = tuple(ai + bi for ai, bi in zip(a, b))
            acc ^= {m}            # F2: a monomial appearing twice cancels
    return acc

def power(p, k):
    r = {tuple([0]*NV)}           # the constant 1
    for _ in range(k):
        r = mul(r, p)
    return r

def sq1(poly):
    """Sq^1 as a derivation, Sq^1 x_i = x_i^2 :  m -> sum_{i: m_i odd} (m + e_i)."""
    acc = set()
    for m in poly:
        for i in range(NV):
            if m[i] % 2 == 1:
                mm = list(m); mm[i] += 1; acc ^= {tuple(mm)}
    return acc

def deg(poly):
    return None if not poly else sum(next(iter(poly)))


def run(n):
    global NV
    NV = 2 * n
    N = 2**n - 1                                  # CP^N = CP^{2^n - 1}
    omega = {tuple(1 if j in (i, i + n) else 0 for j in range(NV)) for i in range(n)}
    n_a = sq1(omega)
    print(f"\n{'='*70}\n  n = {n} qubits   ->   target CP^{N}  (H^* = F2[h]/h^{N+1}, |h|=2)")
    print(f"{'='*70}")
    print(f"  omega = sum x_i x_(i+{n})  :  {len(omega)} monomials in H^2(V)")
    print(f"  n_a = Sq^1(omega)          :  {len(n_a)} monomials in H^3(V)   "
          f"(family-A class) -> nonzero: {bool(n_a)}")

    print(f"\n  (1) cup-power ladder  omega^k  (the family-B / geometric part):")
    print(f"      {'k':>2} | {'deg':>3} | {'omega^k != 0':>12} | {'Sq^1(omega^k)':>13} | matches h^k on CP^{N}?")
    print(f"      {'-'*2}-+-{'-'*3}-+-{'-'*12}-+-{'-'*13}-+--------------------")
    for k in range(1, N + 2):                     # include k=N (top) and k=N+1 (truncates)
        wk = power(omega, k)
        s = sq1(wk)
        cp_alive = (k <= N)                        # h^k != 0 on CP^N iff k <= N
        # On CP^N, Sq^1(h^k) = 0 always (Sq^1 h = 0, Cartan).
        match = "Sq^1=0 like h^k" if not s else "Sq^1!=0  (UNLIKE h^k)"
        flag = "" if (bool(wk) == cp_alive) else "   <-- truncation differs"
        print(f"      {k:>2} | {deg(wk) if wk else 0:>3} | {str(bool(wk)):>12} | "
              f"{str(len(s))+' mon':>13} | {match}{flag}")

    print(f"\n  (2) Steenrod-naturality of the realization  h <-> omega:")
    print(f"      on CP^{N}:  Sq^1(h)     = 0        (h = c_1 mod 2, integral reduction)")
    print(f"      on V    :  Sq^1(omega) = n_a  ({len(n_a)} mon, != 0)")
    print(f"      => h |-> omega is a RING iso onto F2[omega], but NOT a Steenrod-module")
    print(f"         map: it fails at the generator, obstruction = n_a (family A).")

    # integral lift test: omega^k lifts to H^*(V;Z) iff its integral Bockstein
    # vanishes; a *necessary* condition is Sq^1(omega^k)=0.
    print(f"\n  (3) integral-lift obstruction (does omega^k come from a Chern class?):")
    for k in (1, 2, 3):
        if k > N + 1: break
        s = sq1(power(omega, k))
        verdict = "lifts (Sq^1=0): a c_1-power" if not s else \
                  "does NOT lift (Sq^1!=0): obstruction n_a*omega^(k-1)"
        print(f"      omega^{k}: {verdict}")
    print(f"      => omega itself is NOT a Chern class (Sq^1 omega = n_a != 0);")
    print(f"         the family-A class is the precise obstruction.")


if __name__ == "__main__":
    print(__doc__)
    for n in (2, 3):
        run(n)
    print(f"""
{'='*70}
CONCLUSION  (item 13)
{'='*70}
  The conjectured higher-differential family d_k^eff DOES exist on CP^{{2^n-1}} --
  but only as the FAMILY-B cup-power ladder h^k <-> omega^k (the Sq^2 ladder).
  Paper VIII's Thm 2.1 (h <-> Peres-Mermin class) is its k=1 case; PM is family B.

  The FAMILY-A H^3 Borromean class n_a = Sq^1(omega) has NO faithful realization
  on CP^{{2^n-1}}:
    - CP^N is Sq^1-acyclic (even degree, every class a c_1-power), so a
      Steenrod-natural realization sends n_a = Sq^1(omega) |-> Sq^1(h) = 0;
    - n_a is exactly the obstruction to omega lifting to an integral (Chern)
      class, i.e. to the family-B realization h <-> omega being natural.
  The geometric/twistor side hosts Sq^2 (family B) and is structurally BLIND to
  Sq^1 (family A) -- the same orthogonality found operationally (item 24) and
  the same A<->B / Sq^1 wall that is the open capstone (item 23), now on CP.

  Obstacle audit (Paper VIII Sec.3):
    1. "no n>=3 config"  -> DISSOLVED: the Mermin pentagram is the 3-qubit config;
       "different combinatorics" = the family A/B split, now understood.
    2. "Ext^1 of Sigma_0^(n) not computed" -> REDIRECTED: the pentagram's Cech
       nerve collapses (Paper XX); the H^3 class lives on the Maslov-Wall complex
       (partial Delta^4 = S^3), not on Sigma_0^(n) subset CP^{{2^n-1}}.
    3. "c_2(O(1))=0, need another class" -> RESOLVED: the target is the cup-POWER
       h^k = c_1^k (nonzero), not the Chern class c_k (zero for a line bundle).
""")
