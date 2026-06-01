# The Logic of Observation: A Unified Cohomological Theory of Quantum Contextuality

A Eleven-paper series with epilogue exploring the cohomological foundations of quantum contextuality: from geometric phases to the necessity of complex numbers, extended by Paper VIII with explicit functor construction and twisted Penrose transform, Paper IX with the 3-qubit obstruction ladder and two non-conjugate Klein quartic bridges, Paper X with the equiangular characterization of Mermin pentagrams, and Paper XI with the quadratic refinement proof of the parity theorem.

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
│   └── Paper11_quadratic_refinement.tex
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
│   └── paper10/
│       ├── LICENSE                         # MIT
│       ├── README.md
│       ├── p0_enumerate_contexts.py
│       ├── p1_orbit_check.py
│       ├── p2_typeB_analysis.py
│       ├── p3_sign_patterns.py
│       ├── p4_typeF4_analysis.py
│       ├── p5_ghost_pentagon.py
│       ├── p6_equiangular_check.py
│       ├── p7_ray_cap.py
│       ├── p8_sufficiency_check.py
│       ├── g2_orbits.py
│       └── orbit_type_lagrangian.py
│   └── paper11/
│       ├── LICENSE                         # MIT
│       ├── README.md
│       ├── quadratic_refinement_v2.py
│       ├── decompose_omega.py
│       ├── prove_disjoint_omega.py
│       ├── verify_quadratic_identity.py
│       ├── omega_integer_values.py
│       ├── analyze_T_structure.py
│       ├── check_T.py
│       ├── check_full_identity.py
│       ├── check_sum_q_plus_c.py
│       ├── verify_conditions.py
│       ├── class2_characterization.py
│       ├── quadratic_refinement.py
│       └── verify_identity.py
```

---

## Reading Guide

### Recommended Order

```
Paper I → Paper II → Paper III → Paper IV → Epilogue → Paper V → Paper VI → Paper VII → Paper VIII → Paper IX → Paper X → Paper XI
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
| L-S Note I (geometric phase) | [10.5281/zenodo.20102566](https://doi.org/10.5281/zenodo.20102566) |
| L-S Note II (non-commutativity) | [10.5281/zenodo.20102587](https://doi.org/10.5281/zenodo.20102587) |
| L-S Note III (associativity / $\mathbb{O}$) | [10.5281/zenodo.20102638](https://doi.org/10.5281/zenodo.20102638) |
| `construct_16cell.py` | [10.5281/zenodo.20070954](https://doi.org/10.5281/zenodo.20070954) |
| `paper7_conj42.py`/`paper7_conj42_layer2.py` | [10.5281/zenodo.20437675](https://doi.org/10.5281/zenodo.20437675) |
| `supplementary/paper10/` (12 scripts) | [10.5281/zenodo.20472357](https://doi.org/10.5281/zenodo.20472357) |
| `supplementary/paper11/` (13 scripts) | [10.5281/zenodo.20482283](https://doi.org/10.5281/zenodo.20482283) |

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
  note   = {Eleven-paper series with epilogue},
  url    = {https://github.com/co-nlang/research}
}
```

---

## License

- **Papers** (LaTeX sources in `papers/`): [CC BY 4.0](LICENSE)
- **Supplementary code** (`supplementary/`): [MIT](supplementary/construct_16cell/LICENSE)
