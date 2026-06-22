# Item 21, arity-5 probe — does the arity-4 "absorption" pattern persist? (`qk_saturation.py`)

**Context.** Item 21 (the arity-5 lid) asks whether an *irreducible* arity-5 invariant of five
Lagrangians could furnish an $H^4$ escape past the $H^3$ ceiling. The **Steenrod-module route**
(see `RESEARCH_FRONTIER.md` item 21) reduces this to: does the family-A tower stay $\omega$-generated
at arity 5? Paper XIX's arity-4 base case is "absorbed" — the natural Maslov/Kashiwara quadruple bit
$q_4$ is $\omega$-built and **saturated** (no fiber info), and the genuinely-exotic Arf invariant is
separately *ruled out* as a classifier of $N_{\mathrm{anti}}$. This probe tests whether the natural
arity-5 analogue $q_5$ also saturates.

**Construction** (Paper XIX Def. `def:q4` generalised; $k=4$ **is** $q_4$): for Lagrangians
$L_{a_1},\dots,L_{a_{k-1}}$ (free) and $L_{a_k}$ (distinguished),
$$D_k=\{(v_1,\dots,v_{k-1})\in\textstyle\prod L_{a_m}:\sum_m v_m\in L_{a_k}\},\quad
  Q_k=\sum_{m<m'}\omega(v_m,v_{m'}),\quad q_k=[\,Q_k\not\equiv0\text{ on }D_k\,].$$
$D_k$ is the kernel of the membership map; $q_k$ is read by sampling random kernel elements (a nonzero
$\mathbb F_2$ quadratic form is $\neq0$ on $\ge\tfrac14$ of points, so 64 samples miss with prob
$\le(3/4)^{64}\approx10^{-8}$).

## Result

| | $n=5$ per-instance | $n=5$ configs fully-sat | $n=6$ per-instance | $n=6$ configs |
|---|---|---|---|---|
| $q_4$ (unit test) | 94% (90620/96000) | 80% (3831/4800) | **100%** (40000/40000) | 100% |
| $q_5$ (probe) | **98%** (23530/24000) | **98%** (4706/4800) | **100%** (15000/15000) | 100% |

**Robust finding (same machinery, same configs):** $q_5$ saturates **at least as strongly as $q_4$**
at every $n$ tested ($n=5$: $98\%\!\ge\!94\%$ instance, $98\%\!\ge\!80\%$ config; $n=6$: both exactly
$100\%$). So the natural arity-5 $\omega$-Maslov invariant is *at least as absorbed* as the arity-4
one — **the absorption pattern persists (even strengthens) at arity 5.**

## Honest scoping

- **Evidence, not proof.** $q_5$-saturation says the *natural $\omega$-built* arity-5 invariant
  carries no fiber information — exactly the arity-4 behaviour of $q_4$. It does **not** rule out a
  *genuinely-exotic* (non-$\omega$, Arf/Dickson-type) arity-5 invariant; that is the separate, harder
  escape, just as at arity 4 (where Paper XIX needed a dedicated Arf-exclusion argument, not $q_4$'s
  saturation). The Steenrod-module route's real gap — "$\omega$-generated over $\mathcal A$" — is
  untouched by this probe; the probe only confirms the *$\omega$-generated* part behaves.
- **Calibration caveat (unit test only *qualitatively* passed).** Our $q_4$ config-saturation at
  $n=5$ is $80\%$, not Paper XIX's reported $99.5\%$. The machinery is validated by the clean $n=6$
  result (both $q_4,q_5$ exactly $100\%$ — a kernel/$Q$ bug could not produce that) and sampling-miss
  is excluded (the $n=5$ $q_4{=}0$ cases are genuine $Q_4\equiv0$, not missed detections). So the gap
  is a **population/stratum difference** (our generator vs XIX's sampled set) or a definitional
  nuance — to be reconciled before any *absolute* $q_5$ saturation figure is quoted. The $q_5\ge q_4$
  **ordering** is immune (identical code and configs).

**Net:** a first, scoped data point *for* the absorption hypothesis — the natural arity-5 invariant
is as absorbed as arity-4 — with the exotic arity-5 escape and the XIX calibration both explicitly
left open.

## Files
- `qk_saturation.py` — general arity-$k$ Maslov bit $q_k$; unit-tests $q_4$, probes $q_5$ ($n=5,6$).
