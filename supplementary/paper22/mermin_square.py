"""Lateral test for the ceiling theorem: the Mermin-Peres 3x3 magic square.

The square is 6 Lagrangians in Sp(4,F2) (3 rows R1,R2,R3 + 3 cols C1,C2,C3); the 9
observables are the cross-intersections R_i cap C_j (rays).  Rows are pairwise
transverse, cols pairwise transverse => the incidence nerve is the BIPARTITE graph
K_{3,3}, NOT the all-pairwise K_N of the resonance tower.

Consequences we test:
 (1) verify the construction: 6 Lagrangians, K_{3,3} incidence, 9 distinct rays;
 (2) every triple of the 6 contexts has a same-class transverse pair => the K_N
     Maslov mu / anticommutation cochains are UNDEFINED here (different family);
 (3) the square's actual KS obstruction is the +-I sign mismatch (a quadratic-
     refinement / central-extension class, the H^2 "KS world" of Papers III-VIII),
     NOT the pentagram's degree-3 anticommutation class.
We compute the sign obstruction directly with Hermitian-Pauli phase tracking.

Encoding: 2-qubit Pauli vector (x,z), x,z in {0..3} (qubit1=bit0, qubit2=bit1).
Hermitian Pauli W(x,z) = i^{parity(x&z)} X^x Z^z  (so W^2 = I).
"""

def par(z): return bin(z).count('1') & 1
def symp(a, b):  # a=(x,z)
    return par(a[0] & b[1]) ^ par(a[1] & b[0])

# --- the 6 contexts as Lagrangians (sets of 3 nonzero (x,z) vectors) ---
R1 = [(1, 0), (2, 0), (3, 0)]   # XI, IX, XX   (all-X plane)
R2 = [(0, 1), (0, 2), (0, 3)]   # IZ, ZI, ZZ   (all-Z plane)
R3 = [(1, 2), (2, 1), (3, 3)]   # XZ, ZX, YY
C1 = [(1, 0), (0, 2), (1, 2)]   # XI, IZ, XZ
C2 = [(2, 0), (0, 1), (2, 1)]   # IX, ZI, ZX
C3 = [(3, 0), (0, 3), (3, 3)]   # XX, ZZ, YY
rows = [R1, R2, R3]; cols = [C1, C2, C3]
contexts = {"R1": R1, "R2": R2, "R3": R3, "C1": C1, "C2": C2, "C3": C3}

def isotropic(L):
    return all(symp(u, v) == 0 for u in L for v in L)
def closed(L):  # 3 nonzero vectors of a 2-dim space sum to 0
    return (L[0][0]^L[1][0]^L[2][0], L[0][1]^L[1][1]^L[2][1]) == (0, 0)
def inter(A, B):
    return set(A) & set(B)

def check_construction():
    print("  (1) construction:")
    for name, L in contexts.items():
        assert isotropic(L) and closed(L) and len(set(L)) == 3, name
    print("      all 6 contexts are Lagrangians (isotropic, closed, 3 rays each)")
    # incidence
    rays = set()
    bip_ok = True
    for i, R in enumerate(rows):
        for j, C in enumerate(cols):
            it = inter(R, C)
            if len(it) != 1: bip_ok = False
            rays |= it
    rr = all(len(inter(rows[i], rows[j])) == 0 for i in range(3) for j in range(i+1, 3))
    cc = all(len(inter(cols[i], cols[j])) == 0 for i in range(3) for j in range(i+1, 3))
    print(f"      row_i cap col_j = 1 ray each: {bip_ok};  rows pairwise transverse: {rr};"
          f"  cols pairwise transverse: {cc}")
    print(f"      distinct rays (observables): {len(rays)} (expect 9)")
    return rr and cc and bip_ok and len(rays) == 9

def check_no_KN_cochain():
    print("  (2) every triple of the 6 contexts has a transverse (no-ray) pair:")
    names = list(contexts)
    from itertools import combinations
    bad = 0
    for a, b, c in combinations(names, 3):
        L = [contexts[a], contexts[b], contexts[c]]
        haspair = any(len(inter(L[i], L[j])) == 0 for i, j in [(0,1),(0,2),(1,2)])
        if not haspair: bad += 1
    print(f"      triples lacking a transverse pair: {bad}/20  "
          f"=> Maslov/anticommutation (need 3 pairwise rays) {'UNDEFINED' if bad==0 else 'partial'}")
    return bad == 0

# --- Hermitian-Pauli phase: W(x,z)=i^{par(x&z)} X^x Z^z ; track (phase mod 4, x, z) ---
def W(v):
    x, z = v
    return (par(x & z) % 4, x, z)
def pmul(A, B):
    pa, xa, za = A; pb, xb, zb = B
    return ((pa + pb + 2 * par(za & xb)) % 4, xa ^ xb, za ^ zb)
def context_sign(L):
    P = (0, 0, 0)
    for v in L: P = pmul(P, W(v))
    p, x, z = P
    assert (x, z) == (0, 0), "context product not proportional to I"
    return +1 if p % 4 == 0 else -1   # p is even for a Hermitian context

def ks_obstruction():
    print("  (3) KS sign obstruction (product of the 6 context signs):")
    signs = {name: context_sign(L) for name, L in contexts.items()}
    print(f"      per-context signs: {signs}")
    prod = 1
    for s in signs.values(): prod *= s
    print(f"      product over all 6 contexts = {prod}  "
          f"=> {'CONTEXTUAL (obstruction = -1)' if prod == -1 else 'consistent (+1)'}")
    return prod

if __name__ == "__main__":
    print("=== Mermin-Peres square as 6 Lagrangians in Sp(4,F2) ===")
    ok = check_construction()
    nd = check_no_KN_cochain()
    obs = ks_obstruction()
    print("\n  SUMMARY:")
    print(f"    bipartite K_3,3 config verified: {ok}")
    print(f"    K_N Maslov/anticommutation cochains undefined here: {nd}")
    print(f"    obstruction = quadratic-refinement / central-extension SIGN class (H^2 world),")
    print(f"      product={obs}; this is a DIFFERENT cohomology family than the pentagram's H^3.")
