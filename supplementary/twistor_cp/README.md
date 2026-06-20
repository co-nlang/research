# Item 13 — the geometric realization on $\mathbb{CP}^{2^n-1}$ is family-B only

Paper VIII §3 conjectured a family of higher differentials $d_k^{\text{eff}}$ realizing
the $n$-qubit obstruction ladder geometrically on $\mathbb{CP}^{2^n-1}$, and flagged three
obstacles for $n\ge3$. This note resolves the item, using the post-Paper-VIII machinery
(Direction D's $n_a=\mathrm{Sq}^1\omega$, the bockstein work).

## The answer

$H^*(\mathbb{CP}^N;\mathbb F_2)=\mathbb F_2[h]/h^{N+1}$, $|h|=2$: **even degree only**, and
$$\mathrm{Sq}^1 h = 0\quad(h=c_1(\mathcal O(1))\bmod2\text{ is an integral reduction}),\qquad
\mathrm{Sq}^2 h = h^2.$$
So $\mathbb{CP}^N$ is $\mathrm{Sq}^1$-**acyclic**; its entire Steenrod structure is the
$\mathrm{Sq}^2$/cup-power ladder $h,h^2,h^3,\dots$.

The framework's family-B class is $\omega\in H^2(V)$ (the Heisenberg/KS extension class);
the family-A pentagram class is $n_a=\mathrm{Sq}^1\omega\in H^3(V)$ (Direction D). Hence:

1. **The conjectured ladder exists — as family B.** The cup-power identification
   $h^k\leftrightarrow\omega^k$ realizes the family-B classes geometrically. Paper VIII's
   Theorem 2.1 ($h\leftrightarrow$ Peres–Mermin class) is its $k=1$ case, and the PM square
   *is* family B. So $d_k^{\text{eff}}$ is the family-B cup-power ladder.

2. **The family-A $H^3$ Borromean class is not faithfully realizable on $\mathbb{CP}^{2^n-1}$.**
   The identification $h\leftrightarrow\omega$ is a ring iso onto $\mathbb F_2[\omega]$ but is
   **not a map of Steenrod modules** — it fails already at the generator:
   $\mathrm{Sq}^1 h=0$ while $\mathrm{Sq}^1\omega=n_a\ne0$. Equivalently, $\omega$ does **not**
   lift to an integral (Chern) class; the obstruction is the integral Bockstein
   $\beta\omega=\mathrm{Sq}^1\omega=n_a$. The family-A class is *precisely the Steenrod
   obstruction to the family-B geometric realization being natural.*

So the geometric/twistor side hosts $\mathrm{Sq}^2$ (family B) and is structurally **blind**
to $\mathrm{Sq}^1$ (family A) — the same orthogonality found operationally (item 24), and the
same $A\!\leftrightarrow\!B$ / $\mathrm{Sq}^1$ wall that is the open capstone (item 23), now
wearing geometric (twistor) clothes.

## Computed (`cp_realization.py`, $n=2\to\mathbb{CP}^3$, $n=3\to\mathbb{CP}^7$)

- $\omega$: 3 monomials in $H^2$; $n_a=\mathrm{Sq}^1\omega$: 6 monomials in $H^3$, $\ne0$.
- Cup-power table: $\mathrm{Sq}^1(\omega^{2j})=0$ (matches $h^{2j}$, genuine $c_1$-powers),
  but $\mathrm{Sq}^1(\omega^{2j+1})=\omega^{2j}n_a\ne0$ (**unlike** any $h^k$, since
  $\mathrm{Sq}^1\equiv0$ on $\mathbb{CP}$) — the family-A class leaks in at every odd power,
  starting at the generator.
- Integral-lift test: $\omega^2$ lifts ($\mathrm{Sq}^1=0$), $\omega$ does not — $\omega$ is
  not a Chern class, obstruction $n_a$.

## Obstacle audit (Paper VIII §3)

1. *"No PM-like config for $n\ge3$."* **Dissolved** — the Mermin pentagram is the 3-qubit
   config (Papers X–XVII); the "different combinatorics" is the family A/B split.
2. *"$\mathrm{Ext}^1$ of $\Sigma_0^{(n)}\subset\mathbb{CP}^{2^n-1}$ not computed."*
   **Redirected** — the pentagram's Čech nerve collapses (Paper XX); the $H^3$ class lives on
   the Maslov–Wall complex $\partial\Delta^4=S^3$, not on $\Sigma_0^{(n)}$. The Ext object is
   the wrong home.
3. *"$c_2(\mathcal O(1))=0$, need another class."* **Resolved** — the target is the
   cup-power $h^k=c_1^k$ (nonzero), not the Chern class $c_k$ (zero for a line bundle). The
   obstacle conflated $c_1^2$ with $c_2$.

## Files
- `cp_realization.py` — cup-power ladder, $\mathrm{Sq}^1$ behaviour, integral-lift obstruction
  for $n=2,3$. Pure $\mathbb F_2$, no deps.
