# The Mathematical Toolbox and Research Frontiers

*A candid inventory of what we used, what we proved, and what remains beyond reach.*

---

## Part I: The Mathematical Toolbox

These are the heavy weapons that make the obstruction ladder possible. Each is essential; none is accidental.

### Topos Theory & Bohrification

**Role:** The bridge between operator algebras and logic. Bohrification sends a non-commutative C*-algebra to the topos of presheaves over its commutative subalgebras (MASAs). This topos has an internal logic (Heyting algebra) that captures the aggregate of all classical perspectives.

**Where used:** Papers I, II (geometric phase reconstruction); Paper V (the $\mathcal{Q} \dashv \mathcal{B}$ adjunction); Paper VI (Solèr-Cohomology Theorem).

**Key references:** Heunen-Landsman-Spitters (2011), Abramsky-Brandenburger (2011).

---

### The Lyndon–Hochschild–Serre (LHS) Spectral Sequence

**Role:** The computational engine of the entire framework. For a group extension $1 \to N \to G \to G/N \to 1$, the LHS spectral sequence systematically decomposes the cohomology of $G$ into contributions from $N$ and $G/N$. Its differentials ($d_2, d_3, \dots$) measure successive layers of obstruction.

**Where used:** Paper IV ($d_2$ transgression for the Pauli group); Paper V (the full computational architecture); Paper VI (exclusion of $\mathbb{H}$ via annihilation of $d_2$).

**Key references:** Hochschild-Serre (1953), Brown (1982).

---

### Group Cohomology & Central Extensions

**Role:** The algebraic language of non-commutativity. A central extension $1 \to N \to G \to Q \to 1$ is classified by $H^2(Q, N)$. The Kochen–Specker obstruction is exactly the non-triviality of a specific 2-cocycle $[f] \in H^2(\bar{\mathcal{P}}_2, \mathbb{Z}/2)$.

**Where used:** Paper III (Peres–Mermin square as central extension); Paper IV ($d_2$ transgression computation); Paper V (invariant characters and the inflation-restriction sequence).

**Key references:** Brown (1982), Karpilovsky (1987).

---

### Solèr's Theorem

**Role:** Provides the rigidity boundary for the division ring underlying quantum mechanics. Solèr (1995) proved: any infinite-dimensional orthomodular space over a division ring that admits an infinite orthonormal sequence must have its division ring equal to $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$. This reduces the problem of "why $\mathbb{C}$?" to a finite classification.

**Where used:** Paper VI (the Solèr-Cohomology Theorem); Epilogue (the division ring table).

**Key references:** Solèr (1995).

---

### The EML (Exp-Minus-Log) Computational System

**Role:** A computational mirror of the geometric obstruction ladder. The operator $\text{eml}(x, y) = \exp(x) - \ln(y)$ exhibits a branch-cut structure whose topology (the fundamental groupoid $\Pi_1(\mathbb{C}^\times)$) reproduces the $U(1)$ phase classification. Over $\mathbb{H}$, the logarithm degenerates into an $S^2$ of solutions.

**Where used:** Epilogue (introduced as a unifying computational principle); Paper V (EML as an instance of the adjunction); Paper VI (Solèr-EML correspondence).

**Key references:** Odrzywołek (2026).

---

### Sheaf Theory & Čech Cohomology

**Role:** The geometric language of local-to-global obstructions. $\check{H}^1(M, U(1))$ classifies flat line bundles — the mathematical home of geometric phases (Aharonov–Bohm, Berry phase). $\check{H}^2(M, \underline{U(1)})$ classifies bundle gerbes — the home of Borromean contextuality.

**Where used:** Papers I, II (geometric phases on $S^2$ and $T^2$); Paper IV ($H^3$ conjecture via Dixmier–Douady class).

**Key references:** Brylinski (1993), Murray (1996).

---

### Bundle Gerbes & the Dixmier–Douady Class

**Role:** The geometric realization of $H^3$ cohomology. While line bundles ($H^2$) measure the twist of a complex line, bundle gerbes ($H^3$) measure the failure of associativity in the categorified patching of transitions.

**Where used:** Paper IV (the $H^3$ correspondence conjecture).

**Key references:** Murray (1996), Dixmier-Douady (1963).

---

### Cross-Polytope Geometry (the 16-Cell)

**Role:** The minimal topological nerve capable of supporting an $S^3$ Borromean contextuality anomaly. The 4-dimensional cross-polytope has 8 vertices (MASAs) and 16 tetrahedra (3-simplices), avoiding the algebraic collapse that destroys smaller triangulations.

**Where used:** Paper IV (quantum nerve collapse lemma, global symplectic collapse, 5-qubit construction).

---

### Algebraic Quantum Logic (MASAs & Orthomodular Lattices)

**Role:** The logical substrate. Maximal abelian subalgebras (MASAs) are the "classical contexts" within a quantum system. Their intersection structure defines the Čech nerve — a simplicial complex whose cohomology encodes contextuality.

**Where used:** Throughout Papers I–VI.

---

### Jordan Algebras & the Albert Algebra $\mathfrak{h}_3(\mathbb{O})$

**Role:** The conjectural algebraic container for non-associative quantum logic. The Albert algebra is the unique 27-dimensional exceptional Jordan algebra, built from $3 \times 3$ Hermitian octonionic matrices. Its non-associativity makes it the natural target for Borromean contextuality beyond matrix mechanics.

**Where used:** Paper IV (conjectural outlook).

**Key references:** Jacobson (1968), Baez (2002).

---

### Z3 SAT Solving & Symbolic Computation

**Role:** Computational verification of the existence (and impossibility) theorems. The 16-cell constraint satisfaction problem reduces to a SAT instance in the symplectic vector space $\mathbb{F}_2^{2N}$. Z3 proves UNSAT for $N=4$ and produces explicit solutions for $N=5$.

**Where used:** Paper IV (supplementary material; 5-qubit operator construction).

---

## Part II: The "Regrets" & Open Questions

*We know exactly where the gaps are. Here they are, unvarnished.*

### 1. The $H^3$ Numerical Invariant for the 5-Qubit 16-Cell

**Status:** The explicit 5-qubit Pauli operators for the 16-cell nerve have been constructed (Paper IV, Appendix A). The $H^3$ topological invariant — the numerical value of the Dixmier–Douady class for this specific configuration — has **not been analytically computed**.

**What's needed:** Compute $\mathrm{DD}(\mathcal{G}) \in H^3(S^3, \mathbb{Z}) \cong \mathbb{Z}$ for the 5-qubit 16-cell. This requires evaluating the Čech 3-cocycle on the explicit transition bundles between the 8 MASAs. The computation is well-defined but combinatorially intensive.

---

### 2. The $\mathcal{Q} \dashv \mathcal{B}$ Adjunction (Conjectural)

**Status:** Paper V formulates the adjunction between quantum and classical structures as **Conjecture 3.1** ("The Adjunction Hypothesis"). The functors $\mathcal{Q}$ (quantization) and $\mathcal{B}$ (Bohrification) are hypothesized to form a Galois connection, but the general construction of $\mathcal{Q}$ remains open.

**What's needed:** Construct the left adjoint $\mathcal{Q}$ explicitly, or prove it cannot exist in sufficient generality. The current formulation works for group-theoretic models (Pauli groups) but the extension to arbitrary C*-algebras requires a substantial categorical innovation.

---

### 3. The $\Phi$ and $\Psi$ Functorial Bridges (Conjectural)

**Status:** Papers IV and V propose natural equivalences $\Phi$ (connecting Bohrification cohomology to group cohomology) and $\Psi$ (connecting geometric Čech cohomology to central characters). **No functorial map $H^2_{\text{group}} \to \check{H}^2_{\text{nerve}}$ has been constructed.** Every theorem in Paper V is conditional on $\Phi$ existing.

**What's needed:** Construct a functor from the category of quantum contextual systems to the category of group extensions, or prove that such a functor cannot capture the full Bohrification structure.

---

### 4. Non-Abelian EML: The Impossibility Proof for $\mathbb{H}$

**Status:** The Epilogue and Paper VI argue that over $\mathbb{H}$, the logarithm of a negative scalar produces a continuous $S^2$ of solutions, preventing consistent computation. This is a **strong conjecture**, not a theorem. Paper VI's exclusion of $\mathbb{H}$ relies on the LHS $d_2$ mechanism, which is a separate argument.

**What's needed:** A rigorous proof that no single-valued computational system over $\mathbb{H}$ can satisfy both completeness (all division algebra operations are computable) and determinism (each input yields a unique output), when the logarithm is included.

---

### 5. Deriving Orthomodularity from Pure Category Theory

**Status:** Solèr's theorem assumes an orthomodular lattice structure. Paper VI asks: can orthomodularity itself be derived from the $\mathcal{Q} \dashv \mathcal{B}$ adjunction? This would eliminate the last axiomatic residue from the derivation of $\mathbb{C}$.

**What's needed:** Show that the adjunction between a quantum category and a classical category forces the quantum logic to be orthomodular. This requires a categorical characterization of orthomodularity — likely via dagger compact closed categories or orthoalgebras.

---

### 6. The $\mathbb{O}$ / Octonionic Frontier

**Status:** Paper IV's Section 6 outlines the Albert algebra $\mathfrak{h}_3(\mathbb{O})$ as the "exceptional horizon." Paper VI briefly mentions it as an open question. **No theorems are claimed.** The octonionic program is entirely speculative.

**What's needed:** 
- Construct an octonionic quantum logic that natively supports the Borromean associator anomaly
- Relate $\mathfrak{h}_3(\mathbb{O})$ to the automorphism group $F_4$ as the "gauge group" of non-associative context switching
- Determine whether the octonionic phase group $S^7$ admits a viable quantum probability interpretation

---

### 7. The $\mathcal{Q} \dashv \mathcal{B}$ One-Direction Proof for Conjecture 5.1

**Status:** Paper IV establishes one direction of the $H^3$ Correspondence (Remark 5.6): if a non-trivial bundle gerbe exists, then Borromean contextuality follows. The converse — Borromean contextuality implies a non-trivial gerbe — remains open.

**What's needed:** Construct a bundle gerbe from a given Borromean system and verify that the associator anomaly maps to a non-trivial Dixmier–Douady class.

---

### 8. Massey Products and Higher Cohomology Operations

**Status:** The Epilogue mentions that Borromean contextuality involves operations "reminiscent of Massey products." This connection has not been developed. The LHS spectral sequence naturally supports Massey products (via matric Massey products on the $E_2$ page), but their physical interpretation is unexplored.

**What's needed:** Determine whether the Borromean 3-cocycle corresponds to a triple Massey product $\langle d_2(\chi_1), d_2(\chi_2), d_2(\chi_3) \rangle$ of $d_2$ transgressions.

---

### 9. Experimental Realization of the 5-Qubit 16-Cell

**Status:** The 5-qubit operators exist on paper. No physical system has been proposed to realize them.

**What's needed:** Identify a physical platform (trapped ions, superconducting qubits, photonic cluster states) capable of measuring the pairwise commutativity and global anti-commutativity structure of the 16-cell, and verify the Borromean contextuality signature.

---

### 10. Relation to Topological Phases of Matter

**Status:** The $H^3$ obstruction ladder is structurally analogous to the classification of SPT phases (e.g., Dijkgraaf-Witten theories, Chern-Simons). The Dixmier–Douady class appears in the WZW model. These connections are noted in passing but not developed.

**What's needed:** Establish a precise dictionary between the Borromean contextuality framework and known classification schemes for topological phases (group cohomology classification, cobordism classification).

---

## How to Contribute

This document is both a guide and an invitation. If you have expertise in any of the areas above — spectral sequences, topos theory, octonions, SAT solving, experimental quantum computing — the open questions listed here are concrete, well-scoped, and mathematically meaningful.

The full paper series is available in the [`papers/`](papers/) directory. Each "regret" above corresponds to a specific section and conjecture within the papers.

---

*"A theory is only as honest as its list of open problems."*
