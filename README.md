# The Logic of Observation: A Unified Cohomological Theory of Quantum Contextuality

A six-paper series with epilogue exploring the cohomological foundations of quantum contextuality: from geometric phases to the necessity of complex numbers.

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

*Models used: Gemini 3 Pro/3.1 Pro, GPT-5.3, Claude Sonnet 4.6, Kimi K2.5/K2.6, GLM-5.0, QWen 3.5 Plus, DeepSeek V4 Pro.*

---

## Repository Structure

```
research/
├── README.md
├── LICENSE                             # CC BY 4.0
├── RESEARCH_FRONTIER.md                # Toolbox & open problems
├── insight/                            # Speculative thought experiment
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
│   └── LsNote_associativity.tex            # L-S contraction & H³ + octonionic boundary
└── supplementary/
    └── construct_16cell/
        ├── LICENSE                     # MIT
        ├── README.md
        └── construct_16cell.py
```

---

## Reading Guide

### Recommended Order

```
Paper I → Paper II → Paper III → Paper IV → Epilogue → Paper V → Paper VI
```

- **Papers I–III** establish the concrete foundation: geometric phases, Riemann surfaces, and the Kochen–Specker obstruction.
- **Paper IV** introduces the $H^3$ frontier (Borromean contextuality) and the Lyndon–Hochschild–Serre transgression.
- **The Epilogue** provides the unifying vision (EML system, Solèr's theorem, obstruction ladder).
- **Papers V–VI** ascend to the categorical abstraction and prove the necessity of $\mathbb{C}$.

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
| `construct_16cell.py` | [10.5281/zenodo.20070954](https://doi.org/10.5281/zenodo.20070954) |
| L-S Note I (geometric phase) | [10.5281/zenodo.20102566](https://doi.org/10.5281/zenodo.20102566) |
| L-S Note II (non-commutativity) | [10.5281/zenodo.20102587](https://doi.org/10.5281/zenodo.20102587) |
| L-S Note III (associativity / $\mathbb{O}$) | [10.5281/zenodo.20102638](https://doi.org/10.5281/zenodo.20102638) |

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
  note   = {Six-paper series with epilogue},
  url    = {https://github.com/co-nlang/research}
}
```

---

## License

- **Papers** (LaTeX sources in `papers/`): [CC BY 4.0](LICENSE)
- **Supplementary code** (`supplementary/`): [MIT](supplementary/construct_16cell/LICENSE)
