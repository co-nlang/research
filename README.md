# The Logic of Observation: A Unified Cohomological Theory of Quantum Contextuality

A twenty-two-paper series (with epilogue) building a unified cohomological theory of quantum contextuality.

**Author:** Zhou-Li Chen (co-nlang Research)

---

## The Series at a Glance

Quantum observation forces an observer to view a system through incompatible contexts — complementary measurement setups, each locally classical, that refuse to glue into a global picture. This series builds the algebraic machinery that measures that refusal: an **obstruction ladder** graded by group cohomology, where $H^1$ captures geometric phases, $H^2$ captures Kochen–Specker contextuality, and $H^3$ captures a Borromean, genuinely multipartite obstruction visible only when five contexts interact.

The series has three arcs. **Papers I–VI** construct the ladder from scratch — Bohrification, spectral sequences, and the necessity of $\mathbb{C}$ from the logic of observation alone. **Papers VII–IX** bridge to twistor geometry, resolving the Penrose googly problem as an $H^2$ obstruction. **Papers X–XXII** descend into the finite symplectic world $\mathrm{Sp}(2n, \mathbb{F}_2)$: the Mermin pentagram's 12,096 configurations in the 3-qubit setting are anatomised computationally (X–XVI), then re-derived from pure algebra (XVII–XVIII), before the $n \ge 5$ deformation opens $H^3$ as a genuine cohomology class (XIX–XX) and the **master rigidity theorem** closes the circle: *$N_{\mathrm{anti}} = 10$ universally if and only if $n = 4$* (XXI). Paper XXII establishes the **arity–resonance ceiling** — the obstruction is intrinsically degree-3 and truncates at $H^3$, with the pentagram as its unique resonant configuration.

The endpoint: the framework's deepest invariant ($H^3$) is conjecturally $\mathrm{Sq}^1\omega$ — a canonical operation applied to the symplectic form that defines the framework itself (the comparison map establishing this is the series' open capstone). The obstruction ladder measures the coherence of self-description, and $n = 4$ is the unique dimension where that coherence is unobstructed.

→ **[READING_GUIDE.md](READING_GUIDE.md)** — per-paper summaries and recommended reading orders.
→ **[RESEARCH_FRONTIER.md](RESEARCH_FRONTIER.md)** — mathematical toolbox and open problems.
→ **[insight/](insight/)** — post-series exploration notes (QEC substrate identity, BHQC, AdS/CFT holographic codes, Klein quartic, and others).

---

## Quick Reference

| # | Title | Key Result |
|---|-------|------------|
| I | *From Contextuality to Phase Cohomology* | $\check{H}^1(M, U(1))$ classifies geometric phases |
| II | *Semiclassical Reconstruction of Riemann Surfaces from Bohrification* | Bohr-Sommerfeld orbits as divisors on spectral curves |
| III | *Kochen–Specker Contextuality as Central Extension* | KS obstruction = $[f] \in H^2(\bar{\mathcal{P}}_2, \mathbb{Z}/2)$ |
| IV | *LHS Transgression and the $H^3$ Frontier* | $d_2$ transgression = KS; Borromean $H^3$ predicted |
| Epilogue | *The Algebraic Logic of Geometry* | $\mathcal{Q} \dashv \mathcal{B}$ adjunction; EML; Solèr |
| V | *Observation as Functor* | LHS spectral sequence unifies all obstructions |
| VI | *Deriving QM from the Logic of Observation* | $\mathbb{C}$ is the unique division ring for non-trivial observation |
| VII | *Twistor Theory from the Obstruction Ladder* | Googly problem = $H^2$ obstruction |
| VIII | *The $\Phi$ Functor* | $\Phi = \ell \circ \tau \circ \iota^*$; $\mathbb{Z}/2$-gerbe on $\mathbb{CP}^3$ |
| IX | *The 3-Qubit Obstruction Ladder* | $GL(3,\mathbb{F}_2) \hookrightarrow PSp(6,\mathbb{F}_2)$; two Klein quartic bridges |
| X | *Equiangular Characterization of Mermin Pentagrams* | $K_5 \Leftrightarrow$ equiangular $\Leftrightarrow$ Mermin; 10-ray cap |
| XI | *Quadratic Refinement and Parity* | $\beta$-formula; $\beta_{\mathrm{sum}} \equiv 2 \pmod{4}$ (12,096/12,096) |
| XII | *The T-Vector Theorem* | $\omega(T,r)=1$ (algebraic); Wu class analogy |
| XIII | *Maslov Index and the KS Obstruction* | Kashiwara ≠ $\beta/2$; $k$-profile theorem |
| XIV | *Stabilizer Algebra and $k$-Profile* | $O_{2,3,4} = S_3$; 7 profiles, 100% odd |
| XV | *Weil Representation and $S_3$ Lifting* | Split / non-split classification; $\beta$-cocycle refuted |
| XVI | *The Weyl Product Identity* | $\prod_C W_C = -I_8$ as Weyl algebra identity |
| XVII | *Cross-Context Anticommutation Theorem* | $\omega(v_{ij},v_{kl})=1$ for all 15 pairs (algebraic) |
| XVIII | *Mermin Pentagrams in $\mathrm{Sp}(8,\mathbb{F}_2)$* | $N_{\mathrm{anti}}=10$ universal at $n=4$ (algebraic, B0+B1+B2) |
| XIX | *$n \ge 5$: Modulus Phenomenon* | No arity-$\le 4$ invariant classifies the fiber |
| XX | *$H^3$ Opens at $n \ge 5$* | $[n_a]=0$ universally $\iff n=4$ |
| XXI | *Master Theorem* | $N_{\mathrm{anti}}=10$ universally $\iff n=4$; even/odd dichotomy |
| XXII | *Arity–Resonance Ceiling* | $H^4$ truncates; ceiling $= \min(\omega(G)-2,3)$; two families |
| L-S I–III | *Contraction Appendices* | Dynamical reinterpretation of $H^1$, $H^2$, $H^3$ |

---

## The Obstruction Ladder

```
Level 0 (Foundation):  H¹  —  E_∞^{1,0} survivors     —  Geometric phases (Aharonov–Bohm, Berry)
Level 1 (Obstruction): H²  —  d₂ transgression         —  Kochen–Specker contextuality
Level 2 (Obstruction): H³  —  d₃ higher differential   —  Borromean non-associativity
                                                            (truncates: H⁴ = 0, Paper XXII)
```

Geometric phases are stable features surviving the entire spectral sequence ($E_\infty$). Quantum anomalies are obstructions measured by the differentials ($d_2, d_3$) — the cost of forcing classical logic onto quantum systems.

---

## Repository Structure

```
research/
├── README.md
├── READING_GUIDE.md                    # Per-paper summaries & reading orders
├── RESEARCH_FRONTIER.md                # Toolbox & open problems
├── LICENSE                             # CC BY 4.0
├── insight/                            # Post-series exploration notes
├── papers/
│   ├── Paper1_contextuality_phase.tex
│   ├── ...
│   ├── Paper22_resonance_ceiling.tex
│   ├── Epilogue_algebraic_logic.tex
│   ├── LsNote_*.tex                    # L-S contraction appendices (3)
│   └── timescape_cross_validation.tex  # SN × void-fraction empirical test
└── supplementary/
    ├── construct_16cell/               # Z3 SAT, 16-cell nerve (Paper IV)
    ├── paper7_conj42/                  # Φ* pullback verification (Paper VII)
    ├── paper10/ – paper22/             # Per-paper computational scripts
    ├── klein/                          # Klein quartic / PSL(2,7) bridge
    ├── adscft/                         # HaPPY holographic codes (insight)
    ├── mbqc/                           # l2-MBQC computational degree (insight)
    ├── bockstein/                      # Z/4-Bockstein / Sq¹-acyclicity (insight)
    ├── twistor_cp/                     # item 13: CP^{2^n-1} realization is family-B only
    ├── familyB_resonance/              # item 22: family B is family A's omega=2 floor
    └── timescape/                      # SN × void-fraction cross-validation
```

---

## Supplementary Materials

| Directory | Paper | Description |
|-----------|-------|-------------|
| [`construct_16cell/`](supplementary/construct_16cell/) | IV | Z3 SAT construction of the 16-cell nerve |
| [`paper7_conj42/`](supplementary/paper7_conj42/) | VII | $\Phi^*$ pullback verification |
| [`paper10/`](supplementary/paper10/) | X | 12,096 pentagrams, equiangular characterization, $G_2(2)$ orbits |
| [`paper11/`](supplementary/paper11/) | XI | $\beta$-formula, $\omega$ decomposition, parity theorem |
| [`paper12/`](supplementary/paper12/) | XII | T-vector, Arf search, $G_2(2)$ transitivity |
| [`paper13/`](supplementary/paper13/) | XIII | Kashiwara index, $k$-profile theorem |
| [`paper14/`](supplementary/paper14/) | XIV | Stabilizer classification, $\beta_{\mathrm{sum}}$ statistics |
| [`paper15/`](supplementary/paper15/) | XV | Metaplectic lifting, $\beta$-cocycle test |
| [`paper16/`](supplementary/paper16/) | XVI | Weyl product identity verification |
| [`paper17/`](supplementary/paper17/) | XVII | Cross-context anticommutation (12,096) |
| [`paper18/`](supplementary/paper18/) | XVIII | B0/B1/B2 recheck, landscape table, Key Lemma |
| [`paper19/`](supplementary/paper19/) | XIX | Upper-bound ladder, modulus witness, Arf ruling-out |
| [`paper20/`](supplementary/paper20/) | XX | $n_a = \delta\mu$ verification, rank-parity |
| [`paper21/`](supplementary/paper21/) | XXI | Master theorem, spread-stabilisation witnesses |
| [`paper22/`](supplementary/paper22/) | XXII | Arity–resonance, truncation, clique criterion, $\mathrm{Sq}^1\omega$ bridge |
| [`klein/`](supplementary/klein/) | IX | 168-action, bitangent bijection, theta/spin spiral |
| [`adscft/`](supplementary/adscft/) | insight | HaPPY holographic codes; reconstruction is blind to contextuality |
| [`mbqc/`](supplementary/mbqc/) | insight | l2-MBQC: computational degree $\ne$ cohomological degree |
| [`bockstein/`](supplementary/bockstein/) | insight | $\mathbb{Z}/4$-Bockstein / $\mathrm{Sq}^1$-acyclicity: the $H^3$ ceiling is not an $\mathbb{F}_2$ artifact |
| [`twistor_cp/`](supplementary/twistor_cp/) | VIII | item 13: the $\mathbb{CP}^{2^n-1}$ realization is family-B only ($\mathrm{Sq}^1$-blind to family A) |
| [`familyB_resonance/`](supplementary/familyB_resonance/) | XXII | item 22: no family-B resonance — it is the $\omega=2$ floor of family A's clique tower |
| [`timescape/`](supplementary/timescape/) | — | SN Hubble-residual $\times$ void-fraction cross-validation |

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
| Paper XVII | [10.5281/zenodo.20530757](https://doi.org/10.5281/zenodo.20530757) |
| Paper XVIII | [10.5281/zenodo.20579239](https://doi.org/10.5281/zenodo.20579239) |
| Paper XIX | [10.5281/zenodo.20590195](https://doi.org/10.5281/zenodo.20590195) |
| Paper XX | [10.5281/zenodo.20608302](https://doi.org/10.5281/zenodo.20608302) |
| Paper XXI | [10.5281/zenodo.20685669](https://doi.org/10.5281/zenodo.20685669) |
| Paper XXII | [10.5281/zenodo.20685777](https://doi.org/10.5281/zenodo.20685777) |
| L-S Note I | [10.5281/zenodo.20102566](https://doi.org/10.5281/zenodo.20102566) |
| L-S Note II | [10.5281/zenodo.20102587](https://doi.org/10.5281/zenodo.20102587) |
| L-S Note III | [10.5281/zenodo.20102638](https://doi.org/10.5281/zenodo.20102638) |
| `construct_16cell.py` | [10.5281/zenodo.20070954](https://doi.org/10.5281/zenodo.20070954) |
| `paper7_conj42/` | [10.5281/zenodo.20437675](https://doi.org/10.5281/zenodo.20437675) |
| `paper10/` | [10.5281/zenodo.20472357](https://doi.org/10.5281/zenodo.20472357) |
| `paper11/` | [10.5281/zenodo.20482283](https://doi.org/10.5281/zenodo.20482283) |
| `paper12/` | [10.5281/zenodo.20488394](https://doi.org/10.5281/zenodo.20488394) |
| `paper13/` | [10.5281/zenodo.20495857](https://doi.org/10.5281/zenodo.20495857) |
| `paper14/` | [10.5281/zenodo.20501961](https://doi.org/10.5281/zenodo.20501961) |
| `paper15/` | [10.5281/zenodo.20509690](https://doi.org/10.5281/zenodo.20509690) |
| `paper16/` | [10.5281/zenodo.20519672](https://doi.org/10.5281/zenodo.20519672) |
| `paper17/` | [10.5281/zenodo.20528739](https://doi.org/10.5281/zenodo.20528739) |
| `paper18/` | [10.5281/zenodo.20546121](https://doi.org/10.5281/zenodo.20546121) |
| `paper19/` | [10.5281/zenodo.20579390](https://doi.org/10.5281/zenodo.20579390) |
| `paper20/` | [10.5281/zenodo.20604140](https://doi.org/10.5281/zenodo.20604140) |
| `paper21/` | [10.5281/zenodo.20636220](https://doi.org/10.5281/zenodo.20636220) |
| `paper22/` | [10.5281/zenodo.20685721](https://doi.org/10.5281/zenodo.20685721) |

---

## AI Collaboration Disclosure

This research project integrated various Large Language Models (LLMs) across multiple stages to enhance rigor and clarity. The author(s) maintain full accountability for the final content.

- **Theoretical Derivation:** AI was used to assist in symbolic manipulation, cross-verifying mathematical proofs, and identifying potential edge cases in formulas.
- **Development & Typesetting:** Code implementation and LaTeX structural optimization were supported by AI-assisted pair programming.
- **Language & Refinement:** Sentences were polished for academic flow and grammatical precision.
- **Simulated Peer Review:** AI agents were tasked to act as independent reviewers to provide critical feedback and identify logical gaps prior to publication.

*Models used: Gemini 3 Pro/3.1 Pro, GPT-5.3, Claude Sonnet 4.6/Opus 4.6&4.8, Kimi K2.5/K2.6, GLM-5.0, QWen 3.5 Plus, DeepSeek V4 Pro/Flash.*

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
  note   = {Twenty-two-paper series with epilogue},
  url    = {https://github.com/co-nlang/research}
}
```

---

## License

- **Papers** (LaTeX sources in `papers/`): [CC BY 4.0](LICENSE)
- **Supplementary code** (`supplementary/`): [MIT](supplementary/construct_16cell/LICENSE)
