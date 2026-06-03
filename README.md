# The Logic of Observation: A Unified Cohomological Theory of Quantum Contextuality

A Sixteen-paper series with epilogue exploring the cohomological foundations of quantum contextuality: from geometric phases to the necessity of complex numbers, extended by Paper VIII with explicit functor construction and twisted Penrose transform, Paper IX with the 3-qubit obstruction ladder and two non-conjugate Klein quartic bridges, Paper X with the equiangular characterization of Mermin pentagrams, Paper XI with the quadratic refinement proof of the parity theorem, Paper XII with the T-vector theorem and symplectic characteristic elements, Paper XIII with the Maslov index investigation, the $k$-profile theorem, and the Orbit 4 parity anomaly, Paper XIV with the stabilizer algebra classification ($O_1=\mathbb{Z}_2$, $O_{2,3,4}=S_3$), the full 12,096-pentagram $k$-profile theorem, the 3-pattern $h$-structure theorem, and the 5-minus exclusion proposition, Paper XV with the Weil representation and metaplectic lifting classification of the three non-conjugate $S_3$ stabilizers (split, non-split symmetric, non-split asymmetric), the $G_2(2)$ Lagrangian orbit structure (72+63), and the structural refutation of the Lagrangian-level $\beta$-cocycle conjecture, and Paper XVI with the Weyl Product Identity $W_C = s(C)\cdot I_8$ resolving the context-level $\beta$ identification, showing that the Kochen--Specker obstruction $\prod_C W_C = -I_8$ is a Weyl-algebra identity arising from the integer symplectic form in the Weyl commutation relation and the Fano zero-sum property.

**Author:** Zhou-Li Chen (co-nlang Research)

---

## Overview

Why does quantum mechanics require complex numbers? Why do geometric phases and Kochen–Specker contextuality arise from the same underlying structure? This series proposes a unified answer: quantum observation is governed by a **cohomological obstruction ladder**, where each rung corresponds to a deeper level of algebraic failure—from consistent phase patching ($H^1$), through non-commutativity ($H^2$), to non-associativity ($H^3$).

The series builds a bridge between three mathematical domains:
- **Quantum logic** (Bohrification topos, MASA posets)
- **Group cohomology** (Lyndon–Hochschild–Serre spectral sequence)
- **Higher geometry** (line bundles, bundle gerbes, Dixmier–Douady class)

---

## AI Collaboration Disclosure

This research project integrated various Large Language Models (LLMs) across multiple stages to enhance rigor and clarity. The author(s) maintain full accountability for the final content.

- **Theoretical Derivation:** AI was used to assist in symbolic manipulation, cross-verifying mathematical proofs, and identifying potential edge cases in formulas.
- **Development & Typesetting:** Code implementation and LaTeX structural optimization were supported by AI-assisted pair programming.
- **Language & Refinement:** Sentences were polished for academic flow and grammatical precision.
- **Simulated Peer Review:** AI agents were tasked to act as independent reviewers to provide critical feedback and identify logical gaps prior to publication.

*Models used: Gemini 3 Pro/3.1 Pro, GPT-5.3, Claude Sonnet 4.6/Opus 4.6, Kimi K2.5/K2.6, GLM-5.0, QWen 3.5 Plus, DeepSeek V4 Pro/Flash.*

---

## Repository Structure

```
research/
├── README.md
├── LICENSE                             # CC BY 4.0
├── RESEARCH_FRONTIER.md                # Toolbox & open problems
├── insight/                            # Insight Notes | Speculative thought experiment
├── papers/
│   ├── Paper1_contextuality_phase.tex
│   ├── Paper2_riemann_bohrification.tex
│   ├── Paper3_ks_central_extension.tex
│   ├── Paper4_lhs_borromean.tex
│   ├── Paper5_homological_bridge.tex
│   ├── Paper6_necessity_complex.tex
│   ├── Epilogue_algebraic_logic.tex
│   ├── LsNote_geometric_phase.tex          # L-S contraction & H¹ (Appendix to Paper I)
│   ├── LsNote_noncommutativity.tex         # L-S contraction & H² (Appendix to Paper III)
│   ├── LsNote_associativity.tex            # L-S contraction & H³ + octonionic boundary
│   ├── Paper7_twistor_googly.tex
│   ├── Paper8_explicit_construction.tex
│   ├── Paper9_obstruction_ladder.tex
│   ├── Paper10_equiangular_characterization.tex
│   ├── Paper11_quadratic_refinement.tex
│   ├── Paper12_T_vector_theorem.tex
│   ├── Paper13_maslov_index.tex
│   ├── Paper14_stabilizer_kprofile.tex
│   ├── Paper15_weil_metaplectic.tex
│   └── Paper16_weyl_product.tex
├── supplementary/
│   ├── construct_16cell/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   └── construct_16cell.py
│   ├── paper7_conj42/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── paper7_conj42.py
│   │   └── paper7_conj42_layer2.py
│   ├── paper10/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── p0_enumerate_contexts.py
│   │   ├── p1_orbit_check.py
│   │   ├── p2_typeB_analysis.py
│   │   ├── p3_sign_patterns.py
│   │   ├── p4_typeF4_analysis.py
│   │   ├── p5_ghost_pentagon.py
│   │   ├── p6_equiangular_check.py
│   │   ├── p7_ray_cap.py
│   │   ├── p8_sufficiency_check.py
│   │   ├── g2_orbits.py
│   │   └── orbit_type_lagrangian.py
│   ├── paper11/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── quadratic_refinement_v2.py
│   │   ├── decompose_omega.py
│   │   ├── prove_disjoint_omega.py
│   │   ├── verify_quadratic_identity.py
│   │   ├── omega_integer_values.py
│   │   ├── analyze_T_structure.py
│   │   ├── check_T.py
│   │   ├── check_full_identity.py
│   │   ├── check_sum_q_plus_c.py
│   │   ├── verify_conditions.py
│   │   ├── class2_characterization.py
│   │   ├── quadratic_refinement.py
│   │   └── verify_identity.py
│   ├── paper12/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── arf_candidate_search.py
│   │   ├── g2_preserves_q.py
│   │   └── t_vector_analysis.py
│   ├── paper13/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── maslov_index.py
│   │   ├── maslov_candidates.py
│   │   ├── path_a_half_symplectic_sample.py
│   │   ├── analyze_h_structure.py
│   │   └── analyze_h_correlation.py
│   ├── paper14/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── stabilizer_algebra.py
│   │   └── beta_distribution.py
│   ├── paper15/
│   │   ├── LICENSE                         # MIT
│   │   ├── README.md
│   │   ├── metaplectic_lift.py
│   │   └── weil_cocycle.py
│   └── paper16/
│       ├── LICENSE                         # MIT
│       └── displacement_operator.py
```

---

## Reading Guide

### Recommended Order

```
Paper I → Paper II → Paper III → Paper IV → Epilogue → Paper V → Paper VI → Paper VII → Paper VIII → Paper IX → Paper X → Paper XI → Paper XII → Paper XIII → Paper XIV → Paper XV → Paper XVI
```

- **Papers I–III** establish the concrete foundation: geometric phases, Riemann surfaces, and the Kochen–Specker obstruction.
- **Paper IV** introduces the $H^3$ frontier (Borromean contextuality) and the Lyndon–Hochschild–Serre transgression.
- **The Epilogue** provides the unifying vision (EML system, Solèr's theorem, obstruction ladder).
- **Papers V–VI** ascend to the categorical abstraction and prove the necessity of $\mathbb{C}$.
- **Paper VII** resolves the Penrose googly problem (twistor theory's 59-year open question) as an $H^2$ obstruction, with $\Phi^*([f]) = c_1(\mathcal{O}(1)) \bmod 2$ verified computationally.
- **Paper VIII** completes the explicit construction of the $\Phi$ functor, identifies the PM nerve as $K_{3,3}$ (not a 2-simplex), decomposes $\Phi$ as a transgression $\ell \circ \tau \circ \iota^*$, and formulates the twisted Penrose transform via $\Z/2$-gerbe as an open problem.
- **Paper IX** steps up to 3 qubits: the hyperbolic embedding $GL(3,\mathbb{F}_2) \hookrightarrow PSp(6,\mathbb{F}_2)$ realizes the Fano plane as an isotropic subgeometry of $W(5,\mathbb{F}_2)$, and reveals two non-conjugate $PSL(2,7)$ subgroups (hyperbolic vs.\ $G_2(2)$ path) — two distinct Klein quartic bridges in $PSp(6,\mathbb{F}_2)$.
- **Paper X** proves that every Mermin pentagram has equiangular Lagrangian configuration ($\dim(L_i \cap L_j) = 1$ for all 10 pairs), and conversely every equiangular $K_5$ is a Mermin pentagram. The 10 shared operators form a 10-point cap in $PG(5,\mathbb{F}_2)$. Collinearity in the Fano plane is shown to be a shadow, not the obstruction. $G_2(2)$ acts with 4 orbits revealing a 2-class geometric structure.
- **Paper XI** provides the $\beta$-formula for context signs ($s(C) = (-1)^{\beta(C)/2}$ where $\beta$ is the integer symplectic form sum) and a geometric proof of the parity theorem. The 45 ray pairs decompose into 30 sharing ($\omega=0$, Lagrangian) and 15 disjoint ($\omega=1$, proven algebraically via cap property + Lagrangian self-orthogonality). The parity theorem $\beta_{\text{sum}} \equiv 2 \pmod{4}$ is verified computationally for all 12,096 pentagrams.
- **Paper XII** proves the T-vector theorem: for any equiangular pentagram, $T = \sum r_{ij}$ satisfies $\omega(T, r) = 1$ for all rays (algebraic, $G_2(2)$-equivariant). $T$ is interpreted as a symplectic characteristic element, analogous to the Wu class in algebraic topology. The Arf invariant framework for the KS obstruction is shown to be incompatible with $G_2(2)$ symmetry: $G_2(2)$ acts transitively on $\mathbb{F}_2^6 \setminus \{0\}$ and no $G_2(2)$-invariant quadratic form exists. The mod 4 lifting from $\omega(T,r)=1$ to $\beta_{\text{sum}} \equiv 2 \pmod{4}$ remains open.
- **Paper XIII** investigates the Maslov index as a potential geometric explanation for the parity theorem. The Kashiwara triple index is shown to $\emph{not}$ match $\beta_{\text{sum}}/2$ (range mismatch: $\{-2,\ldots,+2\}$ vs.\ $\{-13,\ldots,+9\}$). The $k$-profile theorem is established: the parity $\sum h_i \pmod{2}$ is completely determined by the Lagrangian $V$-intersection profile, with all 7 occurring profiles giving odd parity. The $V$-contribution to $\beta_{\text{sum}}$ is shown to be individually unconstrained mod 4, establishing that parity is holistic. $G_2(2)$-equivariant invariants cannot distinguish the two orbit classes, and Orbit 4 exhibits a distinct parity anomaly.
- **Paper XIV** completes the computational foundations: the $k$-profile theorem is verified for all 12,096 pentagrams (7 types, 100\% odd parity). The stabilizer classification reveals $O_1=\mathbb{Z}_2$ and $O_{2,3,4}=S_3$ — no cyclic $\mathbb{Z}_6$ stabilizer exists. The $h$-pattern structure is remarkably constrained: only 3 of 16 theoretically possible patterns occur. The 5-minus exclusion is proven algebraically for $(7,1,1,1,1)$ and computationally for $(3,3,3,0,0)$. The Orbit 4 anomaly is shown $\emph{not}$ to be explained by stabilizer algebra type, pointing to non-conjugate $S_3$ embeddings in $G_2(2)$ as the true source. Full $\beta_{\text{sum}}$ statistics: range $[-34,30]$, mean $-2.5$ (negative bias).
- **Paper XV** applies the Weil representation of $Sp(6,\mathbb{F}_2)$ on $\mathbb{C}^8$ to the metaplectic lifting problem. The three non-conjugate $S_3$ stabilizers lift differently: $O_3$ splits ($\widetilde{S}_3 \cong S_3$), $O_2$ is non-split symmetric (both order-3 elements acquire metaplectic order 6), and $O_4$ is non-split asymmetric (mixed orders 6 and 3). The $O_3$ split correlates with its unique 25\%/25\%/25\% $k$-profile uniformity. The $O_4$ asymmetric lift is the first structural difference at the group-theoretic level that may explain the Orbit 4 parity anomaly. $G_2(2)$ acts on the 135 Lagrangians in two orbits (72+63). The Lagrangian-level $\beta$-cocycle conjecture is refuted (48.8\% match); 81/135 Lagrangians have varying $h$-values across contexts, proving $\beta(C)$ is a context-level invariant.
- **Paper XVI** resolves the context-level $\beta$ identification problem via the Weyl Product Identity: $W_C = W(v_1)W(v_2)W(v_3)W(v_4) = s(C)\cdot I_8$ for all 945 contexts, where $s(C) = (-1)^{\beta(C)/2}$. The proof combines the exact Weyl commutation relation $W(v)W(w) = (-i)^{\omega_{\mathrm{int}}(v,w)}W(v+w)$ (integer, not mod 2) with the Fano zero-sum property $v_1\oplus v_2\oplus v_3\oplus v_4 = 0$. The KS obstruction follows: $\prod_C W_C = -I_8$ for all 12,096 pentagrams, recovering $\beta_{\mathrm{sum}} \equiv 2 \pmod 4$ as a Weyl-algebra identity. The mod 4 structure is intrinsic to the Weyl algebra, not a lift of any mod-2 phenomenon.

### Supplementary L-S Appendices

Three companion notes connect Lohmiller–Slotine contraction theory to the obstruction ladder. Each provides a dynamical reinterpretation of a cohomological level, framed as a companion appendix to the relevant paper:

- **LsNote\_geometric\_phase** (companion to Paper I): Liouville's theorem proves no global contraction metric exists for the Aharonov–Bohm system; the gauge mismatch Čech 1-cocycle equals the geometric phase.
- **LsNote\_noncommutativity** (companion to Paper III): The Peres–Mermin $K_{3,3}$ nerve carries a flat $SU(2)$ connection whose 4-cycle holonomy is $-\mathbf{I}$, proving the Kochen–Specker obstruction equals the central extension class.
- **LsNote\_associativity** (companion to Paper IV): The 16-cell $S^3$ nerve carries a global Čech 3-cocycle (conjectured pairing $-1$); octonionic dynamics break the chain rule, proving L-S theory inapplicable for $\mathbb{O}$.

### Quick Reference

| # | Title | Focus | Key Result |
|---|-------|-------|------------|
| I | *From Contextuality to Phase Cohomology: A Computable Bridge Between Bohrification and Geometric Quantization* | Bohrification ↔ geometric quantization | $\check{H}^1(M, U(1))$ classifies geometric phases |
| II | *Semiclassical Reconstruction of Riemann Surfaces from Bohrification* | Riemann surface state spaces | Bohr-Sommerfeld orbits as divisors on spectral curves |
| III | *Kochen–Specker Contextuality as Central Extension: The Peres-Mermin Square and the Pauli Group* | Peres–Mermin square & Pauli group | KS obstruction = non-split central extension $[f] \in H^2(\bar{\mathcal{P}}_2, \mathbb{Z}/2)$ |
| IV | *The Cohomological Obstruction Ladder: Lyndon–Hochschild–Serre Transgression and the $H^3$ Frontier* | Borromean contextuality & bundle gerbes | $N \geq 5$ qubit threshold; $d_2$ transgression = KS obstruction |
| Epilogue | *The Algebraic Logic of Geometry* | EML system & Solèr's theorem | $\mathcal{Q} \dashv \mathcal{B}$ adjunction and the obstruction ladder |
| V | *Observation as Functor: The Adjunction of Quantum and Classical* | LHS spectral sequence as computational engine | Conditionally unifies all obstructions via a single algebraic machine |
| VI | *The Ultimate Axiom: Deriving Quantum Mechanics from the Logic of Observation* | Solèr-Cohomology Theorem | $\mathbb{C}$ is the unique division ring permitting non-trivial continuous observation |
| VII | *Twistor Theory from the Obstruction Ladder: The Googly Problem as an H2 Obstruction* | Peres–Mermin → $\mathbb{CP}^3$ | Googly problem = $H^2$ obstruction; $\Phi^*([f]) = c_1(\mathcal{O}(1)) \bmod 2$ verified |
| VIII | *The $\Phi$ Functor and the $n$-Qubit Obstruction Ladder: Explicit Transgression and Twisted Penrose Transform* | $K_{3,3}$ nerve, transgression, gerbe | $\Phi = \ell \circ \tau \circ \iota^*$; MASA count $(4^n-1)(4^{n-1}-1)/3$; $\Z/2$-gerbe classified by $[e] \in H^2(\mathbb{CP}^3,\Z/2)$ |
| IX | *The 3-Qubit Obstruction Ladder: Hyperbolic Embedding, Mermin Pentagram, and Two Klein Quartic Bridges* | $W(5,\mathbb{F}_2)$, Fano isotropic subgeometry, $G_2(2)$ | $GL(3,\mathbb{F}_2) \hookrightarrow PSp(6,\mathbb{F}_2)$; two non-conjugate $PSL(2,7)$ paths; $[f_3] \in H^1(K_5,\mathcal{F})$ |
| X | *The Equiangular Characterization of Mermin Pentagrams: Symplectic Embedding, 10-Ray Cap, and the Failure of the Collinearity–Obstruction Dictionary* | Equiangular Lagrangian config, 10-ray cap, $G_2(2)$ orbits | $K_5 \Leftrightarrow$ equiangular $\Leftrightarrow$ Mermin; collinearity is shadow; 4 orbits, 2-class structure |
| XI | *Quadratic Refinement and the Parity of Mermin Pentagrams: The $\beta$-Formula, Geometric Decomposition, and the Kochen–Specker Obstruction from Equiangular Geometry* | $\beta$-formula, $\omega$ decomposition, parity theorem | $s(C)=(-1)^{\beta/2}$ (0/945); $\omega_{\text{disjoint}}=1$ (algebraic); $\beta_{\text{sum}}\equiv 2\pmod{4}$ (computational) |
| XII | *The T-Vector Theorem: Symplectic Characteristic Elements and the Kochen–Specker Obstruction* | T-vector theorem, symplectic characteristic element, Arf incompatibility | $\omega(T,r)=1$ (algebraic); Wu class analogy; no $G_2(2)$-invariant quadratic form; mod 4 lifting open |
| XIII | *The Maslov Index and the Kochen–Specker Obstruction: Negative Results, the $k$-Profile Theorem, and Orbit 4 Anomaly* | Maslov index, Kashiwara triple index, $k$-profile theorem, orbit structure | Kashiwara $\neq$ $\beta_{\text{sum}}/2$; $\beta_{\text{sum}} \equiv 2\pmod{4}$ ordering-invariant; 7 $k$-profiles all give odd parity; $G_2(2)$-equivariant invariants cannot distinguish orbit classes; Orbit 4 parity anomaly |
| XIV | *Stabilizer Algebra and the $k$-Profile Theorem for Mermin Pentagrams* | Stabilizer classification, $k$-profile theorem, $h$-pattern structure, $\beta_{\text{sum}}$ statistics | $O_1=\mathbb{Z}_2$, $O_{2,3,4}=S_3$ (no $\mathbb{Z}_6$); 7 $k$-profiles, 100\% odd (12{,}096); only 3 $h$-patterns; 5-minus exclusion; $\beta_{\text{sum}}\in[-34,30]$ |
| XV | *The Weil Representation and the $S_3$ Lifting Classification for Mermin Pentagrams* | Weil representation, metaplectic cocycle, $S_3$ lifting, Lagrangian orbits | $O_3$ split, $O_2$ non-split symmetric, $O_4$ non-split asymmetric; $G_2(2)$ Lagrangian orbits: 72+63; $\beta$-cocycle refuted (context-level invariant) |
| XVI | *The Weyl Product Identity and the Algebraic Origin of the Kochen--Specker Obstruction* | Weyl algebra, Fano zero-sum, context-level $\beta$, KS as Weyl identity | $W_C = s(C)\cdot I_8$ (945/945); $\prod_C W_C = -I_8$ (12,096/12,096); mod 4 from Weyl algebra, not mod-2 lift |
| L-S I | *L-S Contraction and the Cohomological Origin of Geometric Phases* | Liouville vs contraction (A-B effect) | $\check{H}^1$ 1-cocycle = geometric phase holonomy |
| L-S II | *L-S Contraction and the Cohomological Origin of Non-Commutativity* | 4-cycle holonomy in PM square | $-\mathbf{I}$ = central extension class $[f]$ |
| L-S III | *L-S Contraction and the Boundary of Applicability: $H^3$, the 16-Cell, and Non-Associative Algebra* | 16-cell $S^3$ nerve + $\mathbb{O}$ chain rule failure | $H^3$ pairing conjecture; $\mathbb{O}$-dynamics incompatible with L-S |

---

## The Obstruction Ladder

```
Level 0 (Foundation):  H¹  —  E_∞^{1,0} survivors     —  Geometric phases (Aharonov–Bohm, Berry)
Level 1 (Obstruction): H²  —  d₂ transgression         —  Kochen–Specker contextuality
Level 2 (Obstruction): H³  —  d₃ higher differential   —  Borromean non-associativity
```

The distinction is crucial: **geometric phases are stable features** that survive the entire spectral sequence filtration ($E_\infty$ page). **Quantum anomalies are obstructions** measured by the differentials ($d_2, d_3$) that measure the cost of forcing classical logic onto quantum systems.

---

## [`RESEARCH_FRONTIER.md`](RESEARCH_FRONTIER.md)

A candid inventory of the mathematical machinery powering this series and the open problems that remain. Includes:

- **Part I: The Mathematical Toolbox** — 11 core tools (Topos Theory, LHS Spectral Sequence, Group Cohomology, Solèr's Theorem, EML, Sheaf/Čech Cohomology, Bundle Gerbes, 16-Cell Geometry, MASA Logic, Albert Algebra, Z3 SAT)
- **Part II: The "Regrets" & Open Questions** — 10 unsolved problems, including the $H^3$ numerical invariant for the 5-qubit 16-cell, the $\mathcal{Q} \dashv \mathcal{B}$ adjunction proof, non-abelian EML impossibility, the octonionic frontier, and experimental realization.

---

## Supplementary Materials

| Directory | Description |
|-----------|-------------|
| [`supplementary/construct_16cell/`](supplementary/construct_16cell/) | Z3 SAT solver construction of the 16-cell nerve for $S^3$-type Borromean contextuality (Paper IV) |
| [`supplementary/paper7_conj42/`](supplementary/paper7_conj42/) | Verification scripts for Conjecture 4.2: Peres-Mermin obstruction class and $\Phi^*$ pullback computation (Paper VII) |
| [`supplementary/paper10/`](supplementary/paper10/) | Computational enumeration of Mermin pentagrams: 135 Lagrangians, 945 proper contexts, 12,096 pentagrams, equiangular characterization, $G_2(2)$ orbit decomposition (Paper X) |
| [`supplementary/paper11/`](supplementary/paper11/) | Quadratic refinement scripts: $\beta$-formula verification, $\omega$ decomposition, geometric proof of disjoint pair $\omega=1$, parity theorem verification (Paper XI) |
| [`supplementary/paper12/`](supplementary/paper12/) | T-vector analysis: Arf candidate search, $G_2(2)$ transitivity on $\mathbb{F}_2^6$, $G_2(2)$-invariant quadratic form search, T-vector statistics (Paper XII) |
| [`supplementary/paper13/`](supplementary/paper13/) | Maslov index computation: Kashiwara triple index, $k$-profile theorem verification, $h$-structure analysis, $G_2(2)$ orbit invariant enumeration (Paper XIII) |
| [`supplementary/paper14/`](supplementary/paper14/) | Stabilizer algebra computation: $G_2(2)$ orbit stabilizers ($\mathbb{Z}_2$ vs $S_3$), full 12,096 $k$-profile verification, $\beta_{\text{sum}}$ distribution, $h$-pattern analysis (Paper XIV) |
| [`supplementary/paper15/`](supplementary/paper15/) | Weil representation scripts: metaplectic lifting classification of $S_3$ stabilizers, $\beta$-cocycle verification, $G_2(2)$ Lagrangian orbit enumeration (Paper XV) |
| [`supplementary/paper16/`](supplementary/paper16/) | Weyl product identity verification: Fano zero-sum, $W_C = s(C)\cdot I_8$, pentagram product $\prod W_C = -I_8$, $G_2(2)$ equivariance (Paper XVI) |

---

## DOIs

All components are archived on Zenodo:

| Component | DOI |
|-----------|-----|
| Paper I | [10.5281/zenodo.20072818](https://doi.org/10.5281/zenodo.20072818) |
| Paper II | [10.5281/zenodo.20073010](https://doi.org/10.5281/zenodo.20073010) |
| Paper III | [10.5281/zenodo.20073127](https://doi.org/10.5281/zenodo.20073127) |
| Paper IV | [10.5281/zenodo.20073184](https://doi.org/10.5281/zenodo.20073184) |
| Epilogue | [10.5281/zenodo.20073253](https://doi.org/10.5281/zenodo.20073253) |
| Paper V | [10.5281/zenodo.20073318](https://doi.org/10.5281/zenodo.20073318) |
| Paper VI | [10.5281/zenodo.20073424](https://doi.org/10.5281/zenodo.20073424) |
| Paper VII | [10.5281/zenodo.20438042](https://doi.org/10.5281/zenodo.20438042) |
| Paper VIII | [10.5281/zenodo.20454120](https://doi.org/10.5281/zenodo.20454120) |
| Paper IX | [10.5281/zenodo.20465623](https://doi.org/10.5281/zenodo.20465623) |
| Paper X | [10.5281/zenodo.20476659](https://doi.org/10.5281/zenodo.20476659) |
| Paper XI | [10.5281/zenodo.20482595](https://doi.org/10.5281/zenodo.20482595) |
| Paper XII | [10.5281/zenodo.20490118](https://doi.org/10.5281/zenodo.20490118) |
| Paper XIII | [10.5281/zenodo.20496513](https://doi.org/10.5281/zenodo.20496513) |
| Paper XIV | [10.5281/zenodo.20502868](https://doi.org/10.5281/zenodo.20502868) |
| Paper XV | [10.5281/zenodo.20519654](https://doi.org/10.5281/zenodo.20519654) |
| Paper XVI | [10.5281/zenodo.20519733](https://doi.org/10.5281/zenodo.20519733) |
| L-S Note I (geometric phase) | [10.5281/zenodo.20102566](https://doi.org/10.5281/zenodo.20102566) |
| L-S Note II (non-commutativity) | [10.5281/zenodo.20102587](https://doi.org/10.5281/zenodo.20102587) |
| L-S Note III (associativity / $\mathbb{O}$) | [10.5281/zenodo.20102638](https://doi.org/10.5281/zenodo.20102638) |
| `construct_16cell.py` | [10.5281/zenodo.20070954](https://doi.org/10.5281/zenodo.20070954) |
| `paper7_conj42.py`/`paper7_conj42_layer2.py` | [10.5281/zenodo.20437675](https://doi.org/10.5281/zenodo.20437675) |
| `supplementary/paper10/` (12 scripts) | [10.5281/zenodo.20472357](https://doi.org/10.5281/zenodo.20472357) |
| `supplementary/paper11/` (13 scripts) | [10.5281/zenodo.20482283](https://doi.org/10.5281/zenodo.20482283) |
| `supplementary/paper12/` (3 scripts) | [10.5281/zenodo.20488394](https://doi.org/10.5281/zenodo.20488394) |
| `supplementary/paper13/` (5 scripts) | [10.5281/zenodo.20495857](https://doi.org/10.5281/zenodo.20495857) |
| `supplementary/paper14/` (2 scripts) | [10.5281/zenodo.20501961](https://doi.org/10.5281/zenodo.20501961) |
| `supplementary/paper15/` (2 scripts) | [10.5281/zenodo.20509690](https://doi.org/10.5281/zenodo.20509690) |
| `supplementary/paper16/` (1 script) | [10.5281/zenodo.20519672](https://doi.org/10.5281/zenodo.20519672) |

---

## Build

Each paper is a standalone LaTeX document. Compile with:

```bash
pdflatex Paper1_contextuality_phase.tex
pdflatex Paper1_contextuality_phase.tex
pdflatex Paper1_contextuality_phase.tex
```

Requirements: TeX Live 2023+ with `amsmath`, `amssymb`, `amsthm`, `tikz-cd`, `booktabs`, `hyperref`.

---

## Citation

To cite the series, please reference the individual paper(s) by DOI (see above). For the series as a whole:

```bibtex
@misc{chen2026cohomological,
  author = {Chen, Zhou-Li},
  title  = {The Logic of Observation: A Unified Cohomological Theory of Quantum Contextuality},
  year   = {2026},
  note   = {Sixteen-paper series with epilogue},
  url    = {https://github.com/co-nlang/research}
}
```

---

## License

- **Papers** (LaTeX sources in `papers/`): [CC BY 4.0](LICENSE)
- **Supplementary code** (`supplementary/`): [MIT](supplementary/construct_16cell/LICENSE)
