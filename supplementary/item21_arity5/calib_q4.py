#!/usr/bin/env python3
"""
Calibration: reconcile our kernel-sampled q_k (k=4) against Paper XIX's EXACT exhaustive q4_bit,
on the SAME configs. Decides whether the 80%-vs-99% gap is (i) a sampling/kernel BUG in our q_k, or
(ii) a population/dedup difference (XIX computes q4 on deduplicated invariant-buckets, we on raw K5s).

For each proper K5 (nerve_cochain.build), each of the 20 quadruples:
  EXACT  = XIX q4_bit: exists (x,y,z) in (La u {0})x(Lb u {0})x(Lc u {0}) with x+y+z in Ld and Q4!=0
  SAMPLED= our kernel-sampled q_k
We tally: agreement EXACT==SAMPLED, and each method's per-instance / per-config saturation.
If EXACT==SAMPLED always -> our machinery is correct, the gap is population/dedup (not a bug).
"""
import sys, random
sys.path.insert(0, "supplementary/paper22")
from nerve_cochain import build
from itertools import combinations
from collections import Counter

def basis_of(vectors):
    piv = {}
    for v in vectors:
        x = v
        while x:
            h = x.bit_length() - 1
            if h in piv: x ^= piv[h]
            else: piv[h] = x; break
    return list(piv.values())

def nullspace(rows, ncols):
    pivcol = {}
    for row in rows:
        x = row
        for c, pr in pivcol.items():
            if (x >> c) & 1: x ^= pr
        if x:
            c = (x & -x).bit_length() - 1
            for cc in list(pivcol):
                if (pivcol[cc] >> c) & 1: pivcol[cc] ^= x
            pivcol[c] = x
    pivots = set(pivcol)
    ker = []
    for f in (c for c in range(ncols) if c not in pivots):
        v = 1 << f
        for c, pr in pivcol.items():
            if (pr >> f) & 1: v |= (1 << c)
        ker.append(v)
    return ker

def run(N, n_lag, cap, seeds, samples=64, budget=90):
    import time
    symp, gen, k5s, mu = build(N); rng = random.Random(7)
    MSK = (1 << N) - 1
    def q4_exact(La, Lb, Lc, Ld):           # XIX: La etc. are nonzero-vector sets; add 0
        La0 = list(La) + [0]; Lb0 = list(Lb) + [0]; Lc0 = list(Lc) + [0]; Ld0 = set(Lc) | {0}
        Ldset = set(Ld) | {0}
        for x in La0:
            for y in Lb0:
                xy = x ^ y
                for z in Lc0:
                    if (xy ^ z) in Ldset and (symp(x, y) ^ symp(x, z) ^ symp(y, z)):
                        return 1
        return 0
    def q4_sampled(Bf, Bd):
        k1 = len(Bf); n = len(Bd); ncols = k1 * n
        rows = []
        for i in range(n):
            b = Bd[i]; row = 0
            for m in range(k1):
                for t in range(n):
                    if symp(Bf[m][t], b): row |= 1 << (m * n + t)
            rows.append(row)
        ker = nullspace(rows, ncols)
        if not ker: return 0
        for _ in range(samples):
            c = 0
            for kv in ker:
                if rng.getrandbits(1): c ^= kv
            if not c: continue
            vs = []
            for m in range(k1):
                vm = 0
                for t in range(n):
                    if (c >> (m * n + t)) & 1: vm ^= Bf[m][t]
                vs.append(vm)
            if symp(vs[0], vs[1]) ^ symp(vs[0], vs[2]) ^ symp(vs[1], vs[2]):
                return 1
        return 0
    agree = Counter(); exact_sat = Counter(); samp_sat = Counter()
    exact_cfg = Counter(); samp_cfg = Counter(); t0 = time.time()
    for s in range(seeds):
        if time.time() - t0 > budget: break
        lags, adj = gen(61000 + 23 * s, n_lag)
        for five, sh in k5s(lags, adj, cap):
            Bsets = [set(L) for L in five]
            Bbasis = [basis_of(L) for L in five]
            ev = []; sv = []
            for combo in combinations(range(5), 4):
                for di in range(4):
                    dist = combo[di]; free = [combo[j] for j in range(4) if j != di]
                    e = q4_exact(Bsets[free[0]], Bsets[free[1]], Bsets[free[2]], Bsets[dist])
                    sm = q4_sampled([Bbasis[m] for m in free], Bbasis[dist])
                    agree[e == sm] += 1; exact_sat[e] += 1; samp_sat[sm] += 1
                    ev.append(e); sv.append(sm)
            exact_cfg[all(ev)] += 1; samp_cfg[all(sv)] += 1
        if time.time() - t0 > budget: break
    T = agree[True] + agree[False]
    print(f"  n={N}: instances={T}", flush=True)
    print(f"    EXACT==SAMPLED agreement: {agree[True]}/{T} "
          f"({'PERFECT' if agree[False]==0 else 'MISMATCH '+str(agree[False])})", flush=True)
    print(f"    exact  q4==1: {exact_sat[1]}/{T}; configs full-sat: {exact_cfg[True]}/{exact_cfg[True]+exact_cfg[False]}", flush=True)
    print(f"    sampled q4==1: {samp_sat[1]}/{T}; configs full-sat: {samp_cfg[True]}/{samp_cfg[True]+samp_cfg[False]}", flush=True)

if __name__ == "__main__":
    print(__doc__, flush=True)
    run(5, 2000, 800, 4)
