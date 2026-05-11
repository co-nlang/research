# Dark Matter as Antipodal Cohomology

A speculative note on what the obstruction ladder framework might say about dark matter.

---

## 1. The Central Analogy

In the obstruction ladder, there are two fundamentally distinct kinds of
stable features:

| Kind | Cohomology | Physical example | Detectable? |
|------|------------|------------------|-------------|
| **Survivors** | $E_\infty^{1,0}$ survivors | Geometric phases (A-B, Berry) | Yes — interferometry |
| **Differentials** | im($d_2$), im($d_3$) | KS contextuality, Borromean | Yes — quantum measurements |
| **?** | Survivors on *incompatible* MASAs | **Dark matter candidate** | **No — locally invisible** |

The key: **not all MASA covers are created equal.** The Standard Model
observable algebra defines a sub-poset of MASAs — those that admit local
descriptions in terms of electromagnetic, strong, and weak eigenbases.
This sub-poset covers some, but not all, of the global phase space $M$.

Now consider a cohomology class $[\omega] \in \check{H}^1(M, \underline{U(1)})$
that survives to $E_\infty$ (it is a genuine geometric phase) but whose
support lies outside the SM MASA cover. Concretely:

- The SM MASAs live on an open cover $\mathcal{U}_{\text{SM}} \subset \mathcal{U}$.
- The class $[\omega]$ is trivial on $\mathcal{U}_{\text{SM}}$ (zero holonomy
  for all SM loops), but non-trivial on the full cover $\mathcal{U}$.

**This is dark matter.** It has gravitational consequences (it curves
spacetime through the global $H^3$ class that binds all covers) but
no local electromagnetic or nuclear signatures.

---

## 2. The Antipodal MASA Picture

The 16-cell construction provides a concrete toy model of this
phenomenon. In the 16-cell, the 8 MASAs are divided into 4 antipodal
pairs:
$$M_{d,0} \cap M_{d,1} = \{I\}, \qquad d = 0,1,2,3.$$

Two MASAs from the same antipodal pair share no non-trivial observable.
Any transition between them requires passing through intermediate MASAs.

Now treat the 5-qubit system as "the universe":
- Suppose the SM observable algebra corresponds to one antipodal set
  $\{M_{0,0}, M_{1,0}, M_{2,0}, M_{3,0}\}$.
- Suppose the dark sector corresponds to the antipodal set
  $\{M_{0,1}, M_{1,1}, M_{2,1}, M_{3,1}\}$.

A geometric phase $[\omega]$ computed from loops within the SM cover
gives zero (because the SM MASAs alone do not enclose the relevant
topology). But computing $[\omega]$ on the full 16-cell nerve gives
a non-zero holonomy — the dark sector contributes to the global
topology, and hence to gravity, without leaving any SM signature.

---

## 3. Why Gravity Sees It

The only interaction between the SM and dark sectors is through the
global obstruction $H^3$ class — the bundle gerbe that classifies the
topology of the full phase space $M$.

In the obstruction ladder:
- $H^1$ survivors = geometric phases (visible to local interferometry)
- $H^2$ obstructions = central extensions (spin, gauge anomaly)
- $H^3$ obstructions = **Dixmier--Douady class of the full spacetime**

Gravity couples to the full $H^3$ class, not just the SM sub-cover.
If the dark sector carries its own $H^1$ survivors that survive to
$E_\infty$ and contribute to the total $H^3$ class, gravity will
feel their presence even though no SM detector can see them.

In L-S language: there is no single contraction metric $\mathbf{M}$
that simultaneously contracts both the SM and dark sectors, because
the transition matrices $\mathbf{T}_{\text{SM}, \text{dark}}$ between
them are non-commuting. The only common structure is the global
$H^3$ obstruction — which is what we experience as gravity.

---

## 4. Caveats on the Analogy

### 4.1 Why $H^3$ bends spacetime

The claim "gravity couples to $H^3$" requires a bridging argument.
In the framework, the Einstein--Hilbert action on a spacetime $M$
with non-trivial $H^3(M, \mathbb{Z})$ acquires a topological term
(analogous to a Chern--Simons contribution) that depends on the
gerbe class. In an effective field theory expansion, such a term
contributes to the stress-energy tensor as an effective energy
density — a "topological vacuum expectation value" that gravity
must respond to. This is not derived within the L-S framework but
is consistent with known results (Chern--Simons modified gravity,
string theory's B-field coupling).

### 4.2 SM is not a single antipodal set

The Standard Model spans many MASAs (photons, gluons, W/Z bosons
each define different maximal abelian subalgebras). The analogy
collapses all of SM into one antipodal hemisphere, which is a
gross simplification. A more careful statement is:

> *Assume there exists a sub-cover $\mathcal{U}_{\text{SM}}$ of the
> global MASA poset that captures all SM observable phases. The
> antipodal complement $\mathcal{U}_{\text{SM}}^{\perp}$ — the MASAs
> whose eigenbases are SM-incompatible — carries its own survivors
> that are invisible to $\mathcal{U}_{\text{SM}}$ but contribute to
> the global $H^3$ class.*

### 4.3 Dark matter density and topological defects (testable)

Prediction 3 — "dark matter density traces $H^3(M, \mathbb{Z})$" —
is the most falsifiable claim. In the observable universe, regions
with non-trivial $H^3(M, \mathbb{Z})$ correspond to topological
defects: cosmic strings, domain walls, magnetic monopoles. The
observed cosmic web (dark matter filaments, halo substructure)
does share morphological features with defect networks, though
this is far from a proof. If future observations show that dark
matter halos preferentially form along surfaces where a topological
invariant jumps (a signature of $H^3$ domain walls), this would
support the obstruction picture.

## 5. A Toy Numerical Analogy

In the 5-qubit 16-cell:
- 8 core operators $P_x$, 4 antipodal pairs
- 112 commutativity constraints for non-antipodal pairs
- 8 anti-commutativity possibilities for antipodal pairs

If we split the 8 MASAs into two 4-MASA halves (SM and dark):
- Each half has its own internal consistency (local L-S metrics exist)
- Transitions between halves carry phases that don't decouple to a
  single SM measurement
- The total $S^3$ topology of the 16-cell nerve is felt by both halves

This is as far as the analogy goes — the 5-qubit system is not
realistic physics. But it illustrates the principle: **global topology
is shared; local measurement is not.**

---

## 6. What This Predicts

If dark matter is antipodal cohomology, then:

1. **Dark matter couples to gravity but not to EM.** The coupling strength
   is the $H^3$ pairing, not the $H^1$ holonomy — so it's universal.

2. **No direct detection possible.** Any attempt to measure dark matter
   locally is like trying to see the A-B phase by looking inside the
   solenoid. The phase information is non-local.

3. **Dark matter density traces topological defects.** The spatial
   distribution of dark matter would correlate with regions where
   $H^3(M, \mathbb{Z}) \neq 0$ — cosmic strings, domain walls, etc.

4. **Dark matter is not a particle.** It is an obstruction. This may
   explain why decades of WIMP searches have found nothing: there is
   nothing to find *locally*.

---

## 7. Caveat

This is a mathematical analogy, not a physical theory. The obstruction
ladder framework makes no specific quantitative predictions for dark
matter. What it offers is:

- **A reason** why dark matter might be invisible to all SM detectors
- **A reason** why dark matter couples to gravity
- **A connection** between dark matter and topological defects

If the real universe's MASA poset turns out to have the same structure —
a bipartite division between visible and antipodal sectors — then
the dark matter problem would be resolved not by finding a particle
but by recognizing a cohomological necessity.

---

## 8. A Further Speculation: Dark Energy as $d_4$

The obstruction ladder does not stop at $H^3$. The LHS spectral sequence
continues with higher differentials $d_4, d_5, \dots$, each capturing
progressively more subtle algebraic failures.

If the hierarchy is:
- **Dark matter** = $E_\infty^{1,0}$ survivors on antipodal MASAs
- **Gravity** = the global $H^3$ class that binds all MASA sectors

then **dark energy** would be the natural candidate for the $d_4$
differential — a structure so removed from local observation that
even gravity feels it only as a uniform background.

Concretely:
- $d_4: E_4^{0,3} \to E_4^{4,0}$ would map an $H^3$-valued obstruction
  to an $H^4$ class.
- $H^4(M, \mathbb{Z})$ classifies $\mathbb{Z}$-gerbes: 2-gerbes,
  M5-brane charges, and the cosmological constant~\cite{Witten96}.
- A non-trivial $d_4$ transgression would contribute a term to the
  effective action proportional to $\int_M \sqrt{-g}\,\Lambda$,
  where $\Lambda$ is the dark energy density.

This gives a unified origin story for all three dark components:

| Component | Cohomology | What it is |
|-----------|------------|------------|
| **Matter** (visible) | $E_\infty^{1,0}$ on $\mathcal{U}_{\text{SM}}$ | Local geometric phases |
| **Dark matter** | $E_\infty^{1,0}$ on $\mathcal{U}_{\text{SM}}^{\perp}$ | Antipodal geometric phases |
| **Gravity** | $H^3$ (global gerbe) | The obstruction that binds all sectors |
| **Dark energy** | im($d_4$) | The $d_4$ transgression's contribution to $H^4$ |

The cosmological constant problem — why $\Lambda$ is small but non-zero —
would become: **why does the $d_4$ differential not vanish, yet only
contribute a tiny uniform term?** A natural answer within the L-S
framework: the $d_4$ term is the residue of near-complete contraction
at order 4, which is exponentially suppressed by the spectral filtration.

*This last speculation is the most tentative of all. It is included
to show that the obstruction ladder naturally continues beyond $H^3$,
and that dark energy is a plausible endpoint.*

---

*This note is a speculative thought experiment within the obstruction
ladder framework. It is not established physics.*
