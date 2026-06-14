# Graph Coloring as a Cohomological Obstruction

**Moser Spindle, Petersen = Kneser, and the distributed bridge.**

> **Revision note (2026-06-14).** This note began (Paper IV–VI era) as an
> intuition-driven sketch titled *"The $d_2$ Transgression in Moser Spindle."*
> The combinatorial core was right; the machinery was shoehorned. This revision
> keeps the worked example, **retracts** the $d_2$/$U(1)$-transgression and
> "NP-completeness fingerprint" overclaims, and replaces them with the correct
> cohomological framing — plus the genuinely rigorous coloring/topology theorem
> (Lovász–Borsuk–Ulam) that the original was groping toward, and the distributed
> bridge (Herlihy) that actually connects back to `n/`.

---

## 1. The worked example: why Moser Spindle is not 3-colorable

The Moser spindle is the smallest unit-distance graph requiring 4 colors:
7 vertices, 11 edges. Vertices $\{w, A, B, C, D, y_1, y_2\}$, built from two
"rigid diamonds" (each = two triangles sharing an edge) glued at $w$, with a
cross edge $(y_1, y_2)$.

**Local rigidity (the heart).** In a diamond — two triangles sharing edge
$(A,B)$, apex vertices $w$ and $y_1$ — any 3-coloring forces $w$ and $y_1$ to
the *same* color (each is the unique third color against $\{c(A),c(B)\}$). So:

- Left diamond $U_L=\{w,A,B,y_1\}$ forces $c(y_1)=c(w)$.
- Right diamond $U_R=\{w,C,D,y_2\}$ forces $c(y_2)=c(w)$.
- Cross edge $U_C=\{y_1,y_2\}$ requires $c(y_1)\ne c(y_2)$.

Hence $c(y_1)=c(w)=c(y_2)$ yet $c(y_1)\ne c(y_2)$ — contradiction. No global
3-coloring. This is the entire proof, and it is correct.

## 2. The clean cohomological framing (corrected)

Cover the graph by the three contexts $U_L, U_R, U_C$ above (pairwise overlaps
$\{w\}$ — vacuous, $\{y_1\}$, $\{y_2\}$; empty triple overlap, so the nerve is
**1-dimensional**). Let $\mathcal{F}$ be the presheaf of locally-consistent
3-colorings ($\mathcal F(U)$ = colorings of $U$'s vertices satisfying its edges).

The right statement is **Abramsky's sheaf-theoretic contextuality**
(Abramsky–Brandenburger; Abramsky–Mansfield–Barbosa, *contextuality, cohomology
and paradox*): a CSP / coloring problem is an empirical model over this cover;
**non-colorability = no global section = $\check H^0(\mathcal U,\mathcal F)=\varnothing$**,
and the **Čech $\check H^1$ obstruction** (with the abelian linearization of
$\mathcal F$) is a *witness* for it. Here the witness is the cocycle on the cross
edge: the two diamonds each transport "$c(w)$" to $y_1, y_2$, and the edge
$(y_1,y_2)$ refuses to glue them — a local-to-global gluing failure on a
1-dimensional nerve. **This is the same machine as Kochen–Specker** (§6).

What is *not* right (the retraction): there is no central $U(1)$ extension and no
LHS $d_2$ transgression here — 3-coloring constraints are $\mathbb Z/3$/set-valued,
not a group extension. The "$d_2$" language and the "spectral fingerprint of
NP-completeness" claim were forced analogies. (A single fixed 4-chromatic graph
is a finite fact; NP-completeness is a worst-case statement over *all* graphs —
the two are not the same object.)

## 3. The rigorous coloring/topology theorem — and where Petersen sits

The genuinely rigorous "coloring = cohomology" statement is **Lovász's
topological lower bound** (his proof of the Kneser conjecture via Borsuk–Ulam):
$$\chi(G)\ \ge\ \mathrm{conn}\big(N(G)\big)+3 \quad\Longleftrightarrow\quad
  \chi(G)\ \ge\ \mathrm{ind}_{\mathbb Z/2}\big(B(G)\big)+2,$$
where $N(G)$ is the neighborhood complex and $B(G)$ the (box) complex. The
chromatic number is bounded below by a **$\mathbb Z/2$-Borsuk–Ulam obstruction**,
detected by Stiefel–Whitney classes. This is "the obstruction to $k$-coloring is
a $\mathbb Z/2$ cohomology class" — rigorously, not by analogy.

**The connection to this project:** the bound is *tight* exactly on **Kneser
graphs**, $\chi(K(n,k))=n-2k+2$ — and **the Petersen graph of Paper XVII is the
Kneser graph $K(5,2)$** (vertices = 2-subsets of $\{1,\dots,5\}$ = the 10 rays;
edges = disjoint pairs = the 15 anticommuting cross-context pairs). So XVII's
anticommutation graph sits precisely in the family where chromatic number *is* a
Borsuk–Ulam cohomological obstruction. $\chi(K(5,2))=3$.

## 4. Correction: Petersen is 3-(vertex)-colorable; it is a snark

RESEARCH_FRONTIER item 16 states "Petersen is non-3-colorable ($\chi=4$)" — this
is **wrong for vertex coloring**: $\chi(\text{Petersen})=3$ (the Kneser value).
What is special is that Petersen is the **smallest snark**: bridgeless cubic and
*not 3-edge-colorable*, $\chi'=4=\Delta+1$. So a precise KS $\leftrightarrow$
Petersen link must go through either (a) the **snark / edge-coloring** property,
or (b) the **Borsuk–Ulam / Kneser** structure of §3 — not generic vertex
non-3-colorability. (Item 16 should be re-posed accordingly.)

## 5. The distributed bridge — the part that returns to `n/`

The coloring $\to$ topology $\to$ distributed-computing chain is real and
load-bearing: **Herlihy–Kozlov–Rajsbaum, *Distributed Computing Through
Combinatorial Topology*** (the asynchronous computability theorem of
Herlihy–Shavit). Wait-free solvability of a task $\Longleftrightarrow$ existence
of a **chromatic** simplicial map from a *chromatic subdivision* of the input
complex to the output complex — where "chromatic" literally means colored by
process IDs, and unsolvability is a topological obstruction.

This is the version of "coloring = topology" that matters for `n/`: APP_07
already maps the obstruction ladder onto distributed computing (CAP/FLP/Byzantine).
Herlihy's chromatic-subdivision topology is the rigorous body that should sit
behind APP_07's $H^2/H^3$ rows — more relevant than any plane-coloring result.

## 6. Comparison with Kochen–Specker (refined)

| Feature | Peres–Mermin (KS) | Moser Spindle (CSP) |
|---|---|---|
| Base nerve | $K_{3,3}$ (1-dim) | 3-context cover (1-dim) |
| Fiber / coefficients | Pauli group (central $\pm1$) | 3-coloring constraint presheaf |
| Obstruction | $-\mathbf I$ central sign, $H^2$(group) | no global section, $\check H^1$(sheaf) |
| Common form | **1-dim nerve, gluing failure carried by the fiber/coefficients** | same |

Both are local-to-global gluing failures on a 1-dimensional nerve — the shared
"holographic" shape of the whole series (boundary/local data fails to determine
the global). The honest caveat: the *coefficient systems differ* (a group
central extension vs a constraint presheaf), so they are siblings under the
Abramsky sheaf framework, not literally the same class.

## 7. Off-ladder (kept as scenery): Hadwiger–Nelson

Moser Spindle's native home is the **Hadwiger–Nelson problem** (chromatic number
of the plane): it was the standing lower-bound witness ($\chi(\mathbb R^2)\ge4$)
until **de Grey (2018)** built a 1581-vertex unit-distance graph with $\chi=5$
(later reduced to ~509 by Polymath16), giving $\chi(\mathbb R^2)\ge5$. But these
bounds are *geometric/combinatorial* (exhibit a finite $k$-chromatic
unit-distance graph); the Lovász–Borsuk–Ulam machinery of §3 does **not** grab
the plane's chromatic number. Beautiful, but it does not feed the cohomological
ladder — a genuine rabbit hole, correctly left in the backlog
(RESEARCH_FRONTIER, alongside item 12).

---

*Summary of the revision: the CSP-as-gluing-failure instinct was right and is
exactly Abramsky's sheaf contextuality; the rigorous coloring-cohomology is
Lovász/Borsuk–Ulam, sharp on Kneser = Petersen (XVII); the `n/`-relevant bridge
is Herlihy's distributed topology; the $d_2$/NP framing and the Hadwiger–Nelson
line are retracted to honest status.*
