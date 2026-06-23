# Item 21, M4 — the intrinsic exotic at K₆ vs the H⁴ fiber (the crux)

> ## ⚠ CORRECTION (2026-06-23, `m4_cochain.py`) — two errors below are superseded
> A collaborator caught that this note's `n=6` conclusion ("Arf is a Dickson polynomial in arity-≤4
> Gram entries ⟹ no `H⁴` escape") is an invalid **value-level → cochain-level leap** — the same leap
> the `n=4` control (`m5_relations.py`, §1 CORRECTION) showed is *not* valid. Investigating it exposed a
> second error:
> 1. **Wrong object/arity.** This note computed `Arf(Q₆)` = Arf of the *whole 6-Lagrangian config* = an
>    **arity-6** invariant (a 5-cochain → `H⁵/K₇`). The item-21 object is the **arity-5** `Arf(Q₅)` of
>    each 5-Lagrangian *face*, assembled over `K₆`'s 6 facets. The "non-constant `{0:39,1:4}` mechanism
>    shift at `n=6`" was an **arity-6 red herring**.
> 2. **The correct arity-5 `Arf(Q₅)` is value-level ~constant 0** (essentially always 0 where defined,
>    `533/534` standalone `K₅` at `n=5` — *consistent with Paper XIX, which is the `n≥5` program*; at
>    `n=4` the intrinsic `Q₅` never exists). The genuine mechanism is **constancy**, not "reducibility."
> 3. **No cochain-level closure for this candidate.** `Arf(Q₅)` is a **partial** function (undefined
>    where `Q₅` doesn't exist — never at `n=4`, ~12% of faces at `n≥5`), so it is **not a total arity-5
>    cochain** and the `H⁴` pairing is ill-posed for it. The direct test `Σ_m Arf(face m)` is mostly 0
>    with sporadic 1's that merely track the rare `Arf=1` faces (odd-count of rare events), **not** a
>    structured `H⁴` class → **no evidence of an escape**, but **also not** a cochain-level exactness
>    proof.
>
> **Corrected M4 status:** the intrinsic-Arf P2 candidate is **value-level absorbed** (`Arf(Q₅)≈0` where
> defined, XIX-consistent) and shows **no `H⁴` escape**, but M4 does **not** establish cochain-level
> exactness (the candidate is partial; the original "reducibility ⟹ exact" argument is retracted). Item
> 21 (M5) is **unchanged — still open**. The body below is kept for the record; read it through this
> correction. See `m4_cochain.py` + the M5 README.

*Result (2026-06-23, `m4_intrinsic.py`): the P2 candidate — the intrinsic Arf invariant at `K₆` —
is **absorbed (reducible to arity ≤4)** at `n≥5`, and **does not exist** at `n=4`. This is **outcome
(a)** of the attack plan's three-way branch: one more evidence point **for** item 21, completing the
P2 lift. It does **not** close item 21 (M5, the general FFT theorem, is untouched). Scope: bounded-
sample on the generic stratum + a structural proof; **not** a nonexistence proof for all exotica.
[SUPERSEDED in part — see the CORRECTION banner above.]*

## What M4 builds (the faithful lift of XIX §`sec:arf` / P2)

At `K₅`, Paper XIX's Arf-exclusion: an intrinsic quadratic refinement `q` (vanishing on the 10 rays)
exists generically, but `Arf(Q|_W)=0` **always** while `N_anti` splits 404/103 — so Arf is **blind**
to the fiber. M4 lifts this to `K₆`:

- 6 Lagrangians in proper position → 15 rays `r_{ij}∈F₂^{2n}`, span `W₆`.
- Restrict to the **generic stratum** `(2n,2n,0)` (M2: `W₆=F₂^{2n}`, `ω|_{W₆}` nondegenerate) so the
  Arf invariant is a clean single bit.
- **Intrinsic exotic `Q₆`** = the unique quadratic refinement of `ω` on `W₆` with `Q₆(r_{ij})=0` for
  all 15 rays and polarization `ω`. Exists ⟺ `o₆|_{R₆}≡0` (M2's consistency condition); when it
  exists it is **unique and `Sp`-invariant**.
- `Arf(Q₆)∈{0,1}` via greedy symplectic-basis extraction.
- **Fiber tested against:** the six sub-`K₅` `H³` classes `c_m=N_anti(face m)`, and the total
  `M=N_anti(all 6)` — all arity-≤4, all vary across configs (`A4=Σc_m≡0` by M1, verified).

## Results

| `n` | proper `K₆` | generic `(2n,2n,0)` | `Q₆` exists | `Arf(Q₆)` | basis-indep. validation |
|----|----|----|----|----|----|
| 4 | 200 | 200 | **0** | — | — |
| 5 | 200 | 188 | 65 | `{0:65}` **constant** | 0/65 mismatches |
| 6 | 160 | 133 | 43 | `{0:39, 1:4}` **VARIES** | 0/43 mismatches |

- **`n=4` → outcome (b):** no intrinsic exotic exists on the generic stratum (existence 0%, matching
  M2). The "exists-but-blind" P2 shape has nothing to act on. *(Irrelevant to item 21, which is `n≥5`;
  `n=4` is settled by the master theorem.)*
- **`n=5` → outcome (a), via the K₅ mechanism:** `Arf(Q₆)≡0` (constant), exactly like XIX's `K₅` — Arf
  is blind to the fiber by being constant. Reducibility corroborated non-vacuously: the rich arity-≤4
  signature has 2 non-singleton buckets, **0 splits**.
- **`n=6` → outcome (a), via a NEW mechanism:** `Arf(Q₆)` is **non-constant** (`{0:39,1:4}`) — the K₅
  "always 0" phenomenon does **not** persist. The basis-independence validation (0/43 mismatches)
  confirms this variation is **real** (intrinsic, `Sp`-invariant), not a basis-choice artifact. So the
  K₅ "killed by being constant" argument **fails** at `n=6`. Arf is nonetheless **reducible** — see
  next section.

## Why `Arf(Q₆)` is reducible even though it varies (the structural proof — the real argument)

The coarse `(c,M)` signature showed 3 split buckets at `n=6` → a `(c)`-flag. The O1 stress-test
(enrich to all 15 four- + 6 five-subset `N_anti`'s) collapsed the splits to 0 — **but** at `n=6` the
rich signature is *injective* on the sample (all buckets singletons), so that statistic is **vacuous**.
The decisive argument is structural, not statistical:

> **Claim.** `Arf(Q₆)` is a polynomial in arity-≤4 invariants (hence reducible).
> 1. Each ray `r_{ij}=ker(S_i−S_j)` is a function of the **2-Lagrangian pair** `{L_i,L_j}`.
> 2. Hence each Gram entry `G₆[(ij),(kl)]=ω(r_{ij},r_{kl})` is a function of **≤4 Lagrangians**
>    `{i,j,k,l}` — an arity-≤4 invariant.
> 3. `Q₆` is determined by `ω` and `Q₆(r_{ij})=0`; in any ray-basis its coefficients are Gram entries
>    (`Q₆(Σx_a b_a)=Σ_{a<b} x_a x_b ω(b_a,b_b)`).
> 4. `Arf` over `F₂` is the **Dickson polynomial** in the form's coefficients.
> ∴ `Arf(Q₆)∈F₂[arity-≤4 invariants]`. ∎

This is **stratum-independent** (on degenerate strata replace `W₆` by `W₆/rad`; the entries are still
arity-≤4); we computed on the generic stratum only for a clean single-bit Arf. The code's `arf(...)`
reads **only** `Om={ω(b_i,b_j)}` and the relation masks — never any genuinely 5-/6-index datum — so the
reducibility is visible in the construction itself.

**Mechanism shift (the genuine discovery):** the intrinsic Arf is absorbed at *both* `n=5` and `n=6`,
but by *different* mechanisms — at `K₅`/`n=5` by being **constant** (value-level), at `K₆`/`n=6` by
being **reducible** (a nonconstant polynomial in arity-≤4 data). The P2 template lifts, but the "killed
by constancy" form is `n=5`-special; the `n≥6` form is "killed by reducibility."

## Scope (carry the discipline)

- M4 absorbs **one** candidate exotic — the intrinsic Arf (the natural P2 object). It is **evidence
  for** item 21 and **completes the P2 lift**, but it is **not** a proof that *no* arity-5 invariant
  escapes. The space of exotic invariants is unparametrized (O3); other (non-Arf) candidates are not
  addressed here. **Closing item 21 is M5.**
- The `n=6` reducibility rests on the **structural proof**, not the (vacuous, injective-sample)
  rich-bucket statistic. The statistic is non-vacuous only at `n=5`.
- Rates (`Q₆`-existence 0/65/43, generic-stratum fractions) are population-dependent; the robust
  content is the **orderings/limits and the constant-vs-varies-but-reducible dichotomy**, not raw %s.

## Status of the P2 prong after M4

- **P1 (frame-`q` not `Sp`-invariant):** DONE-IN-SPIRIT (XIX `Prop frameq`, arity-agnostic). [M3]
- **P2 (intrinsic exotic exists-but-absorbed):** **DONE for the Arf candidate** — outcome (a) at
  `n≥5` (constant at `n=5`, nonconstant-but-reducible at `n=6`), nonexistent at `n=4`. [M4]
- Remaining = M5: the general generation/FFT theorem (no exotic of *any* type), genuinely char-2, no
  reduction shortcut (`co_reduce.py`).

## Files
- `m4_intrinsic.py` — this experiment (build `Q₆`, `Arf`, coarse + rich reducibility tests,
  basis-independence validation).
- `k6_skeleton.py` / `M2_skeleton_README.md` — M2 (the `(2n,2n,0)` stratum + `Q₆`-existence rates).
- XIX `sec:arf` (`lem:skeleton`, `intrinsicq`, `noq_odd`) — the `K₅` template lifted here.
