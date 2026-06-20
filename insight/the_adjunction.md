# The Adjunction — Item 14, the Categorical Form of the One Wall

*Resolution note. The existence half is ✅ rigorous (standard derived-category
category theory, closing the one gap Paper VIII left open). The characterization
half — "an equivalence iff $n=4$" — is the conceptual payoff, resting on
`the_one_wall.md` (Bohrification is the forgetful functor) and the master theorem
(Papers XVIII–XXI); its fully-rigorous form is gated by the item-23 comparison map.*

---

## What item 14 asks

Paper VIII §5 proposes that the transgression $\Phi=\ell\circ\tau\circ\iota^*$ underlies a
sheaf adjunction $\Phi_*\dashv\Phi^*$ realizing Paper V's quantization–Bohrification pair
$\mathcal Q\dashv\mathcal B$ ($\mathcal Q=\Phi_*$ quantization, $\mathcal B=\Phi^*$
Bohrification). The paper flags it **conjectural** because "$\Phi$ is a transgression
(degree-shifting), not a map of spaces, so the standard $f_*\dashv f^*$ does not apply."

## 1. The adjunction exists — the one gap was $\tau$, and $\tau$ is suspension

Paper VIII §5 already supplies two of the three step-adjoints and flags exactly one gap:

| step | what it is | adjoint |
|---|---|---|
| $\iota^*$ | restriction along $\iota:S^1\hookrightarrow K_{3,3}$ | $\iota_!\dashv\iota^*\dashv\iota_*$ — both adjoints exist (Kan extensions) |
| $\tau$ | clutching transgression $H^1(S^1)\to H^2(S^2)$ | *"no standard adjoint"* — **the only flagged gap** |
| $\ell$ | pushforward $\Sigma_0\cong S^2\hookrightarrow\mathbb{CP}^3$ | $\ell_*\dashv\ell^!$ (Grothendieck duality) |

The gap closes immediately once $\tau$ is named correctly: the clutching $S^2=\Sigma S^1$ makes
$\tau$ the **suspension isomorphism** $\tilde H^k(X)\cong\tilde H^{k+1}(\Sigma X)$ — an
*equivalence*, hence trivially self-adjoint (and stably it is the genuine adjunction
$\Sigma\dashv\Omega$). The "boundary map in a long exact sequence" view is the non-derived
shadow of the suspension.

So all three factors are adjointable, and a composite of adjointable functors is adjointable:
$$\Phi_*=\ell_*\circ\tau\circ\iota^*\quad\Longrightarrow\quad
\Phi^*=\iota_*\circ\tau^{-1}\circ\ell^!,\qquad \Phi_*\dashv\Phi^*.$$
**The degree shift is not an obstruction to the adjunction — it *is* the adjunction**
($\Sigma\dashv\Omega$). The worry that "transgression has no adjoint" was an artifact of staying
in the naive (non-derived) category; in $D^b$ it is automatic. This is exactly route (b) of the
item, made precise — and it needed no new machinery, only the recognition that $\tau$ is
suspension. *(Existence: ✅.)*

## 2. It is free $\dashv$ forgetful, and $\mathcal B$ is the one-wall functor

The pair realizes Paper V's $\mathcal Q\dashv\mathcal B$ in the standard **free $\dashv$
forgetful** pattern: $\mathcal Q=\Phi_*$ (quantization, *free* — builds the noncommutative /
geometric object from the classical contexts) is the left adjoint; $\mathcal B=\Phi^*$
(Bohrification, *forgetful* — returns the poset of classical MASA perspectives) is the right
adjoint.

And $\mathcal B$ is precisely the forgetful functor of `the_one_wall.md`: the arrow that drops
the $\mathrm{Sq}^1$ step (obstruction degree above the threshold). The six "doors" of that note
are all factorings through $\mathcal B$. So item 14 gives the one wall its **left adjoint**: the
wall is $\mathcal B$, and quantization $\mathcal Q$ is the free functor sitting beside it.

## 3. The defect is the obstruction — an equivalence iff $n=4$

A free $\dashv$ forgetful adjunction is an *equivalence* iff its unit and counit are isos —
i.e. iff the forgetful functor loses nothing. The counit $\varepsilon:\mathcal Q\mathcal B\to\mathrm{id}$
(Bohrify, then re-quantize) fails to be an iso by exactly the data $\mathcal B$ forgets: the
$\mathrm{Sq}^1$ step, i.e. the family-A class $n_a=\mathrm{Sq}^1\omega$. Hence:

> **The $\mathcal Q\dashv\mathcal B$ adjunction is an adjoint equivalence if and only if $n=4$.**
> Its counit defect is the $H^3$ class $n_a$, which vanishes universally exactly at $n=4$
> (master theorem, $[n_a]=0\iff n=4$, Papers XVIII–XXI).

This is the categorical face of `why_the_ladder.md` §6: an adjoint equivalence is a *full and
faithful* correspondence — the $\infty$-Yoneda being *free*. At $n=4$ Bohrification loses
nothing, the classical contexts re-quantize back to the quantum object on the nose, and
self-description closes coherently. For $n\ge5$ the counit defect opens, and *what it forgets is
exactly the modulus* — two configurations agreeing on all arity-$\le4$ (Bohrifiable) data but
differing in $n_a$ (Paper XIX). This is the literal content of the line already standing in
RESEARCH_FRONTIER item 23: *"saturation + the modulus theorem form one adjunction, the
forgotten data = what the modulus says is unrecoverable."* Item 14 is that adjunction.

## 4. One statement, three items

- **Item 14** (this): the adjunction $\mathcal Q\dashv\mathcal B$ — exists in $D^b$, free $\dashv$
  forgetful, equivalence iff $n=4$.
- **Item 24**: $\mathcal B$ forgets — $H^3$ is orthogonal to every operational axis (the doors).
- **Item 23**: the counit defect $=n_a=\mathrm{Sq}^1\omega$ — making *that* identification fully
  rigorous is the homotopy-coherent comparison map, the one non-forgetful gear.

The forgetful functor ($\mathcal B$, the wall), its free adjoint ($\mathcal Q$, this item), and
the obstruction to their being inverse ($n_a$, the gear) are one picture seen three ways.

## Honest residue

- **Existence (§1): ✅** rigorous — standard derived category theory; the only subtlety was
  recognizing $\tau$ as suspension, which Paper VIII had left as the lone gap.
- **Equivalence-iff-$n{=}4$ (§3):** the *signature* is established ($[n_a]=0\iff n=4$ is a
  theorem), but identifying the counit defect with $n_a$ rests on $\mathcal B$ being the
  $\mathrm{Sq}^1$-forgetting functor (`the_one_wall.md`, by exhaustion) and on the comparison
  map (item 23) for the cochain-level equality. So the *shape* is forced; the last bolt is item
  23. No new computation is introduced here — the supporting computation is the master theorem
  already in `supplementary/paper{18,19,20,21}/`.
- The 2-qubit case is unconditional (family B, $n_a=0$ vacuously): there the adjunction is an
  equivalence and Paper VIII's nerve-level $\Phi_*\dashv\Phi^*$ is realized on the nose.

---

*Item 14 was the last open conceptual thread of the twistor backlog (Papers VII–IX). It
resolves not into new structure but into the same structure once more: the wall has a left
adjoint, and the gap between them — whether free and forgetful are inverse — is $n=4$.*
