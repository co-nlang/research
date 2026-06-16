# Backlog: Klein quartic / Ramanujan — step 1, the 168-group bridge

Companion to `RESEARCH_FRONTIER.md` item 12 / Paper VIII §7 / Paper IX. Establishes the
*substrate side* of the chain
$$W(5,\mathbb F_2)\ \longrightarrow\ GL(3,\mathbb F_2)\cong PSL(2,7)\ \longrightarrow\
\text{Klein quartic } X(7)\ \longrightarrow\ \text{(level-7 modular / Ramanujan }\tau).$$

## Result (`klein_168_bridge.py`, pure F2, reproducible)

$GL(3,\mathbb F_2)$ — the automorphism group of the Fano plane, and the unique simple
group of order **168** — embeds in $\mathrm{Sp}(6,\mathbb F_2)$ (Siegel/Levi:
$x\mapsto gx,\ z\mapsto (g^{-1})^{\!\top}z$), acting faithfully and symplectically on the
3-qubit substrate. Verified: $|G|=168$; symplectic; **2-transitive on the 7 Fano points**;
**perfect** ($G=[G,G]$) — hence $G$ is the unique simple group of order 168,
$\;GL(3,\mathbb F_2)\cong PSL(2,7)=\mathrm{Aut}(X(7))$.

**Orbit decomposition of the 63 three-qubit Pauli classes** (points of $W(5,2)$):

| orbit size | stabilizer order | meaning |
|---|---|---|
| 7  | 24 | Fano plane $PG(2,2)$ — the invariant isotropic Lagrangian (Paper IX) |
| 7  | 24 | dual Fano $V^*$ |
| 21 | 8  | flags (incident point–line pairs of the Fano plane) |
| **28** | **6** | **anti-flags ⟷ the 28 bitangents of the Klein quartic** |

$7+7+21+28 = 63$. ✓

## The hinge (honest)

The size-**28** orbit is the concrete bridge: the 3-qubit Pauli geometry carries, as a
$GL(3,2)$-orbit, a 28-point $PSL(2,7)$-set with point-stabilizer of order 6 — exactly the
profile of the **28 bitangents of the Klein quartic** ($PSL(2,7)$ acts on them with
stabilizer $S_3$, order 6). Same group, same orbit size, same stabilizer order $\Rightarrow$
the two are almost certainly the *same* $PSL(2,7)$-set; a full proof matches the permutation
characters (next). Likewise $7$ = Fano = the curve's $PSL(2,7)$-action on the Fano plane.

So this is not a numerical coincidence dressed up — it is the same exceptional 168-symmetry,
realised on the framework's substrate, carrying the Klein quartic's defining combinatorics.

## What this is and isn't

- ✅ **Rigorous:** the 168-action on $W(5,2)$, the iso to $PSL(2,7)$, the $7{+}7{+}21{+}28$
  decomposition, the 28-orbit's stabilizer order 6.
- ⟶ **Strong but to be tightened:** "28-orbit = the 28 bitangents" as an *isomorphism of
  $PSL(2,7)$-sets* (match permutation characters / a $G$-equivariant bijection to the
  bitangents).
- 🔭 **The reach (the Ramanujan end):** $X(7)$ is the level-7 modular curve with **24 cusps**
  ($168/24=7$); the $\tau$ connection runs through the "24" ($\Delta=\eta^{24}$, weight 12)
  and mock-modular signatures. That end is genuine analytic number theory, not a quick
  computation; the near-term computable targets are (a) the $GL(3,2)$-stabilised $H^1$ class
  $[f_3]$, and (b) the 3-qubit transgression $\Phi_3$.

## Files
- `klein_168_bridge.py` — the 168-action, $PSL(2,7)$ identification, orbit decomposition.
