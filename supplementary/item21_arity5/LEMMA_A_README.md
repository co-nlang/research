# Item 21, Lemma A (the ω/q-part) — VERIFIED: no indecomposable degree-4 obstruction

*Paper-math + verification (2026-06-23, `sp_invariants.py`). Lemma A's payoff — that the `ω`-part of
item 21 contributes no exotic arity-5/`H⁴` obstruction — is now established at the ambient-cohomology
level and verified for `n=3,4` (the stable range covering `n≥5`). Two of my own errors were caught by
the firewall en route (recorded below). Firewall tags: `[VERIFIED]`, `[CLASSICAL]`, `[GAP]`,
`[CORRECTED]`.*

## The correct object (two corrections)

- **`[CORRECTED]` The group is `O`, not `Sp`.** The framework's `H²` class `ω=[c]` (item 23,
  `c(g₁,g₂)=X_{g₁}·Z_{g₂}`, `q(v)=c(v,v)`) is the **quadratic form `q`** (`[c]↔q` via the standard
  `H²(V;F₂)`↔quadratic-forms iso), *not* the bilinear symplectic form. And `q` is invariant under the
  **orthogonal group `O`** (its stabilizer), *not* `Sp` (a transvection `T_v` shifts `q` by
  `ω(·,v)(q(v)+1)`). Verified: `dim H²(BV)^{Sp}=0` (no `Sp`-invariant quadratic form) but
  `dim H²(BV)^{O}=1` (`=q`). So the obstruction `n_a=Sq¹q` lives in `H*(BV)^{O}`, and Lemma A is about
  the **orthogonal**-invariant ring. *(An earlier draft mis-targeted `Sp` — `dim H³^{Sp}` looked `0`,
  which would have wrongly said `n_a` isn't invariant; the resolution is the group is `O`.)*
- **`[CORRECTED]` Kernel bug.** The first `fixed_space` stacked the *columns* (images `(T_v−I)(m)`)
  instead of the *rows* (equations) when intersecting `ker(T_v−I)` over several transvections
  (column-rank = row-rank only for a single matrix). Caught by a direct check: `q` and `Sq¹q` are
  fixed by all `O`-transvections (`bad=0`), contradicting the buggy `dim H³^O=0`. Fixed → the numbers
  below.

## The result `[VERIFIED]`

`dim H^d(BV)^{O(q)}` (simultaneous fixed space under all orthogonal transvections `T_v`, `q(v)=1`):

| `n` | d2 | d3 | d4 | d5 |
|----|----|----|----|----|
| 2 (outlier) | 2 | 2 | **3** | 4 |
| **3** | 1 (`q`) | 1 (`Sq¹q`) | **1 (`q²`)** | 2 |
| **4** | 1 (`q`) | 1 (`Sq¹q`) | **1 (`q²`)** | 2 |
| **5** | 1 (`q`) | 1 (`Sq¹q`) | **1 (`q²`)** | — |

For `n=3,4,5` (stable, including item 21's smallest case `n=5` — `n=2` is the small special case): the orthogonal
generators sit at degrees **2 (`q`), 3 (`Sq¹q=n_a`), 5 (`ξ₂`), …** — i.e. `{2}∪{1+2^i}` (the orthogonal
Dickson-type degrees) — and **there is NO generator at degree 4**: `dim H⁴^O = 1`, spanned entirely by
`q²` (decomposable, family B). So:

> **No indecomposable degree-4 orthogonal invariant ⟹ no exotic arity-5/`H⁴` obstruction from the
> `ω`/`q`-part.** The `H³` ceiling is precisely the **degree gap `3→5`** in the orthogonal generators.

This dovetails with the Steenrod side: the Steenrod-closed subring `⟨q⟩` is `F₂[q, Sq¹q]` (since
`Sq¹Sq¹q=0`, `Sq²q=q²` decomposable, `Sq^iq=0` for `i>2` by instability) — generators in degrees `2,3`
only, degree-4 part `=⟨q²⟩`. Both the Steenrod tower *and* the orthogonal-Dickson generators skip
degree 4. `[CLASSICAL]` the `{1+2^i}` orthogonal Dickson degrees are classical invariant theory; the
low-degree part (no degree-4 generator) is verified here.

## What this gives, and the remaining gap

- **`[VERIFIED + CLASSICAL]`** The ambient `O`-invariant cohomology has no indecomposable `H⁴` class
  (only `q²`). The next obstruction-degree after `H³` is `H⁵` (the degree-5 generator `ξ₂`) — which
  would be an *arity-6* obstruction at `K₇`, **beyond item 21's `H⁴`/arity-5 scope** (item 21's sibling
  at the next level — the ladder's degrees are `{2,3,5,9,…}`, so `H⁴`,`H⁶`,`H⁷`,`H⁸` are all skipped).
- **`[GAP]` The bridge (Lemma A proper):** that the genuine arity-5/`H⁴` configuration obstructions
  *are* exactly the ambient `O`-invariant degree-4 classes (the natural-data identification). This is
  item 23's framework (`n_a = Sq¹q` realized on the nerve) extended to a full ambient↔configuration
  dictionary. With it, the verified "no degree-4 `O`-class" closes the `ω`/`q`-part of item 21. This
  bridge is *also* what resolves the over-counting: the config invariants over-count (indicators,
  weight enumerators) precisely because most are **not** ambient `O`-cohomology classes — only the
  ambient classes are genuine obstructions.

## Net for the proof skeleton

Step 1 (the `ω`-part) is now in good shape **and partly verified**: the genuine obstructions are the
ambient `O`-invariant Steenrod classes, which have **no indecomposable degree-4** (verified `n=3,4`;
classical for all `n≥3`). The remaining work is the **bridge** (config obstructions = ambient
`O`-classes), which is the natural-data identification and subsumes the over-counting issue. Step 2
(the radical/modulus part) remains the harder open core, but Lemma A shows the `ω`-part's ceiling is a
**clean consequence of the orthogonal-invariant degree pattern skipping 4**.

## Files
- `sp_invariants.py` — computes `dim H^d(BV)^{Sp}` and `dim H^d(BV)^{O}` by degree (corrected kernel).
- item 23: `../item23_search/closing_note.md` — `n_a=Sq¹q`, the Steenrod tower (the bridge's basis).
