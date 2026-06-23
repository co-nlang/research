#!/usr/bin/env python3
"""
Item 21, arity-5 resonance: the degree-matching follows from naturality + REPRESENTABILITY.

The resonance step item 21 relied on -- "genuine arity-5 obstruction => a degree-4 AMBIENT O-class"
(so it is bounded by H^4(BV)^O = <q^2>) -- comes down to a DEGREE-MATCHING: why must the ambient class
have polynomial degree exactly 4? The clean answer is REPRESENTABILITY of natural operations (Yoneda):
a NATURAL (functorial), O-invariant, pointwise-cohomological assignment of degree-k cochains is
represented by an element of H^k(BV)^O -- degree-matched automatically. So the resonance step is NOT
independent of the naturality [CONDITION]; it FOLLOWS from it. The two residuals collapse toward one.

Representability makes a sharp, falsifiable prediction that EXCLUDES the incidence over-counters a SECOND
way (independent of phase_blind):

  The climbing over-counter A_w (weight enumerator of the relation code R) is GL(2n,F2)-invariant
  (phase_blind.py). IF A_w were a natural ambient class, it would live in H*(BV)^{GL} = the DICKSON
  algebra. But Dickson invariants of GL(m,F2) sit only in degrees {2^m - 2^i : 0<=i<m}; for m=2n the
  LOWEST is 2^{2n} - 2^{2n-1} = 2^{2n-1} (=8 at n=2, 32 at n=3, ...). So H^d(BV)^{GL}=0 for 0<d<2^{2n-1},
  in particular H^4(BV)^{GL}=0 for all n>=2. Hence A_w (nonzero as a config function) is NOT a natural
  ambient class -- it is not pointwise-cohomological (R is a *relational/incidence* datum, not the
  evaluation of a fixed polynomial). This is exactly why representability excludes it.

This script VERIFIES dim H^d(BV)^{GL(2n,F2)} by degree (simultaneous fixed space under all elementary
GL-transvections x_i -> x_i + x_j), confirming 0 below the lowest Dickson degree -- in particular
H^4 = 0 -- contrasted with H^d(BV)^O (from sp_invariants) which carries q (deg2), Sq^1 q (deg3),
q^2 (deg4). Reuses sp_invariants helpers.
"""
from itertools import product
from sp_invariants import make_omega, mono_basis, subst_monomial, fixed_space


def gl_transvections(N):
    """Elementary GL(N,F2) transvections as (vvec, Lv): x_i -> x_i + x_j, i != j.
    Encoded for subst_monomial: vvec = e_i (only x_i is substituted), Lv = {e_j} (add x_j)."""
    out = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            vvec = tuple(1 if t == i else 0 for t in range(N))
            Lv = {tuple(1 if t == j else 0 for t in range(N))}
            out.append((vvec, Lv))
    return out


def fixed_space_gl(N, d, transvecs):
    """dim of simultaneous fixed space under GL elementary transvections, given as (vvec,Lv) pairs.
    Same row-stacking kernel as sp_invariants.fixed_space, but the substitution is supplied directly."""
    basis = mono_basis(N, d)
    idx = {m: i for i, m in enumerate(basis)}
    B = len(basis)
    eqrows = []
    for (vvec, Lv) in transvecs:
        rowsets = [0] * B
        for m in basis:
            i = idx[m]
            for mm in (subst_monomial(m, N, vvec, Lv) ^ {m}):   # (T - I)(m)
                rowsets[idx[mm]] ^= (1 << i)
        eqrows.extend(r for r in rowsets if r)
    piv = []
    for r in eqrows:
        x = r
        for p in piv:
            x = min(x, x ^ p)
        if x:
            piv.append(x); piv.sort(reverse=True)
    return B - len(piv)


def run(n, dmax=6):
    N = 2 * n
    _, omega = make_omega(n)
    qf = lambda v: sum(v[2 * k] & v[2 * k + 1] for k in range(n)) & 1
    transv_o = [v for v in product((0, 1), repeat=N) if any(v) and qf(v) == 1]
    gl_tv = gl_transvections(N)
    lowest_dickson = 1 << (N - 1)   # 2^{2n-1}
    print(f"  n={n} (N={N}): lowest Dickson(GL) degree = {lowest_dickson}; "
          f"|GL-transv|={len(gl_tv)}, |O-transv|={len(transv_o)}", flush=True)
    for d in range(1, dmax + 1):
        dgl = fixed_space_gl(N, d, gl_tv)
        do, _, _ = fixed_space(N, d, transv_o, omega)
        flag = ""
        if d == 4:
            flag = "  <== deg 4: H^GL must be 0 (A_w cannot be a natural ambient class); H^O = <q^2>"
        print(f"    deg {d}: dim H^d(BV)^GL = {dgl},   dim H^d(BV)^O = {do}{flag}", flush=True)


if __name__ == "__main__":
    print(__doc__, flush=True)
    print("=== representability check: H^d(BV)^GL = 0 below Dickson (so A_w is not a natural class) ===",
          flush=True)
    run(2)
    run(3)
