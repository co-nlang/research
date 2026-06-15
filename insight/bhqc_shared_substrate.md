# BHQC / finite-geometry of the Pauli group: the framework's shared home

*Status: ✓ shared **substrate** (rigorous, not analogy) — the closest external body of
work to Papers IX–XXII, closer than QEC. **Carries a real citation / novelty action
item** (see §6): a quantitative contextuality measure at n=4,5,6 already exists in this
community, so the framework's originality must be located precisely.*

This is not a "resonance" like the amplituhedron. The black-hole/qubit correspondence
(Duff, Borsten, Lévay) and the finite-geometry-of-the-Pauli-group program
(Saniga, Planat, Holweck, de Boutray, Giorgetti, …) are the **mathematical home** the
framework's substrate already lives in and already cites.

## 1. The shared substrate (every row of the table checks out)

| BHQC / finite-geometry program | Framework (Papers X–XXII) |
|---|---|
| $\mathbb F_2$ | $\mathbb F_2$ |
| $\mathrm{Sp}(2n,\mathbb F_2)$ | $\mathrm{Sp}(2n,\mathbb F_2)$ |
| Lagrangians = stabilizer states | Lagrangians = MASAs / contexts *(same identity)* |
| Fano plane $\mathrm{PG}(2,\mathbb F_2)$ | Paper IX: Fano isotropic embedding |
| Doily $\mathrm{GQ}(2,2)=\mathrm{Sp}(4,2)\cong S_6$ | Paper XIX: rank-4 stratum descent to $S_6$ doily |
| Mermin square in $W(3,2)$ | Paper XXII §7: family B, $K_{3,3}$ |
| Mermin pentagram in $W(5,2)$ (12,096) | Papers X–XXII: the main series |

Rows 4–7 are places the papers **already draw on this lineage** (Paper X cites 12,096
as "the literature value for the $G_2(2)$ orbit"; XIX leans on the $S_6$ doily — Saniga
*wrote the book on the doily*). No positivity wall, no $\mathbb F_2$ gap: same field,
same objects, same key configurations.

## 2. The sobering lit-check finding: "contextuality degree" already lives at n=4,5,6

There is an **active, current** sub-program quantifying contextuality on exactly these
spaces, at exactly the framework's $n$:

- de Boutray–Giorgetti–Holweck–Masson–Saniga, *Contextuality degree of quadrics in
  multi-qubit symplectic polar spaces* (arXiv:2105.13798) — contextuality for quadrics
  at $n=3,4,5$.
- *New and improved bounds on the contextuality degree of multi-qubit configurations*
  (arXiv:2305.10225) — algorithms/C-code, ranks 2–7.
- *A new heuristic approach … four- to six-qubit portrayals* (arXiv:2407.02928) —
  contextuality degree at **n = 4, 5, 6** (e.g. 5-qubit hyperbolic quadric, 6975
  unsatisfied contexts; 6-qubit split Cayley hexagons / $K_{7,7}$).

"Contextuality degree" = the unsatisfiability of the $\pm1$ sign system (number of
contexts that cannot be consistently signed). **This is a sibling order-parameter to the
framework's $N_{\text{anti}}$** — both are scalar contextuality measures on the same
finite geometry. They are not obviously identical ($N_{\text{anti}}$ counts cross-context
*anticommuting Lagrangian pairs*; contextuality degree counts *unsignable contexts*), but
they are close cousins computed on the same objects at the same $n$. **The framework must
cite this lineage and state the $N_{\text{anti}}\leftrightarrow$ contextuality-degree
relationship explicitly** (see §6). The *numerical* face of the framework's program is
not solitary — this community is doing parallel computation.

## 3. Where the framework is genuinely novel: it is the *bridge*

The lit check (incl. a dedicated search) is clean on two points the contextuality-degree
papers do **not** contain:

1. **No cohomological framing.** None of 2105.13798 / 2305.10225 / 2407.02928 uses
   cohomology, the Maslov index, or coboundary/cocycle ($n_a=\delta\mu$). Their measure
   is a *scalar* (a count / a linear-system defect). The framework's distinctive object
   is the **cohomology class** $n_a$ — with $n_a=\delta\mu$ at $n=4$, the rank-parity
   lemma, the Maslov–Wall complex — *not* the scalar. The required Maslov/Wall/signature
   machinery exists, but in **pure topology, disconnected from qubits** (Benson–
   Campagnolo–Ranicki–Rovi, *Signature cocycles on the mapping class group and symplectic
   groups*). **The framework is the bridge between two existing-but-separate bodies:**
   finite-geometry contextuality degree ↔ symplectic signature/Maslov cohomology.

2. **No structural $n$-dependence.** The degree papers are explicitly *computational and
   case-by-case* ("concrete rather than asymptotic"), and report **no special role for
   $n=4$ and no even/odd parity effect**. The framework's XVIII–XXII contribution is to
   turn the $n$-dependence into *theorems*: master rigidity ($N_{\text{anti}}=10
   \Leftrightarrow n=4$), the modulus opening at $n\ge5$, the even/odd carrier dichotomy,
   and the arity-resonance truncation ($H^3$ ceiling). So frame XVIII–XXII as
   *"we prove structurally what their computations make visible numerically."*

So the novel layer is sharply located: **the cohomological obstruction reading + the
structural $n$-scaling theorems.** Everything below it (the symplectic geometry, the
configurations, even a scalar contextuality measure) is shared and must be cited.

## 4. Two distinctions to keep straight

- **vs. Veldkamp space.** The community's dual/cohomology-*adjacent* construction is the
  *Veldkamp space* (the projective space of geometric hyperplanes; "magic three-qubit
  Veldkamp line," Lévay–Saniga–Holweck, arXiv:1704.01598, already tied to black-hole
  entropy). The framework's $H^\bullet$ is **group cohomology of $\mathrm{Sp}(2n,\mathbb
  F_2)$ (Maslov/Wall)** — a *different* object from the Veldkamp (hyperplane) space.
  State this so a reviewer can't collapse "obstruction ladder" into "Veldkamp space."
- **vs. Abramsky sheaf cohomology.** "Contextuality, cohomology and paradox" (Abramsky–
  Mansfield–Barbosa) is *measurement-scenario Čech sheaf* cohomology — the framework
  already cites it as the operational bridge (item 24). That is yet another, *third*
  cohomology, distinct from both Veldkamp and from the framework's group cohomology.

## 5. The genuine asset: BHQC is the third door on item 24

Item 24 (operational meaning of the $H^3$ class) now has three doors:
- **QI door** — QEC / contextuality-as-magic (`quantum_applications.md`);
- **GR door** — cosmology (delegated, `open_problems.md` §A′);
- **string-theory door** — BHQC: the magic Veldkamp line *already* ties Mermin
  pentagrams ($W(5,2)$) to **black-hole entropy / form theories of gravity**
  (1704.01598). If the dictionary extends from the invariants up to the cohomological
  layer, the $H^3$ modulus would acquire a candidate black-hole-entropy meaning.

⚠️ Caveat inherited from BHQC itself: it is widely read as a **coincidence of invariant
theory / shared U-duality (nilpotent-orbit) structure**, not an established dynamical
duality (Borsten–Duff are careful; review arXiv:1206.3166). So this door may *relocate*
"what does $H^3$ mean" to "what does the black-hole/qubit coincidence mean" rather than
resolve it.

## 6. Action items (citation hygiene — XVIII–XXII are already on Zenodo)

1. **Cite the contextuality-degree lineage** (2105.13798, 2305.10225, 2407.02928) wherever
   the papers use $N_{\text{anti}}$ / count contextual constraints, and **state the
   $N_{\text{anti}}\leftrightarrow$ contextuality-degree relationship** (sibling, or
   reducible to one another?).
2. **Cross-check any $n=4,5,6$ numbers** in XVIII/XXI against their published
   computations, so nothing reads as an uncited re-derivation.
3. **Confirm XIX cites Saniga for the doily** it leans on; check Fano-embedding citations
   in IX against Saniga–Planat / Lévay.
4. **Position the cohomology explicitly as group cohomology of $\mathrm{Sp}(2n,2)$**,
   distinct from Veldkamp space (§4) — pre-empt the "this is just Veldkamp" review.

These are about *strengthening* the papers' standing, not retracting anything: the novel
layer (§3) survives the check; it just needs to sit honestly on top of a generously-cited
shared substrate.

---

*See `quantum_applications.md` (same substrate, QI door — the winning line),
`open_problems.md` item 24 + §A′, `amplituhedron_duality.md` (the *other* geometry note,
parked), Papers IX–X (Fano/pentagram, where the lineage is already partly cited),
XVII (anticommutation / $N_{\text{anti}}$ — primary citation-gap site),
XVIII–XXII (the cohomological $n$-scaling layer = the novel contribution),
XV (the $\mathbb C$-lift).*

**Sources (lit check, 2026-06-14):**
[Veldkamp space of two-qubits](https://arxiv.org/abs/0704.0495) ·
[Magic three-qubit Veldkamp line / black-hole entropy (1704.01598)](https://arxiv.org/abs/1704.01598) ·
[Contextuality degree of quadrics (2105.13798)](https://arxiv.org/abs/2105.13798) ·
[Bounds on contextuality degree (2305.10225)](https://arxiv.org/abs/2305.10225) ·
[Four- to six-qubit contextuality degree (2407.02928)](https://arxiv.org/abs/2407.02928) ·
[Black-hole/qubit correspondence review (1206.3166)](https://arxiv.org/abs/1206.3166) ·
[Signature cocycles on symplectic groups (Benson–Campagnolo–Ranicki–Rovi)](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/paper3geq2.pdf)
