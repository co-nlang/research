#!/usr/bin/env python3
"""
A CLOSED FORM for the family-A class, found by following the collaborator's lead
(q "almost" determines a -> the Bockstein/Z4 layer; inspect the sparse failures).

  N_anti mod 2  ==  q(T)  XOR  XOR_i q(v_i),     T = XOR of the 10 rays,
  q(v) = parity(X_v . Z_v)   (any quadratic refinement of omega does).

And the COCHAIN-level (per-tetrahedron) form, which is what item 23's pairing needs
(<Sq^1 omega,[K5]> = XOR_m (n_a)_m):

  (n_a)_m mod 2  ==  q(S_m)  XOR  XOR_{6 rays of tetra m} q(v),   S_m = XOR of those 6 rays.

Same proof per tetrahedron (polarization of q on the 6 rays among the 4 vertices != m; their
3 disjoint pairs = (n_a)_m, the 12 adjacent pairs vanish).  Verified 123,000/123,000 per-tetra
checks EXACT at n=4,5,6.  Summing over m recovers the total (T = XOR_m S_m up to ray multiplicity).

This is EXACT and provable for ALL n (elementary):
  (1) q is a quadratic refinement: q(u+v) = q(u) + q(v) + omega(u,v)
      [parity((Xu+Xv)(Zu+Zv)) = q(u)+q(v) + f(u,v)+f(v,u), and f(u,v)+f(v,u)=omega(u,v)].
  (2) Polarization (induction): q(XOR_i v_i) = XOR_i q(v_i)  XOR  XOR_{i<j} omega(v_i,v_j).
  (3) Composable (shared-Lagrangian) ray pairs commute: omega = 0 (phi_omega_zero.py).
      So XOR_{i<j over all 10 rays} omega(v_i,v_j) = XOR_{disjoint pairs} omega = N_anti mod 2.
  => N_anti mod 2 = q(T) XOR XOR_i q(v_i).   QED (all n).

Verified: 24,600/24,600 configs EXACT at n=4,5,6.

WHAT IT IS / IS NOT (honest):
  - It corrects the earlier overstated "no cochain-level summary statistic determines a":
    a IS determined -- by the 11-bit q-summary {q(v_1..v_10), q(T)}. The earlier collision
    keys had the per-ray q(v_i) but were MISSING the GLOBAL term q(T) (q of the sum). The
    collaborator's wording caution was right: the failures were "every LOCAL/low-arity
    candidate tested fails", not a universal impossibility. (No contradiction with the
    Paper XIX modulus: q(T) is a GLOBAL/arity-10 functional, not a low-arity invariant.)
  - It is the AMBIENT/unconditional form of Paper XIX's intrinsic Q(T)=N_anti (noq_odd_proof
    S5): with the intrinsic Q, Q(rays)=0 so Q(T)=N_anti directly; with the ambient q the
    correction XOR_i q(v_i) appears, and no "intrinsic-q exists" hypothesis is needed.
  - It does NOT by itself close item 23 (the cohomological bridge N_anti=<Sq^1 omega,[K5]>):
    the q's are frame-dependent (q is not Sp-invariant; only the net combination is), so this
    is a COORDINATE closed form, not the intrinsic Steenrod identity. But q is exactly the Z/4
    lift of omega and Sq^1 omega = beta_{Z/4}(omega), so this is the explicit q-handle the
    beta_{Z/4}(q) direction predicted; the remaining open step is to identify
    q(T) XOR XOR_i q(v_i) with the chain-level <Sq^1 omega, [K5]> -- both sides now explicit.

Pure Python (reuses paper22/nerve_cochain.build); no deps.
"""
import sys, time
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def make_q(N):
    MSK = (1 << N) - 1
    def q(v): return bin((v & MSK) & ((v >> N) & MSK)).count('1') & 1   # parity(X . Z)
    return q

def run(N, n_lag, seeds, cap, budget):
    symp, gen, k5s, mu_triple = build(N); q = make_q(N)
    res = Counter(); per = Counter(); t0 = time.time()
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(21000 + 11*s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            def R(i, j): return sh[(i, j)] if i < j else sh[(j, i)]
            rays = [R(i, j) for i, j in combinations(range(5), 2)]
            T = 0
            for r in rays: T ^= r
            Na = 0
            for m in range(5):
                t = [x for x in range(5) if x != m]; a, b, c, d = t
                prs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
                Na += sum(1 for (p, qq) in prs if symp(R(*p), R(*qq)))
            rhs = q(T)
            for r in rays: rhs ^= q(r)
            res[(Na & 1) == rhs] += 1
            # per-tetrahedron (cochain) form
            for m in range(5):
                verts = [x for x in range(5) if x != m]
                r6 = [R(i, j) for i, j in combinations(verts, 2)]
                S = 0
                for r in r6: S ^= r
                pr = q(S)
                for r in r6: pr ^= q(r)
                a, b, c, d = verts
                prs = [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]
                lhs = sum(1 for (p, qq) in prs if symp(R(*p), R(*qq))) & 1
                per[lhs == pr] += 1
        if time.time() - t0 > budget: break
    tot = res[True] + res[False]; ptot = per[True] + per[False]
    print(f"  n={N}: configs={tot}, TOTAL N_anti==q(T)^XORq(v_i): {res[True]}/{tot} "
          f"({'EXACT' if res[False] == 0 else 'FAILS ' + str(res[False])}); "
          f"PER-TETRA (n_a)_m==q(S_m)^XORq(6): {per[True]}/{ptot} "
          f"({'EXACT' if per[False] == 0 else 'FAILS ' + str(per[False])})", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    for N, nl, sd, cp, bd in [(4,1200,4,1500,30), (5,3000,6,2500,55), (6,2500,4,1800,45)]:
        run(N, nl, sd, cp, bd)
