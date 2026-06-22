# Item 21 M2 — the `K₆` structural skeleton (`k6_skeleton.py`)

Extends Paper XIX's `lem:skeleton` (`K₅`/10-ray) to `K₆`/15-ray. **Status: M2 done** (the skeleton is
built and its structural facts verified; the generic stratum is identified). Results are *sampled*
(150/150/120 proper `K₆` at n=4/5/6) — "generic" = empirical, not a proof for all configs.

## Objects (15 rays `r₁..r₁₅` of a proper `K₆` in `F₂^{2n}`)

`W₆`=ray span; `G₆`=15×15 Gram, `G₆[i][j]=ω(rᵢ,rⱼ)`; `R₆={a∈F₂¹⁵:Σaᵢrᵢ=0}`;
`o₆(a)=Σ_{i<j}aᵢaⱼG₆[i][j]` (quadratic, polarization `G₆`); `ker G₆`; `ℓ₆=o₆|_{ker G₆}` (linear).

## Result 1 — the generic stratum is `(2n, 2n, 0)` (full-span, NONDEGENERATE)

| `n` | `(dim W₆, rank G₆, dim rad W₆)` distribution |
|---|---|
| 4 | `(8,8,0)`: 150/150 |
| 5 | `(10,10,0)`: 140/150, `(9,8,1)`: 10 |
| 6 | `(12,12,0)`: 97/120, `(11,10,1)`: 22, `(10,8,2)`: 1 |

The 15 rays generically **span the full `F₂^{2n}`**, so `W₆=V`, `W₆^⊥=0`, `rad W₆=0`, `rank G₆=2n`.
This is **structurally different from XIX's `K₅` generic `(8,6,2)`** (degenerate, 2-dim radical): more
rays (15 vs 10) ⟹ full span. (Once the rays span, `(2n,2n,0)` is forced — `ω` is nondegenerate on `V`.)

## Result 2 — structural skeleton facts hold at `K₆` (all 100%)

`R₆ ⊆ ker G₆`; `o₆|_{ker G₆}` linear; `dim R₆ = 15 − dim W₆`; `dim ker G₆ − dim R₆ = dim rad W₆`
(i.e. `ker G₆/R₆ ≅ rad W₆`); coisotropy `W₆^⊥ ⊆ W₆` (`⟺ dim rad W₆ = 2n − dim W₆`). All verified
150/150/120. **Consequence at the generic stratum (`rad W₆=0`): `ker G₆ = R₆`** — the Gram kernel *is*
the relation space, and `ℓ₆ = o₆|_{R₆}`.

## Result 3 (M4 preview) — intrinsic-`q` existence `⟺ o₆|_{R₆} ≡ 0`

| `n` | intrinsic-`q` exists | reading |
|---|---|---|
| 4 | **0/150 (never)** | branch **(b)** — *no* intrinsic exotic at `K₆`/`n=4` |
| 5 | 60/150 (40%) | branches (a)/(c) live |
| 6 | 37/120 (31%) | branches (a)/(c) live |

**This is the key M2→M4 hand-off.** At `n=4` an intrinsic exotic *never* exists, so M4's branch (b) is
**real, not hypothetical** — the P2 "exists-but-blind" template (XIX's arity-4 Arf-exclusion shape)
**does not lift verbatim**; `n=4` needs the `noq_odd`-style realizability/exactness route instead.
(`n=4` is anyway settled by the master theorem — no `H⁴` — so this is consistent; the *interesting*
cases are `n≥5`, where intrinsic-`q` exists ~30–40% and branches (a)/(c) must both be checked.)

## What M2 changes for the ladder

- The `K₆` skeleton is **not** a carbon copy of `K₅`: the generic geometry flips from degenerate
  coisotropic `(8,6,2)` to **nondegenerate full-span `(2n,2n,0)`**. So "intrinsic-`q` vanishing on the
  rays" is a *tighter* condition at `K₆` (a quadratic refinement of the full `ω` vanishing on 15
  spanning vectors), and it genuinely fails to exist a large fraction of the time.
- M4 must branch on intrinsic-`q` existence per the rates above; do **not** assume the arity-4 replay.

## Files
- `k6_skeleton.py` — stratum + structural-fact verification + intrinsic-`q` existence rate (n=4,5,6).
