#!/usr/bin/env python3
"""
AdS/CFT line, step 3: the THREE-tile network and the H^3 test.

Three [[5,1,3]] perfect tensors glued in a chain (A4=B0, B4=C0) -> an [[11,3]]
holographic code whose THREE bulk qubits form a 3-qubit system W(5,2) -- the home
of the Mermin pentagram = family A / H^3 (the framework's distinctive modulus).

We ask the bridge question decisively:
  (2) is the bulk a FAITHFUL 3-qubit Pauli system?  (=> the framework's H^3 results
      apply to it verbatim, encoding-independently)
  (3) does the minimal reconstruction WEDGE of a bulk operator depend ONLY on which
      tiles it touches (pure erasure/geometry), or on its contextual role too?

If wedge = f(tile-support) exactly, holographic reconstruction is erasure-governed and
the H^3 contextuality is invisible to it: same W(5,2), different obstruction.

Pure F2, set-based Paulis.  Self-contained.
"""
from itertools import combinations

I_PAULI = (frozenset(), frozenset())
def mult(p, q): return (p[0] ^ q[0], p[1] ^ q[1])
def comm(p, q): return (len(p[0] & q[1]) + len(p[1] & q[0])) % 2 == 0
def is_id(p): return len(p[0]) == 0 and len(p[1]) == 0
def X(l): return (frozenset([l]), frozenset())
def Z(l): return (frozenset(), frozenset([l]))

def gf2_reduce(rows):
    basis = []
    for r in rows:
        for b in basis:
            r = min(r, r ^ b)
        if r:
            basis.append(r); basis.sort(reverse=True)
    return basis

def pauli_to_mask(p, labels, idx):
    L = len(labels); m = 0
    for l in p[0]: m |= 1 << idx[l]
    for l in p[1]: m |= 1 << (L + idx[l])
    return m

def reduce_independent(paulis):
    if not paulis: return []
    labels = sorted(set().union(*[p[0] | p[1] for p in paulis]))
    idx = {l: i for i, l in enumerate(labels)}; L = len(labels)
    basis = gf2_reduce([pauli_to_mask(p, labels, idx) for p in paulis if not is_id(p)])
    out = []
    for m in basis:
        xs = frozenset(labels[i] for i in range(L) if (m >> i) & 1)
        zs = frozenset(labels[i] for i in range(L) if (m >> (L + i)) & 1)
        out.append((xs, zs))
    return out

def measure(gens, M):
    anti = [i for i, g in enumerate(gens) if not comm(g, M)]
    if not anti: return list(gens)
    i0 = anti[0]; g0 = gens[i0]
    out = []
    for i, g in enumerate(gens):
        if i == i0: continue
        out.append(mult(g, g0) if not comm(g, M) else g)
    out.append(M)
    return out

def contract(gens, a, b):
    M1 = (frozenset([a, b]), frozenset()); M2 = (frozenset(), frozenset([a, b]))
    g = measure(measure(gens, M1), M2)
    out = []
    for s in g:
        if a in s[0]: s = mult(s, M1)
        if a in s[1]: s = mult(s, M2)
        s = (s[0] - {a, b}, s[1] - {a, b})
        if not is_id(s): out.append(s)
    return reduce_independent(out)

def tile(prefix):
    p = [f"{prefix}{i}" for i in range(5)]; bulk = f"{prefix}B"
    def P(s):
        return (frozenset(p[i] for i, c in enumerate(s) if c in "XY"),
                frozenset(p[i] for i, c in enumerate(s) if c in "ZY"))
    stab = [P("XZZXI"), P("IXZZX"), P("XIXZZ"), P("ZXIXZ")]
    return stab + [mult(P("XXXXX"), X(bulk)), mult(P("ZZZZZ"), Z(bulk))], p, bulk

# ---- linear solver over F2: find a combo of gens matching constraints ----
def _solve(eqs, nvars):
    """eqs: list of (coeff_int over nvars, rhs_bit). Return a solution int or None."""
    piv = {}
    for coeff, rhs in eqs:
        c, r = coeff, rhs
        for pb in list(piv):
            if (c >> pb) & 1:
                pc, pr = piv[pb]; c ^= pc; r ^= pr
        if c == 0:
            if r: return None
            continue
        pb = c.bit_length() - 1
        piv[pb] = (c, r)
    sol = 0
    for pb in sorted(piv):
        c, r = piv[pb]; x = r; cc = c & ~(1 << pb)
        while cc:
            j = cc & -cc; bit = j.bit_length() - 1
            if (sol >> bit) & 1: x ^= 1
            cc ^= j
        if x: sol |= 1 << pb
    return sol

def _setup(gens, bulk_labels):
    labels = sorted(set().union(*[g[0] | g[1] for g in gens]))
    idx = {l: i for i, l in enumerate(labels)}; L = len(labels)
    gmask = [pauli_to_mask(g, labels, idx) for g in gens]
    boundary = [l for l in labels if l not in bulk_labels]
    return labels, idx, L, gmask, boundary

def reconstructable(gens, target, region, bulk_labels, ctx=None):
    labels, idx, L, gmask, boundary = ctx or _setup(gens, bulk_labels)
    tmask = pauli_to_mask(target, labels, idx)
    constr = []
    for bl in bulk_labels:
        constr.append((idx[bl], (tmask >> idx[bl]) & 1))
        constr.append((L + idx[bl], (tmask >> (L + idx[bl])) & 1))
    for bl in boundary:
        if bl not in region:
            constr.append((idx[bl], 0)); constr.append((L + idx[bl], 0))
    eqs = []
    for coord, rhs in constr:
        coeff = 0
        for i, gm in enumerate(gmask):
            if (gm >> coord) & 1: coeff |= 1 << i
        eqs.append((coeff, rhs))
    return _solve(eqs, len(gmask)) is not None

def find_op(gens, target_bulk, bulk_labels, ctx=None):
    """Return a stabilizer-group element with bulk-part = target_bulk (full Pauli)."""
    labels, idx, L, gmask, boundary = ctx or _setup(gens, bulk_labels)
    tmask = pauli_to_mask(target_bulk, labels, idx)
    constr = []
    for bl in bulk_labels:
        constr.append((idx[bl], (tmask >> idx[bl]) & 1))
        constr.append((L + idx[bl], (tmask >> (L + idx[bl])) & 1))
    eqs = []
    for coord, rhs in constr:
        coeff = 0
        for i, gm in enumerate(gmask):
            if (gm >> coord) & 1: coeff |= 1 << i
        eqs.append((coeff, rhs))
    c = _solve(eqs, len(gmask))
    if c is None: return None
    acc = I_PAULI
    for i in range(len(gmask)):
        if (c >> i) & 1: acc = mult(acc, gens[i])
    return acc

def restrict(p, keep):
    return (frozenset(p[0] & keep), frozenset(p[1] & keep))

# ================= build the 3-tile chain =================
gA, _, bA = tile("A"); gB, _, bB = tile("B"); gC, _, bC = tile("C")
gens = gA + gB + gC
gens = contract(gens, "A4", "B0")
gens = contract(gens, "B4", "C0")
bulk = {bA, bB, bC}                       # {AB,BB,CB}
ctx = _setup(gens, bulk)
labels, idx, L, gmask, boundary = ctx
print(f"3-tile chain: [[{len(boundary)},{len(bulk)}]] code")
print(f"  boundary ({len(boundary)}): {boundary}")
print(f"  bulk: {sorted(bulk)}   generators: {len(gens)}\n")

# ---- (2) bulk faithfulness: boundary reps obey the 3-qubit Pauli algebra ----
bl = sorted(bulk)
LX = {b: restrict(find_op(gens, X(b), bulk, ctx), frozenset(boundary)) for b in bl}
LZ = {b: restrict(find_op(gens, Z(b), bulk, ctx), frozenset(boundary)) for b in bl}
print("(2) Bulk faithfulness — symplectic form on boundary logical reps:")
ok = True
for u in bl:
    row = []
    for v in bl:
        cxz = 0 if comm(LX[u], LZ[v]) else 1     # want delta_uv
        cxx = 0 if comm(LX[u], LX[v]) else 1     # want 0
        czz = 0 if comm(LZ[u], LZ[v]) else 1     # want 0
        row.append(f"{cxz}{cxx}{czz}")
        if cxz != (1 if u == v else 0) or cxx or czz: ok = False
    print("   " + u + ": " + "  ".join(f"{v}:{r}" for v, r in zip(bl, row)))
print(f"   (entries = omega(LX_u,LZ_v) omega(LX_u,LX_v) omega(LZ_u,LZ_v))")
print(f"   => faithful 3-qubit Pauli algebra: {ok}  "
      f"(so the framework's H^3/W(5,2) results apply to the bulk verbatim)\n")

# ---- (3) decisive: minimal wedge depends only on tile-support? ----
def tiles_touched(target):
    t = set()
    for b, name in ((bA, 'A'), (bB, 'B'), (bC, 'C')):
        if b in target[0] or b in target[1]: t.add(name)
    return frozenset(t)

def min_wedge(target):
    for k in range(len(boundary) + 1):
        for A in combinations(boundary, k):
            if reconstructable(gens, target, set(A), bulk, ctx):
                return k
    return None

# enumerate all 63 nontrivial bulk Paulis
def bulk_paulis():
    combos = []
    opts = [(0,0),(1,0),(0,1),(1,1)]  # I,X,Z,Y as (x,z)
    for a in opts:
        for b in opts:
            for c in opts:
                xs = set(); zs = set()
                for (xx,zz), lab in zip((a,b,c), (bA,bB,bC)):
                    if xx: xs.add(lab)
                    if zz: zs.add(lab)
                p = (frozenset(xs), frozenset(zs))
                if not is_id(p): combos.append(p)
    return combos

allp = bulk_paulis()
by_support = {}
for p in allp:
    s = tiles_touched(p); w = min_wedge(p)
    by_support.setdefault(s, []).append(w)

print("(3) minimal reconstruction wedge by tile-support class:")
print("   support tiles | #ops | min-wedge sizes observed")
decisive = True
for s in sorted(by_support, key=lambda x: (len(x), sorted(x))):
    ws = by_support[s]; uniq = sorted(set(ws))
    s_str = "{" + ",".join(sorted(s)) + "}"
    print(f"      {s_str} <{len(s)}> | {len(ws):2d} | {uniq}")
    if len(uniq) != 1: decisive = False

print()
if decisive:
    print("VERDICT: min-wedge is CONSTANT within each tile-support class.")
    print("  => holographic reconstruction is purely erasure/geometry (support-governed);")
    print("     the bulk's H^3 contextuality (which DOES live in this faithful W(5,2)) is")
    print("     INVISIBLE to reconstruction. Same W(5,2) substrate, two independent")
    print("     obstructions. The AdS/CFT-framework link is SHAPE-LEVEL (boundary-")
    print("     underdetermines-bulk + complementarity + wedge nesting), not an")
    print("     obstruction-measure identity.")
else:
    print("VERDICT: min-wedge VARIES within a tile-support class -- a contextual")
    print("  signature beyond pure erasure. Worth investigating (possible positive bridge).")
