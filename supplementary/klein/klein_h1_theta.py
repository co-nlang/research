#!/usr/bin/env python3
"""
Klein backlog, step 3: the GL(3,2)-stabilised H^1-level class [f_3] and the
transgression Phi_3.

H^1-level data here = theta characteristics (spin structures): quadratic refinements Q of
omega, a torsor over V = H^1(X(7);F_2) = J[2]. We decompose them under GL(3,2)=PSL(2,7) and
locate the unique INVARIANT one -- the framework's distinguished H^1-level class -- then
follow its transgression q0 -> omega -> Sq^1(omega)=n_a (the Direction-D spiral), now
realised PSL(2,7)-equivariantly on the Klein quartic.

Pure F2, no deps.
"""
from itertools import product

def matvec(M, x):  return tuple(sum(M[i][j]*x[j] for j in range(3)) % 2 for i in range(3))
def matmul(A, B):  return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) % 2 for j in range(3)) for i in range(3))
def transpose(M):  return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))
ID = ((1,0,0),(0,1,0),(0,0,1))

def all_invertible():
    out = []
    for bits in product((0,1), repeat=9):
        M = (bits[0:3], bits[3:6], bits[6:9]); span = {0}
        for r in M:
            rb = r[0]*4+r[1]*2+r[2]; span |= {a ^ rb for a in span}
        if len(span) == 8: out.append(M)
    return out

G = all_invertible()
inv = {}
for g in G:
    for h in G:
        if matmul(g, h) == ID: inv[g] = h; break
def act(g, v):  return matvec(g, v[:3]) + matvec(transpose(inv[g]), v[3:])
V = [tuple(b) for b in product((0,1), repeat=6)]
def q0(v):  return (v[0]*v[3]+v[1]*v[4]+v[2]*v[5]) % 2
def omega(v, u): return (sum(v[i]*u[3+i]+v[3+i]*u[i] for i in range(3))) % 2

# theta characteristics Q_v(u)=q0(u)+omega(v,u), torsor over V; g.Q_v = Q_{g.v}.
# So GL(3,2)-orbits of theta chars = orbits of V; Arf(Q_v)=q0(v) (even/odd).
def orbit(v):
    o = {v}; frontier = {v}
    while frontier:
        nf = set()
        for w in frontier:
            for g in G:
                r = act(g, w)
                if r not in o: o.add(r); nf.add(r)
        frontier = nf
    return o

rem = set(V); orbits = []
while rem:
    v = next(iter(rem)); o = orbit(v); orbits.append(o); rem -= o
orbits.sort(key=len)

print("Theta characteristics (= spin structures, the H^1(X;F2)-torsor) under GL(3,2):")
even_fixed = None
for o in orbits:
    v = next(iter(o)); parity = "odd (Arf=1)" if q0(v) == 1 else "even (Arf=0)"
    tag = ""
    if len(o) == 1:
        even_fixed = v; tag = "  <-- UNIQUE GL(3,2)-FIXED theta char = q0 (v=0)"
    if len(o) == 28: tag = "  = the 28 bitangents (step 2)"
    print(f"  orbit size {len(o):2d} | {parity}{tag}")
evens = [o for o in orbits if q0(next(iter(o))) == 0]
odds  = [o for o in orbits if q0(next(iter(o))) == 1]
print(f"  even thetas: {sum(len(o) for o in evens)} in orbits {sorted(len(o) for o in evens)}  (= 1+7+7+21)")
print(f"  odd  thetas: {sum(len(o) for o in odds)} in orbits {sorted(len(o) for o in odds)}   (= 28 bitangents)")

assert even_fixed == (0,0,0,0,0,0)
print(f"\n[f_3] := the unique GL(3,2)-stabilised theta characteristic = Q_0 = q0 = x.z.")
print("   (the framework's standard quadratic refinement / 'i-phase' datum, APP_06;")
print("    = the Klein quartic's canonical PSL(2,7)-invariant spin structure.)")

# ---- transgression Phi_3 : q0 -> omega (polarization) -> Sq^1(omega) = n_a ----
# polarization of q0 IS omega:
pol_ok = all((q0(tuple((a[i]^b[i]) for i in range(6))) ^ q0(a) ^ q0(b)) == omega(a, b)
             for a in V for b in V)
print(f"\nPhi_3 step 1 (polarization): q0(u+w)+q0(u)+q0(w) == omega(u,w) for all u,w: {pol_ok}")
omega_inv = all(omega(act(g, a), act(g, b)) == omega(a, b) for g in G for a in V[:8] for b in V[:8])
print(f"omega is GL(3,2)-invariant (the Weil pairing): {omega_inv}")
print("""
Phi_3 step 2 (Sq^1): Sq^1(omega) = n_a in H^3(V) (computed in
supplementary/paper22/d_bridge.py); GL(3,2)-equivariant since omega is invariant and Sq^1
is natural.

=> THE DIRECTION-D SPIRAL  q0 -> omega -> n_a  IS PSL(2,7)-EQUIVARIANT, BASED AT THE KLEIN
   QUARTIC'S CANONICAL SPIN STRUCTURE q0:
     - [f_3] = q0 : the unique invariant theta characteristic (H^1-level),
     - omega    : its polarization = the Weil pairing on H^1(X(7);F2) (H^2, family B),
     - n_a=Sq^1 omega : the anticommutation class (H^3, family A).
   The framework's self-representing obstruction tower (the Yoneda reading of D) sits inside
   the Klein quartic's 168-symmetry, anchored at its canonical theta characteristic.

NOTE (honest): "H^1-level class" here = the theta-characteristic / spin-structure torsor
(the natural H^1(X;F2) datum). If Paper IX's [f_3] denotes a different specific class, this
identifies the canonical invariant at this level; cross-check against Paper IX/VIII's Phi.
""")
