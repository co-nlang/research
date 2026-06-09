# Paper XX supplementary — H³ opens at n≥5

Computational backing for Paper XX: the Maslov 2-cochain μ on the 4-simplex
boundary ∂Δ⁴ satisfies **na=δμ at n=4** (H³=0, rigidity exact) and
**na≠δμ generically at n≥5** (H³ opens). The rank-parity lemma proves
**μ≡1 ⟺ n even**, verified here for n=4,5,6.

## Scripts

| Script | Establishes |
|---|---|
| `nerve_cochain.py` | Experiment 1: nerve hollowness (∩ of all 5 Lagrangians = 0, 360/360); N_anti parity split (n=4: all even; n=5: 238/360 even); **na=δμ at n=4 (360/360)** and na≠δμ at n=5 (336/360). |
| `n4_cocycle.py` | μ distribution and δμ-nonzero rate: n=4 μ≡1 (all triples), δμ=0 always; n=5 μ varies (1664/2400 triples μ=1), δμ≠0 in 336 configs. |
| `mu_rank_parity.py` | **Rank-parity periodicity**: proper triple sampling for n=4,5,6; confirms μ≡1 for n even (4: 300/300, 6: 200/200) and μ varies for n odd (5: ~70% μ=1). |

## Run

```
python3 nerve_cochain.py
python3 n4_cocycle.py
python3 mu_rank_parity.py
```

No arguments — parameters and seeds are hardcoded (seeds `1000+7s` for
`nerve_cochain.py` and `n4_cocycle.py`; fixed seeds for `mu_rank_parity.py`).
Pure Python 3, no dependencies.
