#!/usr/bin/env python3
"""
Paper XVIII: Study the Fano-failure vectors w_a = XOR of all 4 rays of L_a.

For n=4, Fano zero-sum fails: w_a = v_{a0}⊕v_{a1}⊕v_{a2}⊕v_{a3}⊕v_{a4} ≠ 0.
These 5 vectors satisfy w_0⊕w_1⊕w_2⊕w_3⊕w_4 = 0 (each v_{ab} appears twice).

We study: ω(w_a, w_b), ω(w_a, v_{bc}), and their relation to Σ_m values.

Key formula: x_m^(a) = v_{ab}⊕v_{ac}⊕v_{ad} = w_a ⊕ v_{am}
So Σ_m = ω(x_m^(a), y_m^(a)) where x_m^(a) = w_a ⊕ v_{am}.
"""
import sys, time, random
from collections import Counter

N_K5 = int(sys.argv[1]) if len(sys.argv) > 1 else 20
SEED = int(sys.argv[2]) if len(sys.argv) > 2 else 42

N = 4; DIM = 8; _SZ = 256; _MSK = 15
random.seed(SEED); t0 = time.time()

_PN = [bin(i).count('1') & 1 for i in range(16)]
_XT = [[_PN[i & j] for j in range(16)] for i in range(16)]
def symp(v, w):
    return _XT[v & _MSK][(w >> N) & _MSK] ^ _XT[(v >> N) & _MSK][w & _MSK]

def xor_span(basis):
    span = set()
    for mask in range(1, 1 << len(basis)):
        s = 0
        for i in range(len(basis)): s ^= basis[i] if (mask >> i) & 1 else 0
        if s: span.add(s)
    return span

ALL_VEC = list(range(1, _SZ))
def random_lagrangian():
    basis = []; span = set()
    for _ in range(N):
        cands = [v for v in ALL_VEC
                 if v not in span and all(symp(v, b) == 0 for b in basis)]
        if not cands: return None
        v = random.choice(cands); basis.append(v); span = xor_span(basis)
    return frozenset(span)

lag_set = set(); lags = []
while len(lags) < 500:
    lag = random_lagrangian()
    if lag and lag not in lag_set: lag_set.add(lag); lags.append(lag)

adj = [set() for _ in range(len(lags))]
for i in range(len(lags)):
    for j in range(i+1, len(lags)):
        if len(lags[i] & lags[j]) == 1:
            adj[i].add(j); adj[j].add(i)

ALL_PAIRS = [(a,b) for a in range(5) for b in range(a+1,5)]

def analyze_k5(idx5):
    five = [lags[x] for x in idx5]
    shared = {}
    for a in range(5):
        for b in range(a+1, 5):
            inter = five[a] & five[b]
            if len(inter) != 1: return None
            shared[(a,b)] = next(iter(inter))
    if len(set(shared.values())) != 10: return None
    return shared

def get_ray(shared, i, j):
    return shared[(min(i,j), max(i,j))]

print(f"Studying Fano-failure vectors for n=4 K₅s  (seed={SEED})", flush=True)

# Track statistics across K₅s
omega_ww_dist  = Counter()   # ω(w_a, w_b) values
omega_wv_dist  = Counter()   # ω(w_a, v_{bc}) where a∉{b,c}
sigma_check    = Counter()   # Σ_m vs ω(w_a, w_b) relationship
ww_vs_sigma    = []          # store (ω(w_a,w_b), Σ values) per K₅

n_k5 = 0; done = False
n_lag = len(lags)

for i in range(n_lag):
    if done: break
    ai = adj[i]
    for j in ai:
        if j<=i or done: continue
        for k in (ai & adj[j]):
            if k<=j or done: continue
            for l in (ai & adj[j] & adj[k]):
                if l<=k or done: continue
                for m in (ai & adj[j] & adj[k] & adj[l]):
                    if m<=l: continue
                    shared = analyze_k5((i,j,k,l,m))
                    if shared is None: continue

                    # Compute w_a = XOR of all 4 rays of L_a
                    w = {}
                    for a in range(5):
                        w[a] = 0
                        for b in range(5):
                            if b != a: w[a] ^= get_ray(shared, a, b)

                    # Verify: XOR of all 5 w vectors = 0
                    xor_all = 0
                    for a in range(5): xor_all ^= w[a]
                    assert xor_all == 0, "w XOR identity failed!"

                    # Compute Σ_m for all 5 matchings
                    sigs = {}
                    for mm in range(5):
                        a,b,c,d = sorted(x for x in range(5) if x != mm)
                        sigs[mm] = (symp(shared[(a,b)],shared[(c,d)]) ^
                                    symp(shared[(a,c)],shared[(b,d)]) ^
                                    symp(shared[(a,d)],shared[(b,c)]))

                    # Compute ω(w_a, w_b) for all pairs a<b
                    omega_ww = {}
                    for a in range(5):
                        for b in range(a+1, 5):
                            omega_ww[(a,b)] = symp(w[a], w[b])
                            omega_ww_dist[omega_ww[(a,b)]] += 1

                    # Compute ω(w_a, v_{bc}) for a ∉ {b,c} (cross-context w vs ray)
                    omega_wv = {}
                    for a in range(5):
                        for b in range(5):
                            for c in range(b+1, 5):
                                if a == b or a == c: continue
                                omega_wv[(a,b,c)] = symp(w[a], shared[(b,c)])
                                omega_wv_dist[omega_wv[(a,b,c)]] += 1

                    n_k5 += 1

                    if n_k5 <= 5:
                        print(f"\n── K₅ #{n_k5} ──")
                        print(f"  w_a nonzero: {[a for a in range(5) if w[a] != 0]}")
                        print(f"  Σ_m = {[sigs[m] for m in range(5)]}")
                        print(f"  ω(w_a,w_b) matrix:")
                        for a in range(5):
                            row = []
                            for b in range(5):
                                if a == b: row.append('-')
                                elif a < b: row.append(str(omega_ww[(a,b)]))
                                else: row.append(str(omega_ww[(b,a)]))
                            print(f"    {row}")

                        # Check: for each m, does ω(w_a, w_b) relate to Σ_m?
                        print(f"  Key formula check: Σ_m = ω(w_a⊕v_{{am}}, y_m^(a))?")
                        for mm in range(5):
                            a,b,c,d = sorted(x for x in range(5) if x != mm)
                            x_m = w[a] ^ get_ray(shared, a, mm)   # = v_{ab}⊕v_{ac}⊕v_{ad}
                            y_m = (shared[(b,c)] ^
                                   shared[(b,d)] ^
                                   shared[(c,d)])
                            check = symp(x_m, y_m)
                            assert check == sigs[mm], f"Formula mismatch!"

                        # Check: ω(w_a, y_m) where y_m is the non-a half of matching m
                        print(f"  ω(w_a, y_m^(a)) for each m (anchor a = min index):")
                        for mm in range(5):
                            a,b,c,d = sorted(x for x in range(5) if x != mm)
                            y_m = (shared[(b,c)] ^
                                   shared[(b,d)] ^
                                   shared[(c,d)])
                            ww_ym = symp(w[a], y_m)
                            vam_ym = symp(get_ray(shared, a, mm), y_m)
                            print(f"    m={mm}: ω(w_{a},y_m)={ww_ym}  ω(v_{{a{mm}}},y_m)={vam_ym}  sum={ww_ym^vam_ym}=Σ_{mm}={sigs[mm]}")

                        # Check: ω(w_a, v_{bc}) for rays NOT involving a
                        print(f"  ω(w_a, v_{{bc}}) for a∉{{b,c}}:")
                        for a in range(5):
                            vals = []
                            for bc in ALL_PAIRS:
                                b,c = bc
                                if a not in (b,c):
                                    vals.append(f"v_{b}{c}:{omega_wv[(a,b,c)]}")
                            print(f"    w_{a}: {' '.join(vals)}")

                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Summary over {n_k5} K₅s ──")
print(f"  ω(w_a,w_b) distribution: {dict(omega_ww_dist)}")
print(f"  ω(w_a,v_bc) distribution (a∉{{b,c}}): {dict(omega_wv_dist)}")

# Check if ω(w_a,w_b) = 0 always
if omega_ww_dist.get(0, 0) == sum(omega_ww_dist.values()):
    print(f"\n>>> ALL ω(w_a,w_b) = 0: the 5 Fano-failure vectors are MUTUALLY ISOTROPIC!")
    print(f"    {w_a} span a totally isotropic subspace (dim ≤ 4 since XOR=0 → dim ≤ 4)")
else:
    print(f"\n>>> ω(w_a,w_b) is NOT always 0.")
    print(f"    0-count: {omega_ww_dist.get(0,0)}  1-count: {omega_ww_dist.get(1,0)}")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
