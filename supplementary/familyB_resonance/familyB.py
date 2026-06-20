#!/usr/bin/env python3
"""
Item A2.2 / Paper XXII Outlook Q1: does the bipartite (family-B) family have its
own resonance -- a larger K_{m,n} whose central-extension class reaches degree 3?

ANSWER: No. The bipartite family is not a parallel tower; it is the clique-number
FLOOR (omega=2) of the single arity-resonance / clique tower (family A). Reasons:

  (1) The clique criterion (Paper XXII Thm) gives family-A ceiling min(omega(G)-2,3),
      omega(G)=clique number of the incidence graph. A complete r-partite graph has
      clique number EXACTLY r. So:
        - growing a bipartite K_{m,n} (bigger m,n) keeps r=2 -> ceiling 0 forever
          (bipartite = triangle-free = 1-dimensional clique complex);
        - the only way to raise the ceiling is to add context-CLASSES (complete
          r-partite), but omega=r is the SAME clique criterion (family A), climbing
          min(r-2,3) and topping at H^3 when r=5, where the complete 5-partite graph
          with singleton parts IS the pentagram K_5 = K_{1,1,1,1,1}.
  (2) The family-B obstruction is the central-extension class omega in H^2 (a single
      +/-I product bit), intrinsically degree 2; growing the grid does not change it.
  (3) The only ascent from omega (H^2, family B) to degree 3 is the Steenrod
      operation Sq^1: H^2 -> H^3, and Sq^1 omega = n_a is the FAMILY-A class
      (Direction D, bockstein/, twistor_cp/). So the family-B -> degree-3 ascent IS
      the A<->B unification (Outlook Q2), not a bigger grid: Q1 collapses into Q2.

Pure Python: F_2 symplectic structure + explicit 4x4 Pauli matrices (no deps).
"""
from itertools import combinations, product

# ---------------------------------------------------------------- Part 1
# The clique / arity-resonance tower: complete r-partite incidence.
def clique_number(verts, adj):
    """max clique by growth over a small graph (verts small)."""
    best = 0
    # greedy-exact over subsets is fine for our tiny graphs
    def extend(clique, cand):
        nonlocal best
        best = max(best, len(clique))
        for i, v in enumerate(cand):
            if all(adj[v][u] for u in clique):
                extend(clique + [v], [w for w in cand[i+1:] if adj[v][w]])
    extend([], list(verts))
    return best

def complete_multipartite(parts):
    """parts = list of part sizes; vertices labelled, adjacent iff different parts."""
    verts, part_of = [], {}
    for p, sz in enumerate(parts):
        for k in range(sz):
            v = (p, k); verts.append(v); part_of[v] = p
    adj = {v: {w: (part_of[v] != part_of[w]) for w in verts} for v in verts}
    return verts, adj

print("="*68)
print(" Part 1.  The clique tower: complete r-partite incidence")
print("="*68)
print(f"  {'config':>22} | {'r-partite':>9} | {'omega':>5} | {'ceiling min(w-2,3)':>18}")
print(f"  {'-'*22}-+-{'-'*9}-+-{'-'*5}-+-{'-'*18}")
cases = [
    ("K_{3,3} Mermin square", [3,3]),
    ("K_{4,4} bigger grid",   [4,4]),
    ("K_{9,9} huge grid",     [9,9]),
    ("K_{3,3,3} tripartite",  [3,3,3]),
    ("K_{2,2,2,2} 4-partite", [2,2,2,2]),
    ("K_5 = K_{1,1,1,1,1}",   [1,1,1,1,1]),
    ("6-partite",             [1,1,1,1,1,1]),
]
for name, parts in cases:
    verts, adj = complete_multipartite(parts)
    w = clique_number(verts, adj)
    ceiling = min(w - 2, 3)
    deg = "none (family B)" if ceiling <= 0 else f"H^{ceiling}"
    star = "   <- pentagram" if parts == [1,1,1,1,1] else ""
    print(f"  {name:>22} | {len(parts):>9} | {w:>5} | {deg:>18}{star}")
print("""
  Reading: bipartite (r=2) -> ceiling 0 for ALL grid sizes (3x3, 4x4, 9x9, ...);
  the grid never climbs.  Climbing needs more PARTS (r), governed by the SAME
  clique criterion = family A, topping at H^3 at r=5 = the pentagram K_5.
  ==> bipartite K_{m,n} has NO resonance of its own; it is the omega=2 floor.""")

# ---------------------------------------------------------------- Part 2
# The Mermin-Peres square: the omega=2 floor, realized in Sp(4,2).
# 2-qubit Pauli vector (x1,x2 | z1,z2) in F_2^4;  omega(a,b)=ax.bz + bx.az.
def sympl(a, b):
    ax, az = a[:2], a[2:]; bx, bz = b[:2], b[2:]
    return (ax[0]*bz[0]+ax[1]*bz[1] + bx[0]*az[0]+bx[1]*az[1]) & 1

P = {  # name -> F_2^4 vector
 'XI':(1,0,0,0),'IX':(0,1,0,0),'XX':(1,1,0,0),
 'IZ':(0,0,0,1),'ZI':(0,0,1,0),'ZZ':(0,0,1,1),
 'XZ':(1,0,0,1),'ZX':(0,1,1,0),'YY':(1,1,1,1),
}
rows = [['XI','IX','XX'], ['IZ','ZI','ZZ'], ['XZ','ZX','YY']]
cols = [['XI','IZ','XZ'], ['IX','ZI','ZX'], ['XX','ZZ','YY']]
contexts = rows + cols  # 6 Lagrangians (each a 2-dim isotropic plane: 3 nonzero rays)

def plane(ctx):  # the 3 nonzero vectors + closure check
    vs = [P[o] for o in ctx]
    return vs
def is_isotropic(ctx):
    vs = [P[o] for o in ctx]
    # closure: third = sum of other two; pairwise omega=0
    s = tuple((vs[0][i]^vs[1][i]) for i in range(4))
    return s == vs[2] and all(sympl(a,b)==0 for a,b in combinations(vs,2))

def shares(c1, c2):  # do two contexts share an observable?
    return bool(set(c1) & set(c2))

print("="*68)
print(" Part 2.  The Mermin-Peres square = the family-B floor (Sp(4,2))")
print("="*68)
print(f"  all 6 contexts isotropic planes : {all(is_isotropic(c) for c in contexts)}")
# incidence graph: edge iff share an observable
edges = [(i,j) for i,j in combinations(range(6),2) if shares(contexts[i],contexts[j])]
row_row = [(i,j) for i,j in combinations(range(3),2)]                 # rows 0,1,2
col_col = [(i+3,j+3) for i,j in combinations(range(3),2)]             # cols 3,4,5
print(f"  rows pairwise share?            : {any(shares(rows[i],rows[j]) for i,j in combinations(range(3),2))}")
print(f"  cols pairwise share?            : {any(shares(cols[i],cols[j]) for i,j in combinations(range(3),2))}")
print(f"  #edges = {len(edges)}  (K_3,3 has 9): {len(edges)==9}")
# triangle-free?
tri = any(all(((a,b) in edges or (b,a) in edges) for a,b in combinations(t,2))
          for t in combinations(range(6),3))
print(f"  triangle-free (omega=2)         : {not tri}")
# every triple of contexts contains a transverse (non-sharing) pair -> mu, a undefined
all_triples_have_transverse = all(
    any(not shares(contexts[a],contexts[b]) for a,b in combinations(t,2))
    for t in combinations(range(6),3))
print(f"  every triple has a transverse   : {all_triples_have_transverse}"
      f"  => family-A data (mu, a) UNDEFINED")

# ---- the +/-I obstruction via explicit 4x4 Pauli matrices ----
I2=[[1,0],[0,1]]; X=[[0,1],[1,0]]; Z=[[1,0],[0,-1]]; Y=[[0,-1j],[1j,0]]
M1={'I':I2,'X':X,'Y':Y,'Z':Z}
def kron(A,B):
    return [[A[i//2][j//2]*B[i%2][j%2] for j in range(4)] for i in range(4)]
def mat(name):  # 'XI' -> X kron I, etc.
    return kron(M1[name[0]], M1[name[1]])
def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
def prod(ctx):
    R=[[1 if i==j else 0 for j in range(4)] for i in range(4)]
    for o in ctx: R=mul(R,mat(o))
    return R
def scalar(M):  # if M = c*I return c else None
    c=M[0][0]
    if all(abs(M[i][j]-(c if i==j else 0))<1e-9 for i in range(4) for j in range(4)):
        return c
    return None
signs=[scalar(prod(c)) for c in contexts]
print(f"  context products (+1=+I, -1=-I) : {[ '+I' if s==1 else ('-I' if s==-1 else '?') for s in signs]}")
glob=1
for s in signs: glob*=s
print(f"  global product of all 6 contexts: {'+I' if glob==1 else '-I'}"
      f"   (each observable in exactly 1 row & 1 col -> naive parity says +I)")
print(f"  ==> the -I mismatch is the central-extension / quadratic-refinement class")
print(f"      (H^2 group cohomology), a single bit -- degree 2, NOT climbing.")

# ---------------------------------------------------------------- Part 3
print("="*68)
print(" Part 3.  Bipartite incidence is 1-dimensional (no climb within family B)")
print("="*68)
print(f"  {'K_{m,n}':>10} | {'b1 = (m-1)(n-1)':>16} | H^{'>='}2(nerve)")
for (m,n) in [(2,2),(3,3),(4,4),(3,7),(9,9)]:
    print(f"  {f'K_{m},{n}':>10} | {(m-1)*(n-1):>16} | 0   (graph: triangle-free => 1-complex)")
print("""
  A bipartite graph is a 1-dimensional clique complex for ANY (m,n): its cohomology
  is concentrated in degrees 0,1.  So the family-B nerve class is forever degree <=1
  (H^2 in group cohomology = the central extension).  There is no degree-2 or -3
  bipartite nerve class to find.""")

# ---------------------------------------------------------------- Part 4
print("="*68)
print(" Part 4.  The only ascent omega -> degree 3 is Sq^1 (lands in family A)")
print("="*68)
print("""  In group cohomology the family-B class is omega in H^2(V) (the Heisenberg
  central-extension class).  The single natural degree-raising operation is the
  Steenrod square Sq^1: H^2 -> H^3, and Sq^1(omega) = n_a is the FAMILY-A class
  (= N_anti mod 2; Direction D).  See bockstein/ and twistor_cp/ for Sq^1 omega.

  ==> There is NO degree-3 family-B class reachable by enlarging the grid; the
      degree-3 thing reachable from omega is family A.  Outlook Q1 (a family-B
      resonance) collapses into Outlook Q2 (the A<->B comparison map, item 23):
      the family-B -> degree-3 ascent IS the unification, not a bigger K_{m,n}.""")

print("="*68)
print(""" CONCLUSION (A2.2)
   The bipartite family has NO resonance tower of its own.  It is the clique-number
   floor (omega=2) of the single arity-resonance/clique tower (family A):
     - enlarging K_{m,n} keeps omega=2 -> ceiling 0 (1-dimensional forever);
     - climbing needs more parts (complete r-partite), = family A, topping at
       H^3 at r=5 = the pentagram K_5 = K_{1,1,1,1,1};
     - the family-B class is omega in H^2 (a +/-I bit); the only ascent to degree 3
       is Sq^1 omega = n_a, the family-A class.
   So "two families" = one tower with family B as its omega=2 floor, joined to
   family A by Sq^1.  Q1 dissolves into Q2 (the comparison map).""")
print("="*68)
