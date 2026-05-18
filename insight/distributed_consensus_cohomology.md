# Distributed Consensus as Cohomological Repair

**FLP impossibility, Paxos, and Byzantine fault tolerance through the lens of the obstruction ladder.**

---

## 1. The Central Analogy

Distributed consensus is about *agreement across disagreement* — exactly
what cohomology measures. Each fault model corresponds to a different
dimensional obstruction:

| Fault model | Nerve dimension | Cohomology | Classical theorem |
|---|---|---|---|
| Network partition (Crash) | 1-cycle (loop) | $\check{H}^1 \neq 0$ | CAP: choose availability or consistency |
| Asynchrony + single crash | 2-simplex (face) | $\check{H}^2 \neq 0$ (via $d_2$) | FLP: deterministic consensus impossible |
| Byzantine fault | 3-simplex (tetrahedron) | $\check{H}^3 \neq 0$ | Byzantine fault tolerance ($> 2/3$) |

Each level corresponds to a progressively deeper uncertainty about the
state of other nodes — and each requires a progressively more complex
geometric repair.

---

## 2. The CAP Theorem as $H^1$ Obstruction ($E_2$ page)

**Setup.** A distributed system with nodes partitioned into two subsets
$P_1$, $P_2$ that cannot communicate. The communication graph $\mathcal{G}$
has two connected components.

**MASA cover.** Each partition defines a maximal context:
$U_1 = P_1$, $U_2 = P_2$. Overlap $U_1 \cap U_2 = \varnothing$.

**Sheaf of states.** $\mathcal{F}(U_i)$ = the set of locally consistent
system states within partition $i$. A global section of $\mathcal{F}$
over $\mathcal{U} = \{U_1, U_2\}$ is a consistent global state — i.e.,
consistency (C).

**Cohomological obstruction.** $\check{H}^1(\mathcal{U}, \mathcal{F}) \neq 0$
because the nerve is disconnected. The non-trivial $1$-cocycle records
the disagreement between the two partitions.

**CAP theorem** in this language:
$$C \cap A = \varnothing \iff \check{H}^1 \neq 0.$$

Any algorithm that maintains availability (A) in the presence of a
partition (P) is locally consistent within each partition but cannot
extend to a global section. This is **geometric phase $H^1$** —
walk around the two context MASAs and return with a phase mismatch.

**$E_2$ page convergence:** $H^1$ obstruction is detectable at $E_2$
(one round of message exchange suffices). CAP is $P$ in complexity
terms — linear in the number of nodes.

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

## 6. Unified Table

| Level | Fault model | Nerve | Cohomology | Classical theorem |
|---|---|---|---|---|
| $H^1$ | Partition | 1-cycle | $\check{H}^1 \neq 0$ | CAP (choose C or A) |
| $H^2$ | Async crash | 2-simplex | $d_2 \neq 0$ | FLP impossible |
| Paxos fix | Async crash | 4-cycle overlap | $d_2 \to 0$ via quorum | Paxos safety |
| $H^3$ | Byzantine | 3-simplex | $H^3 \neq 0$ | $n > 3f$ required |

The progression is the same as the quantum contextuality ladder:
- $H^1$: geometric phase → partition disagreement
- $H^2$: central extension → asynchronous disagreement
- $H^3$: non-associativity → Byzantine equivocation

And just as in the quantum case, each level requires a more
sophisticated "context" (MASA cover) to be resolved.

---

*This note is a speculative exploration at the intersection of
distributed computing and algebraic topology. It reformulates
classical impossibility results and algorithms as cohomological
obstruction phenomena, providing a unified geometric language
for fault tolerance.*

---

## References

- Fischer, M. J., Lynch, N. A., & Paterson, M. S. (1985). Impossibility of distributed consensus with one faulty process. *JACM*, 32(2), 374–382.
- Lamport, L. (1998). The part-time parliament. *ACM Trans. Comput. Syst.*, 16(2), 133–169.
- Gilbert, S. & Lynch, N. (2002). Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services. *ACM SIGACT News*, 33(2), 51–59.
- Lamport, L., Shostak, R., & Pease, M. (1982). The Byzantine generals problem. *ACM Trans. Program. Lang. Syst.*, 4(3), 382–401.
