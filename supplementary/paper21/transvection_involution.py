"""The foot-bit balance via the transvection involution T_{r23}.

Claim: on the L4-completions of a fixed proper K3 (L1,L2,L3), the map
   L4  |-->  L4' = T_{r23}(L4),   T_w(x) = x + omega(x,w) w,   r23 = L2 cap L3,
(i) is a fixed-point-free involution (r23 not in L4 => T(L4) != L4, T^2=id);
(ii) FIXES the feet on L2 and L3 (since r23 in L2 cap L3, both Lagrangian, T fixes
     L2 and L3 pointwise) -> b2,b3 unchanged;
(iii) FLIPS b1 = omega(v14, r23) -> hence flips Sigma = b1^b2^b3,
EXCEPT on a 'defect' set where T(L4) fails to meet L1 in dim 1 (properness broken).
The defect fraction is the O(2^-n) correction => Sigma balanced up to O(2^-n).

This script measures, over many fibers: feet-preservation, Sigma-flip rate, and the
defect fraction, at n=6 and n=8, to check the 2^-n scaling.
"""
import random, time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def study(N, n_lag, nbase, budget, seed):
    symp, *_ = build(N)
    SZ = 1 << (2*N)
    rng = random.Random(seed)
    ALL = list(range(1, SZ))
    def xspan(b):
        s = {0}
        for x in b: s |= {y ^ x for y in s}
        return s
    def rl():
        b = []; sp = {0}
        for _ in range(N):
            c = [v for v in ALL if v not in sp and all(symp(v, x) == 0 for x in b)]
            if not c: return None
            v = rng.choice(c); b.append(v); sp = xspan(b)
        return frozenset(x for x in sp if x)
    lags = []; ls = set(); t = time.time()
    while len(lags) < n_lag and time.time() - t < budget:
        L = rl()
        if L and L not in ls: ls.add(L); lags.append(L)
    def ray(A, B):
        it = A & B
        return next(iter(it)) if len(it) == 1 else None
    def transvect(L, w):
        return frozenset((x ^ w) if (symp(x, w) & 1) else x for x in L)

    feet_ok = 0; sigma_flip = 0; defect = 0; tot = 0; involution_ok = 0
    bases = 0
    for (i, j, k) in combinations(range(len(lags)), 3):
        if bases >= nbase: break
        L1, L2, L3 = lags[i], lags[j], lags[k]
        r12, r13, r23 = ray(L1, L2), ray(L1, L3), ray(L2, L3)
        if None in (r12, r13, r23) or len({r12, r13, r23}) != 3: continue
        used = False
        for L4 in lags:
            if L4 in (L1, L2, L3): continue
            r14, r24, r34 = ray(L1, L4), ray(L2, L4), ray(L3, L4)
            if None in (r14, r24, r34): continue
            if len({r12, r13, r23, r14, r24, r34}) != 6: continue
            used = True; tot += 1
            b1 = symp(r14, r23); b2 = symp(r24, r13); b3 = symp(r34, r12)
            Sig = b1 ^ b2 ^ b3
            L4p = transvect(L4, r23)
            # T^2 = id check
            if transvect(L4p, r23) == L4: involution_ok += 1
            # feet on L2,L3 preserved?
            r24p, r34p = ray(L2, L4p), ray(L3, L4p)
            if r24p == r24 and r34p == r34: feet_ok += 1
            # foot on L1 / properness
            r14p = ray(L1, L4p)
            if r14p is None:
                defect += 1
                continue
            # new Sigma
            b1p = symp(r14p, r23)
            b2p = symp(r24p if r24p else r24, r13)
            b3p = symp(r34p if r34p else r34, r12)
            Sigp = b1p ^ b2p ^ b3p
            if Sigp == (Sig ^ 1): sigma_flip += 1
        if used: bases += 1
    print(f"  N={N}: {len(lags)} Lagrangians, {bases} fibers, {tot} completions")
    print(f"    T^2=id (involution): {involution_ok}/{tot}")
    print(f"    feet on L2,L3 preserved: {feet_ok}/{tot}")
    print(f"    Sigma flips (non-defect): {sigma_flip}/{tot}")
    print(f"    DEFECT (T L4 not proper on L1): {defect}/{tot} = {defect/tot:.4f}"
          f"   (2^-n = {2.0**-N:.4f}, 1/(2^n-1) = {1/(2**N-1):.4f})")

if __name__ == "__main__":
    print("=== transvection involution T_{r23}: feet-fix, Sigma-flip, defect scaling ===")
    study(6, n_lag=800, nbase=40, budget=70, seed=11)
    study(8, n_lag=260, nbase=20, budget=150, seed=23)
