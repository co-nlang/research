# Item 21 — prior art / literature (the subfield exists; item 21 is its char-2 gap)

*Literature check (2026-06-22), prompted by "has anyone studied invariants of `Sp(2n,F₂)` on
Lagrangian tuples?" Answer: yes — substantially, over `ℝ`/`ℂ` and over algebraically closed fields.
The framework's `F₂`/cohomological version is the genuine gap, and now has a clear template. This note
records what is known, so item 21's M4/M5 are framed against the state of the art, not re-derived.*

## The three relevant bodies of work

1. **Magyar–Weyman–Zelevinsky, "Symplectic multiple flag varieties of finite type"**
   (arXiv:`math/9807061`, J. Algebra 230 (2000)). Classifies when a product of `Sp_{2n}`-flag
   varieties has *finitely many* diagonal orbits. **Theorem 1.1: a tuple of non-trivial symmetric
   compositions is of symplectic finite type ⟹ `k≤3` factors.** So **≤3 Lagrangians → finitely many
   `Sp`-orbits; `≥4` Lagrangians → infinite type (a continuous modulus appears).** Key reduction:
   two multiple symplectic flags are in the same `Sp_{2n}`-orbit *iff* the same `GL_{2n}`-orbit — so
   the problem becomes type-A / quiver representations. (Algebraically closed field.)

2. **Conley–Ovsienko, "Lagrangian configurations and symplectic cross-ratios"**
   (arXiv:`1812.04271`, 2018–20). *The* closest work to item 21. Studies `Sp(2n,K)`-invariants of
   Lagrangian configurations (cyclic `N`-tuples of lines, every `n` consecutive spanning a
   Lagrangian). Establishes: **continuous invariants = symplectic cross-ratios**
   `[x₁,x₂;y₁,y₂] = ω(x₁,y₁)ω(x₂,y₂)/ω(x₁,y₂)ω(x₂,y₁)`, plus **discrete sign invariants**; a
   **generation theorem** (cross-ratios are complete continuous invariants, with explicit Pfaffian/
   continuant relations); moduli space `L_{n,N}(K)` of dimension **`n(N−2n−1)`**, so the first
   continuous (modulus) case is **`N = 2n+2`**. **Only `K=ℝ` or `ℂ`** — finite fields not treated.

3. **Carlisle–Kropholler / Quillen** — the *ambient* modular invariant ring of `Sp(2n,F₂)` on its
   natural module: for `p=2`, `T^{Sp_{2n}} = F₂[κ_{n,0},…,κ_{n,n-1}]` (Dickson-type symplectic
   invariants `ξ_i = Σ X_{2k-1}X_{2k}^{q^i} − X_{2k}X_{2k-1}^{q^i}`). This is invariants on *vectors*,
   not Lagrangian tuples — the backdrop for M5's ambient ring, not the configuration invariants.

## The crux: the symplectic cross-ratio DEGENERATES over `F₂` (this is item 21's whole point)

The continuous invariant is a **ratio of `ω`-values**. Over `F₂`, `ω(·,·)∈{0,1}`, so every
cross-ratio is `1` (when defined) or undefined — **the continuous modulus collapses entirely over
`F₂`.** Therefore:

- Over `ℝ,ℂ` (Conley–Ovsienko): the modulus is *continuous* (cross-ratios, dim `n(N−2n−1)`).
- Over `F₂` (the framework): the cross-ratios are trivial, and the modulus re-emerges as **discrete /
  cohomological** data — exactly Paper XIX's modulus, `n_a = Sq¹ω` the `H³` class, and the
  *exotic arity-5* question (item 21).

So **the framework is the characteristic-2 shadow of Conley–Ovsienko**: the same `Sp`-on-Lagrangian-
configurations problem, in the one regime (`char 2`) where their continuous invariants vanish and the
content moves into the cohomological obstruction. That regime is genuinely *not* in C-O or MWZ.

## What this means for item 21 (M4/M5) — reframed, and difficulty revised

- **M5 (FFT for `Sp(2n,F₂)` on Lagrangian tuples) is the char-2 analog of C-O's generation theorem.**
  Strategy shifts from "invent invariant theory from scratch" (the disposition's framing) to
  **"characteristic-2-reduce Conley–Ovsienko"**: take their cross-ratio + sign generation, reduce mod
  2, and identify what survives (the cross-ratios degenerate; the discrete signs + the cohomological
  remnant are what is left). This is plausibly *more tractable* than feared — a reduction with a known
  `ℝ,ℂ` answer — though it may also expose genuinely new char-2 exotica (the `q₄`/Arf siblings, which
  have no `ℝ,ℂ` analog — O3 of the obstacles).
- **M4 (exotic arity-5 invariant) recast:** over `ℝ,ℂ` a "new arity-5 invariant" *is* a cross-ratio
  (continuous); over `F₂` that degenerates, so the M4 question = **what discrete invariant survives
  the char-2 collapse of the cross-ratio modulus**. The "exotic non-`ω` invariant" we were hunting is
  precisely the char-2 residue of the C-O continuous modulus.
- **MWZ gives the orbit-count backdrop:** `≥4` Lagrangians is infinite type over `\bar K`; over `F₂`
  the "infinite family" becomes a growing *finite* set of orbits whose unclassified part is the
  modulus. The `n`-dependence (Paper XIX: rigid at `n=4`, modulus at `n≥5`) is the `F₂`-points story
  layered on MWZ's `\bar K` infinite-type — to be reconciled (the `F₂` moduli space is a point at
  small `n`, acquires `F₂`-modulus at `n≥5`).

## Honest status

- The subfield **exists and is well-developed** over `ℝ,ℂ` (C-O) and `\bar K` (MWZ). The framework has
  been (re-)deriving pieces: cross-ratio ↔ continuous modulus, Maslov ↔ discrete sign, the finite-type
  boundary. *We should cite C-O and MWZ going forward, not present these as new.*
- The framework's **genuine novelty** is the `char-2`/finite-field/cohomological version (cross-ratio
  degenerate ⟹ `Sq¹ω`/`H³` obstruction) and the quantum-contextuality reading — neither in C-O/MWZ.
- **Next concrete step (supersedes the old M5 framing):** obtain C-O's explicit cross-ratio relations
  (the Pfaffian/continuant identities), reduce mod 2, and check what the framework's `n_a` / exotic
  question becomes. That is the grounded route to M5, and a real prior-art bridge for M4.

## Reduction ATTEMPTED — result tempers the "char-2-reduce C-O" optimism (`co_reduce.py`)

The concrete move ("reduce C-O's cross-ratio relations mod 2") was carried out. **Both naive mod-2
reductions fail to recover the framework's obstruction:**

1. **Cross-ratio relation → VACUOUS.** The cross-ratio is a *ratio of `ω`-values*; over `F₂` every
   defined one `= 1`, so the relation (e.g. hexagon `1/c₀+1/c₁+1/c₂=1`) becomes `1+1+1=1` (`3≡1 mod 2`)
   — a tautology. No `F₂` content. (By hand.)
2. **Pfaffian (the polynomial form C-O cite) → NON-vacuous but COARSE.** `Pf(ray-Gram) mod 2 =
   [rank G = 10]` = indicator of the *full-span nondegenerate stratum*. Computed (`co_reduce.py`):
   `0` always at n=4 (dimension-forced — 10 rays can't be nondegenerate in `2n=8` dims), `≈21%/17%`
   ones at n=5/6. It is a *stratum indicator*, **not** the `H³` obstruction, and a *different*
   invariant from `N_anti` (Pfaffian sums perfect *matchings*; `N_anti` sums *pairs*). (The n=5
   ray-Gram rank spread `{6:1662, 8:2951, 10:1290,…}` is population-dependent — consistent with the
   `calib_q4.py` finding — and need not match XIX's deduplicated-bucket `(8,6,2)` focus.)

**Honest revision (corrects the previous turn's framing).** "M5 = char-2-reduce C-O, plausibly more
tractable" was too optimistic. Concretely, C-O's *continuous* invariants degenerate to vacuous
(cross-ratio) or coarse-stratum (Pfaffian) data over `F₂`; the framework's `N_anti`/`n_a=Sq¹ω`/`H³`
obstruction is **orthogonal to them, not a reduction of them**. What *does* reduce is only the
bottom rung — C-O's discrete *sign* invariant char-2-reduces to the Maslov bit `μ` (the framework's
arity-3 datum). So the reduction recovers `μ`, **not** the `H³` class or the exotic arity-5 content.
*Consequence:* C-O gives the `ℝ,ℂ` template and the `μ`-level dictionary, but item 21's M4/M5 are
**not** shortcut by reduction — the original M4 route (intrinsic exotic at `K₆`) remains the genuine
path, and the char-2 obstruction is confirmed (concretely, not by assertion) to be the irreducibly
char-2 residue C-O do not see.

## Stratum sharpening — the pentagram is not IN C-O's configuration category (checked 2026-07-07)

*Second literature pass (idea C of the 2026-07 review queue), against the ar5iv full text of
arXiv:1812.04271. Three claims verified, one of our own framings corrected.*

**Verified.**
- **Genericity is constitutive, not a convenience.** C-O define "generic" as: ⟨X_i,X_j⟩
  non-isotropic whenever the cyclic distance satisfies |i−j|_N ≥ n; Lemma 2.2 requires
  `ω(x_i, x_{i+n}) ≠ 0` for all i. **Even the discrete sign invariants need nonzero ω's**
  (Lemma 2.4: "if ω_{j_{s-1},j_s} ≠ 0 for all s"). Degenerate configurations get one closure
  remark (§6.3) and no theory. Their entire apparatus lives on the open generic stratum.
- **The dimension formula and its range.** Proposition 2.7: `dim L_{n,N}(K) = n(N−2n−1)`,
  **valid for N > 2n** (where Sp(2n,K) acts freely on generic configurations). N = 2n is a
  single orbit; N = 2n+1 gives two classes over ℝ; first continuous modulus at N = 2n+2. ✓
- **Fields**: "𝕂 will denote either ℝ or ℂ" — explicit; no finite fields anywhere. ✓

**Correction of our earlier framing ("pairwise-transverse generic position").** C-O's cyclic
configurations are NOT pairwise transverse: **consecutive Lagrangians share an (n−1)-plane by
construction** (L_i = ⟨x_i,…,x_{i+n−1}⟩). Genericity constrains the FAR pairs. The correct
statement of the orthogonality is sharper and structural:

1. **Incidence type**: the Mermin pentagram is K₅-incidence — each ray lies in exactly **2** of
   the 5 Lagrangians, every pair shares exactly one ray (10 rays = 10 edges). C-O configurations
   are cyclic-incidence — each line lies in exactly **n consecutive** Lagrangians. Different
   incidence categories; no relabeling maps one to the other.
2. **Parameter range**: under the Lagrangian-count map the pentagram is (N, n) = (5, 4), i.e.
   **N = 5 < 2n = 8 — outside the range of every C-O moduli statement** (all need N > 2n).
   The formula value n(N−2n−1) = −16 < 0 is not "a negative-dimensional stratum"; it is the
   formula evaluated outside its hypothesis.
3. **Field**: F₂ excluded from the outset (and the cross-ratio degenerates there — the
   2026-06-22 crux above).

So the right citation sentence for XXIII is not "our modulus is the degenerate/char-2 shadow of
the C-O modulus" but: **"the framework's configurations live in an incidence category and a
parameter range (and over a field) that the cross-ratio theory constitutively excludes; its
rad(ω|_W) modulus is a discrete invariant on a stratum the generic theory never enters."**

**Why co_reduce.py had to come out "orthogonal, not a reduction" (the retrospective why).**
The reduction applied C-O's *formulas* (cross-ratio, Pfaffian) to pentagram ray-Grams; but the
*theory* behind those formulas (generation/completeness, Prop 2.7) is proven only on the cyclic
generic stratum, which the pentagram never inhabits. The mod-2 failure was overdetermined:
wrong field AND wrong stratum AND wrong incidence category. The one thing that does transfer —
the sign invariant reducing to the Maslov bit μ — is exactly the piece whose definition
(Lemma 2.4) survives on the pentagram's nonzero-ω pairs.

**The n=4 face (internal cross-check, M5_kerG_reduction).** On the framework's own stratum the
nondegenerate locus is 100% at n=4 (400/400, `rad(ω|_W)=0` throughout; strata spread appears
only at n≥5). The dimension where the self-description loop closes is exactly the dimension
where the framework's stratum is uniformly nondegenerate — one more face of n=4 rigidity,
**value-level verified**, independent of C-O.

## Adjacent / checked, low relevance (bank the negatives)

- **Vinroot, "Real representations of finite symplectic groups over fields of characteristic two"**
  (arXiv:1708.07176) — *complex character theory* of the abstract group `Sp(2n,2^k)` (all irreps real,
  Frobenius–Schur `+1`; unipotent character-degree generating function). **Not** about Lagrangian
  configurations / invariant theory / cohomology, so **low direct relevance to item 21.** One thematic
  echo only: FS `= +1` (every irrep orthogonal) is the rep-theoretic face of the same char-2
  "symplectic-becomes-quadratic" phenomenon that makes the cross-ratio degenerate and pushes content
  into the quadratic refinement (`q₀`/Arf/`Sq¹ω`) — a cousin, not a tool. *Checked 2026-06-22; do not
  re-chase for item 21.*

## References
- P. Magyar, J. Weyman, A. Zelevinsky, *Symplectic multiple flag varieties of finite type*,
  arXiv:math/9807061.
- C. Conley, V. Ovsienko, *Lagrangian configurations and symplectic cross-ratios*, arXiv:1812.04271.
- D. Carlisle, P. Kropholler, rings of invariants of symplectic groups (modular, 1990s); D. Quillen,
  mod-2 cohomology / invariants of `Sp_{2n}` (`T^{Sp_{2n}}=F₂[κ_{n,i}]`).
