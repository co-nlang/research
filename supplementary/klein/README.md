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

## Step 2 — the hinge tightened to a theorem (`klein_bitangents.py`)

The size-28 match is upgraded to an **explicit $GL(3,2)$-equivariant bijection**. The 28
bitangents of a genus-3 curve are its 28 **odd theta characteristics** = quadratic
refinements $Q$ of $\omega$ with $\mathrm{Arf}(Q)=1$ (classical). Refinements form a torsor:
fix the even form $q_0(x,z)=x\!\cdot\!z$; every refinement is $Q_v(u)=q_0(u)+\omega(v,u)$
for a unique $v$, with $\mathrm{Arf}(Q_v)=q_0(v)$. Hence

$$\text{odd theta characteristics} \;\longleftrightarrow\; \{v: q_0(v)=1\} \;=\;\text{the 28 anti-flags},
\qquad v\mapsto Q_v,$$

and $v\mapsto Q_v$ is **$GL(3,2)$-equivariant because $GL(3,2)$ preserves $q_0$** (verified
exhaustively: all 168 $g$, all 28 $v$). Point-stabilizer $=S_3$ (order 6), the bitangent
stabilizer in $PSL(2,7)$.

**The embedding is forced, not chosen.** The Klein quartic acts on $J[2]=\mathbb F_2^6$
(Weil pairing $=\omega$) by a faithful 6-dim symplectic $\mathbb F_2$-rep. The $\mathbb F_2$-
irreps of $GL(3,2)$ are $1,3,3',8$; the only faithful 6-dim self-dual symplectic one is
$3\oplus3'$ = the Siegel/Levi embedding used here. So the curve's $J[2]$-embedding and ours
coincide up to conjugacy — the comparison is representation-theoretically forced.

$\Rightarrow$ **the step-1 size-28 orbit IS the 28 bitangents of the Klein quartic, as
$PSL(2,7)$-sets** (a natural isomorphism, now rigorous).

## Step 3 — the $H^1$-level class $[f_3]$ and the transgression $\Phi_3$ (`klein_h1_theta.py`)

$H^1$-level data = theta characteristics (spin structures), the $H^1(X;\mathbb F_2)$-torsor.
Under $GL(3,2)$ they split:
- **odd: 28** (the bitangents, step 2);
- **even: 36 = 1 + 7 + 7 + 21**, and the size-1 orbit is the **unique $GL(3,2)$-fixed** theta
  characteristic $q_0 = x\cdot z$.

So $[f_3] := q_0$ — the framework's standard quadratic refinement (the APP_06 "i-phase"
datum) is the **Klein quartic's canonical $PSL(2,7)$-invariant spin structure**, the unique
invariant at this level.

**Transgression $\Phi_3$**, verified: the polarization of $q_0$ is exactly $\omega$
($q_0(u{+}w)+q_0(u)+q_0(w)=\omega(u,w)$ for all $u,w$), and $\omega$ is $GL(3,2)$-invariant
(the Weil pairing on $H^1(X(7);\mathbb F_2)$). With $\mathrm{Sq}^1\omega = n_a$ (Direction-D,
`paper22/d_bridge.py`), the spiral
$$q_0 \;\xrightarrow{\text{polarize}}\; \omega \;\xrightarrow{\mathrm{Sq}^1}\; n_a$$
is **$PSL(2,7)$-equivariant, based at the canonical theta characteristic $q_0$**:
$[f_3]=q_0$ ($H^1$ / spin) → $\omega$ ($H^2$, family B, Weil pairing) → $n_a$ ($H^3$, family
A). **The Klein backlog line meets Direction D:** the framework's self-representing
obstruction tower (the Yoneda reading of D) sits inside the Klein quartic's 168-symmetry.

## What this is and isn't

- ✅ **Rigorous:** the 168-action on $W(5,2)$, the iso to $PSL(2,7)$, the $7{+}7{+}21{+}28$
  decomposition; (step 2) the explicit $G$-equivariant bijection 28-orbit $\cong$ 28 odd
  theta characteristics $=$ 28 bitangents, embedding forced by rep theory; (step 3) the
  even-theta decomposition $1{+}7{+}7{+}21$, $[f_3]=q_0$ the unique invariant spin structure,
  and the polarization $q_0\to\omega$.
- ⟶ **Interpretive (flagged):** "$H^1$-level class" = the theta-characteristic / spin-structure
  torsor (the natural $H^1(X;\mathbb F_2)$ datum). If Paper IX's $[f_3]$ denotes a different
  specific class, this is the canonical invariant at this level — cross-check against
  Paper IX/VIII's $\Phi$.
- 🔭 **The reach (the Ramanujan end):** $X(7)$ is the level-7 modular curve with **24 cusps**
  ($168/24=7$); the $\tau$ connection runs through the "24" ($\Delta=\eta^{24}$, weight 12)
  and mock-modular signatures. That end is genuine analytic number theory, not a quick
  computation; the near-term computable targets are (a) the $GL(3,2)$-stabilised $H^1$ class
  $[f_3]$, and (b) the 3-qubit transgression $\Phi_3$.

## Files
- `klein_168_bridge.py` — the 168-action, $PSL(2,7)$ identification, orbit decomposition.
- `klein_bitangents.py` — the explicit $G$-equivariant bijection 28-orbit $\cong$ bitangents.
- `klein_h1_theta.py` — theta/spin decomposition, $[f_3]=q_0$ invariant, the $\Phi_3$ spiral.
