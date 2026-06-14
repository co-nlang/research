"""Direction D, geometric route: does Sq^1(Maslov) = the H^3 class on K5?

The geometric incarnation of Sq^1 omega on the K5 nerve is the cup-1 square of the
Maslov 2-cochain mu.  On an ordered tetrahedron (t0,t1,t2,t3):
  (mu cup_1 mu)_T = mu(t0,t2,t3) mu(t0,t1,t2) + mu(t0,t1,t3) mu(t1,t2,t3)   (mod 2)
(Steenrod front/back-face formula for p=q=2, i=1; mu is S_3-symmetric so arg order
within each mu is irrelevant.)

We test, over sampled proper K5 at n=4,5,6:
  class level:  S := <mu cup_1 mu, [S^3]> = sum_m (cup)_m   vs   N_anti mod 2
  cochain level: na_m  vs  (delta mu)_m + (cup)_m   and   na_m vs (cup)_m
Prediction (even/odd dichotomy): mu==1 at even n => cup==0 => S=0 always, so the
geometric/Maslov route should MATCH at odd n (mu varies) but FAIL at even n (where na
carries the class via Part A, invisible to mu).  This pins the route's scope.
"""
import random, time
from itertools import combinations
from collections import Counter
from nerve_cochain import build

def sample(N, nseed, seed0=8000, n_lag=400, cap=80, budget=50):
    symp, _g, k5s, mu_triple = build(N)
    SZ = 1 << (2*N)
    def gen(sd):
        ALL = list(range(1, SZ)); rng = random.Random(sd)
        def xs(b):
            s = {0}
            for x in b: s |= {y ^ x for y in s}
            return s
        def rl():
            b = []; sp = {0}
            for _ in range(N):
                c = [v for v in ALL if v not in sp and all(symp(v, x) == 0 for x in b)]
                if not c: return None
                v = rng.choice(c); b.append(v); sp = xs(b)
            return frozenset(x for x in sp if x)
        L = []; ls = set(); t = time.time()
        while len(L) < n_lag and time.time() - t < budget:
            x = rl()
            if x and x not in ls: ls.add(x); L.append(x)
        adj = [set() for _ in L]
        for i in range(len(L)):
            for j in range(i+1, len(L)):
                if len(L[i] & L[j]) == 1: adj[i].add(j); adj[j].add(i)
        return L, adj
    out = []
    for s in range(nseed):
        L, adj = gen(seed0 + 7*s)
        for five, sh in k5s(L, adj, cap):
            out.append((five, sh))
    return symp, mu_triple, out

def analyze(N, nseed):
    symp, mu_triple, configs = sample(N, nseed)
    cls_match = 0; tot = 0
    na_eq_cup = 0; na_eq_dmu_plus_cup = 0; na_eq_dmu = 0
    Sdist = Counter(); Ndist = Counter()
    for five, sh in configs:
        tot += 1
        ray = {(a, b): sh[(a, b)] for a in range(5) for b in range(a+1, 5)}
        mu = {}
        for t in combinations(range(5), 3):
            mu[t] = mu_triple(five[t[0]], five[t[1]], five[t[2]])
        def M(a, b, c): return mu[tuple(sorted((a, b, c)))]
        na = []; dmu = []; cup = []
        for m in range(5):
            T = [x for x in range(5) if x != m]; i, j, k, l = T
            # na_m
            prs = [((i, j), (k, l)), ((i, k), (j, l)), ((i, l), (j, k))]
            na.append(sum(symp(ray[tuple(sorted(p))], ray[tuple(sorted(q))]) for p, q in prs) % 2)
            # delta mu on tetrahedron T
            dmu.append(sum(mu[f] for f in combinations(T, 3)) % 2)
            # cup_1 on ordered tetrahedron (t0<t1<t2<t3)
            t0, t1, t2, t3 = T
            cup.append((M(t0, t2, t3) * M(t0, t1, t2) ^ M(t0, t1, t3) * M(t1, t2, t3)) % 2)
        Nanti = sum(na) % 2
        S = sum(cup) % 2
        Ndist[Nanti] += 1; Sdist[S] += 1
        if S == Nanti: cls_match += 1
        if all(na[m] == cup[m] for m in range(5)): na_eq_cup += 1
        if all(na[m] == (dmu[m] ^ cup[m]) for m in range(5)): na_eq_dmu_plus_cup += 1
        if all(na[m] == dmu[m] for m in range(5)): na_eq_dmu += 1
    print(f"  n={N}: K5={tot}")
    print(f"    CLASS: <mu cup_1 mu,[S^3]>==N_anti mod2 : {cls_match}/{tot}   "
          f"(N_anti parity {dict(Ndist)}, S parity {dict(Sdist)})")
    print(f"    cochain na==cup: {na_eq_cup}/{tot} | na==dmu+cup: {na_eq_dmu_plus_cup}/{tot}"
          f" | na==dmu: {na_eq_dmu}/{tot}")

if __name__ == "__main__":
    print("=== geometric route: Sq^1(Maslov)=mu cup_1 mu  vs  H^3 class on K5 ===")
    analyze(4, 8)
    analyze(5, 8)
    analyze(6, 30)
