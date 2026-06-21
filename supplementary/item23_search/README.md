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

## The chase's terminus: the symplectic formula-search is *circular* (`phi_omega_zero.py`)

Pursuing the sharpened target ("use ray-pairing / arity-4 data, not $\mu,F$") hits a structural
floor. A **composable** pairing $\omega(v_{ij},v_{jk})$ pairs two rays both lying in the shared
Lagrangian $L_j$ — they **commute**, so it vanishes. Verified: every composable pairing is $0$
(**0/933000** across $n=4,5,6$). Hence:

1. **$\phi^*\omega\equiv0$ at the cochain level** (not just the class) — so $a=\mathrm{Sq}^1\omega$
   pulled back has **no primary part**: it is a *purely* secondary operation (the strongest form
   of "the bridge is secondary/lax").
2. **The only nonzero symplectic pairings on the nerve are the disjoint ones** $\omega(v_{ij},v_{kl})$
   ($\{i,j\}\cap\{k,l\}=\varnothing$) — and their matched sum **is $a$**. Defect pairings reduce to
   these too ($\omega(w_{ijk},v_{il})=\omega(v_{jk},v_{il})$, same-Lagrangian terms drop). So every
   symplectic expression in the rays/defects is a linear combination of the disjoint pairings $=a$
   itself ⟹ **any "formula for $a$ in the symplectic data" is circular.**

So the parametrized-search program cannot produce a non-trivial bridge over symplectic data —
there is no "lower" symplectic datum to build $a$ from. (The earlier "$b_\omega\cup_1 b_\omega$
matches $a$" run was *confounded*: $b_\omega\equiv0$, so its match% is exactly the $a{=}0$
frequency $100\%/76.6\%/50.5\%$.) The one nonzero *non-symplectic* lower datum is the polarized
cocycle $f$ / quadratic refinement $q$ ($\mathbb Z/4$ structure), nonzero even on commuting pairs;
but $\mathrm{cup}_1$ of it matches only $\sim74\%/61\%$ — so the correct object is the
**$\mathbb Z/4$-Bockstein of $q$** ($\mathrm{Sq}^1\omega=\beta_{\mathbb Z/4}$), not a cup-1, a
convention-heavy chain-level computation = the identified next step.

**Net of the chase:** confirmed *insight-bound at a structural level* — the formula-search is
provably circular over symplectic data; the bridge content lives in the $\mathbb Z/4$ quadratic-
refinement / Bockstein (the lax coherence assembling the defects into $\mathrm{Sq}^1\omega$), which
is the genuine $\infty$-categorical / topological work, not algebra over the pairings.

## The ladder of failures: no cochain-level summary determines $a$ (`q_determinacy.py`)

Is the last segment ($\beta_{\mathbb Z/4}(q)$) computable or handwork? We tested whether $a$ is
determined by the **quadratic-refinement / $\mathbb Z/4$ data** $q$ (the polarized $f$ on
composable rays — *non-circular*, nonzero where $\omega$ vanishes, and far finer than $(\mu,F)$).
**Verdict: $a$ is not a function of $q$ either** — witnessed, though narrowly: at $n=5$, 20000
configs give 19896 distinct $q$-keys ($q$ is *nearly injective*) yet **32** keys split (same $q$,
different $a$); $n=6$: 5394 keys, 2 splits. So the three natural cochain-level data layers **all**
fail to determine $a$:

| layer | arity | verdict |
|---|---|---|
| symplectic pairings | 2 | **circular** ($\phi^*\omega\equiv0$; only nonzero pairings $=a$ itself) |
| Maslov + Fano $(\mu,F)$ | 3 | determines-not, **coarsely** (430 keys, 123 split — the arity gap) |
| quadratic refinement $q$ | — | determines-not, **finely** ($q$ nearly injective, still 32 split) |

**Answer to "computable or handwork?" (CORRECTED below).** *Verification* is always computable;
and the three layers above show no **local / low-arity** summary determines $a$. The earlier
phrasing "no cochain-level summary statistic determines $a$" was **overstated** (a universal claim
from a finite set of tested families — the collaborator flagged exactly this): see the next
section — a **global** quadratic-refinement closed form *does* exist.

## CORRECTION + the closed form: $a$ does have a formula in $q$ (`closed_form.py`)

Following the collaborator's lead — "$q$ *almost* determines $a$ (the Bockstein signature)" + the
cheap stratum test (resolved 15/32 of the $n=5$ $q$-collisions) — the missing ingredient turned
out to be a single **global** term. There is an exact, all-$n$, elementary closed form:
$$N_{\mathrm{anti}}\bmod2 \;=\; q(T)\;\oplus\;\bigoplus_i q(v_i),\qquad
  T=\bigoplus_i v_i,\quad q(v)=\mathrm{parity}(X_v\!\cdot\!Z_v).$$
*Proof (all $n$):* $q$ is a quadratic refinement ($q(u{+}v)=q(u)+q(v)+\omega(u,v)$); polarization
gives $q(T)=\bigoplus_i q(v_i)\oplus\bigoplus_{i<j}\omega(v_i,v_j)$; composable pairs vanish
($\phi^*\omega\equiv0$) so $\bigoplus_{i<j}\omega=N_{\mathrm{anti}}$. Verified **24,600/24,600**
exact at $n=4,5,6$.

**Cochain-level (per-tetrahedron) form** — what item 23's pairing actually needs
($\langle\mathrm{Sq}^1\omega,[K_5]\rangle=\bigoplus_m(n_a)_m$): the same polarization applied to
each tetrahedron's 6 rays gives
$$(n_a)_m\bmod2 \;=\; q(S_m)\;\oplus\;\bigoplus_{\text{6 rays of tetra }m} q(v),\qquad
  S_m=\bigoplus_{\text{6 rays}} v,$$
**verified 123,000/123,000 per-tetra checks exact at $n=4,5,6$.** So the family-A *cochain*
$n_a$ — not just the total — is closed-form in $q$.

So the corrected statement: **no *local/low-arity* summary determines $a$, but a *global*
quadratic-refinement closed form does** — the $q$-collision tests missed it only because their keys
had the per-ray $q(v_i)$ but not the global $q(T)$ (no contradiction with the modulus: $q(T)$ is an
arity-10 functional, not a low-arity invariant).

**Attribution (honest):** the *total* formula is **not new** — it is **Paper XI's Proposition
(Quadratic form identity)**, $q(T)=\sum_a q(r_a)+\omega_{\text{total}}\pmod2$, over the *same* 10
rays $r_a=v_{ij}$ (rediscovered here; the "5 representatives" reading was a misread — it is the
10-ray cap in both). It is also the ambient form of Paper XIX's intrinsic $Q(T)=N_{\mathrm{anti}}$
(S5). The genuinely **new** parts are (i) the **per-tetrahedron cochain** refinement above, and
(ii) the **item-23 framing** ($q$-form as the explicit handle for $\langle\mathrm{Sq}^1\omega,[K_5]\rangle$).

**Coordinate, not intrinsic — verified (`basis_invariance.py`).** $q$ is not $\mathrm{Sp}$-invariant:
under a symplectic change of basis (transvections) the individual $q(v_i),q(T)$ change ($\sim97\%$
of configs) but the net XOR stays $=N_{\mathrm{anti}}$ ($900/900$). So the formula is
$\mathrm{Sp}$-invariant though its summands are not — the precise content of "coordinate closed
form, not intrinsic bridge."

**What it does and doesn't do for item 23.** It is a *coordinate* closed form: $q$ is not
$\mathrm{Sp}$-invariant (only the net combination is), so it is not yet the *intrinsic*
cohomological bridge $N_{\mathrm{anti}}=\langle\mathrm{Sq}^1\omega,[K_5]\rangle$. But $q$ is exactly
the $\mathbb Z/4$ lift of $\omega$ and $\mathrm{Sq}^1\omega=\beta_{\mathbb Z/4}(\omega)$, so this is
the explicit $q$-handle the $\beta_{\mathbb Z/4}(q)$ direction predicted — the remaining open step
is to identify $q(T)\oplus\bigoplus_i q(v_i)$ with the chain-level
$\langle\mathrm{Sq}^1\omega,[K_5]\rangle$, **with both sides now explicit** (a checkable identity,
not a blind search). *Net revision of the verdict:* item 23 is more computable than the chase's
terminus suggested — the family-A class has a clean closed form; what remains genuinely symbolic is
the *intrinsic* identification, not the existence of a formula.

## Files
- `quad_search.py` — the degree-$\le2$ $(\mu,F)$ linear system (cochain + class level), with the $n=4$ validation.
- `collision_test.py` — the decisive "is $a$ any function of $(\mu,F)$?" test (no, at all degrees).
- `phi_omega_zero.py` — composable pairings vanish ($\phi^*\omega\equiv0$), so a symplectic-pairing formula for $a$ is circular.
- `q_determinacy.py` — no *local* $q$-key determines $a$ (nearly-injective $q$, still splits) — but it was missing the global $q(T)$ (see `closed_form.py`).
- `closed_form.py` — the closed form (total + per-tetra cochain), exact all-$n$ (24,600 + 123,000 verified). *Total = Paper XI Prop (Quadratic form identity), rediscovered; new = the cochain refinement + item-23 framing.*
- `basis_invariance.py` — the closed form is $\mathrm{Sp}$-invariant though $q$ is not (summands change under basis change, net XOR $=N_{\mathrm{anti}}$, 900/900) — "coordinate, not intrinsic" made concrete.
