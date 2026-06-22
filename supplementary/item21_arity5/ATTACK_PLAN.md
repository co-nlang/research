# Item 21 (b) — The Arity-5 Exotic Escape: Attack Plan / Handover

*Status: open, XXIII-level. Research-program handover. Scaffold M1–M4 now done (M4 = the intrinsic-Arf
P2 candidate, absorbed — outcome (a), 2026-06-23); the one genuine remaining front is **M5**, the
uniform no-exotic generation theorem. This doc localizes it, the template, the obstacles, and the
milestones.*

## 0. Orientation (one paragraph)

Item 21 asks: is `H³` a **hard** ceiling for Pauli contextuality, i.e. is there *no* irreducible
arity-5 invariant of five Lagrangians that could furnish an `H⁴` obstruction at `K₆`? Item 23's
closure (mod Kudo) caps the **Steenrod-generated** ascent (`Sq¹ω` unique, `Sq¹Sq¹ω=0`, `Sq²ω=ω²`
decomposable), and the arity-4 base case is **absorbed**: the natural `ω`-Maslov bit `q₄` is saturated
and Paper XIX rules out the exotic **Arf** invariant as an `H³` classifier. The probe `qk_saturation.py`
shows the natural arity-5 `q₅` also saturates (`q₅≥q₄`, validated). So the **lone hard core** is: does
a *genuinely-exotic* (non-`ω`, Arf/Dickson-type) **arity-5** invariant exist and escape to `H⁴`? The
natural such candidate — the intrinsic Arf at `K₆` — has now been **tested and absorbed (M4, outcome
(a), 2026-06-23):** it is reducible to arity-≤4 at `n≥5` and nonexistent at `n=4`, no `H⁴` escape (the
program was built to distinguish support/re-plan/falsify, and what occurred was *support*). What
remains (M5) is the *uniform* theorem: no exotic of **any** type escapes — M4 closes one candidate,
not the unparametrized space (O3).

## 0.5 Terminology (precise — do not leave these vague; this is a handover)

- **`q_k` instance** — the bit `q_k(a₁,…,a_{k-1} | a_k)` for *one* ordered choice (one distinguished
  Lagrangian, `k−1` free). A proper `K₅` has `5·4=20` `q₄`-instances and `5` `q₅`-instances (using all
  five); a `K₆` has more.
- **`q_k` saturated on a config** := *every* instance of that config equals `1` (`n_{q_k}` at its
  maximum), i.e. `Q_k ≢ 0` on `D_k` for every choice.
- **`q_k` saturated (population claim)** := the saturated-config fraction is `≈1` (and per-instance
  `≈1`). **A saturated invariant is `≈`constant, hence carries `≈0` bits about any fiber** — it cannot
  classify `N_anti` or an `H`-fiber. This is the precise meaning of "carries no information."
  *Caveat:* the absolute fraction is **population/metric-dependent** (raw-config vs deduplicated-bucket
  differ `65%→99%`, `calib_q4.py`); compare to XIX on the *deduplicated-bucket* metric, and otherwise
  quote *orderings* (`q₅≥q₄`) and *`n=6` limits*, never a single raw %.
- **Absorbed** (the route's word) is *stronger* than saturated and comes in three forms, any one of
  which means "contributes no new family-A generator": **(value-level)** constant = saturated;
  **(cochain-level)** `δ` of a lower-arity cochain = *exact* (this is what M1 tests); **(classifier-
  level)** excluded as a fiber classifier by P1/P2. Item 21 needs *cochain-level* absorption (exactness)
  of *every* arity-5 invariant, including the exotic ones — saturation of the natural `q_k` is only the
  value-level form for the `ω`-built invariant.

## 1. The target (precise)

> **Conjecture (item 21).** For all `n≥5`, every `Sp(2n,F₂)`-invariant `F₂`-valued function of five
> Lagrangians in proper position is *reducible* — a polynomial in invariants of arity `≤4`. Hence the
> arity-5 (4-cochain) datum on the `K₆` nerve is exact (`c=δa`), no new `H⁴` class arises, and `H³`
> is the ceiling.

Equivalent operational form (the one to attack computationally first): **no exotic arity-5 invariant
classifies a putative `H⁴` fiber at `K₆`** — the direct analog of XIX's "no Arf of the ray-span
classifies `N_anti`" at `K₅`/`H³`.

## 2. What is already done (the reduction — do not redo)

- **Steenrod-generated front: closed** (item 23). The only indecomposable Steenrod ascent from `ω` is
  `Sq¹ω` (`H³`); `Sq¹Sq¹ω=0`; `Sq²ω=ω²` is decomposable; `Sq^iω=0`, `i>2`. So no *Steenrod* `H⁴`
  escape. (mod the cited Kudo transgression — see `item23_search/closing_note.md`.)
- **Arity-4 absorbed** (Paper XIX). `q₄` (the `ω`-Maslov quadruple bit, Def. `def:q4`) is **saturated**
  (`≈99%` of deduplicated buckets; raw-config `65–87%`). The exotic **Arf invariant** of the ray-span
  is **ruled out** as an `H³`/`N_anti` classifier (§`sec:arf`).
- **Natural arity-5 cochain truncates: PROVEN** (Paper XXII, Theorem `thm:trunc`). The degree-4
  cochain `c_m=N_anti(face m)` equals `δa` (coboundary of the anticommutation 3-cochain), so
  `⟨c,[K₆]⟩=0`, `[c]=0∈H⁴`. Proof = the **4-index *cochain-indexing* argument** (`ω(v_ij,v_kl)` is
  indexed by the 4-subset `{i,j,k,l}` ⟹ `a` is a 3-cochain ⟹ `c=δa` on `∂Δ^N` by the simplicial
  coboundary formula, exact since `[S^{N-2}]` is a cycle) — **purely cochain-level, stratum-agnostic**
  (does *not* assume K₅ geometry; M2's `(2n,2n,0)≠(8,6,2)` is irrelevant to it). Verified
  `k6_truncation.py` (`Σc_m≡0`, n=4,5,6;
  `c_m` realize all 32 even-weight patterns — sub-classes live, top class dead). *This is M1 — already
  a theorem, not an open task.*
- **Arity-5 `ω`-Maslov half: matching value-level evidence.** `q₅` saturates `≥ q₄` on identical
  configs (`qk_saturation.py`; machinery validated `64000/64000` against XIX's exhaustive `q4_bit`,
  `calib_q4.py`) — the value-level shadow of the same truncation.
- **Remaining = the exotic non-`ω` (non-4-index-decomposable) arity-5 invariant.** This is (b)/M4 —
  precisely what the partition argument does *not* reach.

## 3. The template to extend — XIX's arity-4 Arf-exclusion (§`sec:arf`)

Two independent prongs, both must be lifted to arity 5:

**(P1) Frame-`q` is not `Sp`-invariant** (Prop. `frameq`). The Pauli refinement `q(p,x)=p·x`
satisfies `q(v+w)=q(v)+q(w)+ω(v,w)` but a transvection `T_u` changes `q` by `ω(v,u)q(u)` while fixing
`N_anti`. So any frame-`q`-built (coordinate) Arf cannot classify an `Sp`-invariant. *Lifts verbatim*
to arity 5 — frame-`q` is dimension-agnostic.

**(P2) Intrinsic-`q` exists generically but does not classify** (Lemma `lem:skeleton`, Props
`intrinsicq`/`noq_odd`). For the `(8,6,2)`-stratum at `K₅`: rays `r₁..r₁₀`, Gram `G=MΩMᵀ`, relation
space `R={a:Σaᵢrᵢ=0}` (`dim 2`), `o(a)=Σ_{i<j}aᵢaⱼG_{ij}` (quadratic, polarization `G`), `ℓ=o|_{ker G}`
(linear, by (iii)). Then **(iv)** an intrinsic-`q` (a quadratic refinement vanishing on all rays)
exists `⟺ ℓ|_R≡0`; **(v)** `N_anti=o(1)`. Punchline: even where intrinsic-`q` exists, **Arf(Q|_W)=0
always yet `N_anti` parity splits 404/103** — the Arf invariant is blind to the fiber.

The *form* of the argument to replicate: build the linear-algebra skeleton at the next level, show the
candidate exotic invariant is either (a) not `Sp`-invariant (P1-type), or (b) `Sp`-invariant but
constant/exact on the fiber it would need to separate (P2-type).

## 4. The arity-5 structure (where (b) lives)

Resonance bookkeeping: arity-`a` datum = `(a-1)`-cochain, resonates at `K_{a+1}/H^{a-1}`. So:
- `μ` (arity-3) = 2-cochain → `K₄/H²`; `n_a` (arity-4) = 3-cochain → `K₅/H³`;
- **arity-5 = 4-cochain → `K₆/H⁴`.** The nerve is `∂Δ⁵ = S⁴` (6 Lagrangian vertices, 15 rays
  `r_{ij}`); an arity-5 invariant is a function of a 5-subset of vertices; its `H⁴` obstruction is
  `⟨c,[K₆]⟩` summed over the 6 facets (5-subsets).

So the (b)-level objects are: **6 Lagrangians in proper position, 15 rays, ray-span `W₆`, Gram `G₆`
(15×15), relation space `R₆`**. The stratum analog of `(8,6,2)` must be identified empirically first
(what is the generic `(dim W₆, rank G₆, dim rad W₆)` at `K₆`, `n≥5`?).

## 5. The program — concrete sub-tasks (in dependency order)

1. **`c₅` exactness — ALREADY DONE (Paper XXII, Theorem `thm:trunc`).** *Correction (2026-06-22):
   this milestone was mislabelled "open, do first" — it is a proven theorem in Paper XXII, not a task.*
   The natural arity-5 4-cochain is `c_m = N_anti(face m)`; Paper XXII proves `c = δa` (coboundary of
   the anticommutation 3-cochain `a`), so `⟨c,[K₆]⟩ = 0` and `[c]=0 ∈ H⁴(S⁴)`. **Proof mechanism —
   purely simplicial/cochain-level, NOT a K₅ geometric fact (read carefully, this matters for M4):**
   the anticommutation datum `ω(v_ij,v_kl)` is *indexed by* the 4-subset `{i,j,k,l}`, so `a` is a
   **3-cochain on `∂Δ^N` for any `N`**; on `∂Δ⁵=S⁴` its degree-4 assembly is the coboundary `δa` by the
   standard simplicial formula, and `⟨c,[S⁴]⟩=⟨a,∂[S⁴]⟩=0` because the fundamental class is a *cycle*.
   This argument is **independent of the ray-span geometry** — in particular **M2's discovery that
   `K₆`'s generic stratum `(2n,2n,0)` differs from `K₅`'s `(8,6,2)` does NOT bear on M1**: the "4-index
   partition / `Σ_{T⊂face m} a_T`" is *cochain indexing* (which 4-subset `T` an `a`-value sits on), not a
   statement about `dim W`/`rank G`. (So the K₅ geometric picture is *not* being assumed to carry over;
   the coboundary identity is stratum-agnostic.) Verified `k6_truncation.py`: `Σ_m c_m ≡ 0` (200/200 at
   n=4,5,6), `c_m` realizing all 32 even-weight patterns. Our `q₅`-saturation probe is the *value-level*
   shadow. **What M1 covers and the sharp boundary it draws:** the argument works *because and only
   because* the datum is **4-index-indexed** (a 3-cochain). So M1 closes **every 4-index-decomposable
   (= `ω`-generated) arity-5 cochain** — and pinpoints M4's opening: a **genuinely-exotic arity-5
   invariant that is NOT 4-index-decomposable** would not be a coboundary of a 3-cochain and could be a
   true 4-cochain (non-exact). M4 = exactly that non-decomposable remainder. *(Milestone M1: DONE by
   Paper XXII; cochain-level, stratum-agnostic; it isolates, but does not touch, M4.)*
2. **Build the `K₆` skeleton lemma** (extend `lem:skeleton`): the 15-ray Gram `G₆`, relation space
   `R₆`, quadratic `o₆`, linear `ℓ₆=o₆|_{ker G₆}`. Identify the generic stratum. **DONE
   (2026-06-22, `k6_skeleton.py`, `M2_skeleton_README.md`).** Key findings: (i) the generic stratum is
   **`(2n,2n,0)` — full-span, NONDEGENERATE** (rays span all of `F₂^{2n}`, `rad W₆=0`), structurally
   *different* from XIX's degenerate `K₅` `(8,6,2)`; (ii) all structural facts (`R₆⊆ker G₆`, `o₆|_{ker
   G₆}` linear, `ker G₆/R₆≅rad W₆`, coisotropy) verified 100%; at the generic stratum `ker G₆=R₆`;
   (iii) **M4 hand-off:** intrinsic-`q` existence (`o₆|_{R₆}≡0`) is **0% at n=4** (branch (b) is real —
   P2 won't lift verbatim), 40% (n=5), 31% (n=6).
3. **Frame-`q` exclusion at arity 5 (P1) — DONE-IN-SPIRIT (Paper XIX `Prop frameq`).** *Correction
   (2026-06-22): also not open.* XIX's proof uses *only* that a transvection fixes the Gram (hence
   `N_anti` and every `ω`-invariant) while shifting `q` by `ω(v,u)q(u)` — it is **arity/dimension-
   agnostic**, so it lifts verbatim to 15 rays / arity 5 (the ray count never enters the argument). No
   new content; coordinate Arf-type arity-5 invariants are excluded by the same proposition.
   *(Milestone M3: DONE-IN-SPIRIT — cite XIX `Prop frameq`, do not re-derive.)*
4. **Intrinsic exotic at arity 5 (P2) — the crux. DONE for the Arf candidate (2026-06-23,
   `m4_intrinsic.py`, `M4_intrinsic_README.md`): OUTCOME (a).** Built the `K₆` intrinsic exotic `Q₆`
   (the unique quadratic refinement of `ω` on `W₆` vanishing on the 15 rays) and its Arf invariant, and
   tested correlation with the `H⁴`-fiber (`c_m=N_anti(face m)`, `M=N_anti(all 6)`). The computation was
   designed to distinguish all three outcomes; what actually occurred:
   - **(b) at `n=4`:** `Q₆` does **not exist** on the generic stratum (existence 0%, matching M2) — no
     intrinsic exotic to act on. *(Irrelevant to item 21, which is `n≥5`.)*
   - **(a) at `n=5`, K₅-mechanism:** `Arf(Q₆)≡0` **constant** — blind, exactly the XIX `K₅` pattern.
     Reducibility corroborated non-vacuously (rich arity-≤4 signature, 2 non-singleton buckets, 0
     splits).
   - **(a) at `n=6`, NEW mechanism:** `Arf(Q₆)` is **non-constant** (`{0:39,1:4}`; validated
     basis-independent, 0/43 mismatches — the variation is *real*, not artifact). The K₅ "killed by
     constancy" argument *fails*, but Arf is **still reducible** by a **structural proof**: every Gram
     entry `ω(r_{ij},r_{kl})` is arity-≤4 (the ray `r_{ij}` depends on the pair `{i,j}`), and `Arf` is
     the Dickson polynomial in those entries ⟹ `Arf(Q₆)∈F₂[arity-≤4 invariants]`. (The coarse `(c,M)`
     gave a `(c)`-flag; the O1 stress-test collapsed it, but the rich signature is *injective* at `n=6`
     so that statistic is vacuous — the **structural proof** carries it, not the bucket count.)

   **Net:** the intrinsic-Arf (natural P2) candidate is **absorbed at all `n≥5`** — *one more evidence
   point for item 21, and the P2 lift is complete*. The genuine discovery is the **mechanism shift**:
   absorption is by *constancy* at `n=5` (value-level) but by *reducibility* at `n=6` (polynomial in
   arity-≤4). **Crucially this does NOT close item 21:** M4 absorbs *one* candidate, not *all* exotica
   (O3 — the exotic space is unparametrized). The `(c)`-falsification branch did **not** occur for the
   Arf candidate.

   *(Milestone M4 — DONE for the Arf/P2 candidate: outcome (a), no `H⁴` escape from this object. Other
   non-Arf candidates and the general theorem remain → M5.)*
5. **Reducibility / FFT-style generation theorem (the real theorem) — RECAST via prior art
   (`LITERATURE.md`).** This subfield is *already developed over `ℝ,ℂ`*: **Conley–Ovsienko**
   (`1812.04271`) give a generation theorem for `Sp(2n,K)`-invariants of Lagrangian configurations
   (continuous **cross-ratios** + discrete **signs**, with explicit Pfaffian relations), and **MWZ**
   (`math/9807061`) give the finite-type boundary (`≤3` Lagrangians finite, `≥4` infinite type). So M5
   is **not** "invent invariant theory from scratch" — there is a known `ℝ,ℂ` template (C-O). **BUT
   the reduction was attempted (`co_reduce.py`) and does NOT shortcut M5** (corrects an earlier
   optimistic framing): the cross-ratio relation reduces to a tautology (`3≡1`, vacuous); the Pfaffian
   reduces to a coarse *stratum indicator* (`[rank G=10]`), not the obstruction; only C-O's discrete
   *sign* invariant reduces to the Maslov bit `μ` (the bottom rung). The `H³`/exotic content is
   **orthogonal to C-O's invariants, not a reduction of them.** *(Milestone M5 — the full item 21;
   char-2-specific. C-O gives the template + the `μ`-dictionary but NOT the obstruction; M5 still needs
   the genuinely char-2 route via M4. The reduction shortcut is ruled out.)*

## 6. The genuine obstacles (from item 21 §"Why it is genuinely hard", L449)

- **(O1) "Built from `ω`" does not bound arity.** Products of pairwise terms span `≥5` indices
  (`ω(v₁₂,v₃₄)ω(v₁₅,v₂₃)`), so reducibility ≠ "low-degree in `ω`". The reducible/irreducible boundary
  is subtle.
- **(O2) Objects are *subspaces*, not vectors** — Weyl's first fundamental theorem does not apply;
  relative position (Maslov/Wall) is the right but harder invariant theory.
- **(O3) Char 2 harbors exotica** (Arf, Dickson, `q₄`'s siblings). Proving "nothing exotic survives"
  in a ring *known* to contain exotica and *not classified* is the crux — one must exclude a
  non-`ω` `H⁴` escape while *admitting* the `ω`-built `H³` class.
- **(O4) All `n`.** The invariant ring grows with `n`; a fixed-`n` computation is evidence, the
  theorem is uniform in `n`. (Note: the master theorem already gives `n=4` no-`H⁴`; (b) is `n≥5`.)

## 7. Difficulty assessment + milestones

**Grounded ladder status (updated 2026-06-23):** **M1 DONE** (XXII `thm:trunc`), **M2 DONE**
(`k6_skeleton.py` — generic stratum `(2n,2n,0)`, structural facts verified), **M3 DONE-IN-SPIRIT**
(XIX `Prop frameq`, arity-agnostic), **M4 DONE for the Arf/P2 candidate** (`m4_intrinsic.py` — outcome
(a): intrinsic Arf absorbed at `n≥5`, nonexistent at `n=4`; mechanism shift constant→reducible),
**M5 OPEN** (the general theorem). So the genuinely-open content is now **M5 alone**; the
`ω`-generated front, the structural scaffold, *and* the natural P2 exotic candidate are settled. M4
absorbed one candidate, not all (O3); M5 is the uniform no-exotic theorem.

- **M1 (`c₅` exactness at `K₆`)**: **DONE — Paper XXII Theorem `thm:trunc`** (`c=δa`, proven via the
  4-index cochain-indexing argument — *cochain-level, stratum-agnostic*; verified `k6_truncation.py`,
  `Σc_m≡0` at n=4,5,6). Closes the
  `ω`-generated / 4-index-decomposable arity-5 route; *not* re-derived here. It isolates M4.
- **M2 (`K₆` skeleton)**: **DONE** (`k6_skeleton.py`) — generic stratum `(2n,2n,0)` (full-span,
  nondegenerate, *unlike* `K₅`'s `(8,6,2)`); structural facts verified; intrinsic-`q` existence
  0%/40%/31% at n=4/5/6 (hands M4 a real branch (b) at n=4).
- **M3 (frame-`q` P1)**: **DONE-IN-SPIRIT** — XIX `Prop frameq` is arity-agnostic and lifts verbatim
  to 15 rays; cite, don't re-derive.
- **M4 (intrinsic exotic P2)**: **DONE for the Arf candidate** (`m4_intrinsic.py`,
  `M4_intrinsic_README.md`) — **outcome (a)**: the intrinsic Arf at `K₆` is absorbed at `n≥5`
  (constant at `n=5`, nonconstant-but-reducible at `n=6` — reducibility by the structural proof that
  `Arf` is the Dickson polynomial in the arity-≤4 ray-Gram), and does not exist at `n=4`. No `H⁴`
  escape from this object; the `(c)`-falsification branch did not occur. Discovery: the absorption
  *mechanism shifts* from constancy (`n=5`) to reducibility (`n=6`). Scope: absorbs *one* candidate,
  not all exotica (O3) — does **not** close item 21.
- **M5 (FFT/generation)**: the actual theorem. The `ℝ,ℂ` invariant theory is known (C-O), but **the
  reduction shortcut is now known NOT to work** (`co_reduce.py`, `LITERATURE.md`): C-O's cross-ratio
  reduces to a tautology and its Pfaffian to a coarse stratum indicator — only the discrete *sign*
  reduces (to the Maslov bit `μ`). **So M5's difficulty is as originally estimated** (paper-scale,
  XXIII); C-O serves only as a *dictionary for the bottom rung (`μ`)*, not a route to the `H³`/exotic
  content. M1–M4 are scaffold; M5 is the genuinely char-2 proof.

**What counts as progress short of M5:** any of M1–M4 cleanly done is a real contribution (it either
finds an escape — falsifying item 21, very interesting — or adds a validated `H⁴`-level "absorbed"
data point). The honest bar for *closing* item 21 is M5.

## 8. Scoping discipline (carry this in — it has bitten 4×)

- A bounded-family search returning "absorbed/exact" is **evidence, not a nonexistence proof** (the
  space of exotic invariants is unparametrized — O3). Every M1–M4 result must be stated as "the tested
  family/stratum behaves," never "no arity-5 invariant exists."
- Absolute saturation/exactness rates are **population/metric-dependent** (`calib_q4.py`: raw-config
  vs deduplicated-bucket differ 65%→99%). Quote *orderings* and *`n=6` limits*, and the
  *deduplicated-bucket* metric to compare with XIX — not a single raw percentage.
- Item 21 is `n≥5`; `n=4` is already settled (master theorem). Keep `n` explicit.

## 9. Files (this sub-project)
- `LITERATURE.md` — **prior art** (Conley–Ovsienko, MWZ, Carlisle–Kropholler/Quillen); the char-2
  reframing of M4/M5. *Read this first.*
- `qk_saturation.py` — `q_k` saturation, `q₅≥q₄` (the arity-5 `ω`-Maslov evidence).
- `calib_q4.py` — machinery validated against XIX's exhaustive `q4_bit` (64000/64000).
- `k6_skeleton.py` + `M2_skeleton_README.md` — M2: the `K₆` skeleton; generic stratum `(2n,2n,0)`.
- `m4_intrinsic.py` + `M4_intrinsic_README.md` — M4: the intrinsic exotic `Q₆` + its Arf; outcome (a)
  (absorbed at `n≥5`, mechanism shift constant→reducible; structural reducibility proof).
- `co_reduce.py` — the C-O mod-2 reduction attempt: cross-ratio vacuous (`3≡1`), Pfaffian a coarse
  stratum indicator — the `H³`/exotic obstruction is orthogonal to C-O, not a reduction (rules out the
  reduction shortcut for M5).
- M1 is Paper XXII `thm:trunc` (verified `../paper22/k6_truncation.py`) — not re-implemented here.
