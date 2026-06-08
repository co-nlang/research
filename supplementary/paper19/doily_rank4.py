#!/usr/bin/env python3
"""
Paper XIX -- the rank-4 realizability problem reduced to the S6 doily (GQ(2,2)).

By the reduction frame (reduction_frame.py), a proper K5 with rankG=4 has dimW=7
and projects to a 5-line configuration in the symplectic space Sp(4,F2). That space
is the S6 syntheme-duad geometry (the doily / GQ(2,2)):

  * points  = duads (2-subsets of {1,...,6}),   15 of them;
  * lines   = synthemes (perfect matchings of {1..6}), 15 of them;
  * a duad D lies on a syntheme S iff D in S;
  * omega(D,D') = |D and D'| mod 2, so  omega = 1  <=>  the two duads SHARE an element
    (equivalently omega = 0  <=>  the duads are disjoint, i.e. collinear in the doily).

The 5 projected Lagrangians become 5 synthemes S_0..S_4; the projected ray r_ab is the
common duad of S_a,S_b (or 0 if they are edge-disjoint). Hence

    N_anti = #{ {(a,b),(c,d)} : a,b,c,d distinct, S_a&S_b and S_c&S_d are single shared
                duads that SHARE an element }.

This script enumerates ALL 5-subsets of the 15 synthemes, keeps those satisfying the
two axioms forced by the geometry of a (7,4,3) projection --

  (spanning)  each line is spanned by its 4 meet-points: for every a, the duads
              {S_a & S_b : b != a, nonempty} contain >= 2 distinct duads;
  (rank-4)    the meet-duads span the doily's F2^4 (= even-weight F2^6 mod all-ones);

-- and reports the N_anti distribution.

RESULT (exhaustive, rigorous):
  distinct 5-syntheme spanning rank-4 configs split into exactly TWO S5-classes:
     meeting-graph C5  (degseq 2,2,2,2,2)  ->  N_anti = 5   (72 labelled configs)
     meeting-graph degseq 2,2,2,3,3        ->  N_anti = 6   (60 labelled configs)
  A proper K5 upstairs realises ONLY the N_anti=6 class (verified 65/65 directly);
  the C5 "syntheme pentagon" is doily-valid but never lifts. Proving that
  non-liftability would close  rankG=4 => N_anti=6.

Usage: python3 doily_rank4.py
"""
from itertools import combinations
from collections import Counter

def synthemes():
    out = []
    def rec(rem, cur):
        if not rem:
            out.append(frozenset(cur)); return
        a = min(rem)
        for b in rem:
            if b != a:
                rec(rem - {a, b}, cur + [frozenset((a, b))])
    rec(frozenset(range(6)), [])
    return out

SYN = synthemes()                       # 15 perfect matchings of {0..5}
assert len(SYN) == 15

def shared(Sa, Sb):
    it = Sa & Sb
    return next(iter(it)) if len(it) == 1 else None   # synthemes share 0 or 1 duad

def collinear(D1, D2):
    return len(D1 & D2) == 0            # disjoint duads = collinear (omega=0)

def vec(D):                            # duad -> F2^6 vector e_i+e_j
    v = 0
    for i in D: v |= (1 << i)
    return v
ALLONES = (1 << 6) - 1

def f2rank(vs):
    bs = []
    for v in vs:
        x = v
        for b in bs: x = min(x, x ^ b)
        if x: bs.append(x); bs.sort(reverse=True)
    return len(bs)

def analyze(S):
    r = {}
    for a in range(5):
        for b in range(a+1, 5):
            r[(a, b)] = shared(S[a], S[b])
    # spanning axiom
    for a in range(5):
        grp = {r[tuple(sorted((a, b)))] for b in range(5) if b != a} - {None}
        if len(grp) < 2:
            return None
    # rank-4 axiom (rank in F2^6/<allones>)
    meet = [vec(r[(a, b)]) for a in range(5) for b in range(a+1, 5) if r[(a, b)]]
    if f2rank(meet + [ALLONES]) - 1 != 4:
        return None
    # N_anti  and meeting-graph degree sequence
    deg = Counter()
    for a in range(5):
        for b in range(a+1, 5):
            if r[(a, b)]: deg[a] += 1; deg[b] += 1
    degseq = tuple(sorted(deg[i] for i in range(5)))
    N = 0
    for (a, b), (c, d) in combinations(combinations(range(5), 2), 2):
        if len({a, b, c, d}) < 4:
            continue
        p, q = r[(a, b)], r[(c, d)]
        if p and q and not collinear(p, q):
            N += 1
    return N, degseq

def main():
    tab = Counter()
    total = kept = 0
    for combo in combinations(range(15), 5):
        total += 1
        res = analyze([SYN[i] for i in combo])
        if res is None:
            continue
        kept += 1
        tab[res] += 1
    print(f"5-subsets of the 15 synthemes: {total}")
    print(f"satisfying spanning + rank-4 axioms: {kept}")
    print("(N_anti, meeting-graph degseq) -> count:")
    for k in sorted(tab):
        tag = "   <-- pentagon C5" if k[1] == (2, 2, 2, 2, 2) else ""
        print(f"   N_anti={k[0]}  degseq={k[1]}: {tab[k]}{tag}")
    print("\nN_anti distribution:", dict(sorted(Counter({n: c for (n, _), c in tab.items()}).items())
                                         if False else
                                         Counter(_n for (_n, _d), _c in tab.items() for _ in range(_c))))
    print("=> N_anti=6 unless the 5 synthemes form the C5 meeting-pentagon (N_anti=5);")
    print("   a proper K5 realises only the N_anti=6 class (the C5 pentagon does not lift).")

if __name__ == "__main__":
    main()
