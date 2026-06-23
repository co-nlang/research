# Item 21 / M5 — structural reduction: the exotic lives in `rad(ω|_W)` = XIX's modulus

*A verified value-level reduction (2026-06-23, `kerG_reduction.py`) that localizes item 21's `n≥5`
exotic to exactly Paper XIX's radical/modulus data, and ties the open core to XXII's ceiling theorem.
Firewall tags are explicit: **[VERIFIED, value-level]** vs **[CONJECTURAL, cochain-level]**.*

## The reduction

By the completeness lemma, every arity-5 invariant is a function of `(G,R)` (ray-Gram + relation
space). Linear algebra pins how `R` relates to `G`:

- With rays as rows of `M`: `G = MΩMᵀ`, `R = leftnull(M)`. For `a∈R` (`aᵀM=0`) we get `aᵀG=aᵀMΩMᵀ=0`,
  so **`R ⊆ ker(G)` always**, and the skeleton identity gives **`ker(G)/R ≅ rad(ω|_W)`**. Hence

  > **`R = ker(G) ⟺ rad(ω|_W) = 0`** (the nondegenerate stratum).

**[VERIFIED, value-level]** (`kerG_reduction.py`, 5-configs = the arity-5 objects): `R⊆ker(G)`
**1100/1100**; `dim ker(G) − dim R = dim rad(ω|_W)` **1100/1100**. Stratum breakdown and nondegenerate
(`rad=0`) fraction:

| `n` | nondeg `rad=0` | typical strata `(dim W, dim rad)` |
|----|----|----|
| 4 | **100%** (400/400) | `(8,0)` only — **control passes** |
| 5 | **~21%** (83/400) | `(9,1)` 48%, `(8,2)` 28%, `(10,0)` 21% |
| 6 | **~17%** (51/300) | `(10,2)` 43%, `(9,1)` 19%, `(10,0)` 17% |

**Consequence [VERIFIED, value-level].** On the nondegenerate stratum `R = ker(G)` is *recovered from
`G`*, so `(G,R)=(G,ker G)` and **every arity-5 invariant is a function of the `ω`-Gram alone**. *(Caveat
— see the self-correction below: "function of `G`" = **all** invariants here, including indicators, so
this is not by itself a constraint.)* The genuinely-new datum at `n≥5` is what appears **beyond** `G`:
1. on the **nondegenerate** stratum (all of `n=4`; ~20% at `n≥5`) there is **nothing beyond `G`**;
2. on the **degenerate** strata (the bulk at `n≥5`) the extra datum is exactly the **radical**
   `rad(ω|_W)`.

## Why this matters: case (2) IS Paper XIX's modulus

`rad(ω|_W)` is **Paper XIX's order parameter** for the `n≥5` modulus. So the reduction says: the
*extra-`ω`* content available to an arity-5 invariant at `n≥5` is *exactly* the radical/modulus data XIX
already isolated. The `n`-pattern matches: at `n=4` the stratum is 100% nondegenerate (`rad=0`) → no
extra data beyond `G`, no modulus (consistent with `n=4` settled); at `n≥5` the degenerate bulk carries
`rad(ω|_W)>0` → XIX's modulus appears → that is the only place extra-`ω` content can hide.

## ⚠ Self-correction (2026-06-23) — what the reduction does and does NOT give

An earlier draft of this note claimed the reduction *dispatches* a "case (1)" (nondegenerate stratum)
via "every invariant is `ω`-generated ⟹ XXII handles it." **That over-reached** — caught by re-running
the session's own `h4_cohomology` lesson on it:

- On the nondegenerate stratum the orbit **is** `G` (since `R=ker G`), so `{functions of G} = {all
  Sp-invariants}` — including the orbit-**indicators** that give `Σ_m=1` (the `h4_cohomology`
  over-counting). So "ω-generated" is **vacuous as a constraint** there: it does **not** invoke XXII,
  and it does **not** separate natural data from indicators.
- The "product of atoms ⟹ degree `≥6` cochain" sub-sketch was also loose — it conflated *polynomial
  degree in the Gram* with *cochain degree on the nerve*; `F(\text{face})` is just a number, not a cup
  product.

So **neither stratum is "dispatched"** by the reduction. The natural-data delimitation (which invariants
count as obstruction-carriers, excluding indicators) is untouched and remains the insight-bound crux.

## What the reduction DOES give [SOLID]

The verified, surviving content is the **identification of the extra data**:

> The only datum an arity-5 invariant can depend on *beyond the `ω`-Gram `G`* is the **radical
> `rad(ω|_W)`**, which is present exactly on the degenerate strata (`n≥5`) and **is Paper XIX's modulus
> order parameter**.

So: at `n=4` the stratum is 100% nondegenerate (`rad=0`) — no extra data, no modulus (consistent with
`n=4` settled); at `n≥5` the degenerate bulk carries `rad(ω|_W)` = XIX's modulus, and that is the *only*
place extra-`ω` content can live. The natural radical-based exotic (XIX's intrinsic Arf) is found `≈0`
by the corrected M4 (`m4_cochain.py`) — first evidence the radical datum does not climb to `H⁴`.

## Net

The reduction **does not close** item 21 and does **not** dispatch either stratum (the over-counting and
the natural-data problem are untouched — both cochain-level/insight-bound). Its real value is the
**localization**: the extra-`ω` content of item 21 at `n≥5` is exactly `rad(ω|_W)` = **XIX's modulus**,
so item 21's `n≥5` core is "**does XIX's radical modulus climb `H³→H⁴`?**" — XXII's ceiling restated for
the radical (bottom/anticommutation case proven by XXII; natural Arf exotic `≈0` by M4). That connects
item 21 to the XIX/XXII machinery rather than an unparametrized search — but the FFT (which natural
invariants generate, and whether they climb) remains the insight-bound gap. **Firewall note:** the
extra-data localization is value-level/verified; every "⟹ no `H⁴`" is cochain-level/conjectural and
needs a direct `Σ=0`/`δ`-witness or an FFT proof. The over-counting trap (functions-of-`G` ⊋ natural
data) applies on *all* strata and is the reason no computational scan settles this.

## Files
- `kerG_reduction.py` — verifies `R⊆ker(G)`, `R=ker(G)⟺rad=0`, and the stratum/nondeg breakdown.
- `m5_relations.py` / `M5_relations_README.md` — completeness lemma + the ruled-out shortcuts.
- `m4_cochain.py` — the corrected arity-5 Arf test (`Arf(Q₅)≈0`, no escape; case (2) evidence).
