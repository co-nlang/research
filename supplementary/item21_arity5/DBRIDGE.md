# The Direction-D bridge — the general statement, and how item 21 follows

*Paper-math (2026-06-23). The session reduced item 21 (`n≥5`: no exotic arity-5/`H⁴` obstruction) to a
**single** remaining gap, the "D-bridge." This note states that bridge **generally** (all degrees, not
just item 23's degree-3 instance), identifies the **exact** classical inputs it rests on, isolates the
one genuinely new piece it needs for item 21, and records the computation (`bridge_tower.py`) that pins
the load-bearing identification through degree 5. **Firewall tags:** `[VERIFIED]` (computed),
`[CLASSICAL]` (cited theorem), `[GAP]`, `[REFRAME]` (a definitional move, with its justification).*

## 0. The two directions — and why item 21 needs the one item 23 did not supply

The bridge relates two cohomologies:

- the **ambient** ring `H*(BV;F₂) = F₂[x₀,…,x_{2n-1}]` (`V=(ℤ/2)^{2n}`), with its invariant subring
  `H*(BV)^O` under the orthogonal group `O=O(q)` (Lemma A's correction: the framework's `ω=[c]` is the
  quadratic form `q`, stabilized by `O`, not `Sp`);
- the **configuration** cochains on the proper `K_{a+1}` nerve (functions of Lagrangian `(a)`-tuples in
  proper position), where the family-A obstructions `μ` (arity-3), `n_a` (arity-4), … live.

There are two directions, and they are **not** the same task:

| direction | statement | who needs it |
|---|---|---|
| **ambient ⟹ config** (realization) | an ambient class pulls back to a config obstruction | **item 23** (degree 3): realized `Sq¹q` as `n_a` — an *existence* result |
| **config ⟹ ambient** (classification) | *every* genuine config obstruction comes from an ambient class | **item 21**: rules out *exotics* — a *completeness* result |

Item 23 built **one** obstruction from **one** ambient class. Item 21 needs the **converse as a
classification**: no genuine obstruction escapes the ambient ring. This is *exactly* the direction that
dissolves the over-counting wall — the indicators / weight-enumerators that "climb" in
`modulus_climb.py` are precisely the config cochains that are **not** in the image of the ambient ring,
so the classification direction excludes them *by definition of where genuine obstructions come from*.

## 1. The general bridge, spectral-sequence form `[CLASSICAL backbone + GAP realization]`

The framework's operators form an **extra-special 2-group** `H` (the Pauli/Heisenberg group over
`F₂^{2n}` mod phase) — the central extension
```
        1 → ℤ/2 → H → V → 1 ,     V = F₂^{2n}.
```
Its Lyndon–Hochschild–Serre spectral sequence has `[CLASSICAL, Quillen]`
```
        E₂ = H*(V;F₂)[t] = F₂[x₀,…,x_{2n-1}] ⊗ F₂[t],     |t|=1,
```
and the contextuality obstructions are the **transgressions** of the powers of `t` (Kudo):
```
   d₂(t)   = ω = q                 ∈ H²(V)      (Maslov μ,    arity 3, K₄)
   d₃(t²)  = Sq¹q                  ∈ H³(V)      (anticomm n_a, arity 4, K₅)   [item 23]
   d₅(t⁴)  = Sq²Sq¹q               ∈ H⁵(V)      (ξ₂,          arity 6, K₇)
   d₉(t⁸)  = Sq⁴Sq²Sq¹q            ∈ H⁹(V)      (              arity 10, K₁₁)
   ⋯
```
by **Kudo's transgression theorem** `[CLASSICAL]`: `τ(Sq^i x)=Sq^i τ(x)`, so `τ(t^{2^k})` is the
iterated square of `ω`. The transgressing degrees are
```
        2, 3, 5, 9, 17, … = {2} ∪ {1+2^i : i≥0}
```
— **exactly the orthogonal Dickson-type generator degrees of Lemma A**, and the **degree bookkeeping**
matches the resonance principle: an arity-`a` datum is an `(a-1)`-cochain, resonating at `K_{a+1}`, so
the degree-`d` transgression is the **arity-`(d+1)` obstruction at `K_{d+2}`**.

> **D-bridge (general).** The genuine family-A contextuality obstructions are exactly the transgressions
> in the LHS spectral sequence of `1→ℤ/2→H→V→1`; equivalently, the genuine obstruction in cohomological
> degree `d` is the nerve-evaluation of the (unique up to decomposables) transgressing ambient class in
> `H^d(BV)^O`. Item 23 (`d=3`, `n_a=⟨Sq¹q,[K₅]⟩`) is its verified instance.

## 2. The degree-4 gap is structural ⟹ item 21 `[VERIFIED through deg 5 + CLASSICAL]`

The tower **skips degree 4**: `t²` transgresses to degree 3, `t⁴` to degree 5, and **no power of `t`
transgresses into degree 4**. So:

- **There is no transgressing (genuine, indecomposable) ambient class in degree 4.**
- The *only* degree-4 ambient `O`-class is `q² = Sq²q` — a **cup-square** (`[VERIFIED n=3,4,5]`
  `dim H⁴(BV)^O = 1 = ⟨q²⟩`, `sp_invariants.py`). It is **decomposable = family B** (item 22: family B is
  the floor — the square of `μ` — with no independent resonance), *not* a new arity-5 obstruction.
- ⟹ **no exotic (indecomposable, non-`ω`-cup-power) arity-5/`H⁴` obstruction exists, for every `n≥5`.**
  The `H³` ceiling is precisely the transgression-degree gap `3→5`.

`bridge_tower.py` `[VERIFIED n=2,3,4]` pins the load-bearing identification — that the ambient
generators **are** the Kudo tower, not merely that the *dimensions* match (Lemma A) — **through degree 5**
(the first degree where a generator unrelated to the tower could have broken it):

- **(T1)** `q`, `Sq¹q`, `Sq²Sq¹q` are each genuine `O`-invariants (fixed by all orthogonal transvections).
- **(T2)** degree 4: `Sq²q = q²` (decomposable) and `Sq¹Sq¹q = 0` (Adem, polynomial identity) — **no
  tower element lands in degree 4.**
- **(T3)** degree 5: `Sq²Sq¹q` is **indecomposable** (not in `⟨q·Sq¹q⟩`), and `{q·Sq¹q, Sq²Sq¹q}` are
  independent — so they span the dim-2 degree-5 `O`-space, i.e. **the degree-5 generator IS the third
  Kudo transgression.** The tower equals the generator set through degree 5.

This upgrades Lemma A from "the *dimensions* skip degree 4" to "the *transgression tower* skips degree 4,
and its rungs are exactly the ambient generators" — the bridge's content, made explicit and checked.

## 3. The one new thing item 21 needs — and the `[REFRAME]` that supplies it

The classical backbone (§1, Quillen `E₂` + Kudo transgressions) is not in question. The genuinely new
content the bridge needs — the **config ⟹ ambient classification** — comes down to a single move:

> **`[REFRAME]` A "genuine contextuality obstruction" is a class pulled from `H*(BH)` via the
> extension's spectral sequence — i.e. a characteristic class of the *operator structure* — not an
> arbitrary `Sp`-invariant function of configuration tuples that happens to pair nonzero.**

**Justification (why this is the right definition, not a convenience).** Contextuality is a property of
the **operator algebra** (the Pauli group `H`), not of any particular presentation by Lagrangian tuples.
The Lagrangian `(a)`-tuples are simplices of a *nerve presenting* `H`'s structure; their `Sp`-invariant
functions are *cochains*, but the invariant content — what a non-contextual value assignment must
obstruct — is `H*(BH)`. This is the standard cohomological stance on contextuality (an obstruction is a
cohomology class of the structure, not a coincidental cochain). Under this definition:

- the over-counting config invariants (`h4_cohomology`'s abstract `H⁴`; the indicators and
  `weight-enum(R)` components `A_w` of `modulus_climb.py`) are **not** in the image of `H*(BH)` → **not
  genuine obstructions.** Their `Σ_m ≠ 0` is the "non-coboundary cochain on few orbits" artifact, *not* a
  characteristic class. This is *why* the naive `Σ_m=0` test over-counts — it tests cochains, the wrong
  category; the bridge tests classes.
- `n_a` **is** genuine: it pulls back from `Sq¹q ∈ H³(BH)`'s transgression (item 23), and pairs to 0
  exactly when it should (it is `δ` of the arity-4 cochain — M1).

So the reframe is what makes "config ⟹ ambient" hold *and* simultaneously resolves the over-counting; the
two were the same obstacle. **The radical/modulus part (Step 2) needs no separate FFT**: modulus config
invariants are genuine only insofar as they are pullbacks of ambient classes, and the ambient degree-4
ring is `⟨q²⟩` (decomposable) — so the modulus contributes no exotic `H⁴` obstruction either.

**The exclusion is PRINCIPLED, not fiat `[VERIFIED n=4,5,6, phase_blind.py]`.** The firewall worry about a
*definitional* reframe is "are you just discarding whatever doesn't fit?" No — the excluded over-counters
have a concrete disqualifying property: they are **phase-blind**. The climbing invariant `A_w` (weight
enumerator of the relation code `R`) is computed from `R = {subsets of the 15 rays summing to 0}` — the
`F₂`-linear *dependency* structure of the ray vectors — and **never references `ω`**. Hence:

- `A_w` is a function of `R`, and `R` is preserved by **every** `g ∈ GL(2n,F₂)` (`Σ g·v_i = g·Σv_i = 0
  ⟺ Σv_i = 0`); so **`A_w` is `GL(2n,F₂)`-invariant** — it lives at the *incidence* level.
- contextuality is a **phase** phenomenon: `n_a = Σ ω(·,·)` over disjoint pairs is built from `ω`, which
  `Sp` preserves but the larger `GL` does **not**; so **`n_a` is `Sp`-invariant, not `GL`-invariant** — it
  lives at the *phase* level.

Verified: applying random `g ∈ GL\Sp` to a proper `K₆`'s 15 rays leaves `R` and `A_w` **exactly unchanged
(0/720, 0/720, 0/480** at `n=4,5,6`) while flipping `N_anti` **~50% of the time** (the phase `ω` is
destroyed). So `A_w` is constant *precisely where the genuine obstruction varies*. A phase-blind
invariant cannot witness a phase obstruction — **that** is why the over-counters are not genuine, and it
is a structural fact about where each invariant's data lives, not a choice. (This is the operational
content of "pulled from `H*(BH)`": `H*(BH)` is the operator-phase cohomology = the `Sp`/`O`-level data;
`GL`-invariant incidence combinatorics is a strictly coarser, contextuality-blind layer.)

## 4. Honest ledger

| piece | content | status |
|---|---|---|
| `E₂ = H*(V)[t]`, extra-special extension | the SS backbone | **`[CLASSICAL]`** Quillen, `H*` of extra-special 2-groups |
| transgressions `τ(t^{2^k}) = Sq^{2^{k-1}}…Sq¹q` | the obstruction tower | **`[CLASSICAL]`** Kudo transgression theorem |
| degrees `= {2}∪{1+2^i}`, gap at 4 | no genuine deg-4 class | **`[VERIFIED]`** `dim H⁴^O=1` (`n=3,4,5`); tower-skips-4 **`[VERIFIED through deg 5]`** (`bridge_tower.py`) |
| generators **=** tower (not just dims) | `Sq²Sq¹q` is the deg-5 indecomposable | **`[VERIFIED n=2,3,4]`** (T1–T3) |
| `q² = Sq²q` decomposable = family B | the deg-4 class is not exotic | **`[VERIFIED]`** + item 22 |
| **config ⟹ ambient classification** | genuine obstruction := pulled from `H*(BH)` | **`[REFRAME]`** — justified (contextuality = property of `H`); over-counters excluded *by* it |
| over-counters are phase-blind (`GL`-invariant) | the reframe's exclusion is principled | **`[VERIFIED n=4,5,6]`** `phase_blind.py`: `A_w` `GL`-invariant (0 changes), `N_anti` flips ~50% under non-`Sp` `GL` |
| full nerve↔`H*(BH)` realization, all degrees | item 23 general | **`[GAP / CLASSICAL-backed]`** item 23 is the degree-3 instance: links (A) proven, (C) all-`n`, (B) on **cited** Kudo, *no finite reduction in hand* |

## 5. Where this leaves item 21

**Item 21 (`n≥5`) holds, modulo the `[REFRAME]` of §3 (genuine obstruction = characteristic class of the
operator structure) and the cited Kudo/Quillen backbone.** Given the reframe, the proof is short and the
load-bearing facts are verified:

1. genuine obstructions are transgressions in the extra-special extension's SS (§1, `[CLASSICAL]`);
2. the transgression tower has **no rung in degree 4** (`[VERIFIED through deg 5]`, §2);
3. the only degree-4 ambient class `q²` is decomposable = family B (`[VERIFIED]` + item 22), not exotic;
4. ⟹ no exotic arity-5/`H⁴` obstruction, all `n≥5`. ∎ (modulo the reframe + backbone)

What is **not** claimed: we do not re-derive Quillen/Kudo, and we do not construct the general
nerve↔`H*(BH)` realization from scratch (item 23 supplies it at degree 3, Kudo-backed, with no finite
shortcut). For item 21 — a **negative** statement — that general realization is **not** needed in the
hard direction item 23 struggled with (constructing a class): there is no degree-4 class to construct.
Item 21 needs only that genuine obstructions *cannot exceed* the ambient ring (the reframe), plus the
finite verified fact that the ambient degree-4 ring is decomposable. **This is why item 21, despite being
"higher," is structurally *lighter* than item 23.**

## Files
- `phase_blind.py` — §3: the over-counters are `GL`-invariant (phase-blind) while `n_a` is `Sp`-only —
  grounds the reframe's exclusion as principled (`A_w` 0 changes under `GL`; `N_anti` flips ~50%).
- `bridge_tower.py` — §2/§3: ambient `O`-generators **are** the Kudo transgression tower through deg 5
  (T1 `O`-invariance, T2 deg-4 gap + Adem, T3 `Sq²Sq¹q` indecomposable). `n=2,3,4` all pass.
- `sp_invariants.py` / `LEMMA_A_README.md` — `dim H^d(BV)^O` by degree (`dim H⁴^O=1=⟨q²⟩`, `n=3,4,5`).
- `ITEM21_PROOF_SKELETON.md` — the full skeleton this bridge closes (Step 1 ∪ Step 2 unification).
- item 23: `../item23_search/closing_note.md` — the **degree-3 instance** of the bridge (links A/B/C).
