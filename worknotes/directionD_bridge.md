# Direction D — unifying A & B: the transgression bridge (first strike 2026-06-13)

Goal: one object whose pages/截面 are the family-B (square, H², central-extension) and
family-A (pentagram, H³, anticommutation) obstructions. The user's "spiral, not ladder"
intuition = a spectral sequence; the discrete degree-ladder is a (non-canonical) FILTRATION;
the smooth object is the abutment + differentials. Script: supplementary/paper22/d_bridge.py.

## The unifying machine
LHS spectral sequence of the Heisenberg/Pauli extension
   1 → Z_2 → P_n → V=F_2^{2n} → 1   (Paper IV's machine).
Base H*(V;F_2) = F_2[x_1..x_{2n}] (elementary abelian 2-group, polynomial, deg x_i=1).
- TRANSGRESSION (d_2): fiber generator ↦ ω = Σ_i x_i x_{i+n} ∈ H^2(V)
  = the symplectic 2-cocycle = family-B / KS central-extension / Mermin-square SIGN class.
- Family-A H^3 candidate source: Sq^1 ω ∈ H^3(V). COMPUTED (d_bridge.py):
  Sq^1 ω = Σ_i (x_i^2 x_{i+n} + x_i x_{i+n}^2), nonzero, 2n monomials, all degree 3.
  (Sq^1 = Bockstein of the Z_4→Z_2 reduction; on the polynomial ring Sq^1 x_i = x_i^2.)

## The bridge (sharp, falsifiable)
Sq^1 ω is ONE class in H^3(V) (fixed by n); na VARIES over pentagrams at fixed n. So the
bridge is a PAIRING, not an identity:
   na = ⟨ Sq^1 ω , [pentagram] ⟩,   [pentagram] ∈ H_3(V;F_2)
a proper K5 defines a fundamental 3-cycle (from its rays via the bar complex); na is its
pairing with the family-A source.
CONSEQUENCES:
1. n=4 RIGIDITY recast: Sq^1 ω ≠ 0 in H^3(F_2^8) but na≡0 at n=4 ⟹ every n=4 pentagram
   3-cycle lies in the ANNIHILATOR of Sq^1 ω. XVIII's B0/B1/B2 = "pentagram cycles cannot
   pair with Sq^1 ω until V is large enough (n≥5)." The master theorem, cohomologically.
2. TWO routes must AGREE (internal check):
   (i) algebraic:  na = ⟨Sq^1 ω, [K5]⟩      (Bockstein of the Heisenberg class)
   (ii) geometric: na = δμ, μ = Maslov 2-cochain = mod-2 metaplectic/Weil cocycle (Paper XV)
   ⟹ PAPER XV (Weil representation) IS the transgression: the map carrying Heisenberg-H^2 (ω)
   up to Maslov-H^3 (na). The spiral, named:
        q →(polarize)→ ω →(Sq^1 = Weil/Maslov)→ na
   with the incidence complex (B's clique number ω(G)) selecting the DEGREE.

## Layering (why it's a spiral, q vs ω)
- Family B (square sign) needs the QUADRATIC REFINEMENT q (Hermitian phase, q(x,z)=x·z,
  q(u+v)=q(u)+q(v)+ω(u,v)) — a Z_4 / Pontryagin-square datum.
- Family A (anticommutation na) needs only ω (commutator) — the POLARIZATION of q.
So q is logically PRIOR (the i-phase), ω is its polarization, na = Sq^1(ω). This inverts the
naive "H^2→H^3 climbing": the families are Bockstein/Steenrod-linked layers of ONE datum (the
Pauli phase), assembled on different nerves. Discreteness of the "ladder" = the filtration
(degree) is a chart; abutment of the LHS SS is the smooth object.

## STATUS — honest
DONE: framework (LHS SS), transgression = ω (family B), algebraic H^3 source Sq^1 ω computed
& nonzero, sharp falsifiable conjecture na=⟨Sq^1ω,[K5]⟩, n=4-vanishing consistency condition,
identification of XV/Weil as the geometric transgression, the q/ω layering.
OPEN (the one real gear): the COMPARISON MAP (proper K5) → [3-cycle in H_3(V)]. KEY
CLARIFICATION: the naive simplicial map ∂Δ⁴→BV (edge {i,j} ↦ loop v_ij) is NOT strict,
because the rays are NOT additive on triangles: v_ij + v_jk ≠ v_ik in general (they sum to 0
only on Fano triangles — B0). That FAILURE OF ADDITIVITY is exactly the Maslov data, and na
is the obstruction to making the config-to-BV map coherent. So:
   na = the homotopy-coherence obstruction of the pentagram's map into BV.
The comparison map is therefore a HOMOTOPY-COHERENT (∞-)map, not a strict one; building it =
the "two theories" reconciliation = genuinely ∞-categorical. Until built, na=⟨Sq^1ω,[K5]⟩ is
conjecture. (This is also why the early Postnikov instinct was right: the obstruction lives in
the homotopy-coherence/k-invariant layer, not a strict chain map.)
NEXT concrete: (a) construct the comparison map and TEST na=⟨Sq^1ω,[K5]⟩ on sampled K5 at
n=4 (predict 0 = annihilator) and n=5 (predict matches N_anti mod 2); (b) verify routes (i)
and (ii) agree by relating Sq^1ω to δμ. See [[project-paper22-resonance]],
[[project-paper20-h3-borromean]] (dir 3 metaplectic checkpoint), truncation_vs_ladder.md.

## SORTING THE ZOO: forgetful-down vs structure-adding-up (2026-06-16, GPT prompt)

Insight (GPT, refined): for the framework→OPERATIONAL relation, the right shape is not a
comparison map but a FORGETFUL FUNCTOR. Recasts the item-24 saturation result categorically:
- F: (framework configs + full ladder) → (operational behaviours) = quotient by
  operational-indistinguishability. Concrete instance: square(H²) ≡ pentagram(H³)
  operationally (MBQC: both deg-2 non-adaptive, both universal adaptive) ⟹ F NOT faithful;
  it forgets all degree above the threshold (≈H²).
- ADJUNCTION unifies saturation + modulus: a forgetful functor's would-be free adjoint =
  "reconstruct structure from operational data"; the MODULUS THEOREM says that fails
  (can't recover H³ from below-threshold data). Saturation (forgetting) and modulus
  (non-reconstruction) = one adjunction. The forgotten datum = the framework's added value.

CRUCIAL DISTINCTION (do NOT conflate with D-proper):
- DOWNWARD (framework → operational, → coarser detect-or-not cohomologies, e.g. AMB sheaf
  ≥ Okay–Raussendorf group-coh): FORGETFUL / lossy. Nothing to "solve" — lossy by nature.
- UPWARD within the framework (H² ω → H³ na via Sq¹): D-PROPER. Sq¹ is a cohomology
  OPERATION (Bockstein) — structure-ADDING, the opposite of forgetful. THIS is the one
  genuine comparison-map (homotopy-coherent) question; the only arrow that is an
  equivalence-type problem, not a forgetful projection.
⟹ The forgetful sorting NARROWS the frontier: most "comparison maps" we worried about are
forgetful (no capstone). The real wall is the single Sq¹ equivalence = the ∂Δ⁴→BV coherent
map below. Item 24 and the operational arrows are now understood as forgetful; D-proper is
what remains — and it is structure-ADDING (Sq¹), so the forgetful lens does not dissolve it.

## WHY D MATTERS (the Yoneda reading, user 2026-06-16)
na = ⟨Sq¹ω, [K5]⟩ is a REPRESENTABILITY statement: the function "na" on pentagram
configurations is represented by ONE universal class Sq¹ω ∈ H³(V). The object's intrinsic
invariant = how it pairs against the universal probe — the Yoneda move. And the representing
class is Sq¹ (a NATURAL operation) applied to ω (the framework's OWN defining symplectic form,
H²). So H³ is not new data: it is the framework's ground-floor datum run through a canonical
operation. The framework explains its top floor in the vocabulary of its ground floor —
self-representation. THIS is the appeal of D, independent of the grind: not "do A & B match"
but "the structure is self-representing." (The grind is real but the result is Yoneda-flavored.)

## GEOMETRIC ROUTE TESTED → NEGATIVE (2026-06-13, supplementary/paper22/geometric_route.py)
Tested the nerve-side shortcut: is the H^3 class = Sq^1(Maslov) realized as the cup-1 square
mu∪_1mu? Cup-1 formula on ordered tetrahedron (t0..t3): (mu∪_1mu)_T = mu(t0,t2,t3)mu(t0,t1,t2)
+ mu(t0,t1,t3)mu(t1,t2,t3). RESULT: NO.
- n=4: ⟨mu∪_1mu,[S³]⟩==N_anti 640/640 but trivially (μ≡1→cup≡0, N_anti≡0; all vanish).
- n=5: class match 365/640≈57% (independence baseline ≈41%, identity would be 100%) — correlated
  but ≠. cochain na==cup 10/640, na==δμ+cup 182/640, na==δμ 14/640 — ALL fail.
- n=6: cup≡0 (μ≡1) but N_anti 50/50 → match 1234/2400≈51% = pure chance.
WHY (principled): μ is NOT a cocycle on the nerve (δμ≠0 at n≥5), so Sq^1 can't be applied
nerve-side; cup-1 square of a non-cocycle is not a cohomology operation. The genuine Sq^1 ω
lives on V (ω a cocycle there); pulling it to the config NEEDS the comparison map — the rays'
non-composition (δμ≠0) IS the obstruction, no Maslov detour around it.
⟹ shortcut CLOSED; comparison map is the irreducible gear. CONFIRMS XX's caution: the H^3
class is NOT a naive Bockstein/Steenrod of the H^2 (KS) class — now verified at cochain level
(no simple Sq^1 of nerve data = na). The bridge na=⟨Sq^1ω,[K5]⟩ remains OPEN, contingent on
the V-side homotopy-coherent comparison map.

## TWISTOR FACE OF D (2026-06-20, supplementary/twistor_cp/) — item 13 resolved
Item 13 (Paper VIII §3, geometric d_k^eff ladder on CP^{2ⁿ⁻¹}) turned out to be the SAME
Sq¹ wall wearing twistor clothes — a third face of D (after algebraic A↔B and the Klein
quartic).
- H*(CP^N;F₂)=F₂[h]/h^{N+1}, |h|=2: even degree, Sq¹h=0 (h=c₁ mod 2 is an integral
  reduction), Sq²h=h². So CP^N is Sq¹-ACYCLIC; its whole Steenrod structure is the Sq²/
  cup-power ladder.
- The realization h↔ω (Paper VIII Thm 2.1, PM=family B) is a RING iso onto F₂[ω] but NOT a
  Steenrod-module map: Sq¹h=0 vs Sq¹ω=na≠0. The obstruction to naturality is exactly na.
  Equivalently ω does not lift to an integral (Chern) class — "ω is not a c₁", obstruction
  the integral Bockstein βω=Sq¹ω=na. Verified: Sq¹(ω^{2j})=0 (matches h^{2j}), but
  Sq¹(ω^{2j+1})=ω^{2j}·na≠0 (unmatchable on CP, where Sq¹≡0).
- So the conjectured ladder EXISTS as family B (cup-powers, Sq²) and is obstructed for
  family A by na. The twistor/CP side hosts Sq² and is blind to Sq¹.
WHY THIS IS D, NOT A SEPARATE PROBLEM: D asks "is Sq¹:H²→H³ a genuine arrow (the comparison
map)?" Item 13 asks "why is CP blind to family A?" — same answer: because the family-A class
IS Sq¹ω, and the geometric/operational shadows (CP cup-powers, GK-magic, HaPPY reconstruction)
all live in the Sq¹-trivial / forgetful image. na is the residue of Sq¹ that no even-degree,
integral-reduction, c₁-power geometry can see. The comparison map is still the irreducible
gear (the geometric route is closed both nerve-side, above, and now twistor-side).

## NAME (2026-06-20): the self-representation map
"comparison map" is the borrowed construction-term (compare the nerve ∂Δ⁴ with BV); it
undersells and mis-frames — comparison is two-object, but this is ONE object in its own terms.
Better name: THE SELF-REPRESENTATION MAP. One gear, three faces:
  - as an OPERATION: Sq¹: H²→H³ (the unique structure-adding / non-forgetful arrow);
  - as a FUNCTOR: the quantization 𝒬 (item 14, free left adjoint; na = counit defect of 𝒬⊣ℬ
    being an equivalence; physically = whether ω lifts to the Z/4 i-phase, Sq¹=Z/4-Bockstein);
  - as a PAIRING: the ∞-Yoneda self-pairing na=⟨Sq¹ω,[K5]⟩ (framework explains its top floor
    in ground-floor vocabulary; alpha_fixed_point: α = the universe's Yoneda self-pairing).
"the one wall" = seen from OUTSIDE (6 doors hit it); "the self-representation map" = seen from
INSIDE (structure in its own mirror). n=4 = the unique dimension where the self-representation
is coherent. Recorded in RESEARCH_FRONTIER item 23 title + the_one_wall.md §4.

## CLEAVING THE PAIRING (2026-06-20): the n-dependence is in [K5], not Sq^1 omega
(collaborator's contribution + corrections; sharpens item 23's open half = the
configuration-side pairing N_anti mod2 = <Sq^1 omega, [K5]>.)

CORE (right): the n-dependence of the pairing lives in the configuration side [K5],
NOT in Sq^1 omega (a fixed/stable class). But the route matters:

(0) NO real conflict with spread-stab. "Sq^1 stable => padding-invariant, yet n_a
    vanishes at n=4 only => contradiction" is NOT a contradiction: padding an n=4 K5
    gives an n>=5 config that STAYS even; the n>=5 ODD configs are new, non-padded.
    "n=4 all-even / n>=5 mixed" is fully consistent with padding-invariance.

(a) STRICT MAP => PAIRING == 0  (the sharp strengthening). If a strict f:S^3->BV
    existed, f*omega in H^2(S^3)=0, so by naturality f*(Sq^1 omega)=Sq^1(f*omega)
    =Sq^1(0)=0 => <Sq^1 omega,[S^3]> == 0 => N_anti always EVEN. But n>=5 has odd.
    => the non-existence of a strict map is ESSENTIAL; the pairing is a SECONDARY
    (functional / Massey-type) operation: primary part f*omega is forced 0 on S^3,
    all n-dependence sits in the coherence (filler) data. This explains "stable
    operator yet n-sensitive answer": primary Sq^1 stable, but the pairing is
    secondary, whose definedness/indeterminacy is unstable. A priori reason the
    naive cup-1 (mu cup_1 mu, geometric_route.py) HAD to fail: it is a primary-
    looking guess that misses the non-strictness corrections.

(b) THE CARRIER is (W, omega|_W), the ray-span + restricted form -- concretely the
    10x10 ray Gram matrix G_{(ij),(kl)}=omega(v_ij,v_kl). N_anti is a function of G.
    NOT "which skeleton" ([K5] is always a degree-3 class). The right invariant is
    (dim W, rank G, dim rad W) = Paper XIX's order parameter rad(omega|_W)
    (noq_odd_proof (8,6,2) stratum; nge5_probe rankG/radW) -- ALREADY computed.
    spread-stab keeps the rays in the V-summand ((L_i+U_i) cap (L_j+U_j)=v_ij+0),
    so it preserves G ENTRYWISE => invisible to any Gram-function. That is the
    precise content of "padding doesn't move the pairing." n-dependence = which G
    are REALIZABLE at dim n (n=4: 2n=8 squeeze/B1/B2 forces even; n>=5 allows odd).

NET on item 23: this does NOT bypass the hard core; it RELOCATES it, with 3
constraints any solution must meet: (1) the pairing is secondary (strict=>0);
(2) n-dependence carrier = ray Gram / (W,omega|_W) = the XIX order parameter;
(3) any bridge must be invisible to spread-stab (Gram-preserving embedding).
The remaining work: compute [K5]'s chain-level image in H_3(BV) via the CORRECT
cup-1 (the secondary representative with coherence corrections, not naive mu cup_1
mu) and prove it = n_a. Item 23's open half is now "secondary-operation on the
known order parameter (W,omega|_W)", not "construct a coherent map from scratch".

## ZERO INDETERMINACY = RESONANCE (2026-06-20): the bridge is an EXACT equation
(collaborator: functional Sq^1's indeterminacy lives in H^{q-1}(X)=H^1(S^3)=0.)
Refines item 23's secondary-operation framing (previous block). Both good news and
bad, and they are the same fact.

(1) BOTH indeterminacy sources die. For functional Sq^1_f(omega) (theta=Sq^1,k=1;
    u=omega,n=2; f:S^3->BV):
      Indet = f* H^3(BV)  +  Sq^1 H^1(S^3).
    - Sq^1 H^1(S^3) = Sq^1(0) = 0   (beta unique up to exact, H^1(S^3)=0) -- the
      collaborator's term.
    - f* H^3(BV) = 0, and STRONGER: [S^3,BV]=H^1(S^3;V)=0, every honest map null.
    => Indet=0. The secondary op, where defined, is a SINGLE rigid bit in
    H^3(S^3)=F_2. So the bridge N_anti mod2 = Sq^1_f(omega) is an EXACT equality,
    no coset fudge. GOOD NEWS for the shape (clean, two-valued, falsifiable).

(2) DUAL CATCH (honest): the same thinness (H^1=H^2=0) removes the topological
    crutch. (a) all S^3->BV null => honest pushforward f_*[S^3]=0 always; (b)
    textbook functional Sq^1_f needs Sq^1 omega = 0 in H^3(BV) (mapping cone:
    i* Sq^1 ~omega = Sq^1 omega must vanish to lift to Sigma X) but Sq^1 omega =
    n_a != 0 -> textbook version OBSTRUCTED. => the real home is the COCHAIN-LEVEL
    LAX map phi: C*(BV)->C*(S^3) (chain map, NOT multiplicative), n_a =
    [phi(omega cup_1 omega)], with beta (phi(omega)=delta beta, exists since
    H^2(S^3)=0) the mu-level nullhomotopy. Rigidity fixes the ANSWER's uniqueness,
    not the CONSTRUCTION: the correct beta (NOT naive mu, geometric_route.py) is
    still chain-level handwork.

(3) UNIFICATION -- ZERO INDETERMINACY *IS* RESONANCE (same fact). The resonance
    nerve is the sphere S^{N-2}, cohomology only in {0, N-2}. This thinness gives
    BOTH:
      - n_a a SINGLE top class (resonance)        <- top H^{N-2}=F_2
      - secondary op ZERO indeterminacy (rigidity) <- middle H^1=0 (beta unique)
    beta-uniqueness (H^1(S^3)=0) = "no middle cohomology" = the resonance condition
    N=a+1 itself. So RESONANCE = RIGIDITY: the pentagram both squeezes the
    obstruction to one H^3 bit AND makes the secondary op computing it
    unambiguous, by the one sphere-ness.

NET (item 23 open half), now FOUR constraints on any bridge:
  (1) secondary (strict => 0); (2) carrier = ray Gram /(W,omega|_W) = XIX order
  param; (3) spread-stab-invisible (Gram-preserving); (4) zero-indeterminacy =>
  bridge is an EXACT equation, same fact as resonance.
The target is cleaner than expected (one rigid bit, exact equality); the path is
NOT shorter (thin sphere gives rigidity but removes the topological crutch ->
explicit coherence-corrected cup-1 with the correct beta remains the work).

## f*H^3(BV)=0 BY DIMENSION + strict/lax = skeleton boundary (2026-06-20)
(collaborator: clean CW argument for the f*H^3 indeterminacy term, replacing my
"every honest map null".)

CLEAN ARGUMENT for f*H^3(BV)=0. The configuration is gens (rays v_ij) + relations
(symplectic pairings) = standard 2-skeleton data. The honest classifying map factors
(up to homotopy) through BV^{(2)}, a 2-complex. H^3(BV^{(2)};F2)=0 PURELY because
there are no 3-cells (cellular cochain complex vanishes above dim 2). So
  f*: H^3(BV) -> H^3(BV^{(2)})=0 -> H^3(S^3),  hence f*H^3(BV)=0.
Better than "[S^3,BV]=H^1(S^3;V)=0 => f null": (a) needs no nullness, no EM-space
property (works for any gens+relations target), (b) kills ALL of H^3 wholesale incl.
Sq^1-irrelevant cubics (x_1^3) -- dimension, not Sq^1-specific, (c) elementary/local
(count cells), in-spirit for an explicit framework. [BV=K(V,1) => null agrees but is
not needed.]

TENSION + RESOLUTION. "f through BV^{(2)} => f*Sq^1 omega = 0" but n_a != 0 (n>=5)?
The CW count computes the HONEST/STRICT shadow -- which IS what the indeterminacy
term f*H^3(BV) refers to -- so killing it there is correct. n_a does NOT live there:
it lives in the LAX coherence data on the 3-cells, exactly what a strict
factor-through-BV^{(2)} map discards.

UPGRADE: strict/lax divide = the skeleton boundary.
  2-skeleton S^{3,(2)}: rays(gens)+symplectic relations -> STRICT, through BV^{(2)},
    H^3-blind by DIMENSION.
  3-cells (5 tetrahedra): coherence fillers -> LAX, the ONLY place H^3/n_a can live.
So "the pairing must be secondary/lax" is no longer an abstract claim but a skeleton
fact: strict 1-/2-cell data cannot support H^3; seeing n_a REQUIRES 3-cell filler =
laxness. Dovetails with zero-indeterminacy=resonance: now BOTH indeterminacy terms
have elementary thinness reasons -- Sq^1 H^1(S^3)=0 (no middle cohomology = resonance,
beta unique) and f*H^3=0 (image in 2-skeleton = dimension). Both = "S^3 thin", second
now landed as cell-counting.

## (mu,F) CORRECTION FAMILY RULED OUT (2026-06-21, supplementary/item23_search/)
Acted on the collaborator's parametrized-search idea via F2 linear algebra (verification is
microseconds, so settle the whole family at once).
FAMILY: a_T = any degree-<=2 F2-poly in T's 4-face data {mu(f0..f3), F(f0..f3)} (37 coeffs;
contains mu cup_1 mu and Fano-weighted mu*F corrections).
RESULT: decisively NEGATIVE.
  - degree-<=2 system inconsistent: cochain 33296/126500 rows, class 10064/25300 rows.
  - collision test (stronger): a is NOT a function of (mu,F) at ANY degree. n=5: ~123 of ~430
    (mu,F)-keys carry >1 distinct a. n=6: even-n forces mu==1, F const -> ONE (mu,F)-key but a
    ranges over all 32 values. (mu,F) is blind to the family-A class.
  - validation passed: n=4 alone consistent with a_T=0 (=delta mu, since mu==1 => delta mu=0).
WHY: the ARITY GAP. a is arity-4 (ray PAIRS); mu,F are arity-3 (triangles). The H^2/H^3
resonance separation IS the irreducibility of the arity-4 class to arity-3 data -> no (mu,F)
formula can give a. This is an empirical shadow of Paper XIX's modulus (arity-<=k invariants
don't classify the H^3 fiber). Explains+generalises geometric_route's mu cup_1 mu failure: not
the wrong COMBINATION of mu, but mu is the wrong ALTITUDE.
NET: meta-strategy (parametrize + F2 linalg) is sound/fast/reusable; the natural (mu,F) family
is killed wholesale. Sharpens (doesn't shave) item 23: the secondary formula must be built from
arity-4 / ray-pairing (Gram, edge-pair) data, not Maslov/Fano triangle summaries -- the lax
map's nullhomotopy lives FINER than mu. Reusable harness in item23_search/ for the next family.

## CHASE TERMINUS (2026-06-21): symplectic formula-search is CIRCULAR; need beta_{Z/4}(q)
Pursued "use ray-pairing/arity-4 data" (user: 追擊). Hit a structural floor.
- COMPOSABLE pairings omega(v_ij,v_jk) VANISH: v_ij,v_jk both in shared Lagrangian L_j ->
  commute. Verified 0/933000 across n=4,5,6 (phi_omega_zero.py).
- => phi*omega == 0 at COCHAIN level (not just class). a=Sq^1omega pullback has NO primary
  part -> PURELY secondary (strongest form of the lax statement).
- => the ONLY nonzero symplectic pairings on the nerve are the DISJOINT ones, whose matched
  sum IS a. Defect pairings reduce to these too: omega(w_ijk,v_il)=omega(v_jk,v_il). So every
  symplectic expression in rays/defects is a lin. comb. of disjoint pairings = a. ANY
  pairing-formula for a is CIRCULAR. The formula-search program cannot give a non-trivial
  bridge over symplectic data -- no "lower" symplectic datum exists.
- CONFOUND CAUGHT: the "b_omega cup_1 b_omega matches a 100/76.6/51%" run was bogus -- b_omega
  identically 0, so the match% just = a==0 frequency (= 100/76.6/50.5%, confirmed).
- The lone nonzero NON-symplectic lower datum: polarized cocycle f / quadratic refinement q
  (Z/4 structure), nonzero on commuting pairs. But cup-1 of it (b_f) matches only 74%/61%
  (n=4/5) -> WRONG. Correct object = Z/4-BOCKSTEIN of q, since Sq^1omega = beta_{Z/4}(omega)
  and q is the Z/4 lift. (Not cup-1.)
NET: "追擊" confirms insight-bound at a STRUCTURAL level -- formula-search provably circular
over symplectic data; bridge content lives in the Z/4 quadratic-refinement/Bockstein (the lax
coherence assembling defects into Sq^1omega) = genuine inf-categorical/topological work.
IDENTIFIED NEXT STEP: chain-level beta_{Z/4}(q) computation (convention-heavy; the real pitch).

## COMPUTABLE OR HANDWORK? failure ladder complete (2026-06-21, q_determinacy.py)
User asked if the final segment (beta_{Z/4}(q)) is pure handwork or computable.
Tested whether the q-layer (quadratic refinement / Z4, polarized f on composable rays --
NON-circular, nonzero where omega=0, far finer than (mu,F)) determines a.
RESULT: a is NOT determined by q either -- witnessed but narrowly. n=5: 20000 configs ->
19896 distinct q-keys (q NEARLY INJECTIVE) yet 32 keys split (same q, different a). n=6: 2.
So all three natural cochain-level data layers FAIL to determine a:
  symplectic pairings (arity-2) -> CIRCULAR (phi*omega=0; only nonzero pairings = a)
  Maslov+Fano (arity-3)         -> determines-not COARSELY (430 keys, 123 split; arity gap)
  quadratic refinement q (Z/4)  -> determines-not FINELY (19896 keys, 32 split; q ~injective)
ANSWER: verification is ALWAYS computable (any fully-specified candidate, microseconds), but
no cochain-level SUMMARY STATISTIC determines a -> there is no shortcut formula to search for.
The bridge is irreducibly the LAX-MAP construction (defects w_ijk + higher coherence assembling
into Sq^1 omega) = symbolic infinity-categorical HANDWORK. The computer is a fast VERIFICATION
ORACLE -- it has now ruled out every natural summary (symplectic/Maslov-Fano/q) -- NOT a
constructor. The creative content (the formula) must come from the coherence construction;
once guessed it is instantly testable (and provable-for-all-n is then separate handwork).

## CLOSED FORM FOUND (2026-06-21, closed_form.py) -- collaborator's lead paid off
Collaborator's 3 points: (1) "no summary statistic" wording too strong -> soften to "every
tested family fails" [CORRECT, now concretely: a global closed form DOES exist]; (2) cheap test
q+stratum on the 32 q-collisions; (3) q almost-determines a = Bockstein signature, go to
beta_{Z/4}(q).
- Ran (2): q + Paper-XIX stratum (dimW,rankG,radW) RESOLVED 15/32 of the n=5 q-collisions, 17
  unresolved. So stratum carries real info but is insufficient. That sent me back to polarization.
- The missing ingredient was a single GLOBAL term q(T), T=XOR of all 10 rays. CLOSED FORM:
     N_anti mod 2 = q(T) XOR XOR_i q(v_i),   q(v)=parity(X.Z).
  PROOF (all n, elementary): q is a quad refinement (q(u+v)=q(u)+q(v)+omega); polarization:
  q(T)=XOR q(v_i) XOR sum_{i<j} omega(v_i,v_j); composable pairs vanish (phi*omega=0) so
  sum_{i<j} omega = N_anti. QED. Verified 24600/24600 EXACT at n=4,5,6.
- This is the AMBIENT/unconditional form of Paper XIX S5 (intrinsic Q(T)=N_anti; intrinsic Q has
  Q(rays)=0 so no correction; ambient q needs the XOR_i q(v_i) correction, no hypothesis).
- CORRECTS my overstatement: a IS determined -- by the 11-bit q-summary {q(v_1..10), q(T)}. The
  q-collision tests' keys had q(v_i) but were MISSING the global q(T). No clash w/ modulus: q(T)
  is arity-10 (global), not low-arity. So the honest statement is "no LOCAL/low-arity summary
  determines a; a GLOBAL quadratic-refinement closed form does."
- FOR ITEM 23: coordinate closed form (q not Sp-invariant; net combo is). NOT yet the intrinsic
  bridge <Sq^1 omega,[K5]>. But q = Z/4 lift of omega, Sq^1 omega = beta_{Z/4}(omega), so this is
  the explicit q-handle the beta_{Z/4}(q) direction predicted. Open step now: identify
  q(T) XOR XOR q(v_i) == chain-level <Sq^1 omega,[K5]> -- BOTH SIDES EXPLICIT (checkable identity,
  not blind search). Revised verdict: item 23 MORE computable than the terminus implied; the
  family-A class has a closed form; what stays symbolic is the intrinsic identification.

## PER-TETRA (COCHAIN) CLOSED FORM (2026-06-21) -- the form item 23 actually pairs with
Extended the closed form to the cochain level (per tetrahedron), exact all-n:
   (n_a)_m mod 2 = q(S_m) XOR XOR_{6 rays of tetra m} q(v),   S_m = XOR of those 6 rays.
Same proof per tetra: polarization of q on the 6 rays among the 4 vertices != m; their 3
disjoint pairs = (n_a)_m, the 12 adjacent pairs vanish. Verified 123,000/123,000 EXACT n=4,5,6.
=> the family-A COCHAIN n_a itself (not just the total N_anti) is closed-form in q. Item 23's
pairing <Sq^1 omega,[K5]> = XOR_m (n_a)_m = XOR_m [q(S_m) XOR XOR_{6}q(v)] is now fully explicit
at cochain level. The remaining open step (identify this with the INTRINSIC Sq^1 omega pullback)
is unchanged, but now both the total AND the cochain have explicit q-forms to match against.

## ATTRIBUTION FIX + basis test (2026-06-21) -- the TOTAL formula is Paper XI, not new
Collaborator walked the polarization chain (closes) and pointed at Paper XI -- with one detail
to correct: my formula uses ALL 10 rays v_{ij} (T=XOR of 10), NOT "5 Lagrangian representatives".
So it is the 10-ray version = Paper XI Proposition (Quadratic form identity):
  q(T) = sum_a q(r_a) + omega_total (mod 2),  over the 10 rays r_a = v_{ij}.
=> the TOTAL closed form is REDISCOVERED Paper XI, not new. (Also the ambient form of Paper XIX
S5's intrinsic Q(T)=N_anti.) Genuinely NEW: (i) the per-tetra COCHAIN refinement
(n_a)_m = q(S_m) XOR XOR_{6 rays} q(v); (ii) the item-23 framing (q-form as explicit handle for
<Sq^1 omega,[K5]>).
BASIS-CHANGE TEST (collaborator's, basis_invariance.py): under symplectic transvections,
individual q(v_i),q(T) change (~97% of configs) but net XOR stays = N_anti (900/900). Confirms
"coordinate closed form, not intrinsic bridge" concretely: Sp-invariant combination, frame-
dependent summands. (If it had failed -> formula basis-dependent = red flag; it did not.)
REMAINING (agreed): identify q(S_m)+XOR q(v) with the chain-level beta_{Z/4}(q) cochain -- not
just same cohomology class but same COCHAIN (item 23 is cochain-level), so the Bockstein
convention (which lift, which boundary sign) must be matched term-by-term. Still symbolic, but
now "verify a conjectured identity between two explicit objects", not "construct a lax map".

=== 2026-06-21 (cont.) — THE LAST STEP: bridge closes modulo Kudo/Quillen ===
Resolved the "remaining symbolic" item above. The right altitude was NOT "beta_{Z/4}(q) as a
Bockstein of a cocycle q" (q is not a cocycle: delta q = omega != 0). The correct framing:

  omega = [c], c(g1,g2)=X_g1.Z_g2 = the cup/extension cocycle of the Heisenberg 2-group;
  q(v)=c(v,v) = its DIAGONAL; Sq^1 omega = [c cup_1 c] (cup-1 self-product, standard Steenrod).

Three-link chain  (n_a)_m = q(S_m)(+)XOR q  =  (c cup_1 c)|_m  =  Sq^1 omega|_m:
 (A) n_a = polarization defect of q       -- OURS, proven all n (polarization + adjacency vanish).
 (C) that defect = Sq^1 omega             -- standard; PINNED by sq1_bar.py:
       bar complex of V, verified [c cup_1 c]=[Sq^1 omega=sum a_i b_i(a_i+b_i)] in H^3,
       n=1 (11/16 pivots), n=2 (234/256); delta r = c cup_1 c + P consistent. Both cocycles, P!=0.
       cup_1 formula used: (c cup_1 c)(g1,g2,g3)=c(g1,g2+g3)c(g2,g3)+c(g1+g2,g3)c(g1,g2).
 (B) join = Kudo transgression tau(t^2)=d_3(t^2)=Sq^1 omega in Heisenberg LHS SS; q is the
       chain trivialization t (delta q = omega). CLASSICAL (Quillen extra-special 2-grp / Kudo),
       CITED not re-derived = Paper XXII outlook backbone.

Resolved a sign/convention trap on the way: the ALTERNATING form is delta q hence [omega-alt]=0;
the nonzero H^2 class is the SYMMETRIC cup class [c]=sum a_i b_i (c+c^T=alternating=delta q). So
"omega" as the operative class = [c], and Sq^1 of it = sum a_i b_i (a_i+b_i) != 0. The "integer
lift delta/2" Bockstein gives 0 for bilinear c (it IS an integral cocycle) -- WRONG route; the
right one is cup_1 (Sq^1 of a class not in the image of integral reduction). sq1_bar.py confirms.

HONEST: NOT a from-scratch proof of Sq^1 omega; (B) is cited. A self-contained proof would build
the self-rep map dDelta^4 -> BH through the extension and recompute d_3 by hand = re-derive Quillen.
phi^*omega=0 still stands: bridge is genuinely SECONDARY (zero indeterminacy, H^1(S^3)=0), q is its
nullhomotopy -- exactly why the primary symplectic-pairing search was circular.
NET: item 23 open half closed-to-citation; lone genuine frontier now = item 21 (and 23's Sq^1
bridge unblocks the Steenrod-action argument for 21's ceiling).
Files: closing_note.md (statement+ledger), sq1_bar.py (link C check).

=== 2026-06-21 (cont.2) — collaborator's methodological catch on (C): "n=1,2 brute or all-n?" ===
Right question. Resolution = the LATTER, and stronger: (C) is ALL-n with ZERO numerical input.
  c=sum a_i cup b_i = cup of 1-cocycles => 2-cocycle, [c]=omega (all n);
  Sq^1[c]:=[c cup_1 c] is STEENROD'S DEFINITION (cup_1 well-defined on cohomology indep of diagonal
    approx choice) (all n);
  Sq^1 omega = sum a_i b_i(a_i+b_i) by Cartan + Sq^1(deg1)=square, identity in F_2[a_i,b_i] (all n).
So [c cup_1 c]=Sq^1 omega for every n by definition+Cartan. The only n-INDEPENDENT thing that could
be wrong = whether my coded cup_1 FORMULA is the standard simplicial one (a fixed combinatorial
expr, no n in it). n=1,2 runs = UNIT TEST of that transcription (confirm it yields NONZERO Sq^1
omega, not 0/wrong). Transcription-correct at n=1,2 => correct all n. delta-r witness need NOT
generalize (only certifies two reps of a definitionally-equal class are cohomologous).
OWNED: my prior framing "convention pinned by computation (n=1,2)" wrongly implied the EMPIRICAL
small-n case, inviting "then only n<=2". Fixed in closing_note/README/FRONTIER: (C) all-n by
def+Cartan; numbers = unit test.
WHERE n-DEPENDENCE LIVES (not in C): (A) (n_a)_m=q-defect verified IN-REGIME n=4,5,6 (123k); and
the pairing vanishing <Sq^1 omega,[K5]>=0 iff n=4 = master thm (XX/XXI). (C) being n-flat is CORRECT.
Secondary point taken: c is a 2-cocycle PROVABLY (cup of 1-cocycles; bilinear form for trivial
action delta c=0) -- added explicit delta c=0 check at n=1,2,3,4 (all pass) + a line in closing_note.
Did NOT run n=3 FULL coboundary solve (O(|V|^5), infeasible & not load-bearing); ran cheap
c-cocycle check at n=3,4 instead.

=== 2026-06-21 (cont.3) — collaborator: split (B) into TWO citations; (B) is SECONDARY ===
Key correction: the join (B) does TWO different classical things, was wrongly bundled as "Kudo".
First, the structural point that forces it: f:S^3->BV has f*omega=0 (H^2(S^3)=0), so by naturality
f*Sq^1 omega = Sq^1(f*omega) = 0 as a PRIMARY class. So N_anti != 0 can ONLY be a SECONDARY
operation -- this is the real reason phi*omega=0 / zero indeterminacy. (Good: explains the earlier
"purely secondary" finding from first principles.)
Nullhomotopy is AUTOMATIC: q's quadratic-refinement identity q(u+w)=q(u)+q(w)+omega(u,w) IS
delta q = omega in coords; being a quad refinement is exactly why q is a nullhomotopy. So (A)'s
polarization defect = by construction the cochain value of the secondary operation with nullhtpy q.
TWO citations (same magnitude):
 (B1) Steenrod-Epstein functional/secondary operation explicit formula (Cohomology Operations):
      secondary op = c cup_1 c + correction terms in the nullhomotopy r. With r=q = the explicit
      cochain SHAPE. "what the operation looks like."
 (B2) Kudo transgression tau(t^2)=d_3(t^2)=Sq^1 omega (Quillen extra-special 2-grp). "what it equals."
FINAL SMALLEST OPEN STEP (honest, NOT done): substitute (c,q) into the Steenrod-Epstein formula and
expand -> should give (A)'s defect term-by-term, no leftover. Difficulty class = "expand known
formula + check algebra" = same as all closed links, NOT a search. Structural identification stands;
only the exact correction-term match is uncertified.
Updated: closing_note (B split into B1/B2 + secondary-op framing + nullhtpy-automatic + the open
expansion flagged), README, FRONTIER ("modulo two cited theorems + one expansion-check"), top status.
Did NOT attempt the Steenrod-Epstein hand-expansion (convention-heavy; risk of writing it subtly
wrong > value; flagged as the minimal residual instead).

=== 2026-06-21 (cont.4) — ATTEMPTED the Steenrod-Epstein expansion: DECISIVE NEGATIVE ===
User said "do the last step, science isn't about always being right." Did it. Result REFUTES the
collaborator's optimistic "expand-known-formula + check algebra, same difficulty class."

se_expand.py findings (nerve, rays r_ij from sh):
 - self-rep map NEVER simplicial: triangle defect w_ijk = r_ij+r_jk+r_ik != 0 in 100% (0/175000).
 - f#c NEVER closed on nerve: delta(f#c)_m == 0 only ~50% (chance). So NO nullhomotopy b with
   delta b = f#c exists => the functional-Sq1 framing DOESN'T APPLY on the nerve.
 - primary simplicial cup_1 of f#c: sum_m == N_anti only 53%/50% (chance); per-tetra 65%/58%. Not it.
 - q(w) triangle-defect patch = 0 identically (each edge in 2 faces -> multiplicity-2 cancel;
   triangle rays adjacent => commute => no omega term). Confirms hand-analysis.

se_search.py (the decisive one): solve CORR_m = (n_a)_m XOR primary_m as F2-linear combo of natural
defect terms {const, q(r_e)x6, q(w_f)x4, c(w_f,w_g) orderedx12, omega(w_f,w_g)x6} (29 basis);
also +ray-defect cross omega(r_e,w_f)x24 (53 basis).
 -> INCONSISTENT: ~50% contradictory rows (15023/30000 n=4; 31275/62500 n=5); rank stuck 12-13;
    cross terms DON'T help. The correction is NOT a function of the local defect data.

INTERPRETATION (honest): the join (B) is IRREDUCIBLY the higher-coherence d_3 transgression. No
finite cochain formula on the nerve realizes it. Same purely-secondary/circular wall (phi_omega_zero)
now at FINEST resolution (no local cup1+defect formula). So:
 - DROP the "B1 Steenrod-Epstein functional formula expand-and-check" as a finite residual; it
   provably does not exist.
 - Status: closed modulo the cited KUDO/QUILLEN transgression (single citation). The BONUS of the
   failed attempt: we now KNOW the transgression is the irreducible floor (not assume it).
 - (A) proven + (C) all-n stand unchanged. Bridge TRUE (Kudo), just not finitely-witnessable at
   cochain level on the nerve.
Subtlety clarified: q is nullhomotopy of the SYMMETRIZED form omega_alt=c+c^T (delta q = omega_alt),
NOT of c; and f#c isn't closed anyway. The "q=t, delta q=omega" shorthand was loose; the real
content is the d_3, period.
Files added: se_expand.py, se_search.py. Updated closing_note/README/FRONTIER + top status.
NET for program: lone open frontier still item 21; item 23 = closed-to-Kudo, irreducibility now
demonstrated.

=== 2026-06-21 (cont.5) — collaborator: SCOPE the step-3 negative (no implicit universal quantifier) ===
Same failure mode as the earlier "no summary statistic determines a" overstatement. A bounded-family
search returning inconsistent is a definite negative ABOUT THAT FAMILY, not a nonexistence proof.
Audited the committed files: found real overreach ("shortcut does not exist", "never simplicial",
"correction is not a finite function", "join is irreducibly d_3", "provably irreducible / no finite
expansion-check exists"). SCOPED everything into three tiers:
 (robust empirical) self-rep map not simplicial (w!=0 all 175k samples) + f#c not closed => the
   FUNCTIONAL-Sq1 ROUTE specifically is inapplicable (it needs a nullhomotopy of f#c). Defensible:
   precondition of a specific construction fails across all samples.
 (definite, bounded) the tested basis {1,q(r),q(w),c(w,w),omega(w,w),omega(r,w)} doesn't contain
   the correction (inconsistent linear system).
 (inference, NOT proof) strong evidence -- consistent w/ phi_omega_zero secondary/circular -- that
   no finite local cochain formula realizes (B); content appears to live in d_3. NOT a nonexistence
   proof (space of finite formulas unparametrized; cf. item 21).
Headline status UNCHANGED and safe: "closed modulo the cited Kudo transgression" (Kudo is a theorem).
Only the "we proved no finite shortcut exists" subclaim was wrong and is now scoped to evidence.
Edited: closing_note.md (section + ledger B1 + bottom + files), README.md, RESEARCH_FRONTIER.md
(L506 + L531), se_search.py docstring. Re-grep clean.
Note: pre-existing "provably circular over symplectic data" (L498) left as-is -- it has a structural
reduction argument (all symplectic exprs reduce to disjoint pairings = a), not just a family search,
so it's more defensible; flag if revisiting.

=== 2026-06-21 (cont.6) — same scoping lens applied to item 21 (user's catch) ===
User: "這樣 item 21 是不是也..." -> yes. Item 21's BODY (L443-451) is already gold-standard honest
(non-existence claim, sampling wrong tool, search space unparametrized, bounded check only nudges
confidence). The overclaim was the POST-23 cross-reference: "with 23's Sq1 bridge, the Steenrod-
action argument for the ceiling is unblocked" (L531) and L451's "bearing directly on item 21".
WHY it's overreach: 23's Steenrod machinery caps only the STEENROD-GENERATED ascent from omega:
  - Sq1 omega (H3, indecomposable), Sq1 Sq1 omega = 0 (Adem),
  - Sq2 omega = omega^2 (H4) but DECOMPOSABLE (family B), Sq^i omega=0 i>2 (instability)
  => no NEW indecomposable obstruction Steenrod-generated past Sq1 omega.
BUT item 21's crux = exotic NON-BILINEAR, NON-STEENROD arity-5 invariant (Arf/Dickson-type, L449
pts iii-iv) -> Steenrod is SILENT on it. So 23 settles a related-but-distinct sub-question (the
Steenrod escape), NOT item 21. Item 21 stays the unparametrized modular-invariant-theory non-
existence problem, genuinely open, NOT reduced by 23.
Same pattern as step-3: "ruled out one family != ruled out all." Fixed L451 + L531 to scope.
Lesson (3rd time now): whenever a sub-result "unblocks"/"closes" a non-existence claim, check it
covers the WHOLE claim, not just the tractable (Steenrod/bilinear/bounded-family) part.
