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

## (C) $V$ side — standard Steenrod, convention PINNED (`sq1_bar.py`)

The symplectic class is $\omega=[c]\in H^2(BV;\mathbb F_2)=\bigoplus_i a_ib_i$, where
$c(g_1,g_2)=X_{g_1}\!\cdot\!Z_{g_2}$ is the cup/extension cocycle of the Heisenberg
(extra-special) $2$-group, and $q(v)=c(v,v)$ is its diagonal. The lowest Steenrod square of a
$2$-cocycle is its cup-1 self-product, so $\mathrm{Sq}^1\omega=[c\cup_1 c]$. We verified **directly
in the bar complex of $V$**, with no configuration and no appeal to a table, that
$$ c\cup_1 c \ \text{is a 3-cocycle},\quad \mathrm{Sq}^1\omega=\textstyle\sum_i a_ib_i(a_i+b_i)\ \text{a nonzero 3-cocycle},\quad
   [c\cup_1 c]=[\mathrm{Sq}^1\omega] $$
($n=1$: $11/16$ pivots; $n=2$: $234/256$; the coboundary equation $\delta r=c\cup_1 c+\mathrm{Sq}^1\omega$
is consistent). So the object built from $q$ **is** the textbook $\mathrm{Sq}^1\omega$ — the
convention match the chase had flagged as the open symbolic step is now a computation, not a claim.

## (B) The join — Kudo transgression of the Heisenberg LHS spectral sequence

(A) and (C) share the *same* $q$: in (A) $q$ is the quadratic refinement whose polarization defect
is $n_a$; in (C) $q=c(v,v)$ is the diagonal of the cocycle whose cup-1 is $\mathrm{Sq}^1\omega$.
The precise identity of these two roles is the **Kudo transgression theorem** for the central
extension $1\to\mathbb Z/2\to H\to V\to 1$: in its LHS spectral sequence
$E_2=H^*(V)[t]$, the transgressive generator satisfies $d_2(t)=\omega$, and
$$\tau(t^2)=d_3(t^2)=\mathrm{Sq}^1\omega .$$
At chain level $q$ **is** the trivialization $t$ ($\delta q=\omega$), and the polarization defect
$q(S_m)\oplus\bigoplus q$ is exactly the chain realization of $\tau(t^2)$. This is the one classical
input; it is the Paper XXII outlook backbone (Quillen's $H^*$ of extra-special $2$-groups), not a
new theorem.

## Honest ledger

| link | content | status |
|---|---|---|
| (A) | $n_a=$ polarization defect of $q$ | **NEW, proven all $n$** (polarization + adjacency vanishing; $123{,}000/123{,}000$) |
| (C) | $q$'s cup-1 $=\mathrm{Sq}^1\omega$ | standard Steenrod; **convention pinned by direct bar-complex check** ($n=1,2$) |
| (B) | the two $q$'s coincide $=\tau(t^2)$ | **classical** (Kudo transgression / Quillen extra-special $2$-groups) — cited, not re-derived |

**What is genuinely closed:** the bridge no longer needs a from-scratch "construct the lax
coherence map." The configuration-side obstruction has an explicit elementary cochain (A); that
cochain is provably the standard $\mathrm{Sq}^1\omega$ on the $V$ side (C); and they meet at the
Kudo transgression (B). The earlier verdict "remaining step is symbolic, convention-heavy
handwork" is resolved into (C), now a finished computation.

**What is *not* claimed:** we do not re-derive Quillen/Kudo (B). A fully self-contained proof would
construct the self-representation map $\partial\Delta^4\to BH$ through the extension and recompute
$d_3$ by hand — which only reproduces the cited theorem. The honest flag from `phi_omega_zero.py`
stands: $\phi^*\omega\equiv0$, so the bridge is genuinely a *secondary* operation (zero
indeterminacy, $H^1(S^3)=0$); $q$ is its nullhomotopy datum, and that is precisely why a primary
(symplectic-pairing) formula was provably circular.

## Files
- `closed_form.py` — link (A): $(n_a)_m=q(S_m)\oplus\bigoplus q$, $123{,}000/123{,}000$ all $n$.
- `sq1_bar.py` — link (C): $[c\cup_1 c]=[\mathrm{Sq}^1\omega]$ in the bar complex ($n=1,2$).
- `phi_omega_zero.py` — $\phi^*\omega\equiv0$: the bridge is purely secondary (why (B) is a transgression, not a primary class).
- `basis_invariance.py` — $q$ is coordinate, not $\mathrm{Sp}$-invariant; only the net defect is — consistent with $q$ being a chain-level trivialization $t$, not an intrinsic class.
