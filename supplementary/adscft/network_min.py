#!/usr/bin/env python3
"""
AdS/CFT line, step 2: the MINIMAL HaPPY network.

Two [[5,1,3]] perfect tensors glued along one edge -> an [[8,2]] holographic
stabilizer code with TWO bulk (logical) qubits.  This is the smallest object that
can carry framework-style CROSS-CONTEXT structure (two overlapping bulk qubits),
which a single tile (one commuting stabilizer group = one context) cannot.

Method: each perfect tensor is the encoder STATE of [[5,1,3]] on 6 qubits
(5 boundary + 1 bulk leg, linked by Xbar(x)X_bulk, Zbar(x)Z_bulk).  Gluing a leg =
Bell contraction (measure X_aX_b, Z_aZ_b; clear and drop a,b) -- an exact stabilizer
operation over F2.  Then we test, for every boundary region A, whether each bulk
qubit's operators are reconstructable on A, and look for cross-context structure.

Pure F2, set-based Paulis.  No dependencies.
"""

from itertools import combinations

# ---------- set-based Paulis over arbitrary labels ----------
# Pauli (mod phase) = (xs, zs): xs = labels carrying X-part, zs = labels carrying Z-part.
I_PAULI = (frozenset(), frozenset())

def mult(p, q):
    return (p[0] ^ q[0], p[1] ^ q[1])

def comm(p, q):
    """True if p,q commute."""
    return (len(p[0] & q[1]) + len(p[1] & q[0])) % 2 == 0

def is_id(p):
    return len(p[0]) == 0 and len(p[1]) == 0

def X(lbl): return (frozenset([lbl]), frozenset())
def Z(lbl): return (frozenset(), frozenset([lbl]))

# ---------- F2 linear algebra ----------
def gf2_reduce(rows):
    """Row-reduce list of int bitmasks; return independent (nonzero) rows."""
    basis = []
    for r in rows:
        for b in basis:
            r = min(r, r ^ b)
        if r:
            basis.append(r)
            basis.sort(reverse=True)
    return basis

def pauli_to_mask(p, labels, idx):
    m = 0
    L = len(labels)
    for lbl in p[0]:
        m |= 1 << idx[lbl]
    for lbl in p[1]:
        m |= 1 << (L + idx[lbl])
    return m

def reduce_independent(paulis):
    """Return an independent generating set (as Paulis) of the group they span."""
    labels = sorted(set().union(*[p[0] | p[1] for p in paulis])) if paulis else []
    idx = {l: i for i, l in enumerate(labels)}
    masks = [pauli_to_mask(p, labels, idx) for p in paulis]
    basis = gf2_reduce([m for m in masks if m])
    L = len(labels)
    out = []
    for m in basis:
        xs = frozenset(labels[i] for i in range(L) if (m >> i) & 1)
        zs = frozenset(labels[i] for i in range(L) if (m >> (L + i)) & 1)
        out.append((xs, zs))
    return out

# ---------- stabilizer measurement & Bell contraction ----------
def measure(gens, M):
    """Post-selected (+1) measurement of Pauli M; return updated generators."""
    anti = [i for i, g in enumerate(gens) if not comm(g, M)]
    if not anti:
        return list(gens)                      # deterministic; group unchanged
    i0 = anti[0]; g0 = gens[i0]
    out = []
    for i, g in enumerate(gens):
        if i == i0:
            continue
        out.append(mult(g, g0) if (not comm(g, M)) else g)
    out.append(M)
    return out

def contract(gens, a, b):
    """Bell-glue legs a,b (measure X_aX_b, Z_aZ_b; clear & drop a,b)."""
    M1 = (frozenset([a, b]), frozenset())       # X_a X_b
    M2 = (frozenset(), frozenset([a, b]))       # Z_a Z_b
    g = measure(gens, M1)
    g = measure(g, M2)
    out = []
    for s in g:
        # a,b content is in the Bell group {I,XX,ZZ,YY}; clearing a auto-clears b
        if a in s[0]:
            s = mult(s, M1)
        if a in s[1]:
            s = mult(s, M2)
        s = (s[0] - {a, b}, s[1] - {a, b})
        if not is_id(s):
            out.append(s)
    return reduce_independent(out)

# ---------- the [[5,1,3]] encoder state on 6 legs ----------
def tile(prefix):
    """Encoder state of [[5,1,3]] on legs prefix0..prefix4 (boundary) + prefixB (bulk)."""
    p = [f"{prefix}{i}" for i in range(5)]
    bulk = f"{prefix}B"
    def P(s):  # 5-char string over IXYZ on the 5 physical legs
        xs = frozenset(p[i] for i, c in enumerate(s) if c in "XY")
        zs = frozenset(p[i] for i, c in enumerate(s) if c in "ZY")
        return (xs, zs)
    stab = [P("XZZXI"), P("IXZZX"), P("XIXZZ"), P("ZXIXZ")]
    # logical links: Xbar(x)X_bulk, Zbar(x)Z_bulk
    Xbar = P("XXXXX"); Zbar = P("ZZZZZ")
    link_x = mult(Xbar, X(bulk))
    link_z = mult(Zbar, Z(bulk))
    gens = stab + [link_x, link_z]
    return gens, p, bulk

# ---------- reconstruction via F2 feasibility ----------
def reconstructable(gens, target, region, bulk_labels):
    """Is `target` (a Pauli on bulk_labels) reconstructable on boundary `region`?
    Feasible iff exists combo of generators equal to target on bulk legs and
    supported within `region` on boundary legs."""
    labels = sorted(set().union(*[g[0] | g[1] for g in gens]))
    idx = {l: i for i, l in enumerate(labels)}; L = len(labels)
    boundary = [l for l in labels if l not in bulk_labels]
    # constraint coordinates: all bulk coords (==target) + boundary coords outside region (==0)
    constr = []   # (coordinate_bit_in_mask, rhs)
    tmask = pauli_to_mask(target, labels, idx)
    for bl in bulk_labels:
        constr.append((idx[bl], (tmask >> idx[bl]) & 1))             # x part
        constr.append((L + idx[bl], (tmask >> (L + idx[bl])) & 1))   # z part
    for bl in boundary:
        if bl not in region:
            constr.append((idx[bl], 0))
            constr.append((L + idx[bl], 0))
    # variables = generators; equation per constraint: sum_i c_i * gen_i[coord] = rhs
    gmask = [pauli_to_mask(g, labels, idx) for g in gens]
    # one linear equation (coeff over generator-variables, rhs bit) per constraint
    eqs = []
    for (coord, rhs) in constr:
        coeff = 0
        for i, gm in enumerate(gmask):
            if (gm >> coord) & 1:
                coeff |= 1 << i
        eqs.append((coeff, rhs))
    # GF(2) Gaussian elimination for feasibility of  A c = rhs
    pivots = []   # (pivot_bit, coeff, rhs)
    for coeff, rhs in eqs:
        c, r = coeff, rhs
        for pb, pc, pr in pivots:
            if (c >> pb) & 1:
                c ^= pc; r ^= pr
        if c == 0:
            if r == 1:
                return False          # 0 = 1  -> infeasible
        else:
            pivots.append((c.bit_length() - 1, c, r))
    return True

def bulk_recon(gens, bulk, bulk_labels, region):
    return (reconstructable(gens, X(bulk), region, bulk_labels) and
            reconstructable(gens, Z(bulk), region, bulk_labels))

# ================= sanity: single tile reproduces step 1 =================
print("=== sanity: single [[5,1,3]] tile via the network machinery ===")
g1, b1, blk1 = tile("A")
sizes = {k: [0, 0] for k in range(6)}
for k in range(6):
    for A in combinations(b1, k):
        sizes[k][1] += 1
        sizes[k][0] += int(bulk_recon(g1, blk1, {blk1}, set(A)))
for k in range(6):
    print(f"  |A|={k}: {sizes[k][0]}/{sizes[k][1]} reconstruct")
print("  expect threshold |A|>=3 (matches happy_513.py)\n")

# ================= the minimal 2-tile network =================
print("=== minimal network: two tiles glued on edge (A4 = B0) ===")
gA, bdA, blkA = tile("A")
gB, bdB, blkB = tile("B")
gens = gA + gB                      # disjoint labels -> commute
gens = contract(gens, "A4", "B0")  # glue
bulk_labels = {blkA, blkB}
boundary = sorted(l for l in set().union(*[g[0] | g[1] for g in gens])
                  if l not in bulk_labels)
print(f"  boundary qubits ({len(boundary)}): {boundary}")
print(f"  bulk qubits: {sorted(bulk_labels)}")
print(f"  stabilizer generators: {len(gens)} (state on {len(boundary)+len(bulk_labels)} qubits)\n")

# reconstruction profile per bulk qubit
for blk in sorted(bulk_labels):
    prof = {k: [0, 0] for k in range(len(boundary) + 1)}
    for k in range(len(boundary) + 1):
        for A in combinations(boundary, k):
            prof[k][1] += 1
            prof[k][0] += int(bulk_recon(gens, blk, bulk_labels, set(A)))
    thr = min((k for k in prof if prof[k][0] == prof[k][1] and prof[k][0] > 0),
              default=None)
    print(f"  bulk {blk}: reconstructing-regions by |A|: "
          + ", ".join(f"{k}:{prof[k][0]}/{prof[k][1]}" for k in prof if prof[k][1]))
    print(f"           first all-reconstruct size = {thr}")

# minimal reconstruction regions (wedges) for each bulk qubit
print("\n  minimal reconstruction regions (smallest A reconstructing each bulk):")
for blk in sorted(bulk_labels):
    minsets = []
    for k in range(len(boundary) + 1):
        found = [set(A) for A in combinations(boundary, k)
                 if bulk_recon(gens, blk, bulk_labels, set(A))]
        if found:
            minsets = found; break
    print(f"   bulk {blk}: size {len(minsets[0])}, e.g. "
          + "; ".join("{" + ",".join(sorted(s)) + "}" for s in minsets[:4])
          + (f"  (+{len(minsets)-4} more)" if len(minsets) > 4 else ""))

# overlap: regions reconstructing BOTH bulk qubits, by size
print("\n  regions reconstructing BOTH bulk qubits (wedge overlap), by |A|:")
both = {k: 0 for k in range(len(boundary) + 1)}
for k in range(len(boundary) + 1):
    for A in combinations(boundary, k):
        if all(bulk_recon(gens, blk, bulk_labels, set(A)) for blk in bulk_labels):
            both[k] += 1
print("   " + ", ".join(f"{k}:{both[k]}" for k in both if both[k]))

print("""
  Reading:
  - Each bulk qubit's wedge is LOCAL to its own tile's legs (correct holography).
  - The bulk is a 2-LOGICAL-QUBIT system => the 2-qubit Pauli geometry W(3,2),
    i.e. the DOILY Sp(4,2): the natural home of the Mermin SQUARE = family B / H^2.
  - So a 2-tile network can only probe the H^2/family-B bridge. The framework's
    DISTINCTIVE object -- the Mermin PENTAGRAM = family A / H^3 -- lives in the
    3-qubit geometry W(5,2), hence needs THREE bulk qubits = a THREE-tile network.

  => Minimal object for the H^3 bridge = 3 tiles (next step). 2 tiles = H^2 home.
""")
