# Paper XXI supplementary — H³ master theorem and even/odd dichotomy

Computational backing for Paper XXI: the master rigidity theorem
(**$N_{\mathrm{anti}}=10$ universally iff $n=4$**) and the even/odd carrier
dichotomy. Four scripts cover Part~A exclusivity (B1/B2 failure at $n\ge5$),
constructive spread-stabilisation, and even-$n$ equidistribution.

## Scripts

| Script | Establishes |
|---|---|
| `partA_exclusivity.py` | Part~A exclusivity: samples proper $K_4$-matchings and counts commuting pairs per matching at $n=3,4,5,6$. **n=4: universal {1:300}**; n=3: bimodal {0,3}; n≥5: full spread with B1-fail (≥2 comm) and B2-fail (0 comm) witnesses. Extracts and verifies the n=5 B1-fail witness explicitly ($S$ isotropic dim~4, $S^\perp\supsetneq S$, escaping rays in $S^\perp\setminus S$). |
| `partA_construction.py` | **Spread-stabilisation lemma**: takes $N_\mathrm{anti}$-odd witnesses at $n=5$ ($N_\mathrm{anti}=9$) and $n=6$ ($N_\mathrm{anti}=11$), stabilises by appending 5 pairwise-transverse Lagrangians in $\mathrm{Sp}(4,\mathbb{F}_2)$, and confirms $N_\mathrm{anti}$ is preserved at dims $n=7,8,9,10$. Closes the $n\ge5$ direction constructively for all $n\ge5$. |
| `n6_periodicity.py` | Even-$n$ equidistribution probe at $n=6$: samples proper $K_5$s and records per-matching $n_a$ distribution ($\approx9\%/32\%/45\%/14\%$ for counts 0/1/2/3) and $N_\mathrm{anti}$-parity split ($\approx50/50$). |
| `n8_confirm.py` | Confirms $n$-independence of even-$n$ distribution at $n=8$: per-matching $n_a$ distribution ($\approx12\%/33\%/43\%/12\%$), near-identical to $n=6$, supporting the equidistribution conjecture. |

## Run

```
python3 partA_exclusivity.py
python3 partA_construction.py
python3 n6_periodicity.py
python3 n8_confirm.py
```

No arguments — parameters and seeds are hardcoded.
Pure Python 3, no dependencies.
