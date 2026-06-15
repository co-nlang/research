# insight/ — A Correspondence Atlas for the Obstruction Ladder

*Speculative notes. Read each as conjecture, not result.*

These notes play "connect-the-dots": they ask whether some domain — physics,
distributed systems, neural networks, constraint solving — has the **same shape**
as the cohomological obstruction ladder (local data failing to glue into a global
section, measured by $H^1, H^2, H^3$). To an outside eye this looks reckless.

It is also, historically, how mathematics actually finds things. Borsuk–Ulam
became Kneser colouring (Lovász). Stone duality tied logic to topology. The
Langlands program is one enormous connect-the-dots. The "same engine, different
vehicle" of `why_the_ladder.md` is the same instinct. **Connect-the-dots is the
conjecture-generation phase; rigour is the verification phase; a healthy project
needs both, and it needs to keep them clearly labelled.**

## The one discipline that separates atlas from crackpottery

> Every note carries its confidence, and the framework's value is the *shape* it
> proposes, not the physics it claims.

`why_the_ladder.md` §4 is the gold standard — an explicit ✅/⚠️/❌ prediction
table. A note earns its place if it is **falsifiable or sharpenable in principle**
and **states its status honestly**. The only real sin is forgetting which lines
are ✅ and which are ❌ — which is exactly the bug that `moser_spindle_d2.md` had
(it asserted a $d_2$/NP framing as if rigorous) and the fix was to *relabel and
sharpen*, not to delete.

## How these have aged

**Philosophical core**
- `why_the_ladder.md` — *why* the ladder is universal at all. Answer: **observation**
  (choose context → record section → compare = Čech coboundary). The spine of the
  whole project; SPEC_00 §1 ("execution is observation") is its engineering form.

**Promoted to the main line**
- `transformers_bohrification.md` — transformer = learned Bohrification functor
  (RoPE = $H^1$ holonomy is the tight correspondence). On the actual endgame:
  `n/` + LLM neuro-symbolic = exact observer (engine) + learned observer (LLM).
- `distributed_consensus_cohomology.md` — FLP = $H^2$, Byzantine = $H^3$,
  Sybil = $H^4$. Already absorbed into the spec (APP_07).

**Upgraded to rigorous math** *(the proof that the nursery sometimes hides treasure)*
- `moser_spindle_d2.md` — the original (intuition-era) $d_2$/NP machinery was wrong,
  but the instinct (colouring obstruction = the same ladder) was right. Digging
  found real mathematics: Petersen = Kneser $K(5,2)$; Lovász–Borsuk–Ulam (chromatic
  number *is* a $\mathbb{Z}/2$ cohomological obstruction); and the Herlihy
  distributed-topology bridge back to `n/`. Revised 2026-06-14.

**Substrate identity (rigorous base, application open)**
- `quantum_applications.md` — the one application note that is *not* connect-the-dots:
  QEC's stabilizer formalism **is** the framework's objects (stabilizer state =
  Lagrangian = MASA; syndrome = anticommutation; MUB = Lagrangian spread). §1 is
  identity, not analogy; §2 is its **Gottesman–Knill** corollary (also rigorous): the
  Bohrified MASA-local CAID *is* the stabilizer representation, so `n/`'s forced
  quantization stayed polynomial because it lives on the efficiently-simulable Clifford
  island — and advantage ⟺ leaving it ⟺ the obstruction ladder. §3 onward
  (contextuality-as-resource; the $H^3$ modulus as a hidden multipartite resource) is
  the same open problem as `open_problems.md` item 24, approached from quantum
  information. The thing Paper VI wanted to write but couldn't until the symplectic
  substrate (X–XXII) existed.

**Shared substrate (rigorous home, with a citation action item)**
- `bhqc_shared_substrate.md` — the black-hole/qubit correspondence + the finite-geometry-
  of-the-Pauli-group program (Saniga, Lévay, Holweck, de Boutray, Borsten–Duff) is the
  framework's *home*, not an analogy: same $\mathbb F_2$, $\mathrm{Sp}(2n,2)$, doily,
  Fano, Mermin pentagram — closer than QEC. Lit check (2026-06-14) found a sibling scalar
  measure, **"contextuality degree," already computed at n=4,5,6** → real citation /
  novelty action item. The framework's genuinely novel layer is sharply located: the
  **cohomological** reading ($n_a=\delta\mu$, Maslov–Wall) + the **structural
  $n$-dependence theorems** (neither is in the degree literature). The framework is the
  *bridge* between finite-geometry contextuality degree and symplectic signature cocycles.
  Also the **third door** on item 24 (black-hole entropy).

**Candidate research line (computable, not parked)**
- `adscft_holographic_codes.md` — the QEC door reaches AdS/CFT, because holographic codes
  (HaPPY) are *finite stabilizer codes* = framework objects, and the XIX modulus
  (boundary↛bulk) mirrors **entanglement-wedge reconstruction** (subregion↛bulk operator).
  Shelved as "too loose" at Paper IX; no longer, because both ends are now sharp. Unlike the
  amplituhedron, the bridge is a **finite computation** (run $N_{\text{anti}}$ / obstruction
  on a HaPPY code; does the arity ceiling match the wedge threshold?). Cautions: geometry
  doesn't transfer (only the code); contextuality-obstruction vs erasure-threshold may not
  coincide — which is what the computation settles. Do *after* citation fixes. Fourth angle
  on item 24.

**Assessed and parked** *(deep analogy, recorded answer, not a research line)*
- `amplituhedron_duality.md` — the amplituhedron is the same observation-primary,
  emergent-global instinct, and is a near-*dual* of the ladder (positivity makes
  gluing *succeed*; the ladder measures how it *fails*) — so it serves as the
  **positive control** for the APP_07 §6 holographic framing. One well-posed but
  XXIII++-distant hook: Paper VIII's $\Phi$ and the amplituhedron both map into
  twistor $\mathbb{CP}^3$. Killed as a research line by the positivity / $\mathbb F_2$
  wall; **chase QEC instead**. Kept so the recurring question has a recorded answer.

**Live thought experiments** *(❌ as physics — kept as framework stress-tests)*
- `time_arrow_obstruction.md`, `higgs_gravity_obstruction.md`,
  `dark_matter_antipodal_cohomology.md` — no observational support (per
  `why_the_ladder.md` §4), and likely to stay that way. Their job is **not** to be
  physics. They stress-test how far the obstruction-ladder shape reaches, and
  *where the analogy breaks is as informative as where it holds*. They cost one
  markdown file each to keep.

## The standing rule

**Keep the dots; label the lines.** A correspondence that is honest about its
status is a free option: it costs almost nothing, and occasionally — Moser → Kneser
→ Lovász → Herlihy — one of them pays for the whole folder.
