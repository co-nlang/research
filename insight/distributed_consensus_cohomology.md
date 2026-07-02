# Distributed Consensus as Cohomological Repair

**FLP impossibility, Paxos, and Byzantine fault tolerance through the lens of the obstruction ladder.**

> **Status (revised 2026-07-03; original is Paper-VI-era).** ⚠️ **Correspondence-level** —
> the mapping (CAP/FLP/Byzantine/Sybil ↔ $H^1$–$H^4$) is a structural analogy, not a
> theorem of the series; the rigorous mathematical neighbor is Herlihy–Kozlov–Rajsbaum's
> topology of distributed computing. This revision: ✅ fixed the $H^0/H^1$ bug in §2
> (a disconnected cover has $\check H^1 = 0$; the genuine $H^1$ is the *heal-loop*
> monodromy); ✅ placed $H^1$/CAP in the ladder's **survivor column**
> (holonomy/classification — repairable) as against the **differential column**
> ($H^2$/$H^3$ — genuine gluing obstructions), matching the series' $E_\infty$-vs-$d_r$
> split; ✅ updated the quantum column to post-XX–XXII status: the quantum tower
> **truncates at $H^3$**, so the two ladders *mismatch at $H^4$* — which is the point
> (§6). Absorbed into the spec as APP_07 §4, which carries the same labels.

---

## 1. The Central Analogy

Distributed consensus is about *agreement across disagreement* — exactly
what cohomology measures. Each fault model corresponds to a different
dimensional obstruction:

| Fault model | Nerve dimension | Cohomology | Classical theorem |
|---|---|---|---|---|
| Network partition + heal (Crash) | 1-cycle (the split→rejoin loop) | $H^1$ holonomy (the in-progress partition is $H^0$; §2) | CAP: choose availability or consistency |
| Asynchrony + single crash | 2-simplex (face) | $\check{H}^2 \neq 0$ (via $d_2$) | FLP: deterministic consensus impossible |
| Byzantine fault | 3-simplex (tetrahedron) | $\check{H}^3 \neq 0$ | Byzantine fault tolerance ($> 2/3$) |
| Sybil attack | vertex set itself | not a class — $E_1$-input corruption ("$H^4$" positional; §6) | Proof of Work / Stake / Space |

Each level corresponds to a progressively deeper uncertainty about the
state of other nodes — and each requires a progressively more complex
geometric repair.

**Two columns, one ladder.** The degrees are shared with the quantum
ladder, but the *semantic column* differs by rung. $H^1$/CAP sits in the
**survivor column** ($E_\infty$-stable classification: a global section
*exists* but returns twisted around a loop — repairable by compensation);
$H^2$/FLP and $H^3$/Byzantine sit in the **differential column** ($d_r$
kills the section: no global section exists); and Sybil is not in the
spectral sequence at all — it forges the $E_1$ *input*. Reading all four
as "obstructions" flattens this distinction; the sections below keep it.

---

## 2. The CAP Theorem as $H^1$ Holonomy ($E_2$ page)

> ⚠️ **Corrected (2026-07-03).** An earlier version derived
> $\check{H}^1 \neq 0$ from a *disconnected* cover ($U_1 \cap U_2 =
> \varnothing$, "the nerve is disconnected"). That is wrong: a disconnected
> cover has **no 1-simplices** in its nerve, so $\check{H}^1 = 0$ — the
> in-progress partition is an $H^0$ phenomenon. The genuine $H^1$ lives on
> the *heal loop*. Both phases are kept below, correctly labelled.

**Phase 1 — partition in progress: $H^0$, not $H^1$.** Nodes split into
$P_1$, $P_2$ with no communication; the cover $\{U_1, U_2\}$ has empty
overlap and the nerve is two disconnected vertices. There is no cocycle to
obstruct — instead there are *too many* global sections: each component
carries its own locally consistent state, and nothing relates them. This is
failure of **uniqueness** ($\operatorname{rank} H^0 = 2$), not of existence.

**Phase 2 — partition then heal: the genuine $H^1$.** The CAP tension is
felt when the partition *ends*. The causal diagram of the run — split,
evolve separately, rejoin — is a loop: transport the state around
split → $P_1$-history → rejoin and compare with
split → $P_2$-history → rejoin. The two transports disagree by the
accumulated divergence of the replicas: a **monodromy**. This is holonomy
in the strict sense — a global section *exists* (the system does reunify),
but carrying it around the loop returns it twisted.

**CAP in this language.** During the partition, an available (A) system
lets both components write, creating the monodromy; a consistent (C)
system refuses writes in at least one component, gauge-fixing the loop so
the holonomy is trivial. "Choose C or A" = choose *how to pay the
monodromy*: trivialize it by waiting, or accept the twist and reconcile
later.

**Why this is the survivor column, not an obstruction.** Unlike FLP
($H^2$, next section), nothing here says a global section cannot exist.
The $H^1$ class *classifies the twist* that reconciliation must pay:
eventual-consistency repair (CRDT merge, read-repair, compensating
transactions) is literally **phase compensation**. This matches the
quantum side, where $H^1$ classes (geometric phases) are $E_\infty$
*survivors* — stable, recorded, transportable — not differentials that
kill sections. CAP is "tolerable/repairable" (APP_07's wording) precisely
because it sits in the survivor column.

**$E_2$ page convergence:** the holonomy is detectable at $E_2$ (one round
of message exchange after heal). CAP is $P$ in complexity terms — linear
in the number of nodes.

---

## 3. FLP Impossibility as $H^2$ Obstruction ($d_2$ Transgression)

**Setup.** Asynchronous distributed system with $n$ processes,
at most one may crash. No timing assumptions. The problem:
deterministic consensus is impossible (Fischer, Lynch, Paterson, 1985).

**Why this is $H^2$.** Consider two processes $A$, $B$ and a third
process $C$ that may crash. The state space has a $2$-simplex
structure:

- Edge $(A, B)$: both $A$ and $B$ see $C$'s pre-crash state (agreement)
- Edge $(A, C)$: $A$ hears from $C$, $B$ does not (disagreement)
- Edge $(B, C)$: $B$ hears from $C$, $A$ does not (disagreement)

The nerve is a triangle $\partial\Delta^2$ (a $1$-dimensional loop
in the protocol state graph). At $E_2$, the system appears to have
a consistent global section: each edge individually admits a solution.

**The $d_2$ transgression.** Fix a bivalent configuration (the system
can decide either $0$ or $1$). The two execution paths are:

$$
\text{Path}_L: A \xrightarrow{e_1} C \xrightarrow{e_2} B
\quad\text{(A proposes, then B)}
$$
$$
\text{Path}_R: B \xrightarrow{e_2} C \xrightarrow{e_1} A
\quad\text{(B proposes, then A)}
$$

In a fault-free asynchronous system, the $d_1$ differential ensures
these two paths arrive at the same state via commutativity
($e_1 \circ e_2 = e_2 \circ e_1$ on unaffected states). But when
$C$ may crash, the partial order of events becomes *non-commutative*
— exactly the $H^2$ obstruction.

**The $d_2$ map:**

$$d_2: E_2^{0,1} \to E_2^{2,0}$$

takes the $1$-cocycle $[\omega]$ representing "both paths locally
consistent" and evaluates it on the boundary of the triangle.
The result is non-zero — a $2$-cocycle obstruction $\mathcal{O}$
that records the irreconcilable split between the two decision
values.

$$d_2([\omega]) = \mathcal{O} \neq 0 \in \check{H}^2(\mathcal{U}, \mathcal{F}).$$

**FLP theorem** in this language:

> In any fully asynchronous system, the LHS spectral sequence
> converges to $E_3^{0,0} = 0$ because $d_2$ is non-zero on
> the $2$-simplex representing the crash uncertainty. No
> deterministic algorithm can produce a survivor to $E_3$.

The $d_2$ transgression captures the **irreducible uncertainty**
of not knowing whether a crashed node would have contributed to
the decision.

---

## 4. Paxos as Cohomological Repair

Paxos achieves safe consensus despite the FLP impossibility by
*introducing a four-context overlap* that trivializes the $d_2$
obstruction — not by eliminating it, but by turning the cohomology
class into a coboundary.

### 4.1 The Paxos MASA cover

Paxos defines three roles: Proposers ($P$), Acceptors ($A$), and
Learners ($L$). The key geometric insight:

> **Majority intersection = $\mathcal{U}$ is a good cover.**
> Any two majorities have at least one node in common. This
> ensures all $2$-simplex overlaps are non-empty, trivializing
> $\check{H}^2$.

The Paxos protocol phases decomposes into a three-context MASA
cover:

| Phase | Context | Action | Cochain |
|---|---|---|---|
| Prepare | $U_P$ | Proposer sends $n$ to all Acceptors | $s_P$ (proposal) |
| Promise | $U_A$ | Acceptor promises not to accept $< n$ | $s_A$ (promise) |
| Accept | $U_L$ | Learner learns committed value | $s_L$ (learn) |

Overlaps:
- $U_P \cap U_A$: the proposer's $n$ must match the acceptor's promise
- $U_A \cap U_L$: the learner must hear from a majority
- $U_P \cap U_L$: indirect (through acceptors)

The critical overlap is $U_P \cap U_A \cap U_L$ — guaranteed
non-empty because the proposer picks a value that a majority of
acceptors have promised to, and at least one of those acceptors
overlaps with the learners' majority.

### 4.2 How $d_2$ is forced to zero: explicit spectral sequence computation

We now work through the $E_1 \to E_2 \to E_3$ passage explicitly,
following the Paxos protocol steps.

**Setup.** $N$ acceptors $A_1, \dots, A_N$. Two proposers $P_1, P_2$
with proposal numbers $n_1 < n_2$. Each $A_i(n)$ is a MASA recording
acceptor $i$'s state for proposal $n$.

**$E_1$ page: Prepare and Promise (building $d_1$ compatibility).**

Proposer $P_1$ picks $n_1$ and sends `Prepare($n_1$)` to quorum $Q_1$
($> N/2$ acceptors). Each acceptor replies with its highest seen
proposal $(n_a, v_a)$. The proposer collects these replies into a
local section $s_1$ on the cover $Q_1$.

The $d_1$ differential checks agreement on overlaps within $Q_1$:
if two acceptors in $Q_1$ report different highest values, $d_1$
detects the inconsistency. In Paxos, $P_1$ picks the highest $v_a$
(reported by any acceptor in $Q_1$) as its proposed value $v_1$.
This ensures $d_1(s_1) = 0$ — the local section is consistent.

At $E_2$, the system appears to have a consistent state $s_1$
on quorum $Q_1$. But $P_2$ may now propose $n_2 > n_1$ on a
*different* quorum $Q_2$.

**$d_2$ attempt: the conflicting proposal.**

The $d_2$ differential attempts to extend the local section
$s_1 = (n_1, v_1)$ on $Q_1$ and $s_2 = (n_2, v_2)$ on $Q_2$
to a global section. The obstruction lives in the intersection
$Q_1 \cap Q_2$:

$$d_2(s_1 \cup s_2) = s_1|_{Q_1 \cap Q_2} - s_2|_{Q_1 \cap Q_2}.$$

In FLP's asynchronous model, $Q_1 \cap Q_2$ might be empty or
disconnected. Even if non-empty, the nodes in the intersection
cannot synchronize their state across proposals. The result:
$d_2 \neq 0$ — the FLP impossibility.

**$d_2$ elimination in Paxos.**

Paxos forces $d_2 = 0$ through two protocol rules:

1. **Quorum intersection axiom.** Any two majorities satisfy
   $Q_1 \cap Q_2 \neq \varnothing$. Hence there exists at least
   one acceptor $C \in Q_1 \cap Q_2$.

2. **Promise propagation.** When $P_2$ sends `Prepare($n_2$)`
   to $Q_2$, acceptor $C$ (which participated in $P_1$'s
   `Accept($n_1, v_1$)`) **must** reply with the value $v_1$
   via its Promise. $P_2$ is then forced to adopt $v_1$ as
   its proposed value instead of $v_2$.

The $d_2$ computation now reads:

$$
\begin{aligned}
d_2(s_1 \cup s_2') &= s_1|_{C} - s_2'|_{C} \\
&= (\text{value chosen by } P_1) - (\text{value adopted by } P_2 \text{ at } C) \\
&= v_1 - v_1 = \mathbf{0}.
\end{aligned}
$$

**Conclusion.** $d_2 = 0$ identically. The local section
extends to a survivor at $E_3$, proving safety:
a global consensus value exists and is unique.

### 4.3 The liveness gap: $E_1$ oscillation

Paxos does not guarantee liveness (termination). In the spectral
sequence language, this corresponds to:

> **Liveness failure = spectral sequence never stabilizes at $E_1$.**

When two proposers $P_1$, $P_2$ repeatedly overwrite each other's
prepares (dueling proposers), the $d_1$ differential never satisfies
the chain complex condition because each Promise round invalidates
the previous one. The system oscillates between different local
sections at $E_1$, unable to converge to $E_2$.

In practice, randomized backoff (or a distinguished leader) is
the geometric equivalent of **perturbing the spectral sequence
to break the $E_1$ deadlock** — a small asymmetric perturbation
that forces the chain complex to converge at a preferred page.

---

## 5. Byzantine Fault Tolerance as $H^3$ Obstruction

**Setup.** $n$ processes, $f$ of which may be arbitrarily malicious
(Byzantine). The system must reach consensus despite $f$ Byzantine
faults. Known bound: $n > 3f$.

**Why $H^3$.** A Byzantine node can equivocate — send different
values to different observers. This creates an associativity violation
at the $3$-simplex level. Three honest nodes $A, B, C$ receiving
messages from a Byzantine node $Z$ each get a different value.
The cocycle condition on quadruple overlap fails.

**VSS and secret sharing.** Byzantine agreement protocols typically
use threshold cryptography or verifiable secret sharing to "bind"
the Byzantine node to a single value. These techniques correspond
to constructing a $3$-cocycle whose Dixmier-Douady class is forced
to zero by requiring $> 2/3$ honest overlap.

**The $2/3$ bound** $n > 3f$ emerges from the topology:
a $3$-simplex with $f$ Byzantine faces cannot be made to close
associatively unless $f < n/3$. This is the Borromean analogy:
remove any one honest node (like removing a Borromean ring),
and the remaining system can be solved.

---

## 6. Sybil Attack as $H^4$ Obstruction

**Setup.** An attacker creates multiple fake identities $Z_1, Z_2,
\dots, Z_k$ that appear as distinct nodes to the honest majority.
The system believes it sees $n + k$ independent participants when
only $n$ real ones exist.

**Why this is $H^4$, not $H^3$.** The Byzantine fault ($H^3$)
involves a *real* node that lies. The cocycle condition on a
$3$-simplex $\partial[A, B, C, Z] \neq 0$ fails because $Z$ sends
different values to $A$, $B$, $C$ — but $A$, $B$, $C$, $Z$ are
all *genuine nodes*. The identity of each participant is trustworthy;
only the messages are malicious.

The Sybil attack is fundamentally different: **the attacker fabricates
identities themselves.** The system's nerve complex becomes fraudulent
at the level of its *vertex set*:

$$|\mathcal{N}(\mathcal{U})|_{\text{apparent}} \neq |\mathcal{N}(\mathcal{U})|_{\text{actual}}.$$

The $4$-simplex picture: the falsehood lives in the relationship between
four apparent identities that collapse to one real entity — four fake
nodes $Z_1, Z_2, Z_3, Z_4$ that the cover $\mathcal{U}$ treats as distinct
vertices, while the actual nerve has them identified. But "$H^4$" here is
**positional shorthand** (the layer one step deeper than intent:
existence), *not* a class the spectral sequence computes — no cocycle
condition on fabricated vertices is well-posed, because the complex itself
is the forgery. The next paragraph is the accurate statement.

**In LHS spectral sequence terms:** the Sybil attack corrupts the
*input* to the spectral sequence itself — it is not an obstruction at
some intermediate page $E_r$, but a falsification of the $E_1$ page's
definition. The base space (the set of participants) is misreported.
This is why Sybil resistance cannot be achieved by consensus logic
alone; it requires external anchoring.

### How Sybil Resistance Mechanisms Anchor $H^4$

Each Sybil resistance mechanism forces the attacker to pay a physical
cost for each fake identity, thereby grounding the nerve's vertex set
in reality:

| Defense mechanism | Geometric interpretation |
|---|---|
| Proof of Work (PoW) | Real computation = lower bound on the volume of a $4$-simplex |
| Proof of Stake (PoS) | Real stake = "mass" of the $H^4$ class |
| Proof of Space (PoSpace) | Real storage = lower bound on $4$-dimensional volume |
| Physical identity (KYC) | Outsources $H^4$ verification to the real world |
| Web of Trust | Graph-theoretic bound on $H^4$ via transitive trust |

Every mechanism forces the nerve's identity dimension to have a
real-world anchor — making the cost of forging an identity equivalent
to the cost of forging a physical $4$-simplex.

### The Mismatch at $H^4$ Is the Content (updated post-XXII)

An earlier version of this note claimed the two ladders "match in full,
$H^1$ through $H^4$" — with the quantum $H^4$ filled in as "2-gerbe /
$d_4$ transgression" and $H^3$ still marked conjectural. The series has
since **proven the $H^3$ rung and refuted the quantum $H^4$**, and the
refutation *sharpens* the correspondence:

| Level | Quantum (post XX–XXII) | Distributed systems |
|---|---|---|
| $H^1$ | Geometric phase (A-B, Berry) — $E_\infty$ survivor | CAP: heal-loop monodromy (survivor column) |
| $H^2$ | KS / central extension — theorem (Paper III) | FLP: asynchronous disagreement |
| $H^3$ | Borromean class $[n_a]$ — **theorem**; $=0$ universally iff $n=4$ (Papers XX–XXI) | Byzantine fault: equivocation |
| $H^4$ | **does not exist** — the tower truncates at $H^3$ (Paper XXII; item 21: no exotic arity-5 class) | Sybil: identity fabrication — **needs a repair layer** |

Each level involves a deeper layer of the system's definition:
$H^1$ questions values, $H^2$ questions timing, $H^3$ questions
intent, $H^4$ questions **existence** — and at exactly that layer the two
columns *diverge*. The distributed stack needs an $H^4$-level repair; the
internal (symplectic/Pauli) mathematics proves there is **no internal
$H^4$ class** with which to detect or perform it. So Sybil resistance
cannot be consensus-internal: it must be anchored *outside* the framework
(PoW / PoS / KYC — and in `n/`, the physical genesis anchor `ORDER_00`).
The mismatch is not a defect of the analogy; it is its sharpest
prediction, and it is exactly APP_07 §4's argument for `ORDER_00`.

---

## 7. Unified Table

| Level | Fault model | Nerve | Cohomology | Classical theorem |
|---|---|---|---|---|
| $H^1$ (survivor) | Partition + heal | 1-cycle (heal loop) | $H^1$ holonomy (in-progress: $H^0$) | CAP (choose C or A) |
| $H^2$ | Async crash | 2-simplex | $d_2 \neq 0$ | FLP impossible |
| Paxos fix | Async crash | 4-cycle overlap | $d_2 \to 0$ via quorum | Paxos safety |
| $H^3$ | Byzantine | 3-simplex | $H^3 \neq 0$ | $n > 3f$ required |
| "$H^4$" | Sybil | vertex set ($E_1$ input) | no internal class (Paper XXII) — external anchor | PoW / PoS / PoSpace |

The progression follows the quantum contextuality ladder — up to its lid:
- $H^1$: geometric phase (survivor) → heal-loop monodromy
- $H^2$: central extension → asynchronous disagreement
- $H^3$: non-associativity → Byzantine equivocation
- "$H^4$": internally empty (truncation) → Sybil repair must be external

---

*This note is a correspondence-level exploration at the intersection of
distributed computing and algebraic topology. It reformulates
classical impossibility results and algorithms as cohomological
obstruction phenomena, providing a unified geometric language
for fault tolerance. The ladders align on $H^1$–$H^3$ (with $H^1$ in the
survivor column), and deliberately **mismatch at $H^4$**: the quantum
tower truncates (Paper XXII), so the Sybil layer has no internal class
and its repair must be externally anchored — the analogy's sharpest, and
most load-bearing, conclusion.*

---

## References

- Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985). Impossibility of distributed consensus with one faulty process. *JACM*, 32(2), 374–382.
- Lamport, L. (1998). The part-time parliament. *ACM Trans. Comput. Syst.*, 16(2), 133–169.
- Gilbert, S. & Lynch, N. (2002). Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News*, 33(2), 51–59.
- Lamport, L., Shostak, R., & Pease, M. (1982). The Byzantine generals problem. *ACM Trans. Program. Lang. Syst.*, 4(3), 382–401.
- Herlihy, M., Kozlov, D., & Rajsbaum, S. (2013). *Distributed Computing Through Combinatorial Topology*. Morgan Kaufmann. (The rigorous coloring→topology→solvability body; this note's mathematical neighbor.)
