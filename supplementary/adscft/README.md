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

## Files
- `happy_513.py` — the building-block computation (pure F2, no deps).
