# Reading Guide

Per-paper summaries and recommended reading orders for the twenty-two-paper series.

→ Back to [README.md](README.md) for the overview, quick-reference table, and DOIs.

---

## Recommended Reading Orders

### The Short Route (core theorem chain, 7 papers)

```
I → III → IV → XVII → XVIII → XXI → XXII
```

Covers: geometric phase → KS as central extension → H³ frontier → cross-context anticommutation → n=4 universality → master rigidity → arity–resonance ceiling. Skips the computational archaeology (X–XVI) and the twistor detour (VII–IX).

### The Full Route

```
I → II → III → IV → Epilogue → V → VI → VII → VIII → IX →
X → XI → XII → XIII → XIV → XV → XVI → XVII →
XVIII → XIX → XX → XXI → XXII
```

### Entry Points

- **Self-contained single paper:** Paper XVII — proves $\prod W_C = -I_8$ from scratch in 10 pages, no prerequisites. Best first taste.
- **The H³ arc only (Papers XVIII–XXII):** start at XVIII, needs only the definitions from X §2.
- **Twistor detour (VII–IX):** largely independent of X–XXII; needs I–IV.

---

## Three Arcs

The series has three natural arcs:

| Arc | Papers | Theme |
|-----|--------|-------|
| **Foundations** | I–VI + Epilogue | Build the obstruction ladder from scratch: Bohrification, geometric phases ($H^1$), KS contextuality ($H^2$), Borromean frontier ($H^3$), the EML system, necessity of $\mathbb{C}$ |
| **Twistor Bridge** | VII–IX | Googly problem as $H^2$ obstruction, the $\Phi$ functor to $\mathbb{CP}^3$, 3-qubit Fano/Klein quartic geometry |
| **Pentagram & Rigidity** | X–XXII | Mermin pentagrams in $\mathrm{Sp}(2n,\mathbb{F}_2)$: computational anatomy (X–XVI), algebraic proofs (XVII–XVIII), the $n \ge 5$ deformation (XIX–XX), master theorem (XXI), arity–resonance ceiling (XXII) |

---

## Per-Paper Summaries

### Arc I: Foundations (Papers I–VI + Epilogue)

**Paper I — *From Contextuality to Phase Cohomology***
Establishes the concrete foundation: $\check{H}^1(M, U(1))$ classifies geometric phases. Bohrification meets geometric quantization.

**Paper II — *Semiclassical Reconstruction of Riemann Surfaces from Bohrification***
Riemann surface state spaces: Bohr-Sommerfeld orbits as divisors on spectral curves.

**Paper III — *Kochen–Specker Contextuality as Central Extension***
The Peres–Mermin square and the Pauli group. KS obstruction = non-split central extension $[f] \in H^2(\bar{\mathcal{P}}_2, \mathbb{Z}/2)$.

**Paper IV — *The Cohomological Obstruction Ladder: LHS Transgression and the $H^3$ Frontier***
Introduces Borromean contextuality and bundle gerbes. The $d_2$ transgression = KS obstruction. First prediction of an $H^3$ level.

**Epilogue — *The Algebraic Logic of Geometry***
The unifying vision: the EML system, Solèr's theorem, and the $\mathcal{Q} \dashv \mathcal{B}$ adjunction. "The epilogue is a prologue to a deeper question."

**Paper V — *Observation as Functor***
LHS spectral sequence as computational engine. Conditionally unifies all obstructions via a single algebraic machine.

**Paper VI — *The Ultimate Axiom: Deriving Quantum Mechanics from the Logic of Observation***
The Solèr–Cohomology Theorem: $\mathbb{C}$ is the unique division ring permitting non-trivial continuous observation.

### Supplementary: L-S Appendices

Three companion notes connecting Lohmiller–Slotine contraction theory to the obstruction ladder:

- **L-S Note I** (companion to Paper I): Geometric phase = gauge mismatch Čech 1-cocycle.
- **L-S Note II** (companion to Paper III): PM $K_{3,3}$ flat $SU(2)$ holonomy $= -\mathbf{I}$.
- **L-S Note III** (companion to Paper IV): 16-cell $S^3$ nerve, octonionic chain-rule failure.

### Arc II: Twistor Bridge (Papers VII–IX)

**Paper VII — *Twistor Theory from the Obstruction Ladder: The Googly Problem as an $H^2$ Obstruction***
Resolves the Penrose googly problem (twistor theory's 59-year open question) as an $H^2$ obstruction. $\Phi^*([f]) = c_1(\mathcal{O}(1)) \bmod 2$ verified computationally.

**Paper VIII — *The $\Phi$ Functor and the $n$-Qubit Obstruction Ladder***
$K_{3,3}$ nerve, $\Phi = \ell \circ \tau \circ \iota^*$ transgression decomposition. MASA count $(4^n-1)(4^{n-1}-1)/3$. $\mathbb{Z}/2$-gerbe on $\mathbb{CP}^3$.

**Paper IX — *The 3-Qubit Obstruction Ladder***
$GL(3,\mathbb{F}_2) \hookrightarrow PSp(6,\mathbb{F}_2)$: Fano plane as isotropic subgeometry of $W(5,\mathbb{F}_2)$. Two non-conjugate $PSL(2,7)$ paths = two Klein quartic bridges.

### Arc III: Pentagram & Rigidity (Papers X–XXII)

**Paper X — *The Equiangular Characterization of Mermin Pentagrams***
$K_5 \Leftrightarrow$ equiangular $\Leftrightarrow$ Mermin. The 10 shared operators form a cap in $PG(5,\mathbb{F}_2)$. Collinearity is shadow, not obstruction. $G_2(2)$ acts with 4 orbits.

**Paper XI — *Quadratic Refinement and the Parity of Mermin Pentagrams***
$s(C) = (-1)^{\beta(C)/2}$. The 15 ray pairs decompose into 30 sharing ($\omega=0$) and 15 disjoint ($\omega=1$). Parity theorem $\beta_{\mathrm{sum}} \equiv 2 \pmod{4}$ verified for all 12,096 pentagrams.

**Paper XII — *The T-Vector Theorem***
$\omega(T, r) = 1$ for all rays (algebraic, $G_2(2)$-equivariant). $T$ is a symplectic characteristic element (Wu class analogy). Arf framework incompatible with $G_2(2)$ symmetry.

**Paper XIII — *The Maslov Index and the KS Obstruction***
Kashiwara triple index ≠ $\beta_{\mathrm{sum}}/2$. The $k$-profile theorem: parity determined by Lagrangian intersection profile. Orbit 4 anomaly.

**Paper XIV — *Stabilizer Algebra and the $k$-Profile Theorem***
$O_1 = \mathbb{Z}_2$, $O_{2,3,4} = S_3$ (no $\mathbb{Z}_6$). 7 $k$-profiles, 100% odd. Only 3 of 16 $h$-patterns occur. Full $\beta_{\mathrm{sum}}$ statistics: range $[-34, 30]$.

**Paper XV — *The Weil Representation and the $S_3$ Lifting Classification***
$O_3$ split, $O_2$ non-split symmetric, $O_4$ non-split asymmetric. $G_2(2)$ Lagrangian orbits: 72+63. $\beta$-cocycle refuted.

**Paper XVI — *The Weyl Product Identity***
$W_C = s(C) \cdot I_8$ for all 945 contexts. $\prod_C W_C = -I_8$ for all 12,096 pentagrams. Mod 4 structure intrinsic to Weyl algebra.

**Paper XVII — *The Cross-Context Anticommutation Theorem***
$\omega(v_{ij}, v_{kl}) = 1$ for all 15 cross-context pairs (algebraic). $\prod W_C = (-1)^{15} I_8 = -I_8$. The 15 pairs form the Petersen graph $K(5,2)$.

**Paper XVIII — *Mermin Pentagrams in $\mathrm{Sp}(8, \mathbb{F}_2)$***
$N_{\mathrm{anti}} = 10$ for all proper $K_5$ (fully algebraic via B0+B1+B2). $n = 4$ is the unique universal dimension.

**Paper XIX — *$n \ge 5$: Structure, Obstruction, and the Modulus Phenomenon***
Modulus theorem: no arity-$\le 4$ invariant classifies the $N_{\mathrm{anti}}$ fiber. Upper-bound ladder. Deterministic tail. Arf ruled out.

**Paper XX — *$H^3$ Opens at $n \ge 5$***
$n_a = \delta\mu$ at $n=4$ (rigorous). Rank-parity lemma. $[n_a] = 0$ universally iff $n = 4$. The $H^3$ class opens at $n = 3$ (all-Fano) and generic $n \ge 5$.

**Paper XXI — *$H^3$ Rigidity is Unique at $n = 4$: Master Theorem***
$N_{\mathrm{anti}} = 10$ universally $\iff n = 4$. The $2n = 8$ squeeze (B1/B2). Even/odd carrier dichotomy: $n_a$ at even $n$, $\delta\mu$ at odd $n$. Explicit witnesses $\forall n \ge 5$.

**Paper XXII — *The Arity–Resonance Ceiling: Why Pauli Contextuality Stops at $H^3$***
Arity-$a$ data $= (a{-}1)$-cochain resonant at $K_{a+1}$. Two rungs: Maslov ($K_4/H^2$) and anticommutation ($K_5/H^3$). $H^4$ truncates ($\mathbf{c} = \delta\mathbf{a}$). Ceiling = $\min(\omega(G){-}2, 3)$. Mermin–Peres square = family B (central extension, no family-A class).
