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

---

### 13. Higher Differentials $d_k^{\text{eff}}$ for the $n$-Qubit Obstruction Ladder (Paper VIII, §3)

**Status:** Paper VIII establishes the 2-qubit case ($d_2^{\text{eff}}$) explicitly and conjectures a general pattern for $n \geq 3$. For $n=3$ (3-qubit, $W(5,\mathbb{F}_2)$, 315 MASAs), the higher differential $d_3^{\text{eff}}$ should pair the contextuality class with a cohomology class on $\mathbb{CP}^7$. Three obstacles prevent an immediate proof:
1. No 3-qubit PM-like configuration (with the right symmetry and product $-\mathbf{I}$) has been explicitly identified.
2. The Ext computation $\mathrm{Ext}^2_{\mathcal{O}_{\mathbb{CP}^7}}(\mathcal{O}, \mathcal{O}(k))$ for the relevant $k$ has not been performed.
3. The cup product target $c_2(\mathcal{O}(1)) = 0$ (since $\mathcal{O}(1)$ is a line bundle, all Chern classes $c_k = 0$ for $k > 1$), so the $n \geq 3$ target cannot be a higher power of $c_1$; a different characteristic class is needed.

**What's needed:** Identify the correct target characteristic class in $H^{2k}(\mathbb{CP}^{2^n-1}, \mathbb{Z}/2)$ for the $d_k^{\text{eff}}$ differential, and find at least one 3-qubit contextuality configuration to serve as the $n=3$ base case.

---

### 14. The $\Phi_* \dashv \Phi^*$ Adjunction for a Transgression (Paper VIII, §5)

**Status:** Paper VIII §5 proposes that the transgression functor $\Phi$ gives rise to a sheaf adjunction $\Phi_* \dashv \Phi^*$. The standard construction of $f_* \dashv f^*$ requires $f$ to be a continuous map or geometric morphism. Transgression is a cohomological operation (not a map of spaces), so the adjunction is conjectural.

**What's needed:** Either (a) realize $\Phi$ as a geometric morphism between suitable toposes (e.g., the topos of sheaves on the nerve category versus the topos of coherent sheaves on $\mathbb{CP}^3$), or (b) reformulate $\Phi_* \dashv \Phi^*$ as an adjunction in the derived category $D^b(\mathbb{CP}^3)$ using the Fourier–Mukai framework, where integral kernels can encode degree-shifting operations.

---

### 15. The $n$-Qubit Cross-Context Anticommutation Theorem (Paper XVII, Open Problem 1)

**Status:** Paper XVII proves that for any $K_5$ configuration of Lagrangians in $Sp(6,\mathbb{F}_2)$ (the 3-qubit case), all 15 cross-context ray pairs satisfy $\omega(v_{ij},v_{kl})=1$. The proof uses a size argument: 10 rays cannot be mutually isotropic because any totally isotropic subspace of $\mathbb{F}_2^6$ has at most $2^3-1=7$ nonzero vectors, and $10>7$.

**Why it fails for $n\geq 4$:** For $n$ qubits, a Lagrangian in $\mathbb{F}_2^{2n}$ has $2^n-1$ nonzero vectors. For $n=4$: $2^4-1=15\geq 10$, so the size argument fails. A $K_5$ of Lagrangians in $Sp(8,\mathbb{F}_2)$ might admit mutually isotropic cross-context rays. The question is whether the Cross-Context Anticommutation Theorem holds for $n\geq 4$ (via a different proof) or genuinely fails.

**What's needed:** Either (a) prove the theorem for all $n$ via a structural argument not relying on the dimension bound, or (b) exhibit an explicit $K_5$ of Lagrangians in $Sp(8,\mathbb{F}_2)$ with $c=0$ (an "even $K_5$"). The latter would imply that the KS obstruction is not universal for $n$-qubit systems with $n\geq 4$.

---

### 16. Petersen Graph Non-3-Colorability and KS No-Coloring (Paper XVII, Open Problem 2)

**Status:** The 15 cross-context ray pairs of any Mermin pentagram form the edge set of the Petersen graph $K(5,2)$. The Petersen graph is famously non-3-colorable (chromatic number 4) and is the unique $(3,5)$-cage. The KS theorem asserts that the 10-ray system admits no binary valuation consistent with the commutativity constraints.

**The connection to make precise:** The Petersen graph's non-3-colorability and the KS no-coloring result both assert the impossibility of a consistent global assignment. Is there a direct combinatorial proof that the Petersen structure of the cross-context anticommutation pattern forces the KS obstruction? A direct proof would bypass the Weyl algebra entirely and give a purely graph-theoretic statement of KS contextuality.

**What's needed:** Formulate the KS coloring constraint as a graph-coloring problem on the Petersen graph and identify which classical graph-theoretic property (non-3-colorability, odd cycle structure, Petersen's theorem on cubic graphs) is the direct witness.

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

## How to Contribute

This document is both a guide and an invitation. If you have expertise in any of the areas above — spectral sequences, topos theory, octonions, SAT solving, twistor theory, symplectic finite geometry, or modular forms — the open questions listed here are concrete, well-scoped, and mathematically meaningful.

The full paper series is available in the [`papers/`](papers/) directory. Each "regret" above corresponds to a specific section and conjecture within the papers. Items 1–10 are from Papers I–VI; items 11–14 are from Papers VII–IX. Items 15–18 are from Papers XVI–XVII and form the current research frontier.

---

*"A theory is only as honest as its list of open problems."*
