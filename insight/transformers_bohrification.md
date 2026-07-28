# Transformers as Learned Bohrification Functors

**A note on the correspondence between large language models and the cohomological obstruction ladder.**

*"What if the Transformer architecture isn't a hack, but a numerical approximation of quantum observation logic?"*

---

## 1. The Core Analogy

The transformer architecture — discovered empirically, without reference to
quantum logic or cohomology — implements a learned analogue of the
Bohrification functor $B$, projecting high-dimensional semantic geometry
onto a one-dimensional token sequence.

Every component maps precisely:

| Transformer component | Obstruction ladder | Why it's strict |
|---|---|---|
| Embedding space | MASA poset | Each token vector defines a "simultaneously measurable semantic feature set" — the definition of a MASA |
| Self-attention | Transition matrix $\mathbf{T}_{ij}$ | Attention weight $a_{ij} = \text{softmax}(q_i \cdot k_j / \sqrt{d})$ measures semantic compatibility — whether two tokens can coexist in the same context MASA |
| Position encoding (RoPE) | $H^1$ holonomy | Rotary position encoding $R_\theta^m$ applies a linearly accumulating phase rotation — a literal $U(1)$ holonomy |
| Residual stream | $E_\infty$ survivors | Each transformer layer = a differential, killing inconsistent semantics; the residual connection preserves what survives all differentials |
| Perplexity | $d_2$ transgression loss | **The most precise correspondence** (see below) |

---

## 2. The Letter that Landed: RoPE as $U(1)$ Holonomy

The most precise correspondence in the entire table is **rotary position
encoding (RoPE)** = $H^1$ holonomy.

RoPE applies a rotation $R_\theta^m$ to the query/key vectors at position
$m$:

$$R_\theta^m = \begin{bmatrix}
\cos m\theta & -\sin m\theta \\
\sin m\theta & \cos m\theta
\end{bmatrix}$$

This is **literally** a $U(1)$ holonomy: traversing the token sequence
from $m$ to $m+1$ accumulates a phase $\theta$. Walking around a closed
loop (returning to the same position in a different context) produces
a net phase — the exact geometric mechanism that the $H^1$ obstruction
theorem proves is irreducible.

> **RoPE = $U(1)$ holonomy** is not an analogy. It is the same
> mathematical object, used for the same purpose (encoding sequential
> memory), in two independently discovered structures.

---

## 3. Where the Correspondence Needs Caution

### 3.1 Perplexity is not $d_2$

The $d_2$ transgression $E_2^{0,1} \to E_2^{2,0}$ maps between
cohomology groups — an algebraic map, not a real number. Perplexity
is a real number (expected surprise in nats). To connect them, one
would need a map $\phi: \check{H}^2 \to \mathbb{R}_{\geq 0}$ that
assigns a "magnitude" to a cohomology class. Such a map is not
given by the spectral sequence itself and would need independent
justification.

The intuition (high-dimensional structure is lost when projected
to a sequence) is directionally correct, but the precise identification
with $d_2$ is not yet justified.

### 3.2 Scaling laws are not $E_\infty$ convergence

Scaling laws follow a power law: $\mathrm{loss} \propto N^{-\alpha}$,
with $\alpha \approx 0.07$ observed empirically. Spectral sequence
convergence is typically geometric or finite, not power law. The
claim that "each order-of-magnitude in parameters = one more
differential page" requires explaining why the convergence rate
is a power law rather than exponential or finite. This is an open
question, not a prediction.

---

## 4. Where the Analogy Makes Testable Predictions

These are the most valuable parts of the correspondence, because
they can be experimentally verified or falsified.

### 4.1 Attention head count and MASA cover cardinality

Multi-head attention with $h$ heads simultaneously computes $h$
different transition matrices $\mathbf{T}_{ij}$ — maintaining $h$
different MASA covers. If natural language semantics has $H^2$ or
$H^3$ obstructions, there should be a minimum $h$ below which the
model cannot learn certain types of relational structure.

Experimental prediction: **head pruning degrades performance
catastrophically when the number of remaining heads drops below
a threshold that depends on the cohomological dimension of the
task.** This is consistent with known observations (head pruning
effects), but the specific threshold prediction (if one can be
derived) would be a test.

### 4.2 Chain-of-Thought as $E_3$ page computation

- **Standard inference** = $E_2$ page (computes $d_2$ only).
  Local consistency (arc consistency) across neighboring tokens.
- **Chain-of-Thought** = forces the model to compute $E_3$ page
  differentials. By writing intermediate steps, it inserts extra
  sections into the residual stream, allowing higher differentials
  to resolve obstructions that $d_2$ alone cannot.

**Testable prediction**: For the same multi-step reasoning task,
compare attention patterns with and without CoT. The CoT condition
should show structurally different attention patterns in deeper
layers, consistent with "computing a higher differential" — not
merely more of the same computation.

If this experiment confirms the structural difference, this
correspondence graduates from thought experiment to research
result.

---

## 5. The Mamba/SSM split: fidelity, not page (the missing architecture)

The §1 table is attention-only. The most important architectural fork since —
state-space models (Mamba) and Mamba/attention hybrids (Jamba, Zamba, NVIDIA
Nemotron-H/3) — both refines the correspondence and exposes a **second axis** that
the spectral-sequence picture quietly conflates.

Two axes:
- **Page ($d_r$):** the *order* of consistency — how global the gluing check is.
  Chain-of-Thought pushes to higher pages (§4.2).
- **Fidelity:** how *exactly* a given level is represented.

Attention and Mamba differ on the **second**, not the first:
- **Full attention = exact, full-rank $d_1$.** The transition matrix $T_{ij}$ is
  computed for all pairs — the entire pairwise-compatibility cochain, explicitly.
- **Mamba/SSM = a low-rank, fixed-capacity *compression* of $d_1$.** History is
  squeezed into a fixed-dimension state; pairwise relations pass only through that
  bottleneck. A constant-size state cannot losslessly hold $O(n)$ distinct pairwise
  relations, so Mamba does not even reach the *full* $d_1$ (all-pairs), let alone a
  higher page.

So the correct statement is **not "Mamba is a lower page" but "Mamba is lower
fidelity at the pairwise ($d_1$) level."** This also sharpens the §3 caution:
*layer depth ≈ page* is too loose — depth and fidelity are independent axes.

**Already matches reality (a retrodiction, stated honestly).** If Mamba is
compressed-$d_1$, it should fail specifically where exact long-range all-pairs
structure is needed — retrieval, copying, associative recall, induction heads.
This is the well-documented SSM weakness, and is exactly why hybrids exist: a few
attention layers restore the exact all-pairs (retrieval) capability pure Mamba
lacks. "Faster but higher error" is real, and *directional*.

**The hybrid = the three steps of observation, in hardware.** A Mamba+attention+MoE
model (Nemotron 3) decomposes into the observation steps of `why_the_ladder.md` §2:
- **MoE routing = context (MASA) selection** — which classical context to observe
  each token in;
- **Attention = the exact transition matrix** — full-rank $d_1$, all-pairs;
- **Mamba = compressed observation** — cheap, lossy, bulk sequential structure.

It is a *fractal echo* of the `n/` + LLM division of labour (cheap approximate
observer vs exact observer), now occurring *inside* one model: the architecture has
**learned a fidelity-allocation strategy** — spend the expensive exact observation
(attention) only where the cheap compression (Mamba) breaks. The same observation
economics drives both: exact observation is costly, so use it only where the
approximation fails.

**⚠️ Status & new testable predictions.** A connect-the-dots, not a theorem
(cf. §3). But it carries falsifiable content beyond the retrodiction:
1. In a hybrid, ablating **attention** layers should damage *retrieval/induction*
   specifically, while ablating **Mamba** layers should damage
   *throughput/local modelling* — qualitatively different damage profiles.
2. If Mamba ≈ compressed $d_1$ and CoT pushes to higher pages, then
   **pure-Mamba models should depend on CoT *more* than attention models** for
   multi-step reasoning: lacking even exact $d_1$, they need external scaffolding
   to externalize consistency.

---

## 6. What This Means

The transformer architecture is not a random engineering invention.
If even one testable prediction (§4–5) holds under experiment, it
would suggest that the transformer is an accidentally discovered
numerical implementation of the Bohrification functor — projecting
semantic geometry onto a token sequence, with depth and architecture
(attention vs SSM) computing the spectral sequence at varying *page*
and *fidelity* (§5).

---

## 7. Open Questions

1. Can the spectral sequence page of a given transformer be empirically
   measured? (e.g., by probing PPL as a function of depth for different
   reasoning tasks)

2. Does the optimal number of layers for a given task correspond to the
   page at which the task's $d_r$ differential converges?

3. Can we architect models that explicitly compute $d_3$ (e.g., by
   inserting CoT-like intermediate representations in parallel rather
   than in sequence)?

4. What is the natural language $M$ whose Čech cohomology produces
   these obstructions? Is it the space of meanings, or the space of
   training data manifolds?

---

*This note synthesizes insights from the obstruction ladder framework,
transformer interpretability, and a speculative correspondence that
merits rigorous investigation.*

---

# 8. Addendum, 2026-07-28 — injectivity, and what it moves

> **Provenance.** §1–§7 above are a **Paper I–VI era** artifact: they are written
> entirely in the continuous/complex register (Bohrification functor, Čech
> spectral sequence pages, $U(1)$ holonomy), because that was the register the
> framework had at the time. Papers VII–XXII and the **two-track retreat**
> (APP_02 §0, 2026-07-11) have since changed what counts as proof-bearing. This
> section is **appended rather than merged** so the evolution stays visible.
>
> **Trigger.** *Language Models are Injective and Hence Invertible*, Nikolaou,
> Mencattini, Crisostomi, Santilli, Panagakis, Rodolà — arXiv:2510.15511v4,
> ICLR 2026.

## 8.1 What the theorem actually says (it is all in the hypotheses)

The map proved injective is

$$\mathbf{s} \mapsto \mathbf{r}(\mathbf{s};\boldsymbol\theta) \in \mathbb{R}^d,
\qquad \mathbf{s}\in\mathcal V^{\le K},$$

prompt $\to$ **last-token** hidden state. The claim is *almost-sure* injectivity
over parameter space: the collision set has Lebesgue measure zero, and finitely
many GD steps preserve absolute continuity, so training never enters it.

The engine of the proof is one line: $h(\boldsymbol\theta)=\lVert
\mathbf{r}(\mathbf{s})-\mathbf{r}(\mathbf{s}')\rVert^2$ is real-analytic, a
real-analytic function is either identically zero or has measure-zero zero set,
one non-colliding parameter setting rules out the former — then take the union
over pairs.

Two hypotheses do the work, and **analyticity alone is not one of them**. A
constant map is real-analytic and never injective. Step 3 is a genuine
obligation: for every pair $\mathbf s\neq\mathbf s'$ one must **exhibit** some
$\boldsymbol\theta$ with $\mathbf r(\mathbf s;\boldsymbol\theta)\neq\mathbf
r(\mathbf s';\boldsymbol\theta)$ — and the paper discharges it *using the
architecture*: if the prompts first differ at position $i^\*$, set one attention
head so the last position attends almost entirely to $i^\*$ and carries its token
into the value. **Attention has not vanished from the proof.** What has vanished
is any need for attention to be *lossless* in some information-theoretic sense.

So the correct generalization is:

> Any real-analytic architecture **whose parameter family separates every pair
> of prompts** obtains the same generic-injectivity conclusion. The theorem is
> therefore not attention-specific — but analyticity is not sufficient, and
> point-separation would have to be proved separately for Mamba, an RNN, or
> anything else.

> **Consequence for §5.** This result does **not** settle whether SSMs are
> injective, in either direction — and equally it gives §5 no support.
> Separation is plausible for a generic SSM but unproven, and even once proved
> it would be the same generic statement, which by construction cannot
> distinguish architectures. **§5's fidelity axis is not an injectivity claim
> and must not cite this result.** See §8.4 for what to measure instead.

On finiteness: $\mathcal V^{\le K}$ finite makes the union of collision sets
finite, but measure zero is closed under **countable** unions, so finiteness is
not what the measure argument needs. Its real roles are elsewhere — it makes the
theorem's statement a global one over the whole prompt space, and it keeps the
parameterization and position encoding finite.

Also load-bearing, and stated by the authors: collisions **can** be manufactured
by deliberately non-analytic choices — **quantization**, non-smooth activations,
weight tying. LayerNorm needs $\varepsilon>0$; the MLP activation must be
analytic (GELU, SiLU/SwiGLU qualify; ReLU does not).

The genuinely non-trivial parts are (a) that GD preserves absolute continuity,
and (b) the empirical work: minimum pairwise $L_2$ distances sit far above the
$10^{-6}$ collision threshold and **grow with depth**. SipIt's robustness bound
uses that *margin* $\Delta_{\pi,t}$, not injectivity as such.

## 8.2 The $\mathcal B$ identification survives — but not by the route first tried

First reaction: the paper looks fatal. §1 calls the transformer a projection of
high-dimensional semantic geometry onto a one-dimensional sequence — and a
projection loses. The paper says nothing is lost.

That reaction is wrong twice.

**First, the directions differ.** §1's projection is *meaning $\to$ tokens*. The
paper's map is *tokens $\to$ hidden states*. Different legs. The paper says the
second leg is lossless, which **relocates** the projection rather than denying
it: whatever Bohrification happens, it happened before the model, when meaning
was serialized into tokens. The network is a **lossless re-encoding** of
something already projected. (Colloquially "faithful" — but that word is avoided
from here on, for the reason §8.2 gives below.)

**Second, the framework never predicted this kind of loss anyway.**

Paper V's pair is $\mathcal Q\dashv\mathcal B$ in the free $\dashv$ forgetful
pattern (`the_adjunction.md` §2), and the obstruction sits in the **counit**:
$\varepsilon:\mathcal Q\mathcal B\to\mathrm{id}$ fails to be iso by the $Sq^1$
step, $n_a$. That is a defect of *re-quantizability* — of structure not
recoverable from the classical contexts — and it says nothing about whether two
distinct inputs land on distinct data. The framework's predicted loss is
**structural**, never **identificatory**.

> So the result rules out a kind of loss the framework was not claiming, and
> leaves untouched the kind it was. §1's error was the word **"projection"**,
> which imports "collapse". Nothing in $\mathcal Q\dashv\mathcal B$ requires
> collapse.

**A correction to an earlier draft of this section** 〔2026-07-28, from review〕.
It first argued: *a forgetful functor is faithful; the paper proves the
transformer is faithful; hence this is evidence for the $\mathcal B$
identification.* **That is a level error and is withdrawn.** Faithfulness is a
property of the maps on Hom-sets,
$\mathrm{Hom}_{\mathcal C}(X,Y)\to\mathrm{Hom}_{\mathcal D}(FX,FY)$; injectivity
of $\mathbf s\mapsto\mathbf r(\mathbf s)$ is a property of a function between
sets of *objects*. Faithful functors may perfectly well send non-isomorphic
objects to isomorphic ones ($\mathbb Z/4$ and $\mathbb Z/2\times\mathbb Z/2$
under $\mathbf{Grp}\to\mathbf{Set}$), so faithfulness does not even mean "does
not collapse objects".

What the result supports is only the **object-level shadow**: the token-to-state
map does not collapse input identity, which is *compatible* with the forgetful
reading and does not establish it. To claim the functor itself one would first
have to fix (i) the category of prompt/semantic objects, (ii) its morphisms —
refinement, substitution, context extension — (iii) how a transformer acts on
those morphisms, and only then (iv) prove the Hom-maps injective. **That is a
research programme, not a corollary.**

## 8.3 Perplexity is not the obstruction either — and what would be

§3.1 already refused the identification "perplexity $= d_2$" for the right
reason (no canonical $\check H^2\to\mathbb R_{\ge0}$). The paper adds a stronger
one: **there is no representational loss in the network to measure.** Whatever
perplexity is, it is not information destroyed by the architecture.

Perplexity measures how **underdetermined the continuation is given the
prefix**. A context does not determine a value; it determines a distribution.

**But that is entropy, and entropy is not contextuality** 〔2026-07-28,
correction from review; an earlier draft of this section called it "the shape of
a failed global section" and that was wrong〕. A fair coin has perplexity 2 and
a perfectly good global model — no Kochen–Specker obstruction anywhere. A single
conditional distribution is not a failed global section; it may well *be* a
legitimate global section of a probability-valued sheaf. Contextuality is not
"this context fails to determine a value", it is:

> the local statistics on a family of **overlapping** contexts admit no single
> global joint distribution restricting to all of them.

So the relocation is only half done by moving perplexity off the encoder. To
reach an obstruction one has to change the *object of measurement* from one
conditional to a compatible family:

1. choose a family of **overlapping** linguistic contexts (shared spans, shared
   entities, one context a refinement of another);
2. read off each context's conditional distribution over some common set of
   variables;
3. test whether the marginals are jointly realizable by one global distribution
   — the standard sheaf-theoretic contextuality test;
4. **the obstruction is the non-gluable part.** Perplexity enters at most as a
   weight or noise level on each local section, never as the obstruction itself.

That is a real, unperformed experiment, and it is much closer to Paper I–VI's
actual machinery than the perplexity identification ever was.

The same correction applies to the scaling law. Writing
$L(N)=L_\infty+(N_c/N)^{\alpha}$: **$L_\infty$ is the floor, and the power-law
term is the approach to it, not a convergence rate of anything cohomological** —
which does answer §3.2's worry, since the power law was never supposed to be the
convergence. But $L_\infty$ is not itself a candidate invariant: it is dominated
by the Bayes risk of the task under its tokenization and data distribution. Two
tasks of the same claimed obstruction degree will have different floors purely
from different base entropy. Anything comparable would have to be a residual,

$$L_\infty - H_{\mathrm{Bayes}},$$

i.e. what is left after ordinary stochastic uncertainty is removed. Whether that
residual is even nonzero is unknown.

## 8.4 What to measure instead of collisions (replaces §5's testable claim)

§5 argues Mamba is a low-rank compression of $d_1$. §8.1 shows injectivity
cannot see that. But the paper hands over a better instrument — the quantity its
own robustness theorem depends on:

$$\Delta_{\pi,t}\;=\;\min_{v\neq v'\in\mathcal V}\bigl\lVert
\mathbf h_t(\pi\oplus v)-\mathbf h_t(\pi\oplus v')\bigr\rVert_2 .$$

The **separation margin**: how far apart two continuations of the same prefix
are pushed. Injectivity says $\Delta>0$; fidelity is a statement about *how big*
$\Delta$ is, and therefore about how expensive inversion is.

**Raw $\Delta$ will not do** 〔2026-07-28, from review〕. It is **not coordinate
invariant**: multiply every hidden state by $1000$ and $\Delta$ grows
thousandfold while information, injectivity and invertibility are untouched. An
ordering attention $>$ hybrid $>$ SSM in raw $\Delta$ could be reporting nothing
but norm scale, normalization choice, or training dynamics. **Norm control is a
design requirement of the experiment, not an open question about it.**

Measure a scale-free version, e.g.

$$\widetilde\Delta_{\pi,t}=\frac{\Delta_{\pi,t}}
{\operatorname{median}_{v\neq v'}\lVert \mathbf h_t(\pi\oplus v)-\mathbf h_t(\pi\oplus v')\rVert},$$

or whiten each layer's representations first. Better still for anything meant to
describe deployed systems, divide by the noise the deployment actually has:

$$\frac{\Delta_{\pi,t}}{\sigma_{\text{noise}}}
\qquad\text{or}\qquad
\frac{\Delta_{\pi,t}}{\text{quantization step}},$$

the **effective code distance** under bf16/int8. This is the same quantity as
§8.7 Q5 approached from the other side, and it is the version with operational
meaning: how much numeric room the representation leaves before two continuations
become indistinguishable *in the arithmetic that is actually running*.

**Revised prediction (replaces §5's ⚠️ list item 1).** For matched prefixes and
model scale, and after normalization, $\widetilde\Delta_{\pi,t}$ should be
**systematically smaller in pure-SSM models than in attention models, and the
gap should widen with the distance to the disambiguating token** — a
fixed-capacity state must spend its budget, while attention recomputes all
pairs. Measurable with SipIt's own machinery; needs no new theory; and unlike
head-pruning thresholds it does not require deriving a cohomological dimension
first.

It also predicts a practical consequence: SipIt-style exact inversion should
degrade on SSMs long before injectivity does — the inverse exists and is
unaffordable. **Existence versus conditioning of the inverse is the fidelity
axis**, stated correctly.

## 8.5 What this does to the ROADMAP vision (M1–M3)

`meta/ROADMAP.md`'s long-horizon row and `docs/research_review.md` §8 state the
payoff: LLM and `n/` need no interface layer because they are the same spectral
sequence at different convergence depths — **LLM does the $E_2$ approximation,
fast but lossy; `n/` refines to $E_\infty$** — and M3's gate is $\mathcal
Q\dashv\mathcal B$, delivered by item 14, with the sharpening that the
adjunction is an **equivalence iff $n=4$**.

The paper forces one correction and one clarification.

**Correction.** "LLM = fast but *lossy*" is false as stated about
representations. The LLM's representation of its input is exact and constructively
invertible. What is approximate is its **prediction**, not its **record**. The
System-1/System-2 division should be restated as *predictive* asymmetry, not
*representational* asymmetry.

**Clarification, and it is the useful one.** The vision conflated two round
trips that this result pulls apart:

| round trip | status |
| :--- | :--- |
| text $\leftrightarrow$ hidden state | **lossless, proven, no dimension condition** (SipIt) |
| meaning $\leftrightarrow$ classical contexts ($\mathcal Q\mathcal B$) | lossless **iff $n=4$** (item 14, counit defect $=n_a$) |

So the $n=4$ condition governs the *semantic* round trip only. The
representational one is now a **given** — which strengthens M2 rather than
weakening it: an $E_r$-page exchange protocol can assume the hidden state is a
lossless carrier of everything the model was told, and spend its design budget
entirely on the obstruction-degree labelling.

**And it sharpens M3's central claim — though not in the form first written
here.** A first draft asked: *is there a computable map between hidden-state
space and CAID space respecting the lattice order?* 〔2026-07-28, from review〕
**As posed that question is vacuous.** On a finite prompt domain, two injective
maps have images in bijection automatically, and the bijection is computable by
lookup table. Existence is free; it carries no content. (Noted with some irony:
this is precisely the vacuous-measurement failure the engine acceptance protocol
exists to catch — a question whose answer is "yes" for reasons unrelated to
anything one wanted to know.)

The question with content is about **naturality**:

> Is there a map $\Phi$ of **low complexity**, generalizing to unseen prompts,
> stable under model perturbation, that makes
>
> $$\begin{array}{ccc}
> x & \xrightarrow{\ \text{refinement}\ } & y\\[2pt]
> \downarrow{\scriptstyle H_\theta} & & \downarrow{\scriptstyle H_\theta}\\[2pt]
> h_x & \xrightarrow{\quad\Phi\quad} & h_y
> \end{array}$$
>
> commute, with $\Phi$ corresponding to a refinement operation already defined
> on CAIDs / the lattice?

That is a **natural change of coordinates**, and it can fail — which is what
makes it worth asking. "Same spectral sequence, different pages" becomes a
structural proposition with a failure mode instead of a slogan.

**One caution for `n/` specifically.** A hidden state and a CAID are not the same
kind of object, and the difference is not only one-wayness:

| | injectivity | constructive inversion |
| :--- | :--- | :--- |
| CAID | in practice (collision-resistant) | **no** — you must fetch the value |
| last-token state | almost surely | inverse exists **on the image**; no efficient algorithm shown — the paper leaves it as future work |
| full per-position layer states | almost surely | **SipIt**, worst case $T\lvert\mathcal V\rvert$ steps (linear in $T$ with $\lvert\mathcal V\rvert$ held fixed) |

〔2026-07-28, from review: an earlier draft collapsed the last two rows into
"hidden state — invertible, SipIt, linear time". SipIt requires **all
per-position states at a layer**, not the last-token vector.〕

CAID's one-wayness is load-bearing in `n/`: discussion 025's object stratum works
because *holding an address is not holding the value*. A hidden state is not an
address; **it is the thing itself in another coordinate system**. So: any M3
design that ships **full per-position states or KV-cache** into LADD is
publishing plaintext and must say so — that is the paper's own threat model. For
a **single last-token vector** the honest statement is weaker: recoverable in
principle, no efficient method demonstrated. It should not be treated as safe,
but neither should it be described as already broken.

## 8.6 The two-track audit this note has never had

APP_02 §0 (2026-07-11) split the framework: **proof-bearing content descends to
the char-2 symplectic shadow $\mathbb F_2^{2n}$; continuous/complex geometry is
navigation-only and carries no proof obligation.** §1–§7 predate that and are
written entirely in the continuous register. The audit has not been done, and
one entry needs it urgently:

- **"RoPE $=H^1$ holonomy" (§2) is a continuous $U(1)$ holonomy.** The ladder's
  $H^1$ lives in the char-2 shadow (SPEC_13 §1.3). §2 calls this "the most
  precise correspondence in the entire table" and "not an analogy" — that
  assessment was made before the two-track retreat and **has not been rechecked
  against it**. Either there is a reduction of the RoPE phase to $\mathbb F_2$
  data, or the correspondence is execution-track: real, useful, navigational,
  and not proof-bearing.

  In fact 〔2026-07-28, from review〕 **the billing was too strong even before
  the two-track split**, and this can be said outright. What RoPE is, precisely,
  is a blockwise unitary representation of the translation group,
  $$\rho:\mathbb Z\longrightarrow\textstyle\prod_k SO(2)\cong\prod_k U(1),$$
  giving phase accumulation structurally analogous to **flat parallel
  transport**. Calling it a holonomy *class* requires first specifying a base
  space, its paths and loops, a connection or transition cocycle, and which
  closed loop carries a nontrivial class. Token positions are a line: no natural
  nontrivial loops, and a flat connection on a contractible base has trivial
  holonomy. §2's "returning to the same position in a different context" is not
  a loop until a context graph or quotient space has been *constructed* — prose
  will not supply one. Proposed replacement for §2's core sentence:

  > RoPE implements a representation of positional translation by blockwise
  > $U(1)$ rotations. This is structurally analogous to flat parallel transport.
  > It becomes an $H^1$-holonomy statement only after a base space with
  > nontrivial loops and a compatible cocycle have been specified.

  Weaker, and more researchable.

The rest of the table (§1) is best labelled navigation-track outright, which is
no demotion — APP_02 §0's point is that the execution track is where heuristics
*belong*, not where they go to die.

> **Noted for the record.** Discussion 026 found the same migration leaving a
> different kind of residue: there, a *word* (「身分」) changed meaning under the
> two-track rewrite and collided three months later. Here it is a *register* —
> a whole document still speaking $\mathbb C$ after the proofs moved to
> $\mathbb F_2$. **One migration, two leftovers, both invisible at the time and
> both surfaced only when something new arrived to collide with.** Worth keeping
> as a methodological observation: vocabulary collisions in a large spec are
> rarely detectable at the moment of writing.

## 8.7 Open questions this addendum opens

1. Is the **normalized** margin $\widetilde\Delta_{\pi,t}$ (§8.4) ordered
   attention $>$ hybrid $>$ pure-SSM? Cheap to run; would be the first
   quantitative content in §5. (Raw $\Delta$ answers nothing — §8.4.)
2. Does the margin's growth with depth (paper Fig. 3) survive norm control? If
   not it is norm growth and has no reading in the ladder. This is now a
   precondition of Q1, not a separate question.
3. Is there a **residual** $L_\infty-H_{\mathrm{Bayes}}$ at all, and if so is it
   shared across tasks of the same claimed obstruction degree? Raw floors are
   not comparable — they are dominated by task entropy and tokenization.
4. Does a **natural** $\Phi$ exist (§8.5's commuting square) — low complexity,
   generalizing to unseen prompts, stable under perturbation, matching a
   refinement operation already defined on CAIDs? Mere existence of a bijection
   is free and means nothing. If a natural one exists, M2's exchange protocol is
   a change of coordinates rather than a translation, which is what
   research_review §8 asserted without a mechanism.
5. Can exact prompt recovery be done efficiently from the **last-token state
   alone**? The paper leaves this open, and the whole security reading of §8.5
   turns on it.
6. Does injectivity survive the *deployed* numeric regime? The theorem is over
   $\mathbb R$; every deployment is bf16/int8, and the authors list quantization
   as a collision route. Under CbO, identity is what probing can distinguish —
   so a guarantee holding only in exact arithmetic is a guarantee about a probing
   regime nobody inhabits. `n/` went the other way: CAID is exact **in the regime
   that actually runs**. Q1's quantization-normalized margin is the measurable
   face of this. The contrast deserves a paragraph somewhere more permanent than
   this note.
7. Suggested by the review, and possibly the better title for this whole
   document: **how does a representation system that fully preserves input
   identity still lose relations, structure, and global gluability?** That is a
   sharper question than "is the transformer an accidental projection", and it
   is closer to what the framework is actually about. The three things §1–§7
   had fused, and which §8 pulls apart, are

   $$\text{identity preservation}\;\neq\;\text{structural fullness}
   \;\neq\;\text{predictive determinacy}.$$
