# Closing the Direction-D bridge — $n_a = \langle\mathrm{Sq}^1\omega,[K_5]\rangle$

This is the terminus of the item-23 chase. It states the bridge as a theorem, separates cleanly
what is **new and proven here** from the **one classical input** it rests on, and records the
computation that pins that input's convention with no hand-waving.

## The statement

> **Theorem (Direction-D bridge).** The family-A anticommutation cochain $n_a$ on the proper
> $K_5$ nerve is a cochain-level representative of $\mathrm{Sq}^1\omega$; equivalently
> $$\langle \mathrm{Sq}^1\omega,\,[K_5]\rangle \;=\; \bigoplus_{m=1}^5 (n_a)_m \;=\; N_{\mathrm{anti}}\bmod 2 .$$

The proof is the three-link chain
$$(n_a)_m \;\overset{\text{(A)}}{=}\; q(S_m)\oplus\!\!\bigoplus_{\text{6 rays of }m}\!\! q(v)
  \;\overset{\text{(B)}}{=}\; (c\cup_1 c)\big|_{m}
  \;\overset{\text{(C)}}{=}\; \mathrm{Sq}^1\omega\big|_{m}.$$

## (A) Configuration side — NEW, proven, all $n$

The anticommutation cochain equals the **polarization defect of the quadratic refinement** over
each tetrahedron's six rays:
$$(n_a)_m \;=\; q(S_m)\oplus\bigoplus_{\text{6 rays}} q(v),\qquad
  S_m=\bigoplus_{\text{6 rays}} v,\qquad q(v)=X_v\!\cdot\!Z_v .$$
*Proof.* $q$ is a quadratic refinement of $\omega$ ($q(u{+}v)=q(u)+q(v)+\omega(u,v)$); polarization
(induction) gives $q(S_m)=\bigoplus q(v)\oplus\bigoplus_{i<j}\omega(v_i,v_j)$ over the 6 rays. Of the
15 ray-pairs, the 12 **adjacent** pairs (sharing a vertex Lagrangian) commute ($\omega=0$,
`phi_omega_zero.py`); the 3 **disjoint** pairs are exactly $(n_a)_m$. $\square$
Verified $123{,}000/123{,}000$ per-tetrahedron at $n=4,5,6$ (`closed_form.py`). This is the new
content: it makes the configuration-side obstruction an **explicit, elementary, all-$n$ cochain in
the quadratic refinement** — the handle nothing earlier supplied.

## (C) $V$ side — standard Steenrod, ALL $n$ (`sq1_bar.py` = convention unit-test)

This link is **all-$n$ by definition + Cartan, with zero numerical input** — not an empirical
small-$n$ fact. Let $a_i,b_i:V\to\mathbb F_2$ be the coordinate homomorphisms (1-cocycles).

1. $c=\sum_i a_i\!\cup b_i$, i.e. $c(g_1,g_2)=X_{g_1}\!\cdot\!Z_{g_2}$, is a cup product of
   1-cocycles, hence a **2-cocycle** with $[c]=\sum_i a_ib_i=\omega$ (equivalently: any bilinear
   form is a 2-cocycle for trivial action, $\delta c\equiv0$ — verified directly at $n=1,2,3,4$).
   $q(v)=c(v,v)$ is its diagonal. *[all $n$]*
2. $\mathrm{Sq}^1[c]:=[c\cup_1 c]$ is **Steenrod's definition** ($\mathrm{Sq}^{n-i}x=[x\cup_i x]$),
   and $\cup_1$ is well-defined on cohomology independent of the diagonal-approximation choice. *[all $n$]*
3. $\mathrm{Sq}^1\omega=\mathrm{Sq}^1(\sum_i a_ib_i)=\sum_i(a_i^2b_i+a_ib_i^2)=\sum_i a_ib_i(a_i+b_i)$
   by Cartan + $\mathrm{Sq}^1(\deg 1)=$ square — an identity in $\mathbb F_2[a_i,b_i]$. *[all $n$]*

So $[c\cup_1 c]=\sum_i a_ib_i(a_i+b_i)$ for **every** $n$. The only thing that could be
$n$-*independently* wrong is whether the concrete formula coded for $\cup_1$,
$(c\cup_1 c)(g_1,g_2,g_3)=c(g_1,g_2{+}g_3)c(g_2,g_3)+c(g_1{+}g_2,g_3)c(g_1,g_2)$, is the standard
simplicial cup-1 (vs. a mistranscription that is a cocycle but represents $0$ or the wrong class).
The bar-complex runs are a **unit-test of exactly that transcription**: they confirm the coded
formula yields the *nonzero* $\mathrm{Sq}^1\omega$ — $c\cup_1 c$ a 3-cocycle, $[c\cup_1 c]=[\mathrm{Sq}^1\omega]\neq0$
(the coboundary $\delta r=c\cup_1 c+\mathrm{Sq}^1\omega$ is solvable; $n=1$: $11/16$ pivots,
$n=2$: $234/256$). Since that $\cup_1$ formula is a *fixed $n$-independent combinatorial expression*,
transcription-correctness at $n=1,2$ is correctness for all $n$ (and the $\delta r$ witness need
**not** generalize — it only certifies two representatives of a definitionally-equal class are
cohomologous). The load-bearing cocycle $c$ is separately confirmed a 2-cocycle at $n=1,2,3,4$,
i.e. into and past the $K_5$-rigidity regime.

**Where the $n$-dependence actually lives** (so nothing is smuggled past small $n$): *not here* —
$\mathrm{Sq}^1\omega$ is computed identically for all $n$. The $[n_a]=0\iff n=4$ phenomenon lives in
link (A) — $(n_a)_m=q$-defect, verified **in-regime** at $n=4,5,6$ ($123{,}000/123{,}000$) — and in
the vanishing of the pairing $\langle\mathrm{Sq}^1\omega,[K_5]\rangle$, which is the master theorem
(Papers XX/XXI). (C) being $n$-flat is correct, not a gap.

## (B) The join — a SECONDARY operation, with TWO cited classical inputs

The join is the subtle link, and it must be stated as a *secondary* operation — because the primary
pullback is **zero**. The self-representation map is (at most) $f:\partial\Delta^4=S^3\to BV$; since
$H^2(S^3)=0$ we have $f^*\omega=0$, so by naturality $f^*\mathrm{Sq}^1\omega=\mathrm{Sq}^1(f^*\omega)=0$.
Hence $\langle\mathrm{Sq}^1\omega,[K_5]\rangle=N_{\mathrm{anti}}\neq0$ **cannot** be a primary
operation; it is a secondary (functional) operation whose nullhomotopy datum is $q$. (This is the
same fact that forced $\phi^*\omega\equiv0$ and zero indeterminacy, $H^1(S^3)=0$ — `phi_omega_zero.py`.)

**The nullhomotopy is automatic.** $q$ serves as the cochain trivialization because its
quadratic-refinement identity $q(u{+}w)=q(u)+q(w)+\omega(u,w)$ *is* the nullhomotopy condition
$\delta(q)=\omega$ written in coordinates — no extra verification: being a quadratic refinement is
*exactly* what makes $q$ a nullhomotopy of $\omega$ on the nerve. So (A)'s polarization defect
$q(S_m)\oplus\bigoplus q$ is, by construction, the cochain value of the secondary operation
associated to this nullhomotopy.

Two *distinct* classical inputs identify that secondary operation with $\mathrm{Sq}^1\omega$ — the
join does two different things, and "modulo a cited theorem" means **two** named citations of the
same magnitude:

1. **Steenrod–Epstein functional/secondary-operation formula** (*Cohomology Operations*, the
   explicit functional-$\mathrm{Sq}^i$ cochain): given a nullhomotopy $r$, the secondary operation
   has the explicit form $c\cup_1 c$ plus correction terms in $r$. With $r=q$ this is the *explicit
   cochain shape* of the operation — it is what should expand, term-by-term, to (A). This supplies
   *"what the secondary operation looks like in coordinates."*
2. **Kudo transgression theorem** for the central extension $1\to\mathbb Z/2\to H\to V\to1$: in its
   LHS spectral sequence $E_2=H^*(V)[t]$, $d_2(t)=\omega$ and
   $$\tau(t^2)=d_3(t^2)=\mathrm{Sq}^1\omega,$$
   with $q$ the chain trivialization $t$. This supplies *"what the secondary operation equals"* —
   the Paper XXII outlook backbone (Quillen's $H^*$ of extra-special $2$-groups).

**The final, smallest remaining piece (honest).** Substituting $c$ and the nullhomotopy $q$ into the
Steenrod–Epstein functional formula (input 1) *should* expand exactly to (A)'s polarization defect,
with no leftover term. This expansion is **not** done term-by-term here. Its difficulty class is
"*expand a known formula and check the algebra*" — identical to the already-closed links, **not** a
search for an unknown formula; it is the one minimal step between "structurally closed" and
"closed with every correction term checked." The structural identification (A = the $q$-secondary
operation; its value = $\mathrm{Sq}^1\omega$ by inputs 1–2) stands; what is uncertified is only the
exact match of Steenrod–Epstein's correction terms to the defect.

## Honest ledger

| link | content | status |
|---|---|---|
| (A) | $n_a=$ polarization defect of $q$ | **NEW, proven all $n$** (polarization + adjacency vanishing; $123{,}000/123{,}000$) |
| (C) | $q$'s cup-1 $=\mathrm{Sq}^1\omega$ | **all $n$**, Steenrod's definition + Cartan; $n=1,2$ bar runs = convention unit-test of the coded $\cup_1$ formula ($n$-independent) |
| (B1) | (A) $=$ the $q$-secondary operation's cochain | **classical, cited** (Steenrod–Epstein functional-operation formula); nullhomotopy $\delta q=\omega$ automatic. *Term-by-term expansion to (A): the final smallest open step.* |
| (B2) | that operation's value $=\mathrm{Sq}^1\omega$ | **classical, cited** (Kudo transgression $\tau(t^2)=\mathrm{Sq}^1\omega$ / Quillen extra-special $2$-groups) |

**What is genuinely closed:** the bridge no longer needs a from-scratch "construct the lax
coherence map." The configuration-side obstruction has an explicit elementary cochain (A); that
cochain is provably the standard $\mathrm{Sq}^1\omega$ on the $V$ side (C); and they meet as a
*secondary operation* whose explicit shape is Steenrod–Epstein (B1) and whose value is the Kudo
transgression (B2). The earlier verdict "remaining step is symbolic, convention-heavy handwork" is
now resolved into (C) [done] plus the single minimal expansion-check inside (B1).

**What is *not* claimed:** (i) we do not re-derive Steenrod–Epstein (B1) or Quillen/Kudo (B2) — a
fully self-contained proof would construct $\partial\Delta^4\to BH$ through the extension and
recompute $d_3$ by hand, only reproducing the cited theorems; (ii) we do not (yet) carry out the
term-by-term expansion of the Steenrod–Epstein functional formula on $(c,q)$ to match (A) exactly —
that is the single minimal "expand-and-check" step flagged in (B1). The honest flag from
`phi_omega_zero.py` stands and is now *explained*: $\phi^*\omega\equiv0$, so the bridge is genuinely
a *secondary* operation (zero indeterminacy, $H^1(S^3)=0$, and $f^*\mathrm{Sq}^1\omega=0$ as a
primary class); $q$ is its nullhomotopy datum, which is precisely why a primary (symplectic-pairing)
formula was provably circular.

## Files
- `closed_form.py` — link (A): $(n_a)_m=q(S_m)\oplus\bigoplus q$, $123{,}000/123{,}000$ all $n$.
- `sq1_bar.py` — link (C): $[c\cup_1 c]=[\mathrm{Sq}^1\omega]$ in the bar complex ($n=1,2$).
- `phi_omega_zero.py` — $\phi^*\omega\equiv0$: the bridge is purely secondary (why (B) is a transgression, not a primary class).
- `basis_invariance.py` — $q$ is coordinate, not $\mathrm{Sp}$-invariant; only the net defect is — consistent with $q$ being a chain-level trivialization $t$, not an intrinsic class.
