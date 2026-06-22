# Item 21 (b) — The Arity-5 Exotic Escape: Attack Plan / Handover

*Status: open, XXIII-level. This is a research-program handover, not a result. It localizes the one
genuine remaining front of item 21 and lays out the concrete route, the template to extend, the
obstacles, and milestones that count as partial progress.*

## 0. Orientation (one paragraph)

Item 21 asks: is `H³` a **hard** ceiling for Pauli contextuality, i.e. is there *no* irreducible
arity-5 invariant of five Lagrangians that could furnish an `H⁴` obstruction at `K₆`? Item 23's
closure (mod Kudo) caps the **Steenrod-generated** ascent (`Sq¹ω` unique, `Sq¹Sq¹ω=0`, `Sq²ω=ω²`
decomposable), and the arity-4 base case is **absorbed**: the natural `ω`-Maslov bit `q₄` is saturated
and Paper XIX rules out the exotic **Arf** invariant as an `H³` classifier. The probe `qk_saturation.py`
shows the natural arity-5 `q₅` also saturates (`q₅≥q₄`, validated). So the **lone hard core** is: does
a *genuinely-exotic* (non-`ω`, Arf/Dickson-type) **arity-5** invariant exist and escape to `H⁴`? (b)
= **test whether** XIX's arity-4 Arf-exclusion extends to arity 5 — which may *support* item 21, may
need *re-planning*, or may *falsify* it (see M4's three outcomes); the program is built to distinguish
these, not to confirm a foregone conclusion.

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
- **Arity-5 `ω`-Maslov half: matching evidence.** `q₅` saturates `≥ q₄` on identical configs
  (`qk_saturation.py`; machinery validated `64000/64000` against XIX's exhaustive `q4_bit`,
  `calib_q4.py`). So the *`ω`-generated* arity-5 invariant carries no fiber info.
- **Remaining = the exotic non-`ω` arity-5 invariant.** This is (b).

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

1. **`q₅` exactness, not just saturation (the Paper XXII `c=δa` route).** Saturation says `q₅` is
   *constant* (value-level); the stronger statement item 21 wants is *cochain-level* — the arity-5
   cochain is `δ` of an arity-4 cochain (exact ⟹ no `H⁴` class). Compute, on `K₆` configs, whether the
   natural arity-5 4-cochain `c₅` satisfies `c₅ = δ(arity-4 cochain)` — i.e. `⟨c₅,[K₆]⟩ = 0` for all
   `K₆` (the direct `H⁴`-analog of `⟨n_a,[K₅]⟩=N_anti`; finite per-config check).
   **Scope of M1 (on the milestone, not just §2): even a perfectly clean M1 (`⟨c₅,[K₆]⟩≡0`) closes
   ONLY the `ω`-generated / natural-cochain arity-5 route.** It says nothing about an exotic non-`ω`
   arity-5 invariant — that is M4. M1 is **necessary, not sufficient**: it removes the easy escape and
   *isolates* the exotic one; item 21 is not advanced past the `ω`-front by M1 alone. *(Milestone M1.)*
2. **Build the `K₆` skeleton lemma** (extend `lem:skeleton`): the 15-ray Gram `G₆`, relation space
   `R₆`, quadratic `o₆`, linear `ℓ₆=o₆|_{ker G₆}`. Identify the generic stratum. *(Milestone M2.)*
3. **Frame-`q` exclusion at arity 5 (P1).** Verify (should be immediate) that frame-`q` non-invariance
   kills coordinate Arf-type arity-5 invariants. *(Milestone M3 — likely cheap.)*
4. **Intrinsic exotic at arity 5 (P2) — the crux, with a genuinely OPEN outcome space.** Build the
   `K₆` intrinsic exotic (a Dickson/Arf-type quadratic refinement of `W₆` vanishing on the 15 rays) and
   test its correlation with the `H⁴`-fiber (the analog of `N_anti`'s parity at `K₅`). **Do not
   presuppose the arity-4 replay.** There are (at least) three structurally distinct outcomes; the plan
   must branch on which actually occurs:
   - **(a) Replay** — an intrinsic exotic exists in the `K₆` stratum but is *blind* to the fiber (the
     `Arf=0`-but-parity-splits pattern recurs). → another evidence point *for* item 21; P2 lifts
     cleanly. *Most expected, but not to be assumed.*
   - **(b) No intrinsic exotic** — the generic `K₆` stratum admits *none* (the `ℓ₆|_{R₆}≢0` analog
     holds generically). → **structurally different**: P2's "exists-but-blind" argument shape does *not*
     apply (there is nothing to show blind). Needs a separate treatment — the `noq_odd`-style
     realizability route, or a direct exactness argument. Flag and re-plan; do **not** force the P2
     template onto (b).
   - **(c) Intrinsic exotic exists AND tracks the fiber** — it *separates* the `H⁴`-fiber. → **this
     FALSIFIES item 21**: an irreducible arity-5 classifier exists, `H³` is *not* the hard ceiling, there
     *is* an `H⁴` escape. This is the single genuinely *interesting* outcome and is a **live branch to
     be actively checked, not assumed away** — indeed if M1–M3 come back clean, (c) becomes the *most
     likely* place the truth could still hide. On (c), pivot the whole item from "prove the ceiling" to
     "characterize the escape" (a new positive result, XXIII+ material) — and revisit Paper XXII's
     `c=δa`-exactness claim, which (c) would contradict at arity 5.

   *(Milestone M4 — the crux; the outcome decides whether item 21 is supported (a), needs re-planning
   (b), or is false (c). Design the computation to distinguish all three, not just to confirm (a).)*
5. **Reducibility / FFT-style generation theorem (the real theorem).** Prove every arity-5
   `Sp(2n,F₂)`-invariant of 5 Lagrangians is a polynomial in arity-`≤4` invariants — a *first/second
   fundamental theorem* for `Sp(2n,F₂)` on Lagrangian tuples. *(Milestone M5 — the full item 21; route
   1 of the disposition. M1–M4 are evidence/structure feeding M5.)*

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

- **M1 (`q₅`/`c₅` exactness at `K₆`)**: computational, finite per config — *do this first*; it directly
  tests "no `H⁴` from the natural cochain." Strong evidence either way. **Tractable now.**
- **M2 (`K₆` skeleton)**: linear algebra, tractable; mostly bookkeeping + stratum identification.
- **M3 (frame-`q` P1)**: cheap, likely immediate.
- **M4 (intrinsic exotic P2)**: the crux of the *computational* evidence; build the `K₆` intrinsic
  exotic and test fiber-correlation. Moderate effort, **but the outcome is genuinely open** — (a)
  replay/blind (supports 21), (b) none-exists (re-plan, P2 inapplicable), or (c) tracks-the-fiber
  (**falsifies 21** — the only "interesting" branch; check it, don't assume it away).
- **M5 (FFT/generation)**: the actual theorem; modular invariant theory of `Sp(2n,F₂)` on Lagrangian
  tuples — a paper-scale (XXIII) project, not a session. M1–M4 are the empirical scaffold; M5 is the
  proof.

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
- `qk_saturation.py` — `q_k` saturation, `q₅≥q₄` (the arity-5 `ω`-Maslov evidence).
- `calib_q4.py` — machinery validated against XIX's exhaustive `q4_bit` (64000/64000).
- *(to add)* `c5_exactness.py` — M1: `⟨c₅,[K₆]⟩` over `K₆` configs.
- *(to add)* `k6_skeleton.py` — M2: the `K₆` Gram/relation skeleton + stratum.
