#!/usr/bin/env python3
"""
Klein backlog, step 2: tighten the hinge -- the 28-orbit IS the 28 bitangents,
as PSL(2,7)-sets, via an explicit GL(3,2)-equivariant bijection.

The 28 bitangents of a genus-3 curve = its 28 ODD theta characteristics = quadratic
refinements Q of the symplectic form omega on F_2^6 with Arf(Q)=1 (classical). Theta
characteristics form a torsor over V: fix the even form q0(x,z)=x.z; every refinement is
Q_v(u) = q0(u) + omega(v,u) for a unique v in V, and Arf(Q_v) = q0(v). Hence
   odd theta characteristics  <->  { v : q0(v)=1 }  =  the 28 anti-flags (our 28-orbit),
and the map v |-> Q_v is GL(3,2)-equivariant because GL(3,2) preserves q0.

Two PSL(2,7)-sets, one explicit natural iso. Pure F2, no deps.
"""
from itertools import product

# ---- GL(3,2) and its symplectic (Siegel/Levi) action on F2^6, from step 1 ----
def matvec(M, x):  return tuple(sum(M[i][j]*x[j] for j in range(3)) % 2 for i in range(3))
def matmul(A, B):  return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) % 2 for j in range(3)) for i in range(3))
def transpose(M):  return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))
ID = ((1,0,0),(0,1,0),(0,0,1))

def all_invertible():
    mats = []
    for bits in product((0,1), repeat=9):
        M = (bits[0:3], bits[3:6], bits[6:9])
        span = {0}
        for r in M:
            rb = r[0]*4 + r[1]*2 + r[2]
            span |= {a ^ rb for a in span}
        if len(span) == 8:
            mats.append(M)
    return mats

G = all_invertible()
inv = {}
for g in G:
    for h in G:
        if matmul(g, h) == ID:
            inv[g] = h; break

def act(g, v):
    x, z = v[:3], v[3:]
    return matvec(g, x) + matvec(transpose(inv[g]), z)

V = [tuple(b) for b in product((0,1), repeat=6)]
def q0(v):  return (v[0]*v[3] + v[1]*v[4] + v[2]*v[5]) % 2          # even quad form x.z
def omega(v, u): return (sum(v[i]*u[3+i] + v[3+i]*u[i] for i in range(3))) % 2

print(f"|GL(3,2)| = {len(G)};  acts symplectically on F2^6 (step 1).")

# G preserves q0  (=> G < O(q0), the orthogonal group of the even form)
assert all(q0(act(g, v)) == q0(v) for g in G for v in V)
print("G preserves the even quadratic form q0(x,z)=x.z  =>  G < O(q0).")

# the 28 anti-flags = { v : q0(v)=1 }
anti = [v for v in V if q0(v) == 1]
assert len(anti) == 28
# (cross-check they are exactly the x!=0,z!=0,x.z=1 orbit of step 1)
assert all(any(v[:3]) and any(v[3:]) for v in anti)
print(f"anti-flags {{v: q0(v)=1}} : {len(anti)} points (= the step-1 size-28 orbit).")

# ---- odd theta characteristics: Q_v(u) = q0(u) + omega(v,u); Arf via #zeros ----
def arf(Qtt):                       # Arf=0 iff value 0 taken 36x; =1 iff 28x  (n=3)
    zeros = sum(1 for b in Qtt if b == 0)
    return 0 if zeros == 36 else 1  # (only 36 or 28 occur for a refinement of omega)

def Q_tt(v):                        # truth table of Q_v over all u in V
    return tuple((q0(u) + omega(v, u)) % 2 for u in V)

odd = [v for v in V if arf(Q_tt(v)) == 1]
print(f"odd theta characteristics (Arf=1) among the 64 refinements Q_v : {len(odd)}")

# the bijection: v |-> Q_v sends anti-flags bijectively onto the odd theta chars
assert set(odd) == set(anti)
print("EXPLICIT BIJECTION  anti-flags  <->  odd theta characteristics :  v |-> Q_v")
print("   (Arf(Q_v) = q0(v), so Arf=1  <=>  v is an anti-flag).")

# ---- G-equivariance of v |-> Q_v ----
# need: Q_{g.v} (u) == (g.Q_v)(u) := Q_v(g^{-1}.u)  for all g, all u
def gtt_equivariant():
    for g in G:
        ginv = inv[g]
        for v in anti:
            lhs = Q_tt(act(g, v))
            rhs = tuple((q0(act(ginv, u)) + omega(v, act(ginv, u))) % 2 for u in V)
            if lhs != rhs:
                return False
    return True

print(f"G-equivariant (Q_{{g.v}} = g.Q_v for all g in G, all 28 v): {gtt_equivariant()}")

# stabilizer of an anti-flag = order 6, and non-abelian => S3
v0 = anti[0]
stab = [g for g in G if act(g, v0) == v0]
# abelian?
ab = all(matmul(a, b) == matmul(b, a) for a in stab for b in stab)
print(f"point-stabilizer |Stab(v0)| = {len(stab)} ; abelian = {ab}  "
      f"=> {'S_3' if (len(stab)==6 and not ab) else '?'}  (matches bitangent stab in PSL(2,7))")

print("""
TIGHTENED HINGE (rigorous)
  v |-> Q_v = (u |-> q0(u)+omega(v,u)) is an EXPLICIT GL(3,2)-EQUIVARIANT BIJECTION from
  the 28 anti-flags to the 28 odd theta characteristics. The 28 odd theta characteristics
  ARE the 28 bitangents of a genus-3 curve (classical). Stabilizer = S_3 (order 6), exactly
  the bitangent stabilizer in PSL(2,7).

  => the step-1 size-28 orbit is the 28 bitangents of the Klein quartic, AS PSL(2,7)-SETS
     -- not a size coincidence but a natural isomorphism.

  Why this is the SAME PSL(2,7) as the curve's: the Klein quartic acts on J[2]=F_2^6
  (Weil pairing = omega) by a faithful 6-dim symplectic F_2-representation. The F_2-irreps
  of GL(3,2)=PSL(2,7) are 1, 3 (natural), 3' (dual), 8 (Steinberg); the only faithful
  6-dim self-dual symplectic one is 3 (+) 3' = the Siegel/Levi embedding used here. So the
  curve's J[2]-embedding and ours coincide up to conjugacy -- the comparison is forced, not
  chosen.
""")
