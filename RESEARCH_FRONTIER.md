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

### Twistor Theory & the Penrose Transform

**Role:** The geometric bridge between quantum contextuality and spacetime physics. The Penrose transform identifies solutions of massless field equations with cohomology classes $H^1(\mathbb{CP}^3, \mathcal{O}(-n-2))$ on twistor space. The googly problem — the failure to produce anti-self-dual fields — is reinterpreted as an $H^2$ obstruction carried by the PM contextuality class.

**Where used:** Paper VII (googly problem as obstruction); Paper VIII (twisted Penrose transform via $\mathbb{Z}/2$-gerbe; open problem for non-vanishing mechanism).

**Key references:** Penrose (1969), Ward-Wells (1990), Mason-Skinner (2014).

---

### The $K_{3,3}$ Nerve and Transgression Functor $\Phi$

**Role:** The Čech nerve of the PM sub-poset (six MASAs: three rows $R_1,R_2,R_3$ and three columns $C_1,C_2,C_3$) is the complete bipartite graph $K_{3,3}$. Since distinct rows are disjoint and distinct columns are disjoint, there are no 2-simplices; the nerve is 1-dimensional. This forces the PM obstruction class into $H^1(K_{3,3}, \mathbb{Z}/2) \cong (\mathbb{Z}/2)^4$ rather than $H^2$.

The transgression functor $\Phi = \ell \circ \tau \circ \iota^*$ shifts cohomological degree by $+1$:
$$H^1(K_{3,3}, \mathbb{Z}/2) \xrightarrow{\iota^*} H^1(S^1, \mathbb{Z}/2) \xrightarrow{\tau} H^2(S^2, \mathbb{Z}/2) \xrightarrow{\ell} H^2(\mathbb{CP}^3, \mathbb{Z}/2)$$
Step $\iota^*$: restriction along the PM Hamiltonian 6-cycle $\iota: S^1 \hookrightarrow K_{3,3}$; step $\tau$: clutching transgression via $\pi_1(SO(3)) \cong \mathbb{Z}/2$; step $\ell$: Leray lift along $\Sigma_0 \hookrightarrow \mathbb{CP}^3$.

Theorem 2.1 (Paper VIII): $\Phi^*([f]) = c_1(\mathcal{O}(1)) \bmod 2$.

**Where used:** Paper VIII (explicit construction of $\Phi$, Theorem 2.1, Lemma 2.3, $n$-qubit generalization Conjecture 3.1).

---

### Symplectic Polar Spaces $W(2n-1, \mathbb{F}_2)$

**Role:** The correct geometric container for the $n$-qubit MASA poset. The $n$-qubit Pauli group modulo phase has $4^n - 1$ non-identity elements (points) and $(4^n-1)(4^{n-1}-1)/3$ maximal isotropic subspaces (lines = MASAs). This is the symplectic polar space $W(2n-1, \mathbb{F}_2)$, not the set of MUBs (which has count $2^n+1$). The automorphism group of $W(2n-1, \mathbb{F}_2)$ is $PSp(2n, \mathbb{F}_2)$.

Key instances: $n=2$: $W(3, \mathbb{F}_2)$, 15 points, 15 lines, $\mathrm{Aut} = PSp(4,\mathbb{F}_2) \cong S_6$. $n=3$: $W(5, \mathbb{F}_2)$, 63 points, 315 lines, $\mathrm{Aut} = PSp(6,\mathbb{F}_2)$ of order $1{,}451{,}520 = 2^9 \cdot 3^4 \cdot 5 \cdot 7$.

The prime $7$ in the 3-qubit automorphism group is geometrically significant: $PSL(2,7) \cong GL(3,\mathbb{F}_2)$ (order 168) embeds in $PSp(6,\mathbb{F}_2)$ via the hyperbolic doubling $g \mapsto \mathrm{diag}(g,\, g^{-T})$, carrying the Fano plane $PG(2,2)$ as an isotropic subgeometry of $W(5,\mathbb{F}_2)$.

**Where used:** Paper VIII §3 ($n$-qubit obstruction ladder, MASA count correction); Paper IX (Klein quartic bridge via $PSL(2,7) \leq PSp(6,\mathbb{F}_2)$).

---

### $\mathbb{Z}/2$-Gerbes Classified by $H^2(X, \mathbb{Z}/2)$

**Role:** When a class $[e] \in H^2(X, \mathbb{Z}/2)$ is to be geometrically realized, one must distinguish: $H^1(X, \mathbb{Z}/2)$ classifies principal $\mathbb{Z}/2$-bundles (double covers), while $H^2(X, \mathbb{Z}/2)$ classifies $\mathbb{Z}/2$-gerbes (stacks, not spaces). For $X = \mathbb{CP}^3$, which is simply connected, $H^1(\mathbb{CP}^3, \mathbb{Z}/2) = 0$ — so no non-trivial $\mathbb{Z}/2$-bundle exists. The non-zero class $[e] \in H^2(\mathbb{CP}^3, \mathbb{Z}/2) \cong \mathbb{Z}/2$ classifies a gerbe $\mathcal{G}$, not a bundle. Sheaf cohomology on $\mathcal{G}$ requires the full machinery of twisted derived categories or ambitwistor geometry to produce non-zero invariants.

**Where used:** Paper VIII §4 (gerbe construction, honest open problem statement for twisted Penrose transform).

**Key references:** Giraud (1971), Brylinski (1993), Hitchin (2001).

---

### Rank-Parity and Symmetric Forms over $\mathbb{F}_2$

**Role:** The order parameter that governs the Maslov cochain and the entire $n$-dependence of the $H^3$ ladder. For a proper triple of Lagrangians the relative position is encoded by a symmetric bilinear form $B$ on a projected Lagrangian, with $\mathrm{rank}\,B = n-3$. Over $\mathbb{F}_2$ a symmetric form is alternating (its diagonal quadratic refinement vanishes) if and only if its rank is even — so the Maslov bit $\mu\equiv1$ exactly when $n$ is even. This single lemma yields $\mu\equiv0$ at $n=3$, $\mu\equiv1$ for even $n$, and varying $\mu$ for odd $n\ge5$, driving both Paper XX's vanishing theorem and Paper XXI's even/odd carrier dichotomy.

**Where used:** Paper XX (rank-parity lemma); Paper XXI (master theorem, dichotomy); Paper XXII (the $K_4/H^2$ rung).

**Key references:** Wall (1963), Dieudonné (1955).

---

### The Maslov–Wall Relative-Position Complex

**Role:** The correct cochain home of the $H^3$ obstruction — *not* the geometric Čech intersection nerve. For a proper $K_N$ the intersection nerve collapses to the 1-skeleton $K_N$ (triple intersections vanish), with $H^3=0$; the obstruction instead lives in the complex of *relative-position* data on the abstract index simplex $\partial\Delta^{N-1}\cong S^{N-2}$. There the Maslov bit $\mu$ is a 2-cochain and the anticommutation count $\mathbf a$ a 3-cochain, with $\mathbf a=\delta\mu$ at $n=4$; the failure $\delta\mu\ne0$ (odd $n\ge5$) is Wall non-additivity of the signature, and $N_{\mathrm{anti}}\bmod2=\langle\mathbf a,[S^{N-2}]\rangle$.

**Where used:** Paper XX (the cochain complex, $\mathbf a=\delta\mu$); Paper XXII (resonance tower, truncation).

**Key references:** Wall (1969), Lion–Vergne (1980), Kashiwara (Maslov index).

---

### The Arity–Resonance Principle and the Incidence-Clique Criterion

**Role:** Pins the *degree* at which a contextuality obstruction lives. A relative-position datum of arity $a$ is intrinsically an $(a-1)$-cochain; on a proper $K_N$ (nerve $S^{N-2}$) it hits the top cohomology iff $N=a+1$. The family-A cohomological ceiling is the graph invariant $\min(\omega(G)-2,\,3)$, where $\omega(G)$ is the clique number of the incidence graph — saturated uniquely at the pentagram ($\omega=5$). A companion construction, **spread-stabilisation** (appending $5$ pairwise-transverse Lagrangians from a Lagrangian spread of $\mathrm{Sp}(2m,\mathbb{F}_2)$, of which a spread contains $2^m+1$), transports witnesses to every $n\ge5$ while preserving the ray Gram matrix.

**Where used:** Paper XXI (spread-stabilisation); Paper XXII (arity-resonance, truncation, clique criterion).

---

### Steenrod Operations and the Heisenberg LHS Spectral Sequence

**Role:** The candidate machine for unifying the $H^2$ (central-extension) and $H^3$ (anticommutation) families. The cohomology of the symplectic vector space is the polynomial ring $H^*(V;\mathbb{F}_2)=\mathbb{F}_2[x_1,\dots,x_{2n}]$; the LHS transgression of the Heisenberg extension $1\to\mathbb{Z}_2\to P_n\to V\to1$ sends the fiber generator to the symplectic form $\omega=\sum_i x_ix_{i+n}\in H^2(V)$ (the family-B class), and the Steenrod square $\mathrm{Sq}^1\omega=\sum_i(x_i^2x_{i+n}+x_ix_{i+n}^2)\in H^3(V)$ is the candidate family-A source. The nerve-side shortcut (the cup-1 square $\mu\cup_1\mu$) is ruled out, since $\mu$ is not a cocycle off the resonance.

**Where used:** Paper XXII (§Outlook, Direction D); builds on Paper IV (LHS transgression) and Paper XV (Weil/metaplectic).

**Key references:** Steenrod–Epstein (1962), Quillen (1971), Hochschild–Serre (1953).

---

### Theta Characteristics, Spin Structures, and the Bitangent Correspondence

**Role:** The $H^1$-level bridge to the Klein quartic. Theta characteristics (quadratic refinements $Q$ of $\omega$, equivalently spin structures) form a torsor over $H^1(X;\mathbb{F}_2)=J[2]=V$ via $Q_v=q_0+\omega(v,\cdot)$, with $\mathrm{Arf}(Q_v)=q_0(v)$. The 28 **odd** ($\mathrm{Arf}=1$) theta characteristics are the 28 bitangents of a genus-3 curve; under the $PSL(2,7)\cong GL(3,\mathbb{F}_2)$ action on the 3-qubit $W(5,\mathbb{F}_2)$ they are exactly the size-28 "anti-flag" Pauli orbit, and the unique invariant **even** one is $q_0=x\cdot z$ — the framework's standard quadratic refinement = the curve's canonical spin structure. Provides the explicit equivariant identification of item 12.

**Where used:** item 12 (Klein quartic, steps 2–3), `supplementary/klein/`; connects to Paper XI (quadratic refinement) and item 23 (the $q_0\to\omega\to\mathrm{Sq}^1\omega$ spiral).

**Key references:** Atiyah (1971, *Riemann surfaces and spin structures*); Klein (1879); Dolgachev (*Classical Algebraic Geometry*, bitangents).

---

### Operational-Test Machinery: Gottesman–Knill, Holographic Codes, l2-MBQC

**Role:** The tools used to answer item 24 — i.e. to *locate* the $H^3$ class against operational quantities and find it orthogonal to each. (i) **Gottesman–Knill**: qubit stabilizer dynamics is classically simulable, so the (stabilizer) $H^3$ class carries no circuit/distillation advantage. (ii) **Holographic (HaPPY) stabilizer codes**: perfect-tensor networks over $\mathbb{F}_2$; bulk reconstruction = erasure/entanglement-wedge (support), provably independent of the bulk's contextuality. (iii) **l2-MBQC** (Anders–Browne / Raussendorf): qubit contextuality as the resource for nonlinear computation, with the computed function a class in $H^2$ of the MBQC chain complex (Okay–Raussendorf) — but degree saturates at the threshold, so cohomological degree $\ne$ computational degree.

**Where used:** item 24 (answered), `supplementary/adscft/`, `supplementary/mbqc/`; `insight/quantum_applications.md`, `insight/adscft_holographic_codes.md`.

**Key references:** Gottesman (1998); Pastawski–Yoshida–Harlow–Preskill (arXiv:1503.06237); Almheiri–Dong–Harlow (arXiv:1411.7041); Anders–Browne (PRL 102, 050502, 2009); Raussendorf (arXiv:0907.5449); Okay–Roberts–Bartlett–Raussendorf (arXiv:2005.00213).

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

### 11. Gerbe Non-Vanishing: Escape from Kodaira Vanishing (Paper VIII, §4)

**Status:** The twisted Penrose transform $H^1_{\mathcal{G}}(\mathbb{CP}^3, \mathcal{O}_{\mathcal{G}}(-n-2))$ should encode both helicities $\pm n/2$ of a massless field. However, the standard Leray spectral sequence for the gerbe projection $\pi: \mathcal{G} \to \mathbb{CP}^3$ gives $R^1\pi_*\mathcal{O}_{\mathcal{G}}(k) = 0$ (since $H^1(B(\mathbb{Z}/2), \mathcal{O}) = 0$ for holomorphic coefficients), and Kodaira vanishing kills all remaining terms for $0 < k < 3$. The twisted cohomology vanishes by the same mechanism as the untwisted case — the gerbe provides no escape.

**What's needed:** One of three possible mechanisms must be found:
1. **Derived category approach:** Work in $D^b_{\mathcal{G}}(\mathbb{CP}^3)$ (gerbe-twisted derived category) where the relevant object is a complex, not a single sheaf, and the vanishing theorem does not apply.
2. **Ambitwistor space:** Replace $\mathbb{CP}^3$ with the ambitwistor space $\mathbb{PA}$ (the space of complexified null geodesics), where both helicities appear naturally from $H^1$ without gerbe twisting.
3. **$\mathbb{F}_2$-linear cohomology:** Replace holomorphic cohomology with a mod-2 theory in which the gerbe structure is non-trivial.

The ambitwistor approach is the most physically motivated; Mason–Skinner (2014) construct a string theory on $\mathbb{PA}$ that naturally produces both helicities.

**Update (2026-06-19) — the $\mathbb{F}_2$-linear route (option 3) is now the main line.** Direction D identifies the mod-2 gerbe class with the framework's family-A class: gerbe non-vanishing over $\mathbb{F}_2$ *is* $[n_a]=\mathrm{Sq}^1\omega\neq0$, governed completely by the master theorem (non-vanishing iff $n\neq4$). So option 3 is **subsumed**, not open. The two genuinely open routes (1 derived-category, 2 ambitwistor) are the **holomorphic / characteristic-0** mechanisms — i.e. the part of this item that lies *across the same $\mathbb{F}_2\to$ char-0 wall* that parks the Amplituhedron line (`insight/amplituhedron_duality.md`). Crossing it is a new program (lifting the framework off $\mathbb{F}_2$), not a backlog cleanup.

---

### 12. The $PSL(2,7) \leq PSp(6, \mathbb{F}_2)$ Bridge: Klein Quartic and Paper IX (Paper VIII §7, Paper IX)

**Status:** The Klein quartic $X(7)$ (genus-3 Riemann surface, automorphism group $PSL(2,7) \cong GL(3,\mathbb{F}_2)$ of order 168) was proposed in Paper VIII §7 as a geometric bridge to mock modular forms. However, $PSL(2,7)$ does **not** embed in $PSp(4,\mathbb{F}_2) \cong S_6$ (the 2-qubit automorphism group, order 720; $168 \nmid 720$, and $S_6$ has no elements of order 7).

The correct home is the 3-qubit framework: $|PSp(6,\mathbb{F}_2)| = 1{,}451{,}520 = 2^9 \cdot 3^4 \cdot 5 \cdot 7$ and $1{,}451{,}520 \div 168 = 8640$. The embedding exists explicitly via **hyperbolic doubling**:
$$GL(3,\mathbb{F}_2) \hookrightarrow Sp(6,\mathbb{F}_2), \quad g \mapsto \begin{pmatrix} g & 0 \\ 0 & g^{-T} \end{pmatrix}$$
This carries the Fano plane $PG(2,2)$ (7 points of $\mathbb{F}_2^3 \setminus \{0\}$) as an isotropic subgeometry of $W(5,\mathbb{F}_2)$.

The conjectural chain for Paper IX:
$$W(5,\mathbb{F}_2) \xrightarrow{\text{Aut}} PSp(6,\mathbb{F}_2) \supset GL(3,\mathbb{F}_2) \cong PSL(2,7) = \text{Aut}(X(7)) \longrightarrow X(7) \longrightarrow \text{mock modular forms}$$

**What's needed:**
- Identify the 3-qubit PM-like configuration (the 3-qubit analogue of the PM square) whose contextuality class $[f_3] \in H^1(K_{\text{3-qubit}}, \mathbb{Z}/2)$ is stabilized by $GL(3,\mathbb{F}_2)$.
- Construct the 3-qubit transgression $\Phi_3: H^1 \to H^2(\mathbb{CP}^7, \mathbb{Z}/2)$ and prove $\Phi_3^*([f_3]) = c_1(\mathcal{O}(1)) \bmod 2$.
- Identify mock modular forms as signatures of the $H^1$ obstruction, using the fact that $X(7)$ is the modular curve $\mathcal{H}/\Gamma(7)$ and the Ramanujan $\tau$-function has $p$-adic structure related to $GL(3,\mathbb{F}_2)$-representations.

**Update — STEPS 1–3 DONE (2026-06-16, `supplementary/klein/`).**
- **Step 1 — the bridge (computed):** built $GL(3,\mathbb F_2)$ ($|G|=168$) and its symplectic Siegel/Levi embedding in $Sp(6,\mathbb F_2)$; verified it is the unique simple group of order 168 (perfect + 2-transitive on the Fano plane) $\cong PSL(2,7)=\mathrm{Aut}(X(7))$. Orbit decomposition of the 63 three-qubit Pauli classes: $7$ (Fano) $+\,7$ (dual) $+\,21$ (flags) $+\,28$ (anti-flags) $=63$.
- **Step 2 — the hinge is a theorem:** the size-28 orbit $\cong$ **the 28 bitangents of the Klein quartic** as $PSL(2,7)$-sets, via the explicit $G$-equivariant bijection $v\mapsto Q_v=q_0+\omega(v,\cdot)$ (the 28 bitangents = 28 odd theta characteristics; $\mathrm{Arf}(Q_v)=q_0(v)$). The embedding is *forced, not chosen*: the only faithful 6-dim symplectic $\mathbb F_2$-rep of $PSL(2,7)$ is $3\oplus3'$ = the curve's $J[2]=H^1(X;\mathbb F_2)$ action.
- **Step 3 — $[f_3]$ and $\Phi_3$:** theta characteristics (spin structures, the $H^1(X;\mathbb F_2)$-torsor) split $1+7+7+21$ (even) $+\,28$ (odd); the unique $G$-fixed one is $[f_3]=q_0=x\cdot z$ — the framework's standard quadratic refinement (APP_06 "i-phase") = the curve's canonical $PSL(2,7)$-invariant spin structure. The transgression $\Phi_3$: $q_0$ polarizes to $\omega$ (the Weil pairing, $G$-invariant), and $\mathrm{Sq}^1\omega=N_{\mathrm{anti}}$ — so **the Direction-D spiral $q_0\to\omega\to N_{\mathrm{anti}}$ is $PSL(2,7)$-equivariant, based at $q_0$. The Klein line meets item 23.**

**Residual (the reach):** the $\tau$ end — $X(7)$'s 24 cusps ($168/24=7$), $\Delta=\eta^{24}$, mock-modular signatures — is genuine analytic number theory, not a quick computation. (Honest caveat: $[f_3]$ here = the natural theta/spin invariant at the $H^1$ level; a cross-check against Paper IX's precise $[f_3]$ is noted.)

**Update (2026-06-19) — the seam is now sharp.** The $\mathbb{F}_2$ / finite-geometry core of this bridge is **harvested**: steps 1–3 take it all the way ($W(5,2)\to$ 28 bitangents $\to q_0=[f_3]\to$ the $PSL(2,7)$-equivariant spiral $q_0\to\omega\to\mathrm{Sq}^1\omega$), landing *inside* the Direction-D capstone (item 23). What remains — the $\tau$ end — is the **characteristic-0** half, behind the same wall as item 11 and the Amplituhedron line. Tell: the "24" (cusps of $X(7)$ over $\mathbb{C}$) never appears in the finite picture (Pauli orbits $7{+}7{+}21{+}28{=}63$; theta characteristics $64$), confirming it is across the seam, not a quick extension of the finite work.

---

### 13. Higher Differentials $d_k^{\text{eff}}$ for the $n$-Qubit Obstruction Ladder (RESOLVED — family-B only, Paper VIII §3)

**Status (original):** Paper VIII establishes the 2-qubit case ($d_2^{\text{eff}}$) explicitly and conjectures a general pattern for $n \geq 3$. For $n=3$ (3-qubit, $W(5,\mathbb{F}_2)$, 315 MASAs), the higher differential $d_3^{\text{eff}}$ should pair the contextuality class with a cohomology class on $\mathbb{CP}^7$. Three obstacles were flagged:
1. No 3-qubit PM-like configuration (with the right symmetry and product $-\mathbf{I}$) has been explicitly identified.
2. The Ext computation $\mathrm{Ext}^2_{\mathcal{O}_{\mathbb{CP}^7}}(\mathcal{O}, \mathcal{O}(k))$ for the relevant $k$ has not been performed.
3. The cup product target $c_2(\mathcal{O}(1)) = 0$ (since $\mathcal{O}(1)$ is a line bundle, all Chern classes $c_k = 0$ for $k > 1$), so the $n \geq 3$ target cannot be a higher power of $c_1$; a different characteristic class is needed.

**Update — RESOLVED (2026-06-20, `supplementary/twistor_cp/`).** $H^*(\mathbb{CP}^N;\mathbb F_2)=\mathbb F_2[h]/h^{N+1}$, $|h|=2$, is concentrated in **even degree** and is $\mathrm{Sq}^1$-**acyclic**: $\mathrm{Sq}^1 h=0$ (as $h=c_1(\mathcal O(1))\bmod2$ is an integral reduction), $\mathrm{Sq}^2 h=h^2$. Its whole Steenrod structure is the $\mathrm{Sq}^2$/cup-power ladder. Against the framework's $\omega\in H^2(V)$ (family B) and $n_a=\mathrm{Sq}^1\omega\in H^3(V)$ (family A):
- **The conjectured ladder exists — as family B.** $d_k^{\text{eff}}$ is the cup-power ladder $h^k\leftrightarrow\omega^k$; Theorem 2.1 ($h\leftrightarrow$ PM class) is its $k=1$ case (PM *is* family B). *Obstacle 3 resolved:* the target is the cup-power $h^k=c_1^k$ (nonzero), **not** the Chern class $c_k$ (zero for a line bundle) — the obstacle conflated $c_1^2$ with $c_2$.
- **The family-A $H^3$ Borromean class is not faithfully realizable on $\mathbb{CP}^{2^n-1}$.** The identification $h\leftrightarrow\omega$ is a ring iso onto $\mathbb F_2[\omega]$ but **not** a Steenrod-module map: it fails at the generator, $\mathrm{Sq}^1 h=0$ vs $\mathrm{Sq}^1\omega=n_a\ne0$ (verified: $\mathrm{Sq}^1(\omega^{2j})=0$ matching $h^{2j}$, but $\mathrm{Sq}^1(\omega^{2j+1})=\omega^{2j}n_a\ne0$, unmatchable on $\mathbb{CP}$). Equivalently $\omega$ does not lift to an integral (Chern) class — the obstruction is $\beta\omega=\mathrm{Sq}^1\omega=n_a$. *The family-A class is precisely the Steenrod obstruction to the family-B geometric realization being natural.*
- *Obstacle 1 dissolved:* the Mermin pentagram is the 3-qubit config; the "different combinatorics" is the family A/B split. *Obstacle 2 redirected:* the pentagram's Čech nerve collapses (Paper XX), so the obstruction lives on the Maslov–Wall complex $\partial\Delta^4=S^3$, not on $\Sigma_0^{(n)}\subset\mathbb{CP}^{2^n-1}$ — the Ext object is the wrong home.

**Verdict:** the geometric/twistor side hosts $\mathrm{Sq}^2$ (family B) and is structurally **blind** to $\mathrm{Sq}^1$ (family A) — the geometric face of item 24's operational orthogonality and the $A\!\leftrightarrow\!B$ / $\mathrm{Sq}^1$ wall of item 23.

---

### 14. The $\Phi_* \dashv \Phi^*$ Adjunction for a Transgression (RESOLVED — derived, equivalence iff $n=4$; Paper VIII §5)

**Status (original):** Paper VIII §5 proposes that the transgression functor $\Phi$ gives rise to a sheaf adjunction $\Phi_* \dashv \Phi^*$ realizing Paper V's $\mathcal Q\dashv\mathcal B$. It is flagged conjectural because transgression is degree-shifting, not a map of spaces, so $f_* \dashv f^*$ does not directly apply. Two routes were proposed: (a) realize $\Phi$ as a geometric morphism of toposes; (b) reformulate in $D^b$ via Fourier–Mukai.

**Update — RESOLVED (2026-06-20, `insight/the_adjunction.md`).** Route (b), made precise — and the only gap was $\tau$. Paper VIII §5 already supplies $\iota_!\dashv\iota^*\dashv\iota_*$ (Kan extensions) and $\ell_*\dashv\ell^!$ (Grothendieck duality), flagging *only* $\tau$ as lacking an adjoint. But the clutching $S^2=\Sigma S^1$ makes $\tau$ the **suspension isomorphism** — an equivalence (stably $\Sigma\dashv\Omega$), trivially self-adjoint. So all three factors are adjointable and the composite is: $\Phi_*=\ell_*\tau\iota^*$ has right adjoint $\Phi^*=\iota_*\tau^{-1}\ell^!$. **The degree shift is not an obstruction to the adjunction — it *is* one ($\Sigma\dashv\Omega$).**
- **Free $\dashv$ forgetful.** The pair realizes $\mathcal Q\dashv\mathcal B$: $\mathcal Q=\Phi_*$ (quantization, free), $\mathcal B=\Phi^*$ (Bohrification, forgetful). $\mathcal B$ is exactly the one-wall forgetful functor (item 24, `the_one_wall.md`) — the arrow dropping the $\mathrm{Sq}^1$ step. So item 14 gives the wall its left adjoint.
- **Equivalence iff $n=4$.** The adjunction is an adjoint equivalence iff its counit $\varepsilon:\mathcal Q\mathcal B\to\mathrm{id}$ is iso, i.e. iff Bohrification loses nothing; the counit defect is the forgotten $\mathrm{Sq}^1$ data $=n_a$, which vanishes universally exactly at $n=4$ (master theorem). This is the categorical face of `why_the_ladder.md` §6 ($\infty$-Yoneda free $\iff n=4$) and the literal fulfillment of item 23's "saturation + modulus = one adjunction" line. For $n\ge5$ the defect = the modulus (Paper XIX).

**Verdict:** the adjunction exists (✅ rigorous — derived category, $\tau$=suspension); it is free $\dashv$ forgetful and an equivalence iff $n=4$ (the $[n_a]=0\iff n=4$ signature is a theorem; identifying the counit defect with $n_a$ at cochain level rests on item 23). The forgetful $\mathcal B$ (item 24), its free adjoint $\mathcal Q$ (this item), and the obstruction to their being inverse ($n_a$, item 23) are one picture seen three ways.

---

### 15. The $n$-Qubit Cross-Context Anticommutation Theorem (Paper XVII, Open Problem 1)

**Status:** Paper XVII proves that for any $K_5$ configuration of Lagrangians in $Sp(6,\mathbb{F}_2)$ (the 3-qubit case), all 15 cross-context ray pairs satisfy $\omega(v_{ij},v_{kl})=1$. The proof uses a size argument: 10 rays cannot be mutually isotropic because any totally isotropic subspace of $\mathbb{F}_2^6$ has at most $2^3-1=7$ nonzero vectors, and $10>7$.

**Why it fails for $n\geq 4$:** For $n$ qubits, a Lagrangian in $\mathbb{F}_2^{2n}$ has $2^n-1$ nonzero vectors. For $n=4$: $2^4-1=15\geq 10$, so the size argument fails. A $K_5$ of Lagrangians in $Sp(8,\mathbb{F}_2)$ might admit mutually isotropic cross-context rays. The question is whether the Cross-Context Anticommutation Theorem holds for $n\geq 4$ (via a different proof) or genuinely fails.

**What's needed:** Either (a) prove the theorem for all $n$ via a structural argument not relying on the dimension bound, or (b) exhibit an explicit $K_5$ of Lagrangians in $Sp(8,\mathbb{F}_2)$ with $c=0$ (an "even $K_5$"). The latter would imply that the KS obstruction is not universal for $n$-qubit systems with $n\geq 4$.

**Update — RESOLVED (Papers XVIII–XXI):** the theorem does not extend as uniform anticommutation. Paper XVIII proves that at $n=4$ every proper $K_5$ has $N_{\mathrm{anti}}=10$ (not $15$) universally, via three $K_4$-level lemmas (B0/B1/B2); Paper XIX exhibits the $n\ge5$ **modulus** (both parities of $N_{\mathrm{anti}}$ occur, with an explicit witness pair); Paper XXI's master theorem shows universal $N_{\mathrm{anti}}=10$ holds **iff $n=4$**. So "even $K_5$s" abound for $n\ge5$ and the KS count is non-universal beyond $n=4$ — but its $\bmod\,2$ reduction is exactly the $H^3$ class of Paper XX (see items 19–24).

---

### 16. KS No-Coloring and the Petersen = Kneser $K(5,2)$ Structure (Paper XVII, Open Problem 2)

**Status (corrected 2026-06-14):** The 15 cross-context ray pairs of any Mermin pentagram form the edge set of the Petersen graph, which **is the Kneser graph $K(5,2)$** (vertices = 2-subsets of $\{1,\dots,5\}$ = the 10 rays; edges = disjoint pairs). The KS theorem asserts the 10-ray system admits no binary valuation consistent with the commutativity constraints.

> ⚠️ **Correction.** An earlier version of this item claimed Petersen is "non-3-colorable ($\chi=4$)." That conflates vertex and edge coloring. Petersen is **3-vertex-colorable**: $\chi=3$, exactly the Kneser value $n-2k+2=3$. What is special is that it is the **smallest snark** — bridgeless cubic and *not 3-edge-colorable*, $\chi'=4=\Delta+1$. So the KS link cannot run through generic vertex non-3-colorability.

**Two rigorous routes to re-pose the connection:**
1. **Snark / edge-coloring.** The genuine "impossibility" property of Petersen is the snark property ($\chi'=4$). If the KS no-valuation maps to non-3-edge-colorability, that is the precise graph-theoretic witness.
2. **Borsuk–Ulam / Kneser (the deep one).** Lovász: $\chi(G)\ge \mathrm{ind}_{\mathbb Z/2}(B(G))+2$, tight on Kneser graphs ($\chi(K(n,k))=n-2k+2$). So on $K(5,2)$ the chromatic number *is* a $\mathbb Z/2$ cohomological (Stiefel–Whitney) obstruction. This is "coloring = cohomology" rigorously, sitting exactly on XVII's graph.

**Honest caveat (Abramsky frame).** KS-no-valuation and graph-coloring share a *form* (no global section on a 1-dim nerve, Abramsky sheaf cohomology) but differ in *coefficient system* (Pauli central $\pm1$ vs a coloring constraint sheaf). They are **siblings**, likely not literally the same class — so the goal is the precise relation, not an identification.

**What's needed:** decide which route (snark vs Borsuk–Ulam) actually carries the KS obstruction, or formalize the sibling relation in the Abramsky framework. For the `n/` payoff, connect to **Herlihy–Kozlov–Rajsbaum distributed-computing topology** (chromatic subdivision; colors = process IDs), the rigorous body linking coloring → topology → distributed solvability that should sit behind APP_07's $H^2/H^3$ rows. See `research/insight/moser_spindle_d2.md` (revised).

---

### 17. Weil Representation Unification of Context- and Pentagram-Level Signs (Paper XVII, Open Problem 4)

**Status:** The series has identified two levels of the KS obstruction:
- **Context level** (Paper XVI): $W_C = s(C)\cdot I_8$, where $s(C)=(-1)^{\beta(C)/2}$ is the Weyl product sign — realised by the Weil representation of $Sp(6,\mathbb{F}_2)$ on $\mathbb{C}^8$.
- **Pentagram level** (Paper XVII): $\prod_C s(C)=-1$, realised by the Petersen graph anticommutation structure.

**What's needed:** A single Weil-representation-theoretic statement encoding both levels. The 5-cycle of the Petersen graph selected by the product ordering (Remark 4.3 of Paper XVII) is a combinatorial shadow of the $K_5$ geometry; there should be a representation-theoretic reason that the 5-cycle count is odd. A character-theoretic or cohomological statement in terms of the Weil representation of $Sp(6,\mathbb{F}_2)$ would unify Papers XVI and XVII into a single theorem.

---

### 18. Symplectic Geometry Beyond $\mathbb{F}_2$: Analogs over $\mathbb{F}_q$ (Paper XVII, Open Problem 3)

**Status:** The entire Mermin pentagram program (Papers X–XVII) is specific to $\mathbb{F}_2$: the Fano zero-sum property ($v_1\oplus\cdots\oplus v_4=0$) uses the fact that $\mathrm{char}=2$, and the Lagrangian size bound uses $|L\setminus\{0\}|=2^3-1=7$.

**What's needed:** Determine which results extend to $Sp(6,\mathbb{F}_q)$ for odd primes $q$:
- The Fano zero-sum analog requires a context-level identity in $\mathbb{F}_q^6$; it is not clear what replaces $v_1\oplus\cdots\oplus v_4=0$ for $q>2$.
- The Weyl operator algebra over $\mathbb{F}_q$ uses $q$-th roots of unity; the commutation relation $W(v)W(w)=\zeta^{\omega(v,w)}W(w)W(v)$ with $\zeta$ a primitive $q$-th root may alter the product structure.
- Are there "even $K_5$s" over $\mathbb{F}_q$ for $q>2$? If so, what is their density?

---

### 19. The Degree Ceiling: Why $H^3$ and Not $H^4$ (RESOLVED, Paper XXII)

**Status: RESOLVED.** A standing worry was whether the ladder continues $H^3\to H^4\to\cdots$. Paper XXII's **arity–resonance principle** answers no: the anticommutation datum is intrinsically a 3-cochain, so on a proper $K_6$ (nerve $S^4$) its degree-4 assembly $\mathbf c$ is the *exact coboundary* $\delta\mathbf a$, and the $H^4$ class vanishes for every proper $K_6$ (which do exist). The pentagram is the unique resonance; the ladder is a two-rung tower ($K_4/H^2$, $K_5/H^3$) with a lid. The sphere $S^4$ carries $H^4$ topologically, but the symplectic data does not climb it.

**Residual:** whether genuinely higher-arity (irreducible 5-Lagrangian) data — not furnished by a bilinear form — could reach $H^4$ on some other configuration (see item 21).

**Update — the $\mathbb Z/4$-Bockstein route is also closed (2026-06-16, `supplementary/bockstein/`).** Objection: the Pauli phase is $\mathbb Z/4$ (not $\mathbb F_2$), so the Bockstein of $0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0$, $\beta:H^3(\cdot;\mathbb F_2)\to H^4(\cdot;\mathbb F_2)$, might leak the $H^3$ class to $H^4$. Resolution: $\beta=\mathrm{Sq}^1$, and the family-A source is itself a Bockstein, $n_a=\mathrm{Sq}^1\omega$, so $\beta(n_a)=\mathrm{Sq}^1\mathrm{Sq}^1\omega=0$ ($\beta^2=0$, Adem) — *verified* on $V=(\mathbb Z/2)^8$. Moreover $H^*(V;\mathbb Z)$ has exponent 2 (no $\mathbb Z/4$ torsion), so $H^*(V;\mathbb F_2)$ is $\mathrm{Sq}^1$-acyclic in positive degrees ($\mathrm{Sq}^1$-cohomology $H^3=H^4=0$, verified) — the Bockstein has no room to make a new obstruction. So the ceiling is **not** an $\mathbb F_2$ artifact; it is controlled by $\beta^2=0$, a fact about the $\mathbb Z/4$ structure itself. (Contingent on $n_a$ being $\mathrm{Sq}^1$-closed = item 23; the exotic non-bilinear route = item 21.)

---

### 20. Even-$n$ Equidistribution of the $H^3$ Class (Open, Partial)

**Status:** For even $n\ge6$ the $H^3$ class $N_{\mathrm{anti}}\bmod2$ is empirically a fair coin, carried by $\mathbf a$ alone (Paper XXI). Partial results: the class reduces to a sum of foot-functional bits $\Sigma=b_1\oplus b_2\oplus b_3$, and the **uniform-foot lemma** (the stabiliser of a Lagrangian surjects onto $\mathrm{GL}(L)$, transitive on $L\setminus\{0\}$) gives a single-constraint foot-bit bias of exactly $1/(2^n-1)$. The fair-coin behaviour is then a **piling-up** (XOR of weakly-biased near-independent bits) phenomenon.

**What's needed:** bound the foot-bit bias and correlations under the *simultaneous* constraints (the multi-constraint foot map $L_4\mapsto(v_{14},v_{24},v_{34})$), upgrading the asymptotic fair coin to a theorem. The per-value distribution is *not* uniform (it peaks at $a_m=2$); the statement concerns the parity only.

---

### 21. The Arity-5 Lid (Open)

**Status:** The truncation theorem (item 19) shows the *bilinear* (Maslov/anticommutation) data tops out at arity 4. Paper XIX's quadruple invariant $q_4$ is itself arity-4 and empirically saturated.

**What's needed:** prove there is no *irreducible* arity-5 symplectic $\mathbb{F}_2$ invariant of five Lagrangians — i.e. that the symplectic form generates nothing genuinely 5-ary. This upgrades the truncation from "the natural data does not climb" to "no natural data can," making $H^3$ a provable hard ceiling for Pauli contextuality.

**Why it is genuinely hard (2026-06-20).** This is a *generation / non-existence* theorem in **modular ($\mathbb F_2$) invariant theory of $\mathrm{Sp}(2n,\mathbb F_2)$ acting on tuples of Lagrangians** — exactly where classical invariant theory has no clean fundamental theorem. (i) The easy argument is false: $\omega$ is bilinear but *products* of pairwise terms span $\ge5$ indices (e.g. $\omega(v_{12},v_{34})\,\omega(v_{15},v_{23})$ uses $\{1,2,3,4,5\}$), so "built from $\omega$" does not bound arity. (ii) The objects are *subspaces* (Lagrangians), not vectors, so the Weyl FFT does not apply; relative position (Maslov/Wall) is richer. (iii) Char 2 admits exotic invariants with no char-0 analog (Arf, Dickson, the $q_4$ of Paper XIX), so the invariant ring cannot be assumed nice — proving "nothing exotic survives" in a ring known to harbour exotica, and not yet classified, is the crux. (iv) The modulus (Paper XIX) shows arity-4 data is genuinely incomplete ($n_a$ itself is a bilinear quantity escaping arity-4), so the reducible/irreducible boundary is delicate: one must exclude a *non-bilinear* $H^4$ escape while admitting the bilinear $H^3$ class. (v) It must hold for all $n$, but the invariant theory grows with $n$.

**Disposition — PARKED for a future (XXIII-level) treatment.** A feasibility estimate (2026-06-20) shows the computational route cannot reach the theorem: at $n=5$ raw enumeration is hopeless ($\#$Lagrangians $=75{,}735$; 5-tuples $\sim10^{24}$, 6-tuples $\sim10^{29}$; even fixing $L_1$, 4-tuples $\sim10^{19}$), and the Paper-XIX *sampling* method (which found the modulus *positively*) is the wrong tool for a *non-existence* claim — and worse, the search space of non-bilinear arity-5 invariants is unparametrized. A bounded check (extend Thm 5.2's "$\delta a$ exact" to an explicit finite list of candidate arity-5 invariants) was considered but only nudges confidence, not the theorem. The genuine path is route 1: a first/second fundamental theorem for $\mathrm{Sp}(2n,\mathbb F_2)$ on Lagrangian tuples — a modular-invariant-theory project, not a computation. **Item 21 and item 23 are the two genuine open frontiers, and likely co-dependent:** if the item-23 comparison map ($n_a=\mathrm{Sq}^1\omega$) is established, the Steenrod-algebra action on $H^*(V;\mathbb F_2)$ would give the ceiling a structural reason (no new Steenrod source past $\mathrm{Sq}^1\omega$; the $\mathbb Z/4$-Bockstein route is already closed, item 19), bearing directly on item 21.

---

### 22. Family-B Resonance and the Contextuality Taxonomy (RESOLVED — no separate tower; family B is family A's floor)

**Status (original):** Paper XXII shows contextuality configurations split (at least) into two cohomological families by the incidence clique number: **family A** (all-pairwise $K_N$, anticommutation, ceiling $H^3$ at the pentagram) and **family B** (bipartite/triangle-free, central-extension sign class — e.g. the Mermin–Peres square, six Lagrangians in $Sp(4,\mathbb{F}_2)$ with $K_{3,3}$ incidence, at $H^2$). The Outlook asks: does a larger bipartite $K_{m,n}$ carry a degree-3 central-extension class (the family-B analogue of "why the pentagram")?

**Update — RESOLVED (2026-06-20, `supplementary/familyB_resonance/`): there is no family-B resonance; family B is the $\omega=2$ floor of family A's single tower.** The clique criterion already settles it, because a **complete $r$-partite graph has clique number exactly $r$**:
- **Enlarging a bipartite $K_{m,n}$ keeps $r=2$**, so the family-A ceiling $\min(\omega-2,3)$ stays $0$ for *every* grid size — a bipartite incidence is triangle-free $=$ a $1$-dimensional clique complex for all $(m,n)$ ($b_1=(m-1)(n-1)$, $H^{\ge2}=0$); it cannot climb.
- **The only way to raise the ceiling is to add context-classes** (complete $r$-partite incidence), but $\omega=r$ is governed by the *same* clique criterion (family A), topping at $H^3$ when $r=5$ — and the complete 5-partite graph with singleton parts *is the pentagram* $K_5=K_{1,1,1,1,1}$. ($r\ge6$ caps at $H^3$ by item 19/21.)
- **The family-B class is $\omega\in H^2$** (the central-extension $\pm I$ bit); the only ascent to degree 3 is $\mathrm{Sq}^1\!:H^2\to H^3$, and $\mathrm{Sq}^1\omega=n_a$ is the **family-A** class. So the family-B$\to$degree-3 ascent *is* the $A\!\leftrightarrow\!B$ unification — **Outlook Q1 collapses into Q2 (item 23)**, not a bigger grid.

**Verdict:** the taxonomy's "two families" is one tower with family B as its $\omega=2$ floor, joined to family A by $\mathrm{Sq}^1$. *Classification by incidence type:* a configuration's family-A content is $\min(\omega(G)-2,3)$ in its incidence clique number $\omega(G)$; $\omega=2$ (triangle-free) $\Rightarrow$ family B (central extension only); $\omega\ge3 \Rightarrow$ family A up to its ceiling. Verified: complete $r$-partite clique tower; the Mermin square as the $\omega=2$ floor (isotropic, $K_{3,3}$, triangle-free, $\mu/\mathbf a$ undefined, global product $-I$ via explicit $4\times4$ Pauli matrices).

---

### 23. The $A\leftrightarrow B$ Unification: The Self-Representation Map (Open — Capstone)

**Name (2026-06-20).** What earlier drafts called the "homotopy-coherent comparison map" is better named **the self-representation map** — it is not a comparison of two objects but a structure represented in its own terms, and the obstruction $\mathbf a=n_a$ is whether that self-representation is *coherent*. It is **one gear with three faces**: *as an operation* it is $\mathrm{Sq}^1\!:H^2\to H^3$ (the unique structure-adding arrow); *as a functor* it is the quantization $\mathcal Q$ of item 14 (the free left adjoint, with $n_a$ the counit defect of $\mathcal Q\dashv\mathcal B$ being an equivalence); *as a pairing* it is the $\infty$-Yoneda self-pairing ($n_a=\langle\mathrm{Sq}^1\omega,[K_5]\rangle$, the framework explaining its top floor in its ground-floor vocabulary — cf. `insight/why_the_ladder.md` §6, `insight/alpha_fixed_point.md`). "The one wall" is this seen from outside (six doors hit it); "the self-representation map" is the same seen from inside (the structure in its own mirror). $n=4$ is the unique dimension where the self-representation is coherent.

**Status:** The two families are conjecturally pages of one Lyndon–Hochschild–Serre spectral sequence (the Heisenberg extension), with $\omega\in H^2(V)$ (family B) transgressing and $\mathrm{Sq}^1\omega\in H^3(V)$ the candidate family-A source. The proposed bridge is the pairing $N_{\mathrm{anti}}\bmod2=\langle\mathrm{Sq}^1\omega,[K_5]\rangle$, with the $n=4$ rigidity recast as: pentagram 3-cycles annihilate $\mathrm{Sq}^1\omega$ until $V$ is large enough. The nerve-side cup-1 shortcut $\mu\cup_1\mu$ is **ruled out** (Paper XXII §Outlook): $\mu$ is not a cocycle off the resonance.

**What's needed:** construct the **self-representation map** (the homotopy-coherent map) $\partial\Delta^4\to BV$ whose coherence obstruction is precisely $\mathbf a$ — the rays fail to compose ($v_{ij}+v_{jk}\ne v_{ik}$ off Fano triangles), so no *strict* simplicial map exists — and verify the pairing; equivalently, prove Paper XV's Weil/metaplectic 2-cocycle is the geometric transgression carrying the $H^2$ class to the $H^3$ class. This is the genuinely $\infty$-categorical heart of the unification.

**Update — the capstone sharpened (2026-06-16)** (no proof of the map yet; still the open wall):
- **Forgetful-functor sorting.** Most "comparison map" worries are actually *forgetful* (lossy) arrows, not equivalences: the framework→operational functor (and the coarser detect-or-not cohomologies) **forget** obstruction degree above the threshold — nothing to "solve" there (cf. item 24's saturation; saturation + the modulus theorem form one adjunction, the forgotten data = what the modulus says is unrecoverable). The **unique** structure-*adding* arrow is $\mathrm{Sq}^1\!: H^2\to H^3$ — this map, item 23 — so it is the only genuine equivalence question in the zoo.
- **The self-description reading (the "why").** $N_{\mathrm{anti}}=\langle\mathrm{Sq}^1\omega,[K_5]\rangle$ is a **representability** statement: $N_{\mathrm{anti}}$ is represented by one universal class $\mathrm{Sq}^1\omega$ built from the framework's *own* $\omega$ — the ∞-Yoneda move. Item 23 is the framework explaining its top floor ($H^3$) in the vocabulary of its ground floor ($\omega$, $H^2$); $\mathbf a$ is exactly the coherence obstruction to that self-representation.
- **A second, geometric face (item 12, step 3).** The spiral $q_0\to\omega\to\mathrm{Sq}^1\omega$ is realized $PSL(2,7)$-equivariantly as the Klein quartic's intrinsic automorphism geometry, based at its canonical spin structure $q_0$. So the $A\!\leftrightarrow\!B$ unification and the Klein-quartic bridge are two faces of one capstone. See `insight/why_the_ladder.md` §6, `insight/quantum_applications.md` §7, `supplementary/klein/`.
- **A third, twistor face (item 13).** The same $\mathrm{Sq}^1$ wall reappears on $\mathbb{CP}^{2^n-1}$: the geometric realization $h\leftrightarrow\omega$ carries the family-B cup-power ladder ($\mathrm{Sq}^2$) but cannot be Steenrod-natural, the obstruction being $n_a=\mathrm{Sq}^1\omega$ — $\mathbb{CP}$ is $\mathrm{Sq}^1$-acyclic. So the "is $\mathrm{Sq}^1$ a genuine arrow?" question of item 23 is exactly "why is the twistor space blind to family A?" of item 13. See `supplementary/twistor_cp/`.

**Update — the LHS $d_3$ identity + cleaving the pairing (2026-06-20).**
- **"Two pages of one SS" is a theorem on the $V$-side (Kudo), not a conjecture.** The Heisenberg extension's LHS has $E_2=H^*(V)\otimes\mathbb F_2[t]$ ($|t|=1$, Quillen extra-special); $d_2(t)=\omega$ (family B) and, since $t^2=\mathrm{Sq}^1 t$, Kudo's transgression theorem gives $d_3(t^2)=\mathrm{Sq}^1\omega=n_a$ (family A). So family A $=\mathrm{Sq}^1$(family B) is forced. The sharp non-vanishing is $d_3(t^2)\ne0$ in $E_3^{3,0}=H^3(V)/\omega\!\cdot\!H^1(V)$, i.e. $\mathrm{Sq}^1\omega\notin(\omega)$ — verified: nonzero for all $n\ge2$, zero (in the ideal) at $n=1$. **This settles the $V$-side; it is $n$-independent, so it does NOT carry the $n=4$ rigidity.**
- **The pairing's $n$-dependence is in $[K_5]$, not $\mathrm{Sq}^1\omega$ — and it is a *secondary* operation.** If a *strict* map $f:S^3\to BV$ existed, $f^*\omega\in H^2(S^3)=0$ would force $f^*\mathrm{Sq}^1\omega=\mathrm{Sq}^1(0)=0$, i.e. $N_{\mathrm{anti}}$ always even — false for $n\ge5$. So no strict map exists *essentially*; the pairing is a **secondary (functional/Massey-type) operation**, primary part forced to vanish, all $n$-dependence in the coherence data. (A priori reason the naive cup-1 $\mu\cup_1\mu$ failed: it is a primary-looking guess missing the non-strictness corrections.)
- **The carrier is the ray Gram / $(W,\omega|_W)$ = Paper XIX's order parameter.** $N_{\mathrm{anti}}$ is a function of the $10\times10$ ray Gram $G_{(ij),(kl)}=\omega(v_{ij},v_{kl})$, equivalently of $(\dim W,\mathrm{rank}\,G,\dim\mathrm{rad}\,W)$ for $W=\langle v_{ij}\rangle$. Spread-stabilisation keeps the rays in the $V$-summand ($(L_i\oplus U_i)\cap(L_j\oplus U_j)=v_{ij}\oplus0$), so it preserves $G$ *entrywise* — invisible to any Gram-function (this is why padding cannot move the pairing). The $n$-dependence is *which $G$ are realizable at $\dim n$* (the $2n=8$ squeeze forces even at $n=4$).
- **Zero indeterminacy $=$ resonance: the bridge is an *exact* equation.** The functional $\mathrm{Sq}^1_f(\omega)$ has indeterminacy $f^*H^3(BV)+\mathrm{Sq}^1 H^1(S^3)$; both die, each for an elementary "thinness" reason. (i) $\mathrm{Sq}^1 H^1(S^3)=0$ since $H^1(S^3)=0$ (the nullhomotopy $\beta$ is unique). (ii) $f^*H^3(BV)=0$ **by a dimension count**: the configuration is generators ($v_{ij}$) + relations (symplectic pairings), so the honest classifying map factors through the 2-skeleton $BV^{(2)}$, which has no 3-cells, hence $H^3(BV^{(2)};\mathbb F_2)=0$ — this kills *all* of $H^3(BV)$ wholesale (even $\mathrm{Sq}^1$-irrelevant cubics like $x_1^3$), not via any property of $\mathrm{Sq}^1$, and without invoking "every map is null" ($BV=K(V,1)$ agrees but is not needed). So the secondary class is a *single rigid bit* in $H^3(S^3)=\mathbb F_2$ and $N_{\mathrm{anti}}\bmod2=\mathrm{Sq}^1_f(\omega)$ is an exact equality (no coset). **This is the *same fact* as resonance:** the nerve $S^{N-2}$ has cohomology only in $\{0,N-2\}$, and that thinness gives both the single top class (resonance) *and* the zero indeterminacy (rigidity) — $\beta$-uniqueness ($H^1=0$) **is** the no-middle-cohomology that defines $N=a+1$.
- **The strict/lax divide is the skeleton boundary.** The dimension argument also *locates* why the bridge must be lax: the 2-skeleton (gens+relations) is the strict part and is $H^3$-blind by dimension; the 3-cells (the five tetrahedra) are the lax coherence fillers, the *only* place $H^3$ content — hence $n_a$ — can live. So "the pairing must be a secondary/lax operation" is not an abstract theorem but a direct consequence of the skeleton: strict 1-/2-cell data cannot support $H^3$; seeing $n_a$ requires 3-cell filler data = laxness. (Resolves the apparent tension "$f$ through $BV^{(2)}\Rightarrow f^*\mathrm{Sq}^1\omega=0$" vs "$n_a\ne0$": the dimension count kills the *honest/strict* shadow — exactly the indeterminacy term — while $n_a$ lives in the lax 3-cell data that the strict map discards.) *Honest catch:* the textbook functional operation needs $\mathrm{Sq}^1\omega=0$ in $H^3(BV)$ (false: $=n_a\ne0$), so the real home is the cochain-level *lax* map $\phi:C^*(BV)\to C^*(S^3)$ with $n_a=[\phi(\omega\cup_1\omega)]$; rigidity fixes the answer's uniqueness, not its construction.
- **Net: item 23's open half is "a secondary operation on the known order parameter $(W,\omega|_W)$, computed by the correct (coherence-corrected) cup-1", with four constraints any bridge must meet — secondary (strict$\Rightarrow0$), Gram-carried, spread-stab-invisible, and zero-indeterminacy/exact (= resonance) — not "construct a coherent map from scratch." The target is cleaner than expected (one rigid bit, exact equality); the path is not shorter (the thin sphere gives rigidity but removes the topological crutch).** (`inner/directionD_bridge.md`.)

**Steepness / computational volume (2026-06-21) — compute-light, insight-bound.** Item 23 is a *slope*, not a wall; the steepness is in discovery, not compute. Three segments:
- *Verification basecamp — trivial.* The nerve $\partial\Delta^4=S^3$ is a **fixed, $n$-independent** complex (5/10/10/5 cells; cup-1 a fixed table); per-config secondary-op evaluation is $O(30\text{ bits})$, microseconds. Testing any candidate cochain formula on thousands of sampled $K_5$ at $n=4,5,6$ is **seconds** (the existing scripts' regime).
- *Exhaustive-by-orbit — feasible in size, but only ever evidence.* Empirical $Sp$-orbit scale (distinct fine-signatures, a lower bound): $n=4\to1$ (rigid), $n=6\to\sim25$ (saturated), $n=5\to1251$ **and still growing** at 12k samples (the modulus; likely low-thousands of true orbits after the $S_5$ quotient). So total compute is small (orbits $\times$ microseconds $=$ seconds–minutes), **but** it needs an $\mathrm{Sp}(2n,2)$ canonical-form / orbit enumerator to *guarantee* completeness ($|\mathrm{Sp}(8,2)|\approx4.7\times10^{10}$, $|\mathrm{Sp}(10,2)|\approx2.5\times10^{16}$ — GAP/Magma-scale engineering, not brute orbit–stabiliser), and even a complete $n\le6$ check is *evidence*, not a proof (need all $n$; spread-stab transports only part).
- *The summit — not a computation.* Closing item 23 = construct the lax/$A_\infty$ map $\phi$ and prove $n_a=[\phi(\omega\cup_1\omega)]$ for all $n$: a **discovery** problem (find the coherence-corrected cup-1 formula; the naive $\mu\cup_1\mu$ matches only $\sim57\%$ at $n=5$) plus an all-$n$ symbolic argument. No finite search space to enumerate.
- **Verdict:** horizontal distance (compute) is short — any candidate is testable instantly, and the four constraints + the failure being localised to the 5 tetrahedra heavily prune guesses; the final pitch (the *correct formula* + all-$n$ proof) is vertical and **insight-bound, not compute-bound.** More optimistic than item 21 (which has an unparametrised search space and a non-existence target); here the standard is a precise, instantly-checkable identity. **Best test bed: $n=5$** (the 1000+ modulus stratum, where $\mu\cup_1\mu$ already revealed its gap).

**Update — the $(\mu,F)$-correction family is ruled out (2026-06-21, `supplementary/item23_search/`).** Acting on the parametrized-search idea: solve, by $\mathbb F_2$ linear algebra, whether $a_T$ is *any* degree-$\le2$ polynomial in the per-face Maslov+Fano data $\{\mu(f_0..f_3),F(f_0..f_3)\}$ (37 coeffs; contains $\mu\cup_1\mu$ and Fano-weighted corrections). **Decisively NO** — degree-$\le2$ system inconsistent (33 296/126 500 cochain rows; 10 064/25 300 class rows), and the collision test shows it is *not a degree issue*: $a$ is **not a function of $(\mu,F)$ at any degree** (distinct configs share full $(\mu,F)$ but differ in $a$; at $n=6$, $(\mu,F)$ collapses to one key while $a$ takes all 32 values). **Why:** this is the arity gap — $a$ is arity-4 (ray *pairs*), $\mu,F$ are arity-3 (triangles); the $H^2/H^3$ resonance separation *is* the irreducibility of the arity-4 class to arity-3 data (an empirical shadow of Paper XIX's modulus). **Consequence:** the meta-strategy (parametrize + linear algebra) is sound, fast, reusable — but the natural $(\mu,F)$ family is killed wholesale, *sharpening* the target: the secondary formula must use **arity-4 / ray-pairing (Gram, edge-pair) data**, not Maslov/Fano triangle summaries — the lax map's "nullhomotopy" lives finer than $\mu$. (Explains+generalises the $\mu\cup_1\mu$ failure: not the wrong combination of $\mu$, but $\mu$ is the wrong altitude.)

**Update — the chase's terminus: the symplectic formula-search is *circular* (2026-06-21, `supplementary/item23_search/phi_omega_zero.py`).** Pursuing "use ray-pairing data" hits a structural floor: a *composable* pairing $\omega(v_{ij},v_{jk})$ pairs two rays both in the shared Lagrangian $L_j$, so they commute and it vanishes — verified $0/933000$ across $n=4,5,6$. Hence **$\phi^*\omega\equiv0$ at the cochain level** (so the pulled-back $a=\mathrm{Sq}^1\omega$ has *no primary part* — purely secondary, the strongest form of the lax statement), and **the only nonzero symplectic pairings on the nerve are the disjoint ones, whose matched sum *is* $a$** (defect pairings reduce to these too: $\omega(w_{ijk},v_{il})=\omega(v_{jk},v_{il})$). So every symplectic expression in the rays/defects is a linear combination of the disjoint pairings $=a$ — **any pairing-formula for $a$ is circular.** The lone nonzero *non-symplectic* lower datum is the polarized cocycle / quadratic refinement $q$ ($\mathbb Z/4$ structure), but $\mathrm{cup}_1$ of it matches only $\sim74\%/61\%$, so the correct object is the **$\mathbb Z/4$-Bockstein of $q$** ($\mathrm{Sq}^1\omega=\beta_{\mathbb Z/4}$). **Net: the chase confirms "insight-bound" at a *structural* level — the formula-search is provably circular over symplectic data; the bridge content lives in the $\mathbb Z/4$ quadratic-refinement/Bockstein (the lax coherence assembling the defects into $\mathrm{Sq}^1\omega$), genuine $\infty$-categorical work. Identified next step: the chain-level $\beta_{\mathbb Z/4}(q)$ computation (convention-heavy).**

**Update — computable or handwork? The failure ladder is complete (2026-06-21, `q_determinacy.py`).** Tested whether the $q$-layer (quadratic refinement / $\mathbb Z/4$ data, polarized $f$ on composable rays — *non-circular*, far finer than $(\mu,F)$) determines $a$. **No** — witnessed though narrowly: $n=5$ gives 19896 distinct $q$-keys for 20000 configs ($q$ nearly injective) yet **32** split (same $q$, different $a$); $n=6$: 2 splits. So all three natural cochain-level layers fail: **symplectic = circular; $(\mu,F)$ = coarse-fail (arity gap); $q$ = fine-fail (nearly injective, still insufficient).** **Verdict on "computable vs handwork": *verification* is always computable; and no *local/low-arity* summary determines $a$.** *(Wording corrected per collaborator + the next update: the earlier "no cochain-level summary statistic determines $a$" was an overstated universal from finitely many tested families — the honest claim is "every local/low-arity candidate tested fails"; a global closed form does exist, below.)*

**Update — a CLOSED FORM for the family-A class (2026-06-21, `closed_form.py`).** Following the collaborator's lead ($q$ *almost* determines $a$ = the Bockstein signature; the cheap stratum test resolved 15/32 of the $n=5$ $q$-collisions), the missing ingredient was a single **global** term. Exact, all-$n$, elementary:
$$N_{\mathrm{anti}}\bmod2 \;=\; q(T)\;\oplus\;\textstyle\bigoplus_i q(v_i),\qquad T=\bigoplus_i v_i,\ \ q(v)=\mathrm{parity}(X_v\!\cdot\!Z_v).$$
*Proof (all $n$):* $q$ is a quadratic refinement ($q(u{+}v)=q(u)+q(v)+\omega(u,v)$); polarization gives $q(T)=\bigoplus_i q(v_i)\oplus\bigoplus_{i<j}\omega(v_i,v_j)$; composable pairs vanish ($\phi^*\omega\equiv0$), so $\bigoplus_{i<j}\omega=N_{\mathrm{anti}}$. **Verified 24,600/24,600 exact at $n=4,5,6$.** **Attribution:** the *total* formula is **not new** — it is **Paper XI's Proposition (Quadratic form identity)** over the same 10 rays (rediscovered); the new parts are the cochain refinement (below) and the item-23 framing. *Coordinate, not intrinsic* (verified, `basis_invariance.py`): under a symplectic change of basis the individual $q(v_i),q(T)$ change ($\sim97\%$) but the net XOR stays $=N_{\mathrm{anti}}$ ($900/900$) — $\mathrm{Sp}$-invariant combination, frame-dependent summands. This is the ambient/unconditional form of Paper XIX's intrinsic $Q(T)=N_{\mathrm{anti}}$ (S5). The **cochain-level** version (what item 23's pairing needs, $\langle\mathrm{Sq}^1\omega,[K_5]\rangle=\bigoplus_m(n_a)_m$) holds per tetrahedron: $(n_a)_m\bmod2=q(S_m)\oplus\bigoplus_{\text{6 rays of tetra }m}q(v)$, $S_m=\bigoplus_{\text{6 rays}}v$ — **verified 123,000/123,000 exact** — so the family-A *cochain* $n_a$ itself is closed-form in $q$. It corrects the "no summary determines $a$" overstatement: the $q$-collision keys merely lacked the global $q(T)$ (no clash with the modulus — $q(T)$ is arity-10, not low-arity). **For item 23:** a *coordinate* closed form ($q$ is not $\mathrm{Sp}$-invariant; only the net combo is), so not yet the *intrinsic* bridge — but $q$ is the $\mathbb Z/4$ lift of $\omega$ and $\mathrm{Sq}^1\omega=\beta_{\mathbb Z/4}(\omega)$, so this is the explicit $q$-handle the $\beta_{\mathbb Z/4}(q)$ direction predicted; the open step is now to identify $q(T)\oplus\bigoplus_i q(v_i)$ with the chain-level $\langle\mathrm{Sq}^1\omega,[K_5]\rangle$, **both sides explicit** (a checkable identity, not a blind search). *Revised verdict:* item 23 is **more computable** than the chase's terminus implied — the family-A class has a clean closed form; what stays symbolic is the *intrinsic* identification, not the existence of a formula.

---

### 24. The Operational Meaning of the $H^3$ Borromean Class (ANSWERED — structural, not operational)

**Status:** The class $[\mathbf a]\in H^3$ is a rigorous symplectic-geometric obstruction, but its meaning as a *physical* quantity was unknown. Paper IV anticipated it as **Borromean contextuality** — not witnessable by any $\le4$-context subsystem — and Paper XIX's modulus witness (two configurations agreeing on all arity-$\le4$ data, opposite $H^3$ class) is exactly such a pair.

**Update — ANSWERED (2026-06-16): the question was mistyped; $[\mathbf a]$ is structural, not operational.** Three independent operational axes were tested, and $[\mathbf a]$ is **orthogonal** to all three:
- **circuit advantage / magic:** qubit stabilizer contextuality is Gottesman–Knill-simulable — no circuit speedup, no magic-state distillation (Raussendorf–Browne–Delfosse–Okay–Bermejo-Vega, arXiv:1511.08506);
- **holographic reconstruction:** in HaPPY stabilizer codes ($[[5,1,3]]\to[[8,2]]\to[[11,3]]$, `supplementary/adscft/`), the 3-tile bulk is a *faithful* $W(5,\mathbb F_2)$ genuinely carrying $H^3$, yet reconstruction is governed by support/erasure (entanglement wedge) and is **blind** to contextuality;
- **MBQC computational degree:** `supplementary/mbqc/` — non-adaptive l2-MBQC on *any* stabilizer resource caps at algebraic degree 2 (GHZ reproduces the Anders–Browne gate; 1200 random Cliffords never exceed it), and degree 3 is reached by adaptively composing $H^2$ gates, **not** the pentagram. The conjecture "cohomological degree = computational degree" is **refuted**.

The precise reason — *not* "cohomology is non-operational" ($H^2$/the Mermin square *is* operational, Anders–Browne) — is **saturation**: operational axes resolve only the *threshold* ("contextual at all?" $\approx H^2$) and max out there; **none grades by cohomological degree**. So $[\mathbf a]$ is a structural refinement below operational resolution.

**Verdict:** the operational meaning of $H^3$ is that it is a **classifying coordinate + certification depth** (the modulus: unwitnessable below five contexts), *not a power* — the framework's "coordinates, not gadgets" thesis, earned by computation. The Abramsky–Mansfield–Barbosa / Raussendorf sheaf comparison remains as the *formal* comparison map (item 23-adjacent), but the operational-*power* question is closed. **Deepest reading:** $H^3$ is the obstruction to coherent *self-description* (the ∞-Yoneda failure) — see `insight/why_the_ladder.md` §6 and `insight/quantum_applications.md` §7.

---

## How to Contribute

This document is both a guide and an invitation. If you have expertise in any of the areas above — spectral sequences, topos theory, octonions, SAT solving, twistor theory, symplectic finite geometry, or modular forms — the open questions listed here are concrete, well-scoped, and mathematically meaningful.

The full paper series is available in the [`papers/`](papers/) directory. Each "regret" above corresponds to a specific section and conjecture within the papers. Items 1–10 are from Papers I–VI; items 11–14 from Papers VII–IX; items 15–18 from Papers XVI–XVII. Items 19–24 are from Papers XVIII–XXII and form the **current research frontier**.

**Status (2026-06-20).** Resolved: **item 13** (the geometric ladder on $\mathbb{CP}^{2^n-1}$ — *answered: $d_k^{\text{eff}}$ exists as the family-B cup-power ladder $h^k\leftrightarrow\omega^k$; the family-A $H^3$ class is not faithfully realizable, being the Steenrod $\mathrm{Sq}^1$-obstruction to that realization, and $\mathbb{CP}$ is $\mathrm{Sq}^1$-acyclic* — `supplementary/twistor_cp/`), **item 14** (the $\mathcal Q\dashv\mathcal B$ transgression adjunction — *exists in $D^b$ ($\tau$=suspension, $\Sigma\dashv\Omega$), free $\dashv$ forgetful, adjoint equivalence iff $n=4$* — `insight/the_adjunction.md`), **item 15** (Papers XVIII–XXI), **item 19** (the arity ceiling), **item 22** (family-B resonance — *answered: none; family B is the $\omega=2$ floor of family A's clique tower, the ascent to degree 3 is $\mathrm{Sq}^1\omega=n_a$ (family A), so Q1 collapses into Q2* — `supplementary/familyB_resonance/`), **item 24** (the operational meaning — *$H^3$ is a structural classifying coordinate, not an operational power; orthogonal to circuit advantage, holographic reconstruction, and MBQC degree* — `supplementary/{adscft,mbqc}/`). Advanced: **item 12** (the Klein quartic bridge — steps 1–3 done; only the $\tau$ end remains — `supplementary/klein/`); **item 23** (the capstone, sharpened: the zoo sorts into forgetful arrows vs the single structure-adding $\mathrm{Sq}^1$ map, now with *three* faces — algebraic $A\!\leftrightarrow\!B$, the Klein quartic, and the twistor $\mathbb{CP}$ blindness of item 13). **The two genuine open frontiers are items 23** (the $\infty$-categorical $A\leftrightarrow B$ comparison map, the capstone) **and 21** (the arity-5 lid, parked for XXIII; likely co-dependent with 23). Remaining addenda: items 20 (even-$n$ equidistribution bound), the K₄/H² algebraic proof, and the optional XVIII Key Lemma; backlog item 11's holomorphic end is across the $\mathbb{F}_2\to$char-0 wall. The deepest synthesis — $H^3$ as the obstruction to coherent self-description (CAID was Yoneda; the ladder maps where the ∞-Yoneda **is** free) — is recorded in `insight/why_the_ladder.md` §6. The centerpiece is positive: $[n_a]=0$ universally **iff $n=4$**, so coherent self-representation is feasible at *exactly* one dimension; the series is the cartography of that feasibility boundary ($n=3$ partial, $n=4$ free, $n\ge5$ obstructed).

---

*"A theory is only as honest as its list of open problems."*
