"""Diagnostic for the matching-parity balance: the three foot-bits.

Sigma_0 = b1 ^ b2 ^ b3  where  b_i = lambda_i(v_i4) = omega(v_i4, r_jk),
{i,j,k}={1,2,3}, over a fixed proper K3 (L1,L2,L3) as L4 varies.  Each lambda_i is
a NONZERO functional on L_i.  We tabulate the joint (b1,b2,b3) over the L4 fiber,
aggregated over many base K3, and report:
  - each marginal P(b_i=1)   (balanced foot-bit?)
  - pairwise/triple correlations
  - resulting P(Sigma=1).
Balanced & independent marginals => Sigma balanced => H^3 class 50/50.
"""
import random, time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def run(N, n_lag=800, nbase=40, budget=70, seed=2718):
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
    print(f"  N={N}: {len(lags)} Lagrangians")

    joint = Counter(); bases = 0
    for (i, j, k) in combinations(range(len(lags)), 3):
        if bases >= nbase: break
        L1, L2, L3 = lags[i], lags[j], lags[k]
        r12, r13, r23 = ray(L1, L2), ray(L1, L3), ray(L2, L3)
        if None in (r12, r13, r23) or len({r12, r13, r23}) != 3: continue
        sub = Counter()
        for L4 in lags:
            if L4 in (L1, L2, L3): continue
            r14, r24, r34 = ray(L1, L4), ray(L2, L4), ray(L3, L4)
            if None in (r14, r24, r34): continue
            if len({r12, r13, r23, r14, r24, r34}) != 6: continue
            b1 = symp(r14, r23); b2 = symp(r24, r13); b3 = symp(r34, r12)
            sub[(b1, b2, b3)] += 1
        if sum(sub.values()) >= 8:
            joint += sub; bases += 1
    tot = sum(joint.values())
    print(f"  aggregated {bases} fibers, {tot} completions")
    print(f"  joint (b1,b2,b3) counts: {dict(sorted(joint.items()))}")
    p1 = sum(v for (b, _, _), v in joint.items() if b) / tot
    p2 = sum(v for (_, b, _), v in joint.items() if b) / tot
    p3 = sum(v for (_, _, b), v in joint.items() if b) / tot
    psig = sum(v for k, v in joint.items() if sum(k) % 2) / tot
    print(f"  marginals: P(b1=1)={p1:.4f}  P(b2=1)={p2:.4f}  P(b3=1)={p3:.4f}")
    # pairwise correlation E[(-1)^{bi+bj}]
    import itertools
    for (a, b) in [(0, 1), (0, 2), (1, 2)]:
        corr = sum(((-1) ** (k[a] ^ k[b])) * v for k, v in joint.items()) / tot
        print(f"  corr b{a+1},b{b+1}: E[(-1)^(bi^bj)]={corr:+.4f}")
    tri = sum(((-1) ** (sum(k) % 2)) * v for k, v in joint.items()) / tot
    print(f"  P(Sigma=1)={psig:.4f}   bias E[(-1)^Sigma]={tri:+.4f}")

if __name__ == "__main__":
    print("=== foot-bit joint distribution (n=6) ===")
    run(6)
