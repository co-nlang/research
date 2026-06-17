# Is the $H^3$ ceiling a $\mathbb F_2$ artifact? — the $\mathbb Z/4$-Bockstein route is closed

Answers a sharp objection: the Pauli group is the central extension
$0\to\mathbb Z/4\to P_n\to V=(\mathbb Z/2)^{2n}\to0$ (phases $\pm1,\pm i$), not the
$\mathbb F_2$ quotient. Lifting coefficients $\mathbb F_2\to\mathbb Z/4$, doesn't the
Bockstein of $0\to\mathbb Z/2\to\mathbb Z/4\to\mathbb Z/2\to0$,
$$\beta:H^3(\cdot;\mathbb Z/2)\to H^4(\cdot;\mathbb Z/2),$$
leak the $H^3$ obstruction into $H^4$ and break the "arity-resonance ceiling"?

## The answer (computed, `sq1_ceiling.py`, $V=(\mathbb Z/2)^8$)

The $\mathbb Z/4$ structure is **already in the framework** ($q$ = quadratic refinement /
$i$-phase, Papers XI/XIII/XV; $\omega$ is its polarization). The Bockstein $\beta$ of that
sequence **is** the Steenrod square $\mathrm{Sq}^1$ on mod-2 cohomology, and the family-A
source is $n_a=\mathrm{Sq}^1\omega$ (Direction D). So the $H^3$ class is *already the
$\mathbb Z/4$-Bockstein of the $H^2$ class* — the objection names the framework's own
$q\to\omega\to\mathrm{Sq}^1\omega$ transgression.

**(A) $\beta^2=0$ (Adem $\mathrm{Sq}^1\mathrm{Sq}^1=0$):** computed $\mathrm{Sq}^1\omega$ =
8 deg-3 monomials ($=n_a$), and $\mathrm{Sq}^1(\mathrm{Sq}^1\omega)=0$. So
$\beta(n_a)=\beta(\beta\omega)=0$ — **the Bockstein annihilates the class it would carry; no
leak to $H^4$.**

**(B) No exotic higher Bockstein:** $H^*(V;\mathbb Z)$ has exponent 2 (no $\mathbb Z/4$
torsion in the cohomology of an elementary abelian 2-group), so the Bockstein spectral
sequence collapses at $E_2$ and $H^*(V;\mathbb F_2)=\mathbb F_2[x_1..x_{2n}]$ is
$\mathrm{Sq}^1$-**acyclic in positive degrees** — computed: $\mathrm{Sq}^1$-cohomology
$H^3=H^4=0$ on $V=(\mathbb Z/2)^8$. The lift reveals nothing past $\mathrm{Sq}^1$; there is no
room to manufacture a new $H^4$ obstruction.

Together with Paper XXII's independent result that the natural degree-4 assembly $c=\delta a$
is exact, **both** candidate $H^4$ classes vanish.

## Verdict

The ceiling is **not** an $\mathbb F_2$ artifact. It is controlled by $\beta^2=0$ — a fact
about the $\mathbb Z/4$ structure itself — plus the exponent-2 cohomology of $V$. Lifting to
$\mathbb Z/4$ (or integrally) does not leak $H^3$ to $H^4$.

**Honest residue.** The no-leak conclusion is contingent on $n_a$ being $\mathrm{Sq}^1$-closed,
i.e. $n_a=\mathrm{Sq}^1\omega$ — exactly **Direction D / item 23 (open)**. If $n_a$ were not
$\mathrm{Sq}^1$-closed, $\beta(n_a)\ne0$ and the objection would bite. So the challenge
sharpens to the framework's own open capstone, not a coefficient-ring mistake. Item 21 (a
genuinely non-bilinear, non-Bockstein arity-5 invariant) is separately open.

## Files
- `sq1_ceiling.py` — (A) $\beta^2\omega=0$ and (B) $\mathrm{Sq}^1$-acyclicity of $H^*(V;\mathbb F_2)$ in degrees 3,4. Pure F2, no deps.
