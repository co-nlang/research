# AdS/CFT, holographic codes, and the modulus: a *computable* line off the QEC door

*Status: ⚠️ candidate **research line** (not a parked dot) — speculative bridge, but with a
concrete, finite, **computable** test. Better-grounded than at Paper IX. Do after the
citation fixes; ahead of the parked items.*

## History (why this was shelved once)

Paper IX (`paper9_idea2.md`) weighed AdS/CFT as the physical reading of the
$\mathcal Q\dashv\mathcal B$ adjunction and **set it aside**: *"類比有趣但太鬆散，需要指定
哪個 AdS、哪個 CFT，否則停留在比喻。"* It chose **Quantum Darwinism** instead, which had real
categorical content ($\mathcal B=\Phi^*$ = coarse-graining; PM contextuality = environment
fragments that cannot be reassembled into a global state; $K_{3,3}$'s $H^1$ = a
non-extendable record-graph section).

That choice was right. But the specific objection that shelved AdS/CFT — *too loose, name
a model* — is now largely answerable.

## Why it is no longer "too loose"

1. **You need a holographic *code*, not continuum AdS/CFT — and those are finite stabilizer
   codes = the framework's objects.** AdS/CFT *is* a QECC (Almheiri–Dong–Harlow 2015): bulk
   operators are redundantly encoded on the boundary, reconstructable from subregions. The
   concrete toy models — **HaPPY codes** (Pastawski–Yoshida–Harlow–Preskill 2015), the
   perfect-tensor / pentagon codes — are **stabilizer codes**, i.e. live in the framework's
   substrate (stabilizer = Lagrangian = MASA, `quantum_applications.md` §1). "Which AdS /
   which CFT" collapses to "the HaPPY code on a hyperbolic tiling," a *finite* $\mathbb F_2$
   object. The looseness was in the continuum; the code side is not.
2. **The framework now has a holographic *theorem* to attach to.** APP_07 §6 (the XIX
   modulus): boundary arity $\le4$ underdetermines bulk $H^3$. AdS/CFT-as-QEC has the
   structurally same statement — **entanglement-wedge reconstruction** (Dong–Harlow–Wall
   2016): a boundary subregion cannot recover a bulk operator unless it is large enough.
   Both are *code-theoretic boundary-underdetermines-bulk with a threshold.* At Paper IX
   neither end was sharp; now both are.
3. **Quantum Darwinism is the bridge, not a rival.** QD is redundant encoding of classical
   records into the environment — exactly the redundancy AdS/CFT-QEC exploits (one bulk
   operator, many boundary subregions). So QD → holographic redundancy → entanglement wedge
   is a *path*. The door you already opened leads here.

## The reason this beats the amplituhedron line: it is computable

The amplituhedron died on positivity and offered only a non-computable comparison map. Here
the objects are finite stabilizer codes, so the bridge is a calculation:

> **Sharp, computable question.** Compute the framework's invariants ($N_{\text{anti}}$ /
> the obstruction classes $n_a$) on a HaPPY-type holographic stabilizer code. Does the
> framework's reconstruction obstruction (the **arity / clique ceiling**, Paper XXII) line
> up with the code's **entanglement-wedge reconstruction threshold** (subregion size)?

Both sides are computable on the *same* finite code. This is an experiment, not a conjecture.

### Concrete next step (when this line is picked up)

1. Build the HaPPY pentagon code explicitly as a stabilizer code → its Lagrangian /
   $\mathrm{Sp}(2n,\mathbb F_2)$ data.
2. For a boundary region $A$, compute (a) the QEC erasure-correction threshold (is the bulk
   operator in the entanglement wedge of $A$?) and (b) the framework's obstruction
   restricted to the contexts supported on $A$.
3. Test the alignment: does "bulk operator becomes reconstructable as $|A|$ crosses the
   wedge" coincide with "the framework's obstruction on $A$ vanishes / the arity ceiling is
   reached"? Tabulate over regions, as the `paper21/` scripts tabulate over configurations.

## Cautions (label the lines)

- **Geometry does not transfer — only the code.** AdS/CFT's bulk is continuous hyperbolic
  space with a metric (RT areas). $\mathbb F_2$ has no metric, so "the tensor network
  *realizes a bulk geometry*" has no finite analogue. The *code* crosses; the *geometry*
  does not. (Same shape as the amplituhedron's positivity gap, but far less fatal — the part
  you need does cross.)
- **Two different "obstructions"; they may not coincide.** The framework's obstruction is
  *contextuality* (cannot glue a global section). AdS/CFT's is an *erasure-correction
  threshold* (cannot recover an operator from too small a region). Both are code-theoretic
  and both say "local data insufficient," but they are formally distinct. Whether they are
  the *same* obstruction on holographic codes is exactly the open question — an honest
  *maybe*, and the computation above is what would settle it.

## Step 1 result (2026-06-16) — building block computed

`supplementary/adscft/happy_513.py`: the [[5,1,3]] perfect tensor in
$\mathrm{Sp}(10,\mathbb F_2)$ ($S$ isotropic, logical $=S^\perp/S$). Over all 32
boundary regions:
- **sharp reconstruction threshold: bulk recoverable $\iff |A|\ge3$**;
- **entanglement-wedge complementarity exact** (exactly one of $A,\bar A$ owns the
  bulk; 0 violations).

So the *shape* (sharp threshold + complementarity + same objects) transfers
rigorously. But the threshold is $|A|\ge3$ of **5 qubits** — a *distance/erasure*
number — not the framework's arity-5 / $H^3$ among *contexts*. The naive "arity
ceiling = wedge threshold" identification **fails at face value**: same shape, same
objects, but contextuality/$H^3$ and erasure/distance are **different faces** of
"local data insufficient" (the caution above, now demonstrated).

A structural consequence pins down step 2: **a single tile is one commuting
stabilizer group = one context, hence trivially non-contextual.** The framework's
contextuality is multipartite, so any genuine obstruction-measure correspondence must
be an **emergent network property** (multiple tiles → multiple bulk qubits / overlapping
contexts), not a tile property. The bridge test therefore *requires* the small-network
build (step 2); the tile alone cannot decide it. A legitimate possible endpoint: the
correspondence is **shape-level** (boundary↛bulk + complementarity), strong but not an
obstruction identity — recorded as such if the network shows no cross-context tracking.

## Disposition

A genuine research line, ahead of the parked items, **behind the citation fixes**. It is the
rigorous successor to the early `COSMOLOGY/07_PHYSICS_Holography_and_Action.md` (fits the
"keep COSMOLOGY front as picture, back → papers" plan). It is also a **fourth angle on item
24** (operational meaning of the $H^3$ class), from the holographic-code door — and unlike the
BHQC black-hole-entropy door, this one comes with a finite computation attached.

---

*See `quantum_applications.md` (QEC substrate identity — the door this opens off),
`bhqc_shared_substrate.md` (the other QEC-adjacent geometry, black-hole side),
APP_07 §6 (holographic / boundary→bulk), `open_problems.md` item 24,
`paper9_idea2.md` (where AdS/CFT was first weighed and Quantum Darwinism chosen),
Papers XIX (modulus), XXII (arity ceiling).*

**Sources:**
[Bulk locality & QEC in AdS/CFT — Almheiri–Dong–Harlow (1411.7041)](https://arxiv.org/abs/1411.7041) ·
[Holographic QEC codes / HaPPY — Pastawski–Yoshida–Harlow–Preskill (1503.06237)](https://arxiv.org/abs/1503.06237) ·
[Entanglement-wedge reconstruction — Dong–Harlow–Wall (1601.05416)](https://arxiv.org/abs/1601.05416) ·
[Entanglement renormalization & holography (MERA) — Swingle (0905.1317)](https://arxiv.org/abs/0905.1317) ·
[Quantum Darwinism — Zurek (0903.5082)](https://arxiv.org/abs/0903.5082)
