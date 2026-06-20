# Item 23 — parametrized correction search (the $(\mu,F)$ family is ruled out)

A concrete attack on item 23's "find the coherence-corrected cup-1" step (suggested by a
collaborator): instead of waiting for insight, **parametrize** the candidate correction as a
finite family and search it by $\mathbb F_2$ linear algebra — verification is microseconds, so
the whole family can be settled at once.

## The family tested

On the fixed nerve $\partial\Delta^4=S^3$, the family-A cochain $a_T=(n_a)_T\bmod2$ (per
tetrahedron) as **any degree-$\le2$ $\mathbb F_2$-polynomial** in $T$'s four-face data
$\{\mu(f_0..f_3),\,F(f_0..f_3)\}$ — $\mu$ the Maslov bit, $F$ the Fano indicator
$[v_{ij}+v_{jk}+v_{ik}=0]$ (8 bits/T; 37 coefficients $=1+8+\binom82$). This family contains the
naive cup-1 $\mu\cup_1\mu$ (two $\mu\mu$ terms) and the "Fano-weighted correction" ($\mu F$ terms).
The system $a_T=\sum_i c_i B_i(T)$ over (config $\times$ 5 tetrahedra) is solved by Gaussian
elimination — consistent $\Rightarrow$ formula found; inconsistent $\Rightarrow$ no such formula.

## Result: NEGATIVE, decisively (`quad_search.py`, `collision_test.py`)

- **Degree-$\le2$ system inconsistent.** Cochain level: rank 11/37, **33 296 / 126 500 rows contradictory**. Class level ($N_{\mathrm{anti}}\bmod2=\sum_T$poly): rank 10/37, **10 064 / 25 300 contradictory**. (Validation: at $n=4$ alone the system is consistent with $a_T=0$, $=\delta\mu$ since $\mu\equiv1\Rightarrow\delta\mu=0$ there.)
- **And it is not a degree question.** The collision test shows $a$ is **not a function of $(\mu,F)$ at any degree**: distinct configs share identical full $(\mu,F)$ on all 10 triangles yet differ in $a$. $n=5$: ~123 of ~430 $(\mu,F)$-keys carry $>1$ value of $a$ (e.g. both $(0,0,0,0,0)$ and $(1,0,0,0,0)$). $n=6$: even $n$ forces $\mu\equiv1$, $F$ constant $\Rightarrow$ a **single** $(\mu,F)$-key, yet $a$ ranges over **all 32** values — $(\mu,F)$ is totally blind to the family-A class.

## Why (the arity gap) — and what it means for item 23

$a$ is intrinsically **arity-4** (anticommutation of ray *pairs*); $\mu,F$ are **arity-3**
(triangle data). The resonance separation $H^2(K_4)$ vs $H^3(K_5)$ *is* the statement that the
arity-4 class is irreducible to arity-3 data — so no $(\mu,F)$-formula can produce $a$. The
collision test is an empirical shadow of **Paper XIX's modulus** (arity-$\le k$ invariants do not
classify the $H^3$ fiber).

**Net for item 23.** The collaborator's *meta-strategy* (parametrize + $\mathbb F_2$ linear
algebra) is sound, fast, and decisive — and the harness is reusable. But the *natural $(\mu,F)$
family is killed wholesale*, and the reason sharpens the target rather than shaving it: the
correct secondary formula must use **arity-4 / ray-pairing (Gram-level, edge-pair) data**, not the
Maslov/Fano triangle summaries — i.e. the "nullhomotopy $\beta$" the lax map needs lives finer
than $\mu$. The naive $\mu\cup_1\mu$ failure (`paper22/geometric_route.py`, ~57% at $n=5$) is now
explained and generalized: not the wrong combination of $\mu$, but $\mu$ is the wrong altitude.

## Files
- `quad_search.py` — the degree-$\le2$ $(\mu,F)$ linear system (cochain + class level), with the $n=4$ validation.
- `collision_test.py` — the decisive "is $a$ any function of $(\mu,F)$?" test (no, at all degrees).
