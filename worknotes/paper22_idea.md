# Paper XXII seed — the arity/configuration resonance tower (Direction B)

## DRAFTED 2026-06-13 → research/papers/Paper22_resonance_ceiling.tex (6pp, compiles clean,
## 0 overfull). Title: "The Arity–Resonance Ceiling: Why Pauli Contextuality Stops at H³".
## Sections: arity-resonance principle (Prop) | two rungs K4/H² + K5/H³ with n-dependence
## from rank-parity (Cor) | truncation theorem (c=δa exact on K6 ⟹ [c]=0; proper K6 exist) |
## clique criterion min(ω-2,3) | Mermin square = family B (bipartite, central-extension) |
## outlook = D/spectral-sequence. Rigor table: most RIGOROUS; "no arity-5 lid" = conjectural;
## even-weight saturation = empirical. KEY clean lemma used: c_m=N_anti(face_m)=⟨a,∂face_m⟩
## =(δa)_m, so the degree-4 assembly is literally a coboundary (one-line truncation proof).
## Needs: PaperXXIIsuppl DOI (placeholder); double-check PaperIII/VIII DOIs (left generic).
## REVIEW ADDRESSED 2026-06-13 (inner/paper22_review.md): (1) Prop 4.1 K4/H² opening
## (odd n≥5 "both values") downgraded from rank-parity-rigorous to COMPUTATIONAL (cites
## resonance_tower.py n=5 211/189); rigor table split vanishing(rigorous)/opening(comp).
## (2) Prop 3.1 group-vs-class nontriviality clarified (class-nontriviality = XX/XXI, not
## this prop). (3) §5 "32 of 2⁵" → "all 32 even-weight in F₂⁶, kernel of Σ". (4) Prop 5.1
## K6 embedding now cites XXI spread-stabilisation. (5) Thm 5.2 states the partition fact
## (15 cross-context pairs partitioned by the 5 four-index subfacets). Recompiles 6pp clean.
## READABILITY PASS 2026-06-13 (like XX): intro local-to-global opener; §3 arity-resonance
## intuition (degree = joint-observation arity); §4 two-rungs lead-in; §5 truncation lead-in.
## REVIEW 2 ADDRESSED 2026-06-14 (inner/paper22_review2.md, strongly positive): (1) arity-5
## lid tightened — NOTE the reviewer's suggested argument ("polynomial in pairwise ω is
## arity≤4") is FALSE (products span more indices, e.g. ω(v12,v34)·ω(v15,v23)→5 indices);
## used the correct version (canonical deg-4 assembly = δa exact via Thm 5.2; q4 arity-4
## saturated; a new invariant needs NON-bilinear data; stays conjectural). (2) added explicit
## K6 sextuple (six symmetric 4×4 F₂, pairwise sums rank 3, 15 distinct rays) as Remark after
## Prop 5.1. Now 7pp, 0 overfull. Reviewer: XXIII = the D comparison map (matches directionD).



Started 2026-06-13. Goal: the CEILING THEOREM generalizing the K5/H³ result + K6
truncation into one structural statement. Scripts: supplementary/paper22/resonance_tower.py
(+ paper21/k6_truncation.py for the truncation rung).

## The thesis
An obstruction built from arity-a symplectic data is intrinsically an (a-1)-cochain on the
index nerve of any configuration. On K_N (nerve ∂Δ^{N-1} ≅ S^{N-2}, nontrivial cohomology
only in degree 0 and N-2) it lands in TOP cohomology H^{N-2} iff a-1 = N-2, i.e. **N = a+1**.
- N < a+1: over-determined (forced coboundary / lower-degree rigidity).
- N = a+1: RESONANCE — genuine top class.
- N > a+1: sub-top, forced exact (TRUNCATION).
Each arity has a unique resonant configuration K_{a+1}. Pauli/symplectic data furnishes
exactly two natural cochains — Maslov μ (arity 3) and anticommutation na=δμ (arity 4) — so
the tower has two live rungs and a lid.

## The tower (ALL VERIFIED)
| cochain | arity | config | nerve | class | n=3 | n=4 | n=5 | n=6 | opens at |
|---|---|---|---|---|---|---|---|---|---|
| Maslov μ | 3 | K4 | S² | H² | rigid(μ≡0) | rigid(μ≡1) | OPEN ~50/50 | rigid(μ≡1) | **odd n≥5** |
| anticomm na=δμ | 4 | K5 | S³ | H³ | mixed(all-Fano=1) | rigid(=0) | OPEN | OPEN | **all n≥5** (n=3 all-Fano) |
| (none, arity5) | 5 | K6 | S⁴ | H⁴ | 0 | 0 | 0 | 0 | **never (truncation)** |

H² class = ⟨μ,[S²]⟩ = Σ_{4 triangles} μ mod 2 (μ is a 2-cocycle on ∂Δ³≅S²; top cells=4
triangles). resonance_tower.py: n=3 {0:400}, n=4 {0:400}, n=5 {0:211,1:189}, n=6 {0:400}.
H³ class = ⟨na,[S³]⟩ = N_anti mod 2 (Papers XX/XXI). H⁴ = ⟨c,[S⁴]⟩ = Σ_m N_anti(face_m) ≡ 0
always (k6_truncation.py; double-count: each disjoint pair in exactly 2 of 6 faces).

## Why this is more than "re-run on another config"
The tower DERIVES the even/odd dichotomy from rank-parity, instead of positing it:
- H² is PURELY a μ-phenomenon ⟹ opens exactly where μ varies = ODD n≥5 (rank-parity:
  μ≡1 even n, μ≡0 n=3, varies odd n≥5). Rigid at every even n and at n=3.
- H³ = ⟨δμ,·⟩-type but na=δμ couples BOTH channels: Part B (μ, odd-n) AND Part A
  (anticommutation count, even-n). So H³ opens at ALL n≥5 — the extra Part-A channel is
  exactly what lets even n≥6 open (XXI even-carrier = na alone). n=3 opens via all-Fano.
- H⁴: no cochain ⟹ never opens. K5 is the unique ceiling because na (arity 4) is the top
  natural cochain.
So the single rank-parity lemma (rank B=n-3) governs the WHOLE tower's n-dependence, and the
arity ceiling governs the degree. One picture, two knobs (degree=config size, openness=n).

## CEILING THEOREM (target statement)
For Pauli contextuality the cohomological ceiling is H³, realized uniquely at the Mermin
pentagram K5, because (i) the natural data tops out at arity 4 (anticommutation), and (ii)
arity-4 data resonates with K5 (S³). Below: K4/H² (Maslov). Above: forced exact. The
n-dependence of each rung is dictated by the rank-parity lemma.

## LATERAL TEST DONE — Mermin-Peres square (2026-06-13, supplementary/paper22/mermin_square.py)
The 3x3 magic square = 6 Lagrangians in Sp(4,F₂): 3 rows + 3 cols. VERIFIED: rows pairwise
transverse, cols pairwise transverse, each row∩col = 1 ray (9 rays = 9 observables) ⟹ the
incidence nerve is BIPARTITE K_{3,3}, NOT the all-pairwise K_N. Every one of the 20 triples
of contexts has a transverse (no-ray) pair ⟹ the K_N Maslov μ / anticommutation cochains
(which need 3 pairwise rays) are UNDEFINED here. The square's obstruction is the ±I SIGN
mismatch (Hermitian-Pauli phase): per-context signs all +1 except R3 (the YY row) = −1,
product over 6 contexts = −1 ⟹ CONTEXTUAL. This is the quadratic-refinement / central-
extension class = the H² "KS world" of Papers III–VIII, a DIFFERENT cohomology theory.

⟹ BIG REFRAME: the ceiling is FAMILY-RELATIVE. (At least) TWO contextuality cohomology
families:
 (A) all-pairwise K_N / Maslov-anticommutation / NERVE cohomology → ceiling H³ at the
     pentagram K5 (Papers XVIII–XXI). Arity/resonance tower is internal to A.
 (B) bipartite K_{m,n} / quadratic-refinement / CENTRAL-EXTENSION (±I sign) → Mermin square
     K_{3,3} at H² (Papers III–VIII). GHZ (3-qubit, 4 contexts) = same sign family.
The pentagram's H³ is NOT a universal ceiling — it is the ceiling of family A. This
concretely EXHIBITS the long-suspected "two cohomology theories" as the natural homes of two
DIFFERENT configuration families, not two rungs of one ladder. ⟹ Direction D's unification
needs a real bridge between the K_{m,n}/quadratic world and the K_N/anticommutation world
(Paper IV's transgression is the candidate); the lateral test located exactly where the gap is.
XXII reframed: a TAXONOMY of contextuality configs by cohomological family, with the
arity/resonance ceiling internal to each family.
OPEN sub-question: is there a family-B resonance tower (does some bigger bipartite K_{m,n}
give H³ in the central-extension family)? — the B-analog of "why the pentagram".

## B CONSOLIDATED — the incidence-clique criterion (2026-06-13, supplementary/paper22/clique_criterion.py)
Define the INCIDENCE GRAPH G of a config: vertices=contexts, edge iff two contexts share a
ray (meet in dim 1). The family-A (Maslov/anticommutation) nerve obstruction is supported on
G's clique complex; a degree-d class needs a (hollow) (d+2)-clique. ⟹
   **family-A ceiling = min(ω(G) − 2, arity−1=3)**,  ω(G)=clique number.
Saturates (RESONANCE) at ω=5 (pentagram). Needs ω≥3 (triangles) to be nonzero at all.
VERIFIED: Mermin square ω=2 (triangle-free K_{3,3}) → ceiling 0 → family-A TRIVIAL → family B
(sign/central-extension); proper K4 ω=4 → H²; proper K5 ω=5 → H³. So the whole resonance
tower compresses to ONE graph invariant, and the A/B split = (ω≥3) vs (ω=2). Triangle-free
incidence FORCES the obstruction (if any) into the central-extension/sign class.
NOTE (subtle, for D): the square's nerve = clique complex of K_{3,3} is 1-dim with H¹=F₂⁴;
its contextuality is detected in nerve-H¹ (Abramsky/sheaf) AND packaged as the central-
extension H² (group cohomology). Reconciling these packagings = the A↔B / IV-transgression
bridge = exactly the "spiral/spectral-sequence" picture (the discrete degree-grading is a
non-canonical filtration; abutment + transgression is the smooth object). Family A and B are
plausibly two pages/截面 of ONE LHS spectral sequence.

## Open / next for XXII
1. Tighten "no natural arity-5 invariant" (q4 is arity-4 & saturated — XIX; argue no
   irreducible 5-Lagrangian symplectic F₂ invariant). This is what makes the lid a theorem.
2. Other configurations beyond K_N (Mermin–Peres 3x3 square, GHZ): different nerves, do they
   give the same ceiling or new ones? (Paper VIII Φ functor touched K_{3,3}.) Lateral test
   of universality — the part that turns "K_N tower" into "ceiling theorem for configs".
3. Decide framing: pure-math ceiling theorem (clean, finishable) vs. tie to the IV
   comparison map / Postnikov lid (Direction D capstone — needs unifying the group-H² and
   nerve-H² theories first; the resonance tower is nerve-cohomology throughout, so it is
   internally consistent and does NOT yet bridge to the early group-cohomology papers).
See [[project-paper21-dichotomy]], [[project-paper20-h3-borromean]], truncation_vs_ladder.md.
