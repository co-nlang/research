"""Consolidating B: the incidence-clique criterion for the family-A ceiling.

For a configuration of Lagrangians (contexts), build the INCIDENCE GRAPH G:
  vertices = contexts;  edge (i,j) iff dim(L_i cap L_j) = 1 (they share a ray).
The family-A (anticommutation/Maslov) NERVE obstruction is supported on the clique
complex of G: a degree-d class needs a (hollow) (d+2)-clique.  So the family-A ceiling
is  min(omega(G) - 2,  arity-1=3),  saturated (resonance) at omega(G) = 5 (pentagram).
When G is triangle-free (omega=2) there is NO family-A obstruction above the graph's
own H^1; the contextuality, if any, must be carried by the central-extension / sign class
(family B).  Mermin square = triangle-free K_{3,3} (omega=2) => family B.
Pentagram = complete K5 (omega=5) => family A at H^3.

This script computes omega(G) and the family-A ceiling for: the Mermin square (explicit),
a sampled proper K5, a sampled proper K4.
"""
import random, time
from itertools import combinations
from nerve_cochain import build

def par(z): return bin(z).count('1') & 1

def clique_number(n, edges):
    E = set(edges)
    best = 0
    # brute-force max clique on a small graph
    verts = list(range(n))
    def grow(clique, cand):
        nonlocal best
        best = max(best, len(clique))
        for i, v in enumerate(cand):
            newcand = [u for u in cand[i+1:] if (min(v, u), max(v, u)) in E]
            grow(clique + [v], newcand)
    grow([], verts)
    return best

def ceiling(omega, arity=4):
    d = max(0, omega - 2)
    return min(d, arity - 1)

# ---- Mermin square (6 contexts in Sp(4,F2)) ----
def square_incidence():
    def symp(a, b): return par(a[0] & b[1]) ^ par(a[1] & b[0])
    R1 = [(1,0),(2,0),(3,0)]; R2=[(0,1),(0,2),(0,3)]; R3=[(1,2),(2,1),(3,3)]
    C1 = [(1,0),(0,2),(1,2)]; C2=[(2,0),(0,1),(2,1)]; C3=[(3,0),(0,3),(3,3)]
    L = [R1, R2, R3, C1, C2, C3]
    edges = []
    for i in range(6):
        for j in range(i+1, 6):
            if len(set(L[i]) & set(L[j])) == 1: edges.append((i, j))
    return 6, edges

# ---- sampled proper K_N (complete incidence by construction) ----
def proper_kn_incidence(N, want, seed):
    symp, *_ = build(N)
    SZ = 1 << (2*N); ALL = list(range(1, SZ)); rng = random.Random(seed)
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
    while len(lags) < 200 and time.time() - t < 30:
        Lg = rl()
        if Lg and Lg not in ls: ls.add(Lg); lags.append(Lg)
    adj = [set() for _ in lags]
    for i in range(len(lags)):
        for j in range(i+1, len(lags)):
            if len(lags[i] & lags[j]) == 1: adj[i].add(j); adj[j].add(i)
    # find a `want`-clique (a proper K_want); return its induced incidence
    for combo in combinations(range(len(lags)), want):
        if all(j in adj[i] for i, j in combinations(combo, 2)):
            return want, list(combinations(range(want), 2))  # complete
    return None

def report(name, n, edges, family_note):
    om = clique_number(n, edges)
    print(f"  {name}: contexts={n}, incidence edges={len(edges)}, clique number omega={om}")
    print(f"      family-A nerve ceiling = min(omega-2, 3) = {ceiling(om)}  "
          f"({'TRIVIAL (omega<3): '+family_note if om < 3 else 'H^'+str(ceiling(om))})")

if __name__ == "__main__":
    print("=== incidence-clique criterion: which cohomological family ===")
    n, e = square_incidence()
    report("Mermin square (K_3,3)", n, e, "family B = central-extension SIGN class (H^2)")
    for N, want in [(4, 4), (5, 5)]:
        r = proper_kn_incidence(N, want, seed=10+N)
        if r: report(f"proper K{want} (n={N})", r[0], r[1], "")
    print("\n  => ceiling is read off the incidence clique number:")
    print("     omega=2 (triangle-free, e.g. Mermin square) -> no family-A; family B (sign).")
    print("     omega=4 (K4)  -> family-A H^2 (Maslov).")
    print("     omega=5 (K5 pentagram) -> family-A H^3 (anticommutation) = RESONANCE/ceiling.")
