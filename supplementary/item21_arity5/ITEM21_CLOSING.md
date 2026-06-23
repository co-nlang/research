# Item 21 — closing note: the reduction, assembled

*Capstone (2026-06-23). This assembles the session's pieces into one statement of where item 21 stands.
It is a **reduction**, not a finished proof: item 21 (`n≥5`, no exotic arity-5/`H⁴` obstruction) is reduced
to a short list of named inputs, most **verified**, the rest **classical** or **ours-established**, with
two honest residuals flagged. Modeled on item 23's `closing_note.md`. **Firewall tags:** `[VERIFIED]`
(computed this session), `[CLASSICAL]` (cited theorem), `[OURS]` (established in the paper series),
`[CONDITION]` (a stated hypothesis doing work), `[GAP]`.*

## The statement

> **Target (item 21, `n≥5`).** No *exotic* (indecomposable, non-`ω`-cup-power) arity-5 invariant of
> Lagrangian 5-tuples in proper position furnishes a nonzero `H⁴` obstruction at `K₆`. Equivalently, `H³`
> is the hard ceiling of the family-A tower (`μ → n_a`); there is no arity-5 rung.

## The reduction — six steps

**Step 0 — the data splits `[VERIFIED]`** (`kerG_reduction.py`, completeness lemma). Every arity-5
invariant is a function of `(G, R)` — the `ω`-Gram of the 15 rays and their relation code `R`. Always
`R ⊆ ker(G)`, with `ker(G)/R ≅ rad(ω|_W)`; the only datum beyond `G` is `rad(ω|_W)` = **Paper XIX's
modulus** (present only on degenerate strata, `n≥5`; `n=4` is 100% nondegenerate, so no modulus — matching
`n=4` settled). So the data is **(I) the `ω`-Gram + (II) the radical/modulus `R`**.

**Step A — genuine ⟹ phase-derived `[VERIFIED n=4,5,6]`** (`phase_blind.py`). A genuine contextuality
obstruction is a property of the *operator phases* (`ω/q`), not of incidence combinatorics. Concretely:
the relation-code invariants (e.g. the weight enumerator `A_w` that "climbs" in `modulus_climb.py`) are
`GL(2n,F₂)`-invariant — they never reference `ω`. Verified: random `g ∈ GL\Sp` on a proper `K₆`'s 15 rays
leaves `R`/`A_w` *exactly* fixed (0/720, 0/720, 0/480) while flipping `N_anti` ~50%. A phase-blind
invariant cannot witness a phase phenomenon ⟹ the part-II (`R`-only) data is **not** a genuine
obstruction. *(This grounds the `[REFRAME]` "genuine = operator-phase class" as principled, not fiat.)*

**Step B — genuine ⟹ natural ⟹ pure-`ω`-Gram `[VERIFIED structural + CONDITION]`.** A genuine obstruction
is a **natural** (functorial) nerve cochain — built from the *fixed* `K₆` combinatorics, not from
config-dependent data. The bottom rung confirms the shape: `(n_a)_m =` the polarization defect
`Σ_{i<j} ω(v_i,v_j)` over the *fixed* disjoint pairs of tetrahedron `m` (item 23 link A, proven all `n`,
`123000/123000`) — a fixed linear combination of `ω`-Gram entries, hence **pure-Gram by construction**.
`[CONDITION]` *Naturality*: the loophole "sum `ω` over pairs *selected by `R`*" is a config-dependent
(non-natural) selection — excluded because cohomology classes are functorial (and pure-`R` is separately
phase-blind, Step A). Structurally confirmed: for a fixed `G`, `ker(G)` is fixed but `R` varies
(`ker(G)/R = rad`, `kerG_reduction.py`) — yet `n_a`, a function of `G`, is constant. So `R` is independent
extra data that genuine natural obstructions do **not** use.

**Step C — pure-Gram genuine ⟹ ambient `O`-class evaluation `[VERIFIED + CLASSICAL]`** (`witt_fft.py`).
- **Polarization** (`[VERIFIED n=2,3,4]`, all-`n` mechanism): `q(Σ_{i∈S}v_i) = Σ q(v_i) ⊕ Σ_{i<j}ω(v_i,v_j)`,
  so the Gram `{q(v_i),ω(v_i,v_j)}` determines `q` on the whole span — phase data **is** the Gram.
- **Witt FFT** (`[CLASSICAL]`; `[VERIFIED n=2]`, `|O(q)|=72`, orbit ⟺ (Gram, relations), 0 splits): the
  Gram (+ relations) is a *complete* `O`-invariant of the ray tuple. With Steps A–B (relations are
  phase-blind/non-natural), the genuine `O`-invariants are exactly functions of the `ω/q`-Gram = the
  **nerve-evaluations of ambient `H*(BV)^O` classes** (`V=(ℤ/2)^{2n}`, `O=O(q)`).

**Step D — the degree-4 ambient `O`-ring is decomposable `[VERIFIED n=3,4,5 + OURS]`.**
- `[OURS, now reduced to naturality]` Resonance / degree-matching: an arity-5 obstruction is a degree-4
  cochain on `K₆ ≅ S⁴`, so the nerve-evaluation of a **degree-4** ambient class. *This degree-matching is
  not an independent input — it follows from Step B's naturality by **representability** (Yoneda): a
  natural, `O`-invariant, pointwise-cohomological degree-`k` assignment is represented by an element of
  `H^k(BV)^O`, degree-matched automatically.* (Confirmed at the bottom: `μ`↔`ω` deg 2, `n_a`↔`Sq¹q` deg 3.)
  Representability also **excludes the over-counters a second, independent way** (`gl_invariants.py`): the
  climbing `A_w` is `GL`-invariant, so a natural ambient version would live in `H*(BV)^{GL}` = the Dickson
  algebra, which is `0` below degree `2^{2n-1}` — `[VERIFIED n=2,3]` `H⁴(BV)^{GL}=0`. So `A_w` (nonzero as
  a config function) is **not** a natural ambient class: it is *relational* (`R`), not
  pointwise-cohomological. (Complements `phase_blind`'s `GL`-invariance exclusion.)
- `[VERIFIED]` `dim H⁴(BV)^O = 1`, spanned by `q²` (`sp_invariants.py`, `bridge_tower.py`); the orthogonal
  generators sit at degrees `{2,3,5,9,…}={2}∪{1+2^i}` — **skipping degree 4**; and these generators *are*
  the Kudo transgression tower (`q, Sq¹q, Sq²Sq¹q`, verified indecomposable through deg 5).
- `q² = Sq²q` is **decomposable** (a cup-square = family B; item 22: family B has no independent
  resonance) — it is `μ²`, not a new rung.

**Conclusion.** A genuine (Steps A–B) arity-5 obstruction is the nerve-evaluation of a degree-4 ambient
`O`-class (Step C + resonance), i.e. an element of `H⁴(BV)^O = ⟨q²⟩` (Step D) — necessarily `μ²`,
**decomposable, not exotic**. Hence no exotic arity-5/`H⁴` obstruction, all `n≥5`. ∎ *(modulo the
residuals below).*

## What this does NOT need: Kudo

The proof of item 23 (`n_a = ⟨Sq¹ω,[K₅]⟩`) rested on the **Kudo transgression** — the *realization*
that a specific ambient class is a *nonzero* obstruction ("no finite reduction in hand"). **Item 21's
negative direction does not use it.** The bridge splits:
- **(b-pos), realization** — *which* ambient classes are realized nonzero = item 23, needs Kudo, gives
  *existence*.
- **(b-neg), classification** — genuine ⊆ ambient `O`-ring, degree-4 part decomposable = item 21, needs
  only **Witt + polarization + resonance + the verified `H⁴^O` computation**.
The negative direction needs only the *containment* and the *target ring's decomposability*; it never
needs the exact transgression *values*. This drops item 21's dependency from "cited Kudo realization" to
"Witt's theorem + polarization + resonance bookkeeping + verified finite facts."

## Honest ledger

| step | claim | status |
|---|---|---|
| 0 | data = `(G, R)`, extra datum = `rad` = XIX modulus | **`[VERIFIED]`** `kerG_reduction.py` (1100/1100) |
| A | genuine ⟹ phase-derived (over-counters are `GL`-invariant) | **`[VERIFIED n=4,5,6]`** `phase_blind.py` |
| B | genuine natural cochain ⟹ pure-`ω`-Gram | **`[VERIFIED structural]`** (`n_a` = fixed Gram-combo, item 23 A; `R` independent, kerG) + **`[CONDITION]`** naturality |
| C | pure-Gram genuine ⟹ ambient `O`-class eval | **`[VERIFIED n=2,3,4 + CLASSICAL]`** `witt_fft.py` (polarization + Witt) |
| D | `H⁴(BV)^O = ⟨q²⟩`, decomposable (family B) | **`[VERIFIED n=3,4,5]`** `sp_invariants.py`,`bridge_tower.py` + item 22 |
| D′ | degree-matching = representability (Yoneda), not an independent input | **`[VERIFIED n=2,3]`** `gl_invariants.py`: `H⁴(BV)^{GL}=0` ⟹ over-counters not natural ambient classes |
| — | (b-pos) realization (which classes nonzero) | **`[CLASSICAL, Kudo]`** — needed for item 23, **not** item 21 |

## The honest residual — now a SINGLE condition

The two residuals previously flagged (naturality; resonance arity↔ambient-degree) **collapse into one**.
The resonance/degree-matching step (D) is **not independent**: by **representability of natural operations**
(Yoneda), a natural `O`-invariant *pointwise-cohomological* degree-`k` assignment is an element of
`H^k(BV)^O` — so the degree-matching *follows from* the naturality condition (Step B). What remains is the
single:

> **`[CONDITION]` Genuine obstruction = natural, pointwise-cohomological nerve cochain.** This (with the
> `[REFRAME]`, grounded by Step A) delimits the objects item 21 quantifies over. It is standard
> (cohomology is functorial; representable) and confirmed at the bottom (`n_a` = the pointwise `q`-defect,
> item 23 link A) — but it is a *condition*, not a theorem.

The condition is grounded **two independent ways**, and both *also* exclude the over-counters: (i) **Step A
phase_blind** — genuine obstructions are `Sp`/`O`-but-not-`GL` (phase-dependent), the over-counters are
`GL`-invariant (phase-blind); (ii) **representability** (`gl_invariants.py`, `H⁴(BV)^{GL}=0` at `n=2,3`) —
the over-counters are *relational* (`R`), not pointwise-cohomological, so not natural ambient classes.
A genuine contextuality obstruction *is* the pointwise operator-phase `q`-defect, which is exactly
pointwise-cohomological — so the condition is well-motivated, not ad hoc.

### The condition, grounded operationally: contextuality = fixed-context gluing

The condition can be reduced further — to the *operational definition of a contextuality scenario* — via
the value-assignment (Kochen–Specker / All-vs-Nothing, Abramsky–Brandenburger) picture. A non-contextual
assignment is a map `λ: rays → F₂` consistent across contexts. Three facts pin it down:

1. **Contextuality is always cross-context.** *Within* a single context (a commuting Lagrangian) the
   operators share eigenstates, so a consistent `λ` always exists locally. Hence every obstruction is a
   *gluing* obstruction across contexts = **nerve cohomology** — built from the **fixed** context
   structure of the scenario. This is exactly *naturality*: the contexts are fixed scenario data, not
   config-dependent, so the obstruction is a natural nerve cochain.
2. **The accidental relations `R` carry no contextuality.** The within-span constraint system
   `{λ·a = q-defect(a) : a ∈ R}` is **always solvable** — by `λ = Q` (the `q`-charge vector
   `Q_i = q(v_i)`) — because `q-defect(a) = Σ_{i∈a} q(v_i) = Q·a` is *linear* on `R` (polarization, since
   `Σ_{i∈a}v_i = 0`). So the config-dependent `R` (the `n≥5` modulus) is **not** an obstruction source —
   the operational confirmation of `phase_blind` (and of why the modulus is an *order parameter*, not a
   witness).
3. **The signs are `q`-defects.** The cross-context gluing carries the signs `q-defect` = pointwise `q`
   evaluated on ray-sums (polarization) — so the obstruction is **pointwise-`q`** = representable. This is
   `n_a` = item 23 link (A).

So the naturality/representability `[CONDITION]` is not a free mathematical assumption: it is the statement
that **the framework's obstruction is the standard contextuality obstruction** (cross-context gluing of
value assignments, fixed contexts, `q`-defect signs). `[GAP, honest]` This is a *modeling identification*,
well-supported but not proven in general here — proving "the framework's obstruction = the AvN nerve-
cohomology obstruction" at all arities **is** the paper-scale piece (the nerve↔`H*(BH)` realization seen
from the contextuality side, = (b-pos)). The reduction lowers the residual's status from "an assumed
mathematical condition" to "the definition of the contextuality scenario the framework models."

This residual is **not** the old "unparametrized exotic search" (O3) — it is one named, well-motivated
condition. **Net: item 21 is reduced from an open modular-invariant-theory non-existence problem to
"Witt + polarization + four verified computations, modulo the single naturality/representability
condition,"** with Kudo confined to the (b-pos) existence side.

## What is NOT claimed
- Item 21 is **not** declared proven: the single naturality/representability `[CONDITION]` is an input,
  not an output, and the Witt FFT is verified only at `n=2` in-setting (classical for all `n`).
- We do not re-derive Quillen/Kudo, nor construct the general nerve↔`H*(BH)` realization (= (b-pos),
  item 23-general). That remains the paper-scale program — but it is **off item 21's critical path**.

## Files
- `kerG_reduction.py`/`M5_kerG_reduction_README.md` (Step 0) · `phase_blind.py` (Step A) ·
  `witt_fft.py` (Step C) · `sp_invariants.py`/`LEMMA_A_README.md`, `bridge_tower.py` (Step D) ·
  `gl_invariants.py` (Step D′: representability — `H⁴(BV)^{GL}=0`, resonance follows from naturality) ·
  `DBRIDGE.md` (the bridge + the (b-pos)/(b-neg) split) · `ITEM21_PROOF_SKELETON.md` (the long form).
- item 23: `../item23_search/closing_note.md` (the degree-3 realization = (b-pos) instance).
