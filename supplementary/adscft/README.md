# AdS/CFT line — step 1: the HaPPY building block in framework-native terms

Companion computation to `research/insight/adscft_holographic_codes.md`.

## What this is

The HaPPY holographic code is built from one perfect tensor: the **[[5,1,3]]**
five-qubit code. `happy_513.py` puts it into the framework's symplectic-F2 language
(stabilizer $S$ = isotropic subspace of $\mathbb F_2^{10}$; logical $=S^\perp/S$;
boundary region $A$ = coordinate subspace) and sweeps all 32 regions.

## Result (rigorous, reproducible — `python3 happy_513.py`)

| $|A|$ | regions reconstructing the bulk |
|---|---|
| 0,1,2 | **none** |
| 3,4,5 | **all** |

- **Sharp reconstruction threshold: bulk recoverable $\iff |A|\ge 3$.** A clean
  "boundary underdetermines bulk" wall, in $\mathrm{Sp}(10,\mathbb F_2)$ terms.
- **Entanglement-wedge complementarity is exact:** over all 32 regions, exactly one
  of $A,\bar A$ owns the bulk — **0 violations**. The entanglement wedge, on the
  building block.

## Honest reading of the bridge

This makes the *shape* concrete and rigorous (sharp threshold + complementarity +
same objects as the framework: stabilizer = Lagrangian = MASA). It does **not**
identify the framework's obstruction with the code's:

- the threshold is $|A|\ge 3$ of **5 qubits** — a *distance/erasure* number
  ($d=3$ corrects $\le 2$ erasures);
- the framework's ceiling is **arity-5 / $H^3$ among *contexts*** (Paper XXII).

Different "5"s indexing different things. So the naive *"arity ceiling = wedge
threshold"* identification **fails at face value on the tile**. What transfers is the
shape, not the number. Verdict: **same shape, same objects — contextuality/$H^3$ and
erasure/distance are different faces of "local data insufficient."** (This is exactly
the caution flagged in the insight note, now demonstrated.)

## Where the bridge could still have teeth (step 2, not yet done)

The tile's reconstruction is pure erasure/distance — no nontrivial contextuality
among one logical qubit. The framework's contextuality (cross-context $N_{\mathrm
{anti}}$, the $H^3$ modulus) is a *multipartite* property. So if a genuine
correspondence exists, it must be an **emergent network property**, not a tile
property. Candidate next probes:

1. **Is the tile contextual at all** in the framework sense? (Likely no — would
   confirm contextuality and reconstruction are orthogonal at tile level.)
2. **Small HaPPY network** (a few pentagons): multiple bulk qubits + tensor gluing.
   Does any cross-context / $H^3$-type structure appear, and does it track which
   bulk operators need $\ge k$ boundary regions to reconstruct?
3. If neither lands, the honest conclusion is that the AdS/CFT connection is a
   *shape*-level correspondence (boundary-underdetermines-bulk + complementarity),
   strong but not an obstruction-measure identity — and the line is recorded as such.

## Step 2 — the minimal network (`network_min.py`)

A general stabilizer-tensor-network contractor in F2 (each perfect tensor = the
6-leg encoder state of [[5,1,3]]; gluing a leg = exact Bell contraction). Two tiles
glued on one edge → an **[[8,2]]** holographic code (8 boundary, 2 bulk). Sanity:
the contractor reproduces the single-tile threshold $|A|\ge3$.

**Results (reproducible — `python3 network_min.py`):**
- **Entanglement wedges are tile-local:** bulk `AB` reconstructs from any 3 of tile
  A's legs `{A0,A1,A2,A3}`; bulk `BB` from any 3 of tile B's legs `{B1,B2,B3,B4}`.
- **Wedge nesting through the bond:** reconstructing *both* bulk qubits needs only
  $|A|\ge5$ (e.g. 3 legs of A + 2 of B), not 6 — the glued bond carries one side's
  information into the other's wedge. Correct holographic behavior, in F2.

**The structural finding that sharpens the whole line.** The bulk of an $m$-tile
network is an $m$-logical-qubit system, so its contextuality lives in the $m$-qubit
Pauli geometry:
- $m=1$: one context → non-contextual (step 1).
- $m=2$: 2-qubit doily $\mathrm{Sp}(4,2)$ → home of the **Mermin square = family B /
  $H^2$**. So a 2-tile network can *only* probe the $H^2$ bridge.
- $m=3$: 3-qubit $W(5,2)$ → home of the **Mermin pentagram = family A / $H^3$** — the
  framework's distinctive modulus.

⟹ **The minimal object that can test the framework's distinctive $H^3$ bridge is a
THREE-tile network** (3 bulk qubits). The 2-tile case lands in $H^2$/family-B
territory by construction. This precisely locates where holography could meet the
$H^3$ modulus, and is the concrete next step.

## Step 3 — the H³ test, and the resolution (`network3_h3.py`)

Three tiles glued in a chain (A4=B0, B4=C0) → an **[[11,3]]** code whose 3 bulk
qubits are a 3-qubit $W(5,2)$ — the home of the Mermin pentagram = family A / $H^3$,
the framework's distinctive modulus.

**Results (reproducible — `python3 network3_h3.py`):**
1. **Bulk faithfulness = True.** The boundary representatives of the 3 bulk qubits
   satisfy the *exact* 3-qubit Pauli algebra ($\omega(L_{X_u},L_{Z_v})=\delta_{uv}$,
   all else 0). So the bulk genuinely *is* $W(5,2)$ and the framework's $H^3$ /
   pentagram results (Papers X–XXII) apply to it verbatim, encoding-independently.
   The contextuality is really present in the bulk.
2. **Decisive test — minimal reconstruction wedge by tile-support:** constant within
   every support class, and tracking the *chain geometry*:
   | support | min wedge |
   |---|---|
   | {A}, {B}, {C} | 3 |
   | {A,B}, {B,C} (adjacent, shared bond) | 4 |
   | {A,C} (non-adjacent) | 6 |
   | {A,B,C} | 5 |
   Textbook entanglement-wedge nesting — *purely geometric*. An operator's contextual
   role makes **zero** difference to its wedge.

**Verdict (the line resolves).** The bulk carries $H^3$ contextuality, but holographic
reconstruction is **invisible to it**: reconstruction is governed by *support /
geometry* (erasure), contextuality by *signs / products*. Two **independent**
obstructions on the *same* $W(5,2)$ substrate. This is **structural, not
chain-specific**: for any stabilizer code, reconstructability of an operator on a
region is a support property, while contextuality is a sign property — different
functions of the same logical operators. So no network can make them coincide.

**Conclusion for the AdS/CFT line.** The correspondence with the framework is **real
but shape-level**: shared objects (stabilizer = Lagrangian = MASA), and the same
*shape* — boundary-underdetermines-bulk, complementarity, wedge nesting — all rigorous
and computed in framework-native F2. It is **not** an obstruction-measure identity:
AdS/CFT-as-QEC reconstruction = erasure/distance; the framework's $H^3$ = contextuality.
The caution flagged at the outset is now *proven*, not assumed. The line is recorded as
resolved at shape-level; the value delivered is the precise demarcation of what
holography and the framework share and what they don't.

## Files
- `happy_513.py` — the building-block computation (step 1; pure F2, no deps).
- `network_min.py` — the stabilizer-network contractor + the 2-tile [[8,2]] network (step 2).
- `network3_h3.py` — the 3-tile [[11,3]] network + the decisive H³ test (step 3).
