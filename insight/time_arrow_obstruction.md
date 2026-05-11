# Time's Arrow as Cohomological Obstruction

A speculative note connecting the cohomological obstruction ladder to the arrow of time, black hole information, and the emergence of spacetime.

---

## 1. The Central Idea

The L-S contraction analysis of the Bohrification functor gives a precise
dynamical meaning to each level of the obstruction ladder. One side effect
is a new origin story for time:

> **Time's arrow is not a fundamental principle — it is the dynamical
> projection of the cohomological obstruction ladder.**

Each level of the ladder corresponds to a specific degree of "memory" —
how much information a classical contracting system fails to forget —
and this memory degree maps directly to a temporal phenomenon.

## 2. The Mapping

| Level | L-S memory | Algebra | Temporal phenomenon |
|-------|------------|---------|---------------------|
| $H^0$ | Complete forgetting | Trivial group $\{1\}$ | Thermodynamic equilibrium — no arrow, no direction |
| $H^1$ | One $U(1)$ phase around a loop | $U(1)$ (abelian) | Periodic time: $S^1$, quantum phase $e^{iEt/\hbar}$ |
| $H^2$ | One $\mathbb{Z}/2$ sign flip around a 4-cycle | $\mathbb{Z}/2$ (central extension) | Irreversibility: $\mathbb{Z}/2$ symmetry breaking = the arrow |
| $H^3$ | One associator phase on a 3-simplex | $H^3(M, \mathbb{Z})$ (bundle gerbe) | Spacetime topology: the Dixmier--Douady class |

### Level 0: Equilibrium ($H^0$)

L-S contraction succeeds globally. The system forgets all initial conditions.
No information flows. This is thermodynamics at equilibrium — static, no
distinction between past and future, no observation possible.

### Level 1: The Cycle ($H^1$)

A loop of measurement contexts fails to close because Liouville prevents
global contraction (the $H^1$ theorem). The system "remembers" one $U(1)$
phase around any closed trajectory. This is the geometric phase — the
simplest form of temporal memory.

In quantum mechanics, this is $e^{iEt/\hbar}$: **time is a circle.**
The phase accumulates linearly with the number of cycles. Periodic
motion (oscillators, orbits) is the physical trace of $H^1$ memory.

Reversibility holds locally: the system returns to its initial state
after one full period. No information is lost, no direction is encoded.

### Level 2: The Flip ($H^2$)

A 4-cycle of pairwise-compatible MASAs accumulates a central sign $-\mathbf{I}$
(the $H^2$ theorem). The system remembers not just a continuous phase but a
discrete **direction**: the sign tells you which way you went around.

This is the dynamical origin of **irreversibility**:
- $H^1$ memory is a phase ($U(1)$) — it distinguishes "how many cycles" but
  not "which way" (because $e^{i\theta} = e^{-i\theta}$ is the same).
- $H^2$ memory is a sign ($\mathbb{Z}/2$) — it distinguishes orientation.
  Going clockwise vs counter-clockwise produces different sign accumulations.

The $\mathbb{Z}/2$ symmetry breaking is the algebraic footprint of the
arrow of time. In the Peres--Mermin system, the sign $-\mathbf{I}$ is the
Kochen--Specker contradiction — a logical obstruction that would be
inconsistent without a direction. In macroscopic language: **you cannot
reverse time because that would flip the sign, which the algebra forbids.**

This is much weaker than the Second Law — it doesn't say *why* entropy
increases — but it says something deeper: **even in principle, reversing
the arrow is algebraically obstructed at the $H^2$ level.**

### Level 3: The Braid ($H^3$)

A 3-simplex of MASAs fails to patch associatively (the $H^3$ conjecture).
The obstruction lives in $H^3(M, \mathbb{Z})$ — the Dixmier--Douady class
of a bundle gerbe.

This is no longer about time alone. $H^3(M, \mathbb{Z})$ classifies
**twisted topological structures on spacetime itself**: B-fields in
string theory, Chern--Simons levels, and the topological sectors of
quantum gravity.

The physical interpretation: **spacetime topology is the $H^3$ memory
of associativity breakdown.** The fact that $M$ has non-trivial
$H^3(M, \mathbb{Z})$ means: to consistently patch local physics across
a triple overlap, you must remember not just phase and not just sign,
but the *order in which overlaps are composed*. This order-dependence
is the germ from which spacetime curvature may arise.

---

## 3. Black Hole Information in This Language

The black hole information paradox becomes a problem in obstruction
theory:

- **Outside the horizon:** $H^1$ obstruction dominates — geometric
  phases along null geodesics carry information. L-S contraction is
  *partially effective* here: local measurements forget, but global
  holonomies remember.

- **Inside the horizon:** $H^3$ obstruction dominates — the entanglement
  structure of Hawking radiation is classified by a bundle gerbe
  $H^3(M, \mathbb{Z})$. L-S contraction *fails completely* here:
  the singularity prevents any contraction metric from existing.

- **The Page time** is the phase transition where the system crosses
  from "contraction partially effective" to "contraction entirely
  failed." In L-S language, this is a bifurcation of the generalized
  Jacobian: on one side the metric $\mathbf{M}$ can be chosen to make
  $\mathbf{F}$ negative-definite (information forgotten); on the other side
  it cannot (information remembered).

- **The information recovery problem** asks whether the $H^1$ obstruction
  (Hawking radiation's geometric phase spectrum) encodes the $H^3$
  obstruction (entanglement gerbe) through a paired transgression:
  $$d_2: H^1 \to H^2, \quad \text{and the pairing } \langle H^2, H^3 \rangle \to U(1).$$

This does not solve the paradox. But it translates a 50-year-old
physics problem into a **well-defined cohomological computation**:
compute the transgression between the $H^1$ and $H^3$ classes across
the horizon. Non-zero transgression = information preserved.
Zero transgression = information lost.

---

## 4. What This Means

This perspective does not *derive* the arrow of time from first
principles. What it does is:

1. **Unify** four temporal phenomena (equilibrium, periodicity,
   irreversibility, spacetime topology) under a single obstruction
   ladder whose rungs are already independently motivated.

2. **Translate** the black hole information paradox into a concrete
   cohomological question (transgression across a horizon).

3. **Predict** that any theory of quantum gravity must contain a
   non-trivial $H^3$ class (a gerbe) at its topological core,
   and that the arrow of time is a $d_2$ transgression phenomenon
   that descends from this $H^3$ class to $H^2$ when a measurement
   context (observer) is introduced.

---

*This note is a speculative direction for future research, not
established mathematics. It is shared as part of the open research
documentation for the obstruction ladder project.*
