# The Quantum Substrate: Error Correction, MUBs, and Contextuality-as-Resource

*The one application note that is not connect-the-dots: here the relationship is a
mathematical identity, not an analogy.*

> **Why this could not be written at Paper VI.** At the VI era the intuition was
> already there — "the framework should touch quantum error correction and quantum
> cryptography" — but only as *domain adjacency*. It was unwriteable because the
> symplectic substrate did not yet exist. Papers X–XXII built it (Lagrangians in
> $\mathrm{Sp}(2n,\mathbb F_2)$, the Pauli group, cross-context anticommutation),
> and that turned "related" into "**identical**." This note is the VI-era thought,
> now sayable.

---

## 1. Substrate identity (✓ — not speculative)

The stabilizer formalism of quantum error correction *is* the framework's objects,
term for term:

| QEC / stabilizer formalism | Framework / Papers X–XXII |
|---|---|
| Pauli group mod phase | $V=\mathbb F_2^{2n}$ with symplectic form $\omega$ |
| Commuting Paulis | $\omega$-isotropic vectors |
| Stabilizer group ($[[n,k]]$ code) | isotropic subspace of dim $n-k$ |
| **Stabilizer state ($k=0$)** | **Lagrangian (maximal isotropic) = a MASA / context** |
| Error syndrome | symplectic pairing $\omega(\text{error}, \text{generator})$ = **anticommutation** |
| Logical operators | $L^\perp/L$ (the framework's reduction quotient, XX–XXI) |

So Bohrification-over-MASAs, read literally, *is* the stabilizer picture: a context
= a stabilizer state, a context switch = a change of code basis, and the
cross-context anticommutation that drives Papers XVII–XXII = the **syndrome**.
The framework does not "apply to" QEC — it is built out of QEC's own algebra. Any
genuine theorem of the framework is automatically a statement about stabilizer
objects. This is a full magnitude stronger than the physics thought-experiments in
this folder (which guess a *shape*); here the *objects coincide*.

A second touchpoint, already handled in XXI: **mutually unbiased bases (MUBs) — the
backbone of QKD — are Lagrangian spreads** (a complete set of $2^n+1$ MUBs = a
partition of the nonzero points into pairwise-transverse Lagrangians). Paper XXI's
spread-stabilization manipulated exactly these. So the quantum-cryptography side
also lands on machinery we already operate.

## 2. Gottesman–Knill: why the *forced* quantization stayed tractable (✓ corollary)

This is the complexity-theoretic face of §1, and it answers a worry APP_06 states
out loud. The `n/` evolution chain (APP_06 §1–4) is: LADD smell-search needs phase
→ EML demands $\mathbb C$ → Solèr **forces** quantization → non-commutativity →
Bohrification rescues local readability (each context a MASA = Heyting algebra,
$\mathrm{CAID}=P_A$ spectral fingerprint). APP_06 §4 worries: *"quantization brings
non-commutativity, which seems to make code unreadable."* Naïvely, forced
quantization means $2^n$ amplitudes — exponential. Why didn't it blow up?

> **Gottesman–Knill theorem.** A computation using only (i) stabilizer-state prep,
> (ii) Clifford gates, (iii) Pauli / computational-basis measurement is
> **classically simulable in polynomial time** — by tracking the stabilizer group
> (a Lagrangian in $\mathrm{Sp}(2n,\mathbb F_2)$) instead of the $2^n$ amplitudes.

Lay it on the chain. By §1's *identity*, every Bohrified context is a
**MASA = stabilizer state = Lagrangian**, and the CAID is the spectral fingerprint
of the projector $P_A$ — i.e. *the stabilizer description itself*. Tracking the
system by its MASA / Lagrangian / stabilizer rather than by a full state vector
**is exactly the Gottesman–Knill efficient representation.** So `CAID_exact` being
polynomial is not an engineering trick — it is the framework living, by
construction, on the efficiently-simulable Clifford/stabilizer island. Gottesman–Knill
is the *theorem-level answer* to APP_06 §4's worry: the forced quantization didn't
explode because the Bohrified local view lands precisely in the simulable fragment.

**But — the same theorem's other edge (a rigorous corollary, not a hope).**
Gottesman–Knill also says: a computation that *stays* in this fragment yields
**no quantum speedup** (it is classically simulable). So `n/`'s stabilizer substrate
is *by design* the efficient-classical island. Any genuine quantum advantage must
come from **leaving** it — from non-Clifford "magic" / contextuality, which is
exactly the Howard et al. resource of §3 and exactly what the obstruction ladder
($H^2/H^3$) measures. The substrate identity (§1) and the resource question (§3)
are thus two sides of one complexity boundary, and Gottesman–Knill is the line
between them.

**Aligns with $\hbar_{n/}$ (APP_06 §6.5).** This gives $\hbar_{n/}$ a
complexity reading:
- $\hbar_{n/}=0$ (single MASA, `CAID_exact`) = on the Gottesman–Knill island = efficiently classical;
- $\hbar_{n/}>0$ (cross-context) = off the island = where the obstruction — and any hardness or advantage — lives.

So $\hbar_{n/}$ is, read this way, *a measure of distance from the Gottesman–Knill
island.* It upgrades §1's identity of **objects** into a statement about `n/`'s
**computational cost**: cheap exactly as far as it stays Clifford, and the price of
leaving is denominated in the obstruction ladder.

## 3. The disciplined "but": identity ≠ new tool (⚠️)

QEC is a mature field; it knows this symplectic algebra cold. The framework earns
its keep only if its *specific* results say something QEC has not already named.
The one sharp candidate is **contextuality-as-resource**:

> Howard–Wallman–Veitch–Emerson (*Nature*, 2014): contextuality is the resource
> that supplies the "magic" for universal (fault-tolerant) quantum computation.

The framework's possible contribution is to **grade** that resource:
- the obstruction ladder $H^1 / H^2 / H^3$ = *depths* of the contextuality resource;
- and the **$n\ge5$ $H^3$ modulus** (Papers XIX–XXII) = a *hidden, genuinely
  multipartite* contextuality resource — one that **no arity-$\le4$ witness can
  see** (this is precisely the modulus theorem). A candidate resource-theoretic
  object that requires five contexts to manifest at all.

Whether this graded resource is *operationally useful* — whether the $H^3$ modulus
powers any magic / advantage / protocol — is open. (⚠️ conjecture, not result.)

## 4. Convergence with the operational-meaning question (the north star)

The honest reduction: **"does the framework help QEC / quantum crypto?" sharpens to
"does the $H^3$ obstruction class have operational meaning?"** — which is exactly
`open_problems.md` **item 24** (the physical/operational interpretation of $H^3$).
The bridge literature is the same on both sides: Howard et al. (contextuality =
resource) and Abramsky–Mansfield–Barbosa / Raussendorf (cohomological
contextuality).

So "quantum applications" is **not a new branch — it is the same north star
approached from the application side**:
- theory side: *what is* the $H^3$ class?
- application side: *what can it do* (QEC resource? protocol?)

Same question, two doors. And both doors are gated by the same wall as everything
else (Direction D — the comparison map that ties the framework's $H^3$ to the
operational/measurement-level cohomology).

## 5. Honest tiering (per `README.md` discipline)

| Claim | Status |
|---|---|
| stabilizer = isotropic; stabilizer state = Lagrangian = MASA; syndrome = anticommutation | ✓ identity (rigorous) |
| MUB = Lagrangian spread (QKD touchpoint) | ✓ known identity |
| MASA-local CAID ($P_A$ fingerprint) = Gottesman–Knill efficient (stabilizer) representation → `CAID_exact` polynomial | ✓ corollary of §1 identity + theorem |
| quantum advantage ⟺ leaving the stabilizer fragment (contextuality / magic) | ✓ corollary (Gottesman–Knill + Howard et al.) |
| $\hbar_{n/}$ = distance from the Gottesman–Knill island | [~] reading, not a new tool |
| obstruction ladder = graded contextuality resource | ⚠️ conjecture |
| $H^3$ modulus = a beyond-Gottesman–Knill resource (state-independent contextuality at $H^3$, glue of five stabilizer contexts, uncertifiable below five) | ⚠️ conjecture (rests on XIX–XXII + §6) |
| framework yields a *new* QEC code / QKD protocol | ❌ unproven — do not claim |
| security of QKD = obstruction-class nonvanishing | [~] restatement, not a new tool |

## 6. The sharp question — relocated to where qubit contextuality is actually a resource

The earlier framing ("beyond-Gottesman–Knill *magic*?") has a partial answer, and it
is **No, in the circuit / distillation sense.** The framework's $H^3$ is contextuality
among **qubit stabilizer** objects, and the qubit stabilizer subtheory is the known
anomaly: *contextual yet efficiently classically simulable* (the Mermin square is
all-Pauli and contextual, but Gottesman–Knill still applies). So qubit contextuality
alone buys **no circuit speedup and no magic-state distillation** [Raussendorf–Browne–
Delfosse–Okay–Bermejo-Vega, arXiv:1511.08506]. Reading $H^3$ as distillation-magic is
the wrong axis — and this dovetails with the AdS/CFT result (`adscft_holographic_codes.md`):
contextuality is one of *two orthogonal softwares* on the stabilizer hardware, and it is
**not** the hardness/advantage axis in the circuit model.

The **right** axis is **measurement-based** computation, where qubit contextuality
genuinely *is* the resource:
- **Anders–Browne (PRL 102, 050502, 2009):** Mermin/GHZ contextuality lets a *linear*
  (parity) classical control computer evaluate a **nonlinear** gate (NAND) — promoting
  it to universal. Contextuality is the fuel.
- **Raussendorf (Contextuality in MBQC, arXiv:0907.5449):** non-contextual l2-MBQC
  computes *exactly the linear* Boolean functions; any **nonlinear** function forces
  strongly contextual correlations.
- **Okay–Roberts–Bartlett–Raussendorf (arXiv:2005.00213):** the Boolean function an
  MBQC computes is *literally a class in $H^2$* of the MBQC chain complex — and that
  class is *simultaneously the contextuality witness*. Cohomological degree already
  meets computational content, at degree 2.

That last result is the launching point: it puts a *computational meaning on $H^2$*,
and the framework's distinctive object is the rung above.

> **Sharp conjecture (cohomological degree $=$ computational degree).** Non-contextual
> $=$ linear (Raussendorf); $H^2$ (Mermin square / Anders–Browne) $=$ the first
> nonlinear rung; the **$H^3$ pentagram modulus** $=$ a strictly higher primitive — a
> degree-3 (cubic) Boolean capability — that **no $H^2$ / $\le4$-context resource can
> compute.** The modulus theorem (the class is invisible below five contexts) becomes
> its computational form: *the cubic primitive is uncomputable by any $\le4$-context
> MBQC resource.*

This is sharp and **falsifiable by small simulation** — does a pentagram resource
state, under linear classical control, deterministically compute a cubic function that
a Mermin-square resource provably cannot? Same pattern as the HaPPY arc: a pose a
computation can settle.

**The honest gap (the standing wall).** It rests on identifying the framework's $H^3$
(group cohomology of $\mathrm{Sp}(2n,\mathbb F_2)$, the Maslov/Wall class
$n_a=\delta\mu$) with degree-3 of the *MBQC chain complex* of Okay–Raussendorf — two
different cohomologies. That identification is a **comparison map**, exactly the kind
that is the project's open wall (Direction D; cf. the Veldkamp / Abramsky-sheaf
distinctions of §3). So the conjecture is well-posed and testable in the *computational*
direction even while the *comparison map* stays open: a simulation can confirm a degree-3
separation empirically before the map is built.

If the separation holds, the framework graduates from "shares QEC's map" to "supplies a
coordinate QEC did not have": a computational *degree* on the contextuality resource,
with the pentagram as its first cubic rung above the Mermin-square quadratic one. If it
fails, §1–§2 stand — a faithful, efficiently-classical re-description.

**Result (2026-06-16, `supplementary/mbqc/`): it fails — the conjecture is refuted in
l2-MBQC.** Computed bulletproof (explicit matrices): (a) the deterministic sign function
of *every* stabilizer resource caps at algebraic **degree 2** (GHZ reproduces the
Anders–Browne degree-2 gate; 1200 random stabilizer states never exceed it) — so
non-adaptively the pentagram ($H^3$) is degree-2 just like the square ($H^2$); (b)
**degree 3 (and any degree) is reached by adaptively composing $H^2$ (GHZ) gates alone**
— the pentagram is not needed (a single $H^2$ resource already makes l2-MBQC universal).
Computational function-degree is set by **adaptive depth**, not by the cohomological rung.
$H^3$ gives **no** computational-degree separation over $H^2$. See §7.

## 7. Item 24 was mistyped — $H^3$ is structural by nature (the orthogonality verdict)

Three independent operational axes have now been tested against the framework's $H^3$
contextuality, and on every one it comes back **orthogonal**:

| operational axis | what actually governs it | role of $H^3$ |
|---|---|---|
| circuit hardness / magic | non-stabilizer magic states (Gottesman–Knill, §2) | none — qubit stabilizer is simulable |
| holographic reconstruction | support / erasure (entanglement wedge) | none — `adscft_holographic_codes.md` |
| MBQC computational degree | adaptive depth (composition) | none — §6 / `supplementary/mbqc/` |

In each case the $H^3$ class is genuinely *present* in the substrate (the bulk of a
3-tile holographic code is a faithful $W(5,2)$; the pentagram really is contextual), yet
it is **not the carrier** of the operational resource. But the deeper reading is not
"tested three axes, found it orthogonal three times" — it is that **item 24 was mistyped.**

**Item 24 asked an operational question of a structural quantity.** $H^3$ is an
obstruction class; obstruction classes are *classifying invariants by construction* — they
measure the failure of local-to-global. Expecting one to be a resource imported a type
(contextuality-as-resource, an odd-qudit phenomenon) that qubit $H^3$ doesn't have; the
GK-simulability of qubit stabilizer contextuality (§2) was the first symptom.

**The one correction that keeps this honest** (or it proves too much): $H^2$, the Mermin
square, is *also* a cohomology class, and it **is** operational — Anders–Browne, it powers
nonlinear MBQC. So cohomology is not non-operational by nature. The precise statement is
about **resolution and saturation**:

> Operational axes resolve only the **threshold** — *is there contextuality / nonlinearity
> / non-classicality at all?* — which sits at the **first** nontrivial rung ($\approx H^2$),
> and they **saturate** there: one $H^2$ resource already gives MBQC universality, one bit
> of Wigner-negativity already crosses the magic line, one erasure already breaks
> reconstruction. **No operational axis grades by cohomological degree.** So $H^3$ and above
> are structural refinements *finer than operational resolution* — not non-operational by
> nature, but below the operational sampling rate. That is exactly why the MBQC test
> saturated at degree 2.

So item 24 conflated two questions: *"does contextuality matter operationally?"* (yes — at
the threshold, $H^2$) and *"does cohomological degree matter operationally?"* (no —
operations don't grade by degree). $H^3$ lives in the second, and that is **structural**:
a classifying coordinate + a certification depth (the modulus: unwitnessable below five
contexts). This is the framework's own nature — the ladder ($H^1$–$H^4$ = CAP/FLP/
Byzantine/Sybil) was always a *taxonomy of types of failure*, not a stack of resources;
item 24 briefly asked a type to be a power. **"Framework = coordinates, cartographer not
competitor"** (cf. `open_problems.md` §A′), now precise.

The computations were not wasted by the question being mistyped — they are what
*established the saturation empirically* (rather than assuming it), and they threw off real
positive structure on the way: the AdS/CFT shape-correspondence, the degree-2 ceiling, the
faithful-$W(5,2)$ bulk. Honest residue: other operational axes (communication complexity,
other resource theories) remain logically open, but the saturation reading predicts
orthogonality there too. What the framework uniquely supplies is the structural coordinate
itself — the rigidity ($N_{\text{anti}}=10\iff n=4$), the even/odd dichotomy, the arity
ceiling — the map of *where* contextuality sits, which the operational literatures do not
draw because they ask what it *does*, not what it *is*.

---

*This note is the strongest-grounded of the application sketches: its §1 is identity,
not analogy, and §2 is that identity's Gottesman–Knill complexity corollary (also
rigorous). §3–§5 framed the resource question; §6 tested it (refuted in l2-MBQC); §7 is
the orthogonality verdict answering item 24. See `why_the_ladder.md`
(observation core), `transformers_bohrification.md` (the other application),
`open_problems.md` item 24, and Papers XVII (anticommutation/Petersen),
XIX (modulus), XX–XXII (H³ arc, spreads).*
