# Paper XXII supplementary — the arity–resonance ceiling

Computational backing for Paper XXII: the **arity–resonance principle**
(an arity-$a$ datum is an $(a-1)$-cochain, resonant with $K_{a+1}$), the
**truncation** of the Pauli contextuality obstruction at $H^3$, the
**incidence-clique criterion** for the cohomological ceiling, and the
**Mermin–Peres square** as a second (central-extension) family. Two further
scripts probe the Direction-D unification discussed in the outlook.

## Scripts

| Script | Establishes |
|---|---|
| `resonance_tower.py` | The **$K_4/H^2$ Maslov rung**: the Maslov $H^2$ class $\langle\mu,[S^2]\rangle$ over proper $K_4$ at $n=3,4,5,6$. **Rigid (0) at $n=3,4,6$, opens (~50/50) only at odd $n\ge5$** — the resonance tower's lower rung, with $n$-dependence from the rank-parity lemma. |
| `k6_truncation.py` | **Truncation at $H^3$**: proper $K_6$ exist for $n=4,5,6$ (symmetric-matrix chart); the degree-4 assembly $\mathbf c_m=N_\mathrm{anti}(\text{face }m)$ satisfies $\sum_m\mathbf c_m\equiv0$ ($\mathbf c=\delta\mathbf a$ exact) so the $H^4$ class vanishes universally, while the six face-classes realise all $2^5$ even-weight patterns (maximally free, $\sum=0$). |
| `clique_criterion.py` | The **incidence-clique ceiling** $\min(\omega(G)-2,3)$: computes the clique number $\omega$ of the incidence graph for the Mermin square ($\omega=2$, family-A trivial), proper $K_4$ ($\omega=4\to H^2$), proper $K_5$ ($\omega=5\to H^3$, resonance). |
| `mermin_square.py` | The **Mermin–Peres square = family B**: realises the $3\times3$ magic square as six Lagrangians in $\mathrm{Sp}(4,\mathbb{F}_2)$, verifies bipartite $K_{3,3}$ incidence (9 rays), shows every context-triple has a transverse pair (Maslov/anticommutation undefined), and computes the $\pm I$ sign obstruction (product $=-I$, contextual). |
| `geometric_route.py` | **Negative result** for the D bridge: the cup-1 square $\mu\cup_1\mu$ ("$\mathrm{Sq}^1$ of the Maslov cochain") does *not* reproduce $N_\mathrm{anti}\bmod2$ (n=5: 365/640 ≈ chance), because $\mu$ is not a cocycle off the resonance. Rules out the nerve-side shortcut to the unification. |
| `d_bridge.py` | The **algebraic skeleton** of the D bridge: in $H^*(V;\mathbb{F}_2)=\mathbb{F}_2[x_1,\dots,x_{2n}]$, computes the transgression class $\omega=\sum_i x_i x_{i+n}$ (family B) and $\mathrm{Sq}^1\omega=\sum_i(x_i^2x_{i+n}+x_ix_{i+n}^2)\in H^3(V)$ (the family-A source candidate), confirming it is nonzero. |
| `nerve_cochain.py` | Shared helper (from Paper XX/XXI): proper-$K_5$ generation, symplectic form, Maslov triple bit. Imported by `resonance_tower`, `clique_criterion`, `geometric_route`. |

## Run

```
python3 resonance_tower.py
python3 k6_truncation.py
python3 clique_criterion.py
python3 mermin_square.py
python3 geometric_route.py
python3 d_bridge.py
```

No arguments — parameters and seeds are hardcoded.
Pure Python 3, no dependencies.
