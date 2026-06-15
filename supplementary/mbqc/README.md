# item 24 / the degree conjecture, tested in l2-MBQC — and refuted

Companion to `research/insight/quantum_applications.md` §6. Tests the conjecture
**cohomological degree = computational degree**: that the $H^3$ pentagram modulus powers
a degree-3 Boolean primitive no $H^2$ / $\le4$-context resource can compute.

The right setting (qubit contextuality *is* a resource there): **l2-MBQC** — a resource
state, per-qubit X/Y measurements, and *linear* (mod-2) classical control
(Anders–Browne; Raussendorf). The function computed is the resource's deterministic
**sign function** $\sigma$, composed with linear control; its algebraic degree is the
computational degree.

## Part 1 — `mbqc_degree.py` (bulletproof, explicit matrices)

For a stabilizer state, $\sigma(m)$ = the $\pm1$ eigenvalue under the X/Y-setting Pauli
$P(m)$, computed by direct linear algebra (no Pauli-phase bookkeeping to get wrong).

- **Anchor:** GHZ$_3$ reproduces the Anders–Browne degree-2 gate (its $\sigma$ is OR/NAND).
- **Ceiling:** GHZ$_{3,4,5}$ and **1200 random stabilizer states** (Clifford on $|0\rangle$)
  *never* exceed $\sigma$-degree **2**. (Theory: a stabilizer sign function is
  linear-in-generators + a quadratic Pauli-reordering phase $\Rightarrow$ degree $\le2$.)

$\Rightarrow$ **Non-adaptive l2-MBQC on any stabilizer resource caps at degree 2** — the
pentagram ($H^3$) included. No non-adaptive separation from the square ($H^2$).

## Part 2 — `mbqc_adaptive.py` (does degree-3 need the pentagram?)

In l2-MBQC the control is linear (it may route a measured bit forward); the nonlinearity
lives in each quantum gate. So one may compose Anders–Browne (GHZ = $H^2$) gates.

- one GHZ gate → degree 2; **two GHZ gates → degree 3**; three → degree 4.

$\Rightarrow$ **Degree 3 (and any degree) is reached from $H^2$ (GHZ) resources alone.**
The $H^3$ pentagram is not needed. (Expected: a single $H^2$ resource already makes
l2-MBQC universal — parity control + one AND = all Boolean functions — so there is no room
above it for $H^3$ to add power.)

## Verdict

**The conjecture is REFUTED in l2-MBQC.** Computational function-degree is governed by
**adaptive depth** (composition), not by the cohomological rung of the resource:
- non-adaptively, every stabilizer resource (square *or* pentagram) = degree 2;
- adaptively, $H^2$ alone already reaches every degree.

The $H^3$ pentagram gives **no computational-degree separation** over the $H^2$ square.

## The pattern this completes (the real finding)

This is the **third** independent operational axis on which the framework's $H^3$
contextuality turns out to be **orthogonal** to the operational quantity:

| axis | what governs it | role of $H^3$ contextuality |
|---|---|---|
| circuit hardness / magic | non-stabilizer magic states (Gottesman–Knill) | none (qubit stabilizer = simulable) |
| holographic reconstruction (AdS/CFT) | support / erasure (entanglement wedge) | none (orthogonal; `adscft/`) |
| MBQC computational degree | adaptive depth (composition) | none (this) |

In all three, the $H^3$ class is **real and present** in the substrate, but it is **not
the carrier** of the operational resource. The deeper reading: **item 24 was mistyped** —
it asked an operational question of a structural quantity. The precise reason is *not*
"cohomology is non-operational" ($H^2$ / the Mermin square **is** operational, Anders–
Browne) — it is **saturation**: operational axes resolve only the *threshold* (contextual
at all? $\approx H^2$) and max out there; **none grades by cohomological degree**. So $H^3$
is a structural refinement *finer than operational resolution* (which is exactly why this
test saturated at degree 2). $H^3$'s meaning is therefore **structural / classifying** — a
coordinate + a certification depth (modulus: needs five contexts to witness) — the
project's "framework = coordinates, cartographer not competitor," now precise. See
`quantum_applications.md` §7.

## Files
- `mbqc_degree.py` — non-adaptive sign-function degree (anchor + ceiling). Needs numpy.
- `mbqc_adaptive.py` — adaptive composition reaches degree 3 from $H^2$ alone. Pure Python.
