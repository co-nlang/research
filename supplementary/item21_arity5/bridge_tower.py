#!/usr/bin/env python3
"""
Item 21, Direction-D bridge: the AMBIENT invariant generators ARE the Kudo transgression tower.

Lemma A (sp_invariants.py) computed the DIMENSIONS of H^d(BV)^O by degree: 2,3,(4=q^2),5,...
with a 1-dim degree-4 = <q^2> (decomposable) and a 2-dim degree-5. That establishes the degree
PATTERN {2}u{1+2^i} -- generators skip degree 4. But the D-bridge needs MORE than the dimensions:
it needs the generators to BE the transgression tower of the LHS spectral sequence of the
extra-special extension  1 -> Z/2 -> H -> V -> 1, i.e. the Kudo tower

    q (=omega, deg2),  Sq^1 q (=n_a, deg3),  Sq^2 Sq^1 q (=xi_2, deg5),  Sq^4 Sq^2 Sq^1 q (deg9), ...

(transgressions tau(t)=omega, tau(t^2)=Sq^1 omega, tau(t^4)=Sq^2 Sq^1 omega, ... -- Kudo). Degrees
2,3,5,9,17 = {2} u {1+2^i}. The DEGREE-4 GAP is then STRUCTURAL: no power of t transgresses into
degree 4 (the next after t^2->deg3 is t^4->deg5), so there is NO genuine arity-5/H^4 obstruction;
the only degree-4 ambient class is q^2 = Sq^2 q (a cup-square = family B, decomposable).

This script VERIFIES the load-bearing identification THROUGH DEGREE 5 (the first place the tower
could have failed -- a degree-5 generator unrelated to Sq^2 Sq^1 q would break "generators = tower"):

  (T1) q, Sq^1 q, Sq^2 Sq^1 q are each genuine O-invariants (fixed by ALL orthogonal transvections).
  (T2) DEGREE 4: the O-invariant space is 1-dim = <q^2>, and q^2 = Sq^2 q (decomposable); NO tower
       element lands in degree 4 (Sq^1 Sq^1 q = 0 by Adem -- checked as a polynomial identity).
  (T3) DEGREE 5: the O-invariant space is 2-dim, spanned by { q.Sq^1 q (decomposable), Sq^2 Sq^1 q }
       with Sq^2 Sq^1 q INDECOMPOSABLE (not in <q.Sq^1 q>). So the degree-5 generator IS the third
       Kudo transgression -- the tower is exactly the generator set through degree 5.

Steenrod squares via the TOTAL square Sq = ring hom with Sq(x_i)=x_i + x_i^2 on H*(BV)=F2[x_0..x_{2n-1}]
(polynomial -- B(Z/2) has polynomial cohomology). Sq^j P = degree-(deg P + j) part of Sq(P).
Pure Python; polynomials = sets of exponent tuples over F2. Reuses sp_invariants helpers.
"""
from itertools import product
from sp_invariants import make_omega, pmul, ppow, mono_basis, subst_monomial


def total_sq_monomial(exp, N):
    """Sq(x^exp) = prod_i (x_i + x_i^2)^{exp_i} = prod_i x_i^{exp_i}(1+x_i)^{exp_i}; F2 set of exps."""
    res = {tuple(0 for _ in range(N))}
    for i in range(N):
        e = exp[i]
        if e == 0:
            continue
        # (x_i + x_i^2)^e = sum_{j: C(e,j) odd} x_i^{e+j}
        factor = set()
        for j in range(e + 1):
            # C(e,j) mod 2 = 1 iff (j & ~e)==0  (Lucas)
            if (j & ~e) == 0:
                m = [0] * N
                m[i] = e + j
                factor ^= {tuple(m)}
        res = pmul(res, factor, N)
    return res


def total_sq(poly, N):
    out = set()
    for m in poly:
        out ^= total_sq_monomial(m, N)
    return out


def sq(poly, j, N, base_deg):
    """Sq^j(poly): degree-(base_deg + j) part of the total square."""
    full = total_sq(poly, N)
    target = base_deg + j
    return {m for m in full if sum(m) == target}


def poly_q(n, N):
    p = set()
    for k in range(n):
        m = [0] * N; m[2 * k] = 1; m[2 * k + 1] = 1
        p ^= {tuple(m)}
    return p


def is_O_fixed(poly, N, transv_o, omega):
    """True iff poly is fixed by every orthogonal transvection T_v."""
    for v in transv_o:
        Lv = set()
        for j in range(N):
            ej = tuple(1 if t == j else 0 for t in range(N))
            if omega(ej, v):
                Lv ^= {tuple(1 if t == j else 0 for t in range(N))}
        img = set()
        for m in poly:
            img ^= subst_monomial(m, N, v, Lv)
        if img != poly:
            return False
    return True


def in_span(target, polys, N, d):
    """Is degree-d poly `target` in the F2-span of `polys`? (gaussian over the monomial basis)"""
    basis = mono_basis(N, d); idx = {m: i for i, m in enumerate(basis)}
    def vec(p):
        x = 0
        for m in p:
            x ^= 1 << idx[m]
        return x
    piv = []
    for p in polys:
        x = vec(p)
        for q in piv:
            x = min(x, x ^ q)
        if x:
            piv.append(x); piv.sort(reverse=True)
    t = vec(target)
    for q in piv:
        t = min(t, t ^ q)
    return t == 0


def run(n):
    N, omega = make_omega(n)
    def qf(v):
        return sum(v[2 * k] & v[2 * k + 1] for k in range(n)) & 1
    transv_o = [v for v in product((0, 1), repeat=N) if any(v) and qf(v) == 1]

    q = poly_q(n, N)
    sq1q = sq(q, 1, N, 2)          # deg 3
    sq2sq1q = sq(sq1q, 2, N, 3)    # deg 5
    sq2q = sq(q, 2, N, 2)          # deg 4 (should equal q^2)
    q2 = ppow(q, 2, N)
    qsq1q = pmul(q, sq1q, N)       # deg 5 decomposable
    sq1sq1q = sq(sq1q, 1, N, 3)    # deg 4 -- Adem: must be 0

    print(f"  n={n}  (N={N}, |O-transv|={len(transv_o)}):", flush=True)

    # (T1) genuine O-invariants
    for name, p, dg in [("q", q, 2), ("Sq^1 q", sq1q, 3), ("Sq^2 Sq^1 q", sq2sq1q, 5)]:
        ok = is_O_fixed(p, N, transv_o, omega)
        print(f"    [T1] {name:12s} deg {dg}: nonzero={bool(p)}, O-invariant={ok}", flush=True)

    # (T2) degree 4: q^2 = Sq^2 q, decomposable; Sq^1 Sq^1 q = 0 (Adem)
    print(f"    [T2] Sq^2 q == q^2 : {sq2q == q2}   (q^2 decomposable, family B)", flush=True)
    print(f"    [T2] Sq^1 Sq^1 q == 0 (Adem, no deg-4 tower element): {sq1sq1q == set()}", flush=True)

    # (T3) degree 5: Sq^2 Sq^1 q indecomposable (not in <q . Sq^1 q>)
    decomp5 = [qsq1q]
    indecomp = not in_span(sq2sq1q, decomp5, N, 5)
    print(f"    [T3] Sq^2 Sq^1 q nonzero={bool(sq2sq1q)}, "
          f"indecomposable (not in <q.Sq^1 q>)={indecomp}", flush=True)
    # and {q.Sq^1 q, Sq^2 Sq^1 q} independent => they span the 2-dim deg-5 O-invariant space
    indep = not in_span(qsq1q, [sq2sq1q], N, 5) and bool(qsq1q)
    print(f"    [T3] {{q.Sq^1 q, Sq^2 Sq^1 q}} independent (= span the dim-2 deg-5 O-space): "
          f"{indep and indecomp}", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== D-bridge: ambient O-generators ARE the Kudo transgression tower (through deg 5) ===",
          flush=True)
    run(2)
    run(3)
    run(4)
