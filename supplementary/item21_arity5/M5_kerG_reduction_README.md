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
`G`*, so `(G,R)=(G,ker G)` and **every arity-5 invariant is a function of the `ω`-Gram alone** — the
nondegenerate-stratum invariant ring is `ω`-generated. So any exotic arity-5 invariant must live in
**one of two places**:
1. an `ω`-Gram-function on the **nondegenerate** stratum (all of `n=4`; ~20% at `n≥5`); or
2. the **radical** data `rad(ω|_W)` on a **degenerate** stratum (the bulk at `n≥5`).

## Why this matters: case (2) IS Paper XIX's modulus

`rad(ω|_W)` is **Paper XIX's order parameter** for the `n≥5` modulus. So the reduction says: item 21's
`n≥5` exotic content lives in *exactly* the radical/modulus data XIX already isolated. The `n`-pattern
matches: at `n=4` the stratum is 100% nondegenerate (`rad=0`) → purely `ω`-generated → no modulus, and
item 21 holds via the `ω`-world (consistent with `n=4` settled); at `n≥5` the degenerate bulk carries
`rad(ω|_W)>0` → XIX's modulus appears → that's where the exotic could hide.

## Item 21, localized — the open core, by case

- **Case (1), `ω`-Gram-functions [CONJECTURAL, cochain-level].** Sketch toward "no `H⁴`": a single
  `ω`-Gram atom `ω(r_{ij},r_{kl})` is `≤4`-index = a `≤3`-cochain; a *sum* of such atoms indexed by the
  4-subsets of a 5-config is `δ(arity-4)` = **exact** (the M1 mechanism, proven for `N_anti`); a
  *product* of `≥2` atoms is a cup product of degree `≥6` (wrong degree for `H⁴` on `S⁴`). So no
  `ω`-Gram-function plausibly furnishes a non-exact 4-cochain — this is XXII's resonance/ceiling applied
  to the full `ω`-ring rather than just the anticommutation datum. **Not yet a proof** (the FFT for the
  `ω`-Gram ring is the gap).
- **Case (2), radical/modulus [partly handled]**. The natural radical-based exotic is the intrinsic Arf
  (XIX's candidate). The corrected M4 (`m4_cochain.py`) finds `Arf(Q₅) ≈ const 0` where defined
  (value-level, no `H⁴` escape) — first evidence the radical datum does **not** climb. A full closure
  needs the FFT for the radical data (which other radical invariants exist, and do they climb?). This is
  the genuine `n≥5` core, and it is **XIX's modulus ↔ XXII's ceiling** restated for `H⁴`.

## Net

Item 21 is reduced (value-level, verified) to: **does XIX's radical/modulus datum climb from `H³` to
`H⁴`?** — i.e. XXII's ceiling theorem applied to the radical, the bottom case (anticommutation) of
which XXII already proved and the natural radical-exotic (Arf) of which M4 finds `≈0`. The reduction
**does not close** item 21 (the two FFT gaps above remain, both cochain-level/insight-bound), but it
localizes the exotic precisely and connects item 21 to the XIX/XXII machinery rather than an
unparametrized search. **Firewall note:** the reduction is value-level/verified; every "⟹ no `H⁴`" step
is flagged cochain-level/conjectural and still requires a direct `Σ=0`/`δ`-witness or an FFT proof.

## Files
- `kerG_reduction.py` — verifies `R⊆ker(G)`, `R=ker(G)⟺rad=0`, and the stratum/nondeg breakdown.
- `m5_relations.py` / `M5_relations_README.md` — completeness lemma + the ruled-out shortcuts.
- `m4_cochain.py` — the corrected arity-5 Arf test (`Arf(Q₅)≈0`, no escape; case (2) evidence).
