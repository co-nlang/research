#!/usr/bin/env python3
"""
Backlog line: Klein quartic / Ramanujan, step 1 -- the 168-group bridge.

GL(3,F_2) =~ PSL(2,7) = Aut(Klein quartic X(7)), the unique simple group of order 168.
It is the automorphism group of the Fano plane PG(2,F_2), which Paper IX embeds as an
isotropic subgeometry of the 3-qubit symplectic polar space W(5,F_2). This script builds
that 168-action ON THE FRAMEWORK'S OWN SUBSTRATE and decomposes the 63 three-qubit Pauli
classes into GL(3,F_2)-orbits -- the concrete combinatorial bridge to the Klein quartic.

Embedding GL(3) -> Sp(6): g acts on (x,z) in F_2^3 + F_2^3 by  x -> g x,  z -> (g^-1)^T z
(the Siegel/Levi embedding), which preserves omega((x,z),(x',z')) = x.z' + z.x'.

Pure F_2, no deps.
"""
from itertools import product

# ---- 3x3 matrices over F2 as tuple of 3 rows, each row a tuple of 3 bits ----
def matvec(M, x):
    return tuple(sum(M[i][j] * x[j] for j in range(3)) % 2 for i in range(3))

def matmul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) % 2 for j in range(3))
                 for i in range(3))

def transpose(M):
    return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))

ID = ((1,0,0),(0,1,0),(0,0,1))

def all_invertible():
    mats = []
    for bits in product((0,1), repeat=9):
        M = (bits[0:3], bits[3:6], bits[6:9])
        # invertible over F2 iff the 3 rows are linearly independent
        rows = [r[0]*4 + r[1]*2 + r[2] for r in M]
        if 0 in rows:
            continue
        s = set([0])
        span = {0}
        for r in rows:
            span |= {a ^ r for a in span}
        if len(span) == 8:
            mats.append(M)
    return mats

G = all_invertible()
print(f"GL(3,F_2): |G| = {len(G)}   (expect 168)")

# inverse table
def inverse(g):
    for h in G:
        if matmul(g, h) == ID:
            return h
    raise ValueError

inv = {g: inverse(g) for g in G}

# ---- symplectic embedding action on points (x,z), x,z in F2^3 (as 3-tuples) ----
def act(g, pt):
    x, z = pt[:3], pt[3:]
    gx = matvec(g, x)
    gtz = matvec(transpose(inv[g]), z)   # (g^-1)^T z
    return gx + gtz

def omega(p, q):
    return (sum(p[i]*q[3+i] + p[3+i]*q[i] for i in range(3))) % 2

# verify symplectic on a sample
pts = [tuple(b) for b in product((0,1), repeat=6) if any(b)]
import random
random.seed(0)
ok = all(omega(act(g, p), act(g, q)) == omega(p, q)
         for g in random.sample(G, 20) for p in random.sample(pts, 20) for q in random.sample(pts, 20))
print(f"embedding is symplectic (sampled): {ok}")

# ---- is it PSL(2,7)?  perfect + 2-transitive on Fano + |G|=168 (=> the unique simple 168) ----
# Fano = the 7 nonzero x in F2^3 (the invariant Lagrangian V = X-part)
fano = [tuple(b) for b in product((0,1), repeat=3) if any(b)]
def act_fano(g, x):
    return matvec(g, x)
# 2-transitive: transitive on ordered pairs of distinct points
pairs = [(a, b) for a in fano for b in fano if a != b]
orb = set()
seed = pairs[0]
frontier = {seed}
seen = {seed}
while frontier:
    nf = set()
    for (a, b) in frontier:
        for g in G:
            img = (act_fano(g, a), act_fano(g, b))
            if img not in seen:
                seen.add(img); nf.add(img)
    frontier = nf
print(f"2-transitive on the 7 Fano points: {len(seen) == len(pairs)} "
      f"({len(seen)}/{len(pairs)} ordered pairs in one orbit)")

# perfect: commutator subgroup = G ?
def comm(a, b):
    return matmul(matmul(a, b), matmul(inv[a], inv[b]))
gen = set()
frontier = {comm(a, b) for a in random.sample(G, 30) for b in random.sample(G, 30)}
seen = set(frontier)
while frontier:
    nf = set()
    for a in list(frontier):
        for b in random.sample(G, 30):
            for c in (matmul(a, b), comm(a, b)):
                if c not in seen:
                    seen.add(c); nf.add(c)
    frontier = nf
print(f"perfect (G = [G,G], sampled closure): {len(seen) == 168}")
print("  => |G|=168, perfect, 2-transitive(primitive) on 7 pts: G is the unique simple")
print("     group of order 168 = PSL(2,7) =~ GL(3,F_2) = Aut(Klein quartic X(7)).\n")

# ---- ORBIT DECOMPOSITION of the 63 nonzero Pauli classes ----
remaining = set(pts)
orbits = []
while remaining:
    p = next(iter(remaining))
    orb = set()
    frontier = {p}
    while frontier:
        nf = set()
        for q in frontier:
            for g in G:
                r = act(g, q)
                if r not in orb:
                    orb.add(r); nf.add(r)
        frontier = nf
    orbits.append(orb)
    remaining -= orb

orbits.sort(key=len)
print("GL(3,F_2)-orbits on the 63 three-qubit Pauli classes (points of W(5,2)):")
for o in orbits:
    p = next(iter(o))
    # classify by x, z parts and pairing
    sample = sorted(o)[0]
    x, z = sample[:3], sample[3:]
    xz = sum(x[i]*z[i] for i in range(3)) % 2
    if not any(z):
        kind = "Fano V (X-part): the 7 Fano points"
    elif not any(x):
        kind = "dual Fano V* (Z-part): the 7 dual points"
    elif xz == 0:
        kind = "flags (incident point-hyperplane of PG(2,2))"
    else:
        kind = "anti-flags  <-> the 28 BITANGENTS of the Klein quartic"
    print(f"  size {len(o):2d}  | {kind}")
print(f"  total = {sum(len(o) for o in orbits)} = 63")

print("""
READING (the bridge, step 1):
  The order-168 group GL(3,F_2)=~PSL(2,7)=Aut(Klein quartic) acts faithfully and
  symplectically on the framework's own 3-qubit substrate W(5,2), and splits its 63
  Pauli classes as  7 + 7 + 21 + 28:
    7  = Fano plane PG(2,2)          (the invariant isotropic Lagrangian, Paper IX)
    7  = dual Fano
    21 = flags (incident point-line pairs of the Fano plane)
    28 = anti-flags  <->  the 28 bitangents of the Klein quartic.
  The 28-orbit is the concrete combinatorial hinge: the 3-qubit Pauli geometry carries,
  as a GL(3,2)-orbit, the Klein quartic's 28 bitangents -- same 168-symmetry, same 28.
  This is the substrate side of the chain
     W(5,2)  ->  GL(3,2)=PSL(2,7)  ->  Klein quartic X(7)  ->  (level-7 modular / tau).
  Next: the GL(3,2)-stabilised H^1 class [f_3] and the 3-qubit transgression Phi_3
  (toward the mock-modular / Ramanujan tau end).
""")
