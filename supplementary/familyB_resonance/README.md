# Family-B resonance (Paper XXII Outlook Q1 / item 22): there is none

Paper XXII split contextuality configurations into family A (all-pairwise $K_N$, the
anticommutation/Maslov tower, ceiling $H^3$ at the pentagram) and family B
(bipartite/triangle-free, the central-extension class — the Mermin–Peres square). Its
Outlook asks: **does the bipartite family have its own resonance — a larger $K_{m,n}$ whose
central-extension class reaches degree 3?**

## Answer: no — family B is the floor of family A's tower, not a parallel tower

The clique criterion (Paper XXII Thm: family-A ceiling $=\min(\omega(G)-2,3)$, $\omega(G)$ the
incidence clique number) already contains the answer, because a **complete $r$-partite graph
has clique number exactly $r$**:

| configuration | parts $r$ | $\omega$ | ceiling $\min(\omega{-}2,3)$ |
|---|---|---|---|
| $K_{3,3}$ Mermin square | 2 | 2 | none (family B) |
| $K_{4,4}$, $K_{9,9}$, any bigger grid | 2 | 2 | **none — still family B** |
| $K_{3,3,3}$ tripartite | 3 | 3 | $H^1$ |
| $K_{2,2,2,2}$ 4-partite | 4 | 4 | $H^2$ |
| $K_5=K_{1,1,1,1,1}$ (pentagram) | 5 | 5 | $H^3$ |
| 6-partite ($\ge K_6$) | $\ge6$ | $\ge6$ | $H^3$ (capped — item 19/21) |

- **Growing a bipartite $K_{m,n}$ keeps $r=2$**, so the ceiling stays 0 for *every* grid size.
  A bipartite incidence is triangle-free = a **1-dimensional** clique complex for all $(m,n)$
  ($b_1=(m-1)(n-1)$, $H^{\ge2}=0$) — it can never climb.
- **The only way to raise the ceiling is to add context-classes** (complete $r$-partite), but
  $\omega=r$ is governed by the *same* clique criterion — i.e. **family A**. It tops at $H^3$
  when $r=5$, and the complete 5-partite graph with singleton parts *is the pentagram*
  $K_5=K_{1,1,1,1,1}$. (The $\min(\cdot,3)$ cap at $r\ge6$ is the arity ceiling, item 19/21.)
- **The family-B class is $\omega\in H^2$** (the Heisenberg central-extension class), a single
  $\pm I$ product bit; the only natural ascent to degree 3 is the Steenrod square
  $\mathrm{Sq}^1\!:H^2\to H^3$, and $\mathrm{Sq}^1\omega=n_a$ is the **family-A** class
  (Direction D; `bockstein/`, `twistor_cp/`).

**So "two families" is one tower with family B as its $\omega=2$ floor, joined to family A by
$\mathrm{Sq}^1$. Outlook Q1 (a family-B resonance) dissolves into Outlook Q2 (the $A\!\leftrightarrow\!B$
comparison map, item 23): the family-B $\to$ degree-3 ascent *is* the unification, not a bigger
grid.**

## Computed (`familyB.py`, no deps)

- **Part 1** — complete $r$-partite clique numbers ($=r$) through the clique criterion: the
  table above; bipartite never climbs, the tower tops at the pentagram.
- **Part 2** — the Mermin–Peres square realized as 6 Lagrangians in $\mathrm{Sp}(4,\mathbb F_2)$:
  all 6 isotropic planes; rows/cols pairwise transverse; incidence $=K_{3,3}$ (9 edges),
  triangle-free ($\omega=2$); every context-triple has a transverse pair (so $\mu,\mathbf a$
  are *undefined* — no family-A datum); context products $[+I,+I,+I,+I,+I,-I]$, global $=-I$
  (the central-extension obstruction), verified by explicit $4\times4$ Pauli matrices.
- **Part 3** — bipartite 1-dimensionality ($b_1=(m-1)(n-1)$, $H^{\ge2}=0$).
- **Part 4** — the $\mathrm{Sq}^1$ ascent $\omega\mapsto n_a$ (family A).

## Files
- `familyB.py` — the four parts above. Pure Python (F₂ symplectic + $4\times4$ Pauli matrices).
