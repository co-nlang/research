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

## Reading Guide

### Recommended Order

```
Paper I → Paper II → Paper III → Paper IV → Epilogue → Paper V → Paper VI
```

- **Papers I–III** establish the concrete foundation: geometric phases, Riemann surfaces, and the Kochen–Specker obstruction.
- **Paper IV** introduces the $H^3$ frontier (Borromean contextuality) and the Lyndon–Hochschild–Serre transgression.
- **The Epilogue** provides the unifying vision (EML system, Solèr's theorem, obstruction ladder).
- **Papers V–VI** ascend to the categorical abstraction and prove the necessity of $\mathbb{C}$.

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

---

## The Obstruction Ladder

```
Level 0 (Foundation):  H¹  —  E_∞^{1,0} survivors     —  Geometric phases (Aharonov–Bohm, Berry)
Level 1 (Obstruction): H²  —  d₂ transgression         —  Kochen–Specker contextuality
Level 2 (Obstruction): H³  —  d₃ higher differential   —  Borromean non-associativity
```

The distinction is crucial: **geometric phases are stable features** that survive the entire spectral sequence filtration ($E_\infty$ page). **Quantum anomalies are obstructions** measured by the differentials ($d_2, d_3$) that measure the cost of forcing classical logic onto quantum systems.

---

## Supplementary Materials

| Directory | Description |
|-----------|-------------|
| [`supplementary/construct_16cell/`](supplementary/construct_16cell/) | Z3 SAT solver construction of the 16-cell nerve for $S^3$-type Borromean contextuality (Paper IV) |

---

## DOIs

DOIs will be assigned via Zenodo. The table below will be populated as each component is published.

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
