#!/usr/bin/env python3
"""
Paper XVIII: Verify the correspondence between two K₅ classifications:
  (A) n_fano = # Lagrangians with w_a=0 (Fano zero-sum)
  (B) comm. pairs graph structure: perfect matching vs non-PM

Hypothesis: n_fano=1 ↔ non-PM (Type I), n_fano=0 ↔ PM (Type II).

If true, the proof of Σ_m=0 splits by type:
  Type II (PM): commuting PM always has all 5 different missing indices → transversal → each
                Mermin matching has exactly 1 commuting pair → Σ_m = 2 mod 2 = 0.
  Type I (non-PM, 1 Fano): different mechanism.
"""
import sys, time, random
from collections import Counter

N_K5 = int(sys.argv[1]) if len(sys.argv) > 1 else 500
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

def get_ray(shared, i, j):
    return shared[(min(i,j), max(i,j))]

print(f"K₅ type correspondence check  n=4  N_K5={N_K5}  seed={SEED}", flush=True)

joint_dist = Counter()   # (n_fano, is_pm, transversal_count)
missing_idx_dist = Counter()   # distribution of missing indices for commuting PM pairs

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
                    five = [lags[x] for x in (i,j,k,l,m)]
                    shared = {}
                    ok = True
                    for a in range(5):
                        for b in range(a+1, 5):
                            inter = five[a] & five[b]
                            if len(inter) != 1: ok = False; break
                            shared[(a,b)] = next(iter(inter))
                        if not ok: break
                    if not ok or len(set(shared.values())) != 10: continue

                    ALL_PAIRS = [(a,b) for a in range(5) for b in range(a+1,5)]

                    # Count Fano Lagrangians
                    n_fano = 0
                    for a in range(5):
                        wa = 0
                        for b in range(5):
                            if b != a: wa ^= get_ray(shared, a, b)
                        if wa == 0: n_fano += 1

                    # Find commuting cross-context pairs
                    comm_pairs = []
                    for p1 in ALL_PAIRS:
                        for p2 in ALL_PAIRS:
                            if p2 <= p1 or set(p1) & set(p2): continue
                            if symp(shared[p1], shared[p2]) == 0:
                                comm_pairs.append((p1, p2))

                    n_comm = len(comm_pairs)

                    # Check if commuting pairs form a perfect matching of K(5,2)
                    from collections import Counter as Ctr
                    vertex_use = Ctr()
                    for p1, p2 in comm_pairs:
                        vertex_use[p1] += 1
                        vertex_use[p2] += 1
                    is_pm = (n_comm == 5 and
                             len(vertex_use) == 10 and
                             all(v == 1 for v in vertex_use.values()))

                    # For each commuting pair, compute its missing index
                    comm_missing = []
                    for p1, p2 in comm_pairs:
                        used = set(p1) | set(p2)
                        missing = [x for x in range(5) if x not in used]
                        assert len(missing) == 1
                        comm_missing.append(missing[0])

                    # Is there exactly one commuting pair per Mermin matching?
                    missing_counts = Ctr(comm_missing)
                    is_transversal = (len(missing_counts) == 5 and
                                      all(v == 1 for v in missing_counts.values()))

                    # Count Σ_m for verification
                    sigs = []
                    for mm in range(5):
                        a,b,c,d = sorted(x for x in range(5) if x != mm)
                        s = (symp(shared[(a,b)],shared[(c,d)]) ^
                             symp(shared[(a,c)],shared[(b,d)]) ^
                             symp(shared[(a,d)],shared[(b,c)]))
                        sigs.append(s)

                    joint_dist[(n_fano, is_pm, is_transversal)] += 1
                    if is_pm:
                        for mval in comm_missing:
                            missing_idx_dist[mval] += 1

                    n_k5 += 1
                    if n_k5 >= N_K5: done = True; break
                if done: break
            if done: break
        if done: break

print(f"\n── Results over {n_k5} K₅s ──")
print(f"  (n_fano, is_perfect_matching, is_transversal) → count")
for key in sorted(joint_dist):
    nf, pm, trans = key
    print(f"    n_fano={nf}  PM={pm}  transversal={trans}  →  {joint_dist[key]}")

print(f"\n  Distribution of missing indices for commuting pairs in PM K₅s:")
total_pm = sum(v for (nf,pm,t),v in joint_dist.items() if pm)
for m_val in range(5):
    print(f"    missing={m_val}: {missing_idx_dist[m_val]}")

# Summary
n_type1 = joint_dist.get((1, False, True), 0)
n_type2 = joint_dist.get((0, True, True), 0)
print(f"\n  Type I  (n_fano=1, non-PM, transversal): {n_type1}")
print(f"  Type II (n_fano=0, PM, transversal):     {n_type2}")
print(f"  Other:  {n_k5 - n_type1 - n_type2}")

if n_type1 + n_type2 == n_k5:
    print(f"\n>>> PERFECT CORRESPONDENCE:")
    print(f"    Type I  = n_fano=1 = non-PM = transversal")
    print(f"    Type II = n_fano=0 = PM     = transversal")
    print(f"    ALL K₅s have exactly 1 commuting pair per Mermin matching.")
    print(f"    Therefore Σ_m = 2 mod 2 = 0 for ALL m.")

print(f"\n[done]  ({time.time()-t0:.1f}s)")
