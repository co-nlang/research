# Open-problems roadmap (post-XXII)

Working roadmap of unfilled pits. Intent: fill these *as addenda / companion notes*
(附論, in the spirit of the LsNote appendices) when time allows — not necessarily as
full papers. Difficulty/status audited 2026-06-14.

Two registers:
- **Main line** (the H³ obstruction program, Papers XVIII–XXII): the live wall is the
  family A↔B unification.
- **Backlog** (mathematically beautiful tangents from Papers VII–IX, already recorded in
  `RESEARCH_FRONTIER.md` Part II): Klein quartic / Ramanujan, twistor gerbe.

---

## A. Main-line frontier (Papers XVIII–XXII)

### A1. The live wall — family A↔B unification (the capstone)
| pit | source | difficulty | nature |
|---|---|---|---|
| Comparison map ∂Δ⁴→BV | XXII Outlook / directionD_bridge | 🔴 hard (∞-categorical) | THE key to unifying family A/B; coherence obstruction = nₐ |
| nₐ = ⟨Sq¹ω, [K₅]⟩ conjecture | directionD_bridge | 🔴 **gated by the comparison map** | sharp, falsifiable — but verification/falsification both need the map; the cup-1 shortcut (μ∪₁μ) is already RULED OUT (geometric_route.py, n=5 ≈ chance) |

NOTE: these two are ONE problem. nₐ=⟨Sq¹ω,[K₅]⟩ is not independently computable — the Sq¹ω
side is algebraically clean (d_bridge.py), all the difficulty is in the coherent map BV side.
This is XXIII material if/when attempted. Metaplectic angle: XV's Weil cocycle is the candidate
transgression carrying the H²(family B) class to the H³(family A) class.

### A2. Addendum-sized (concrete, companion-note scale)
| pit | source | difficulty | nature |
|---|---|---|---|
| K₄/H² opening — algebraic proof | XXII §4 | 🟡 **ADVANCED 2026-06-20 (`supplementary/k4_h2_opening/`), not fully closed** | (a) EXACT certified witnesses n=5,7 (explicit Lagrangians, both classes) — upgrades "211-vs-189 sampled" to existence-by-certificate. (b) FLIP REDUCTION: ⟨μ,[S²]⟩=μ(012)⊕f(L₃), f(L₃)=μ(013)⊕μ(023)⊕μ(123)=|{ij∈{01,02,12}: L₃∩A_ij≠∅}| mod 2, A_ij={x+y:x∈Lᵢ,y∈Lⱼ,ω=1}; surjective ⟺ f non-constant, demoed by a single-Lagrangian swap. **RESIDUE (the medium part): uniform all-odd-n NOT proven. Spread-stabilization fails to transport — even-m spread forces μ_m≡1 (rigid), m=3 preserves μ but flips n-parity (rank-parity coupling). Needs per-n construction or an all-odd-n non-constancy lemma for f(L₃).** Turned out medium-not-quick. |
| Family-B resonance tower | XXII §8 | ✅ **RESOLVED 2026-06-20 (`supplementary/familyB_resonance/`)** | NO separate tower. Complete r-partite graph has clique number = r, so by the clique criterion min(ω-2,3): bipartite K_{m,n} (r=2) stays ceiling 0 for ALL m,n (triangle-free = 1-dim, b₁=(m-1)(n-1), H^≥2=0) — never climbs. Climbing needs more PARTS (r-partite) = family A, topping at H³ at r=5 = pentagram K₅=K_{1,1,1,1,1} (r≥6 capped by item 19/21). Family-B class = ω∈H² (±I bit); only ascent to deg 3 is Sq¹ω=na (family A). ⟹ family B is family A's ω=2 FLOOR; Q1 collapses into Q2 (item 23). Classification: family-A content = min(ω(G)-2,3); ω=2 ⟹ family B (central ext only); ω≥3 ⟹ family A. Mermin square verified (K_{3,3}, triangle-free, μ/a undefined, global product -I via 4×4 matrices). |
| Even-n equidistribution — correlation bound | XXI OP1 | 🟡 partial | uniform-foot lemma DONE (single-constraint bias 1/(2ⁿ−1)); multi-constraint foot-bit correlation/bias bound open |
| Key Lemma — algebraic proof | XVIII appendix | 🟠 optional | Gram rank-8 ↔ Σ=0; alternative route, main theorem doesn't need it (NOT confirmed to be specifically a "Pfaffian" route — XVIII only records it as a structural characterization) |

### A3. Open-ended / conjectural
| pit | source | difficulty | nature |
|---|---|---|---|
| Arity-5 lid (make truncation a hard theorem) | XXII rigor table | 🔴 **conjectural — PARKED 2026-06-20 for XXIII** | must exclude *non-bilinear* 5-Lagrangian invariants. ⚠️ the easy argument "F₂-poly in pairwise ω → arity≤4" is FALSE (products span ≥5 indices, e.g. ω(v₁₂,v₃₄)·ω(v₁₅,v₂₃) uses {1,2,3,4,5}). Real content: canonical deg-4 assembly = δa exact (Thm 5.2), q₄ arity-4 saturated. **The hard core: a generation/non-existence theorem in modular (F₂) invariant theory of Sp(2n,2) on Lagrangian *tuples* — no FFT (subspaces not vectors; char 2 harbours Arf/Dickson/q₄; ring unclassified). Feasibility (2026-06-20): brute enumeration hopeless at n=5 (#Lag=75,735; 5-tuples ~1e24, 6-tuples ~1e29; fix-L1 4-tuples ~1e19); sampling (paper19 method) only proves EXISTENCE (found modulus), wrong tool for non-existence; search space of non-bilinear invariants unparametrized. ⟹ computation can't reach it. Real path = route 1 (FFT/SFT for Lagrangian tuples, char-2 invariant theory), XXIII-level. Co-dependent with item 23: if Sq¹ω=na (the comparison map) holds, the Steenrod action on H*(V) gives the ceiling a structural reason (no source past Sq¹ω; Z/4-Bockstein already closed, item 19). Item 21 & 23 = the two genuine open frontiers.** |
| H³ physical interpretation (item 24) | XXI OP4 | ✅ **DISSOLVED 2026-06-16 (mistyped question)** | item 24 asked an *operational* question of a *structural* quantity. H³ is an obstruction (classifying) class by construction. **Precise reason (not "cohomology is non-operational" — H² IS operational, Anders–Browne):** operational axes resolve only the **threshold** (contextual at all? ≈ H²) and **saturate** there — none grades by cohomological *degree*. So H³ is a structural refinement *finer than operational resolution*. Confirmed by 3 saturating axes: GK-magic (simulable), AdS/CFT (support/erasure), MBQC (deg-2 ceiling, deg-3 from H² alone — `mbqc/`). Verdict: H³ = classifying coordinate + certification depth, not a power. = "framework = coordinates," now precise. See `quantum_applications.md` §7. |

---

## A′. Empirical contact — DELEGATED, not a debt we owe (⚠️ inconclusive)

`research/papers/timescape_cross_validation.tex` (May 2026) — the **only** time the framework
touched real data. Tests the $H^1$ geometric-phase prediction (SN Hubble residual ↔ line-of-sight
void fraction $f_v$) via the Timescape model (Wiltshire 2025) on Pantheon+/Union3/DES-SN5YR × VAST
voids. It is the source of `why_the_ladder.md` §4's lone ⚠️ row.

**Status: inconclusive, leaning unconvincing — and the clean test was never actually done:**
- The tests that *directly* test the prediction ($f_v$ regression) **failed** for engineering
  reasons (column-mapping bug; DES-south × SDSS-north hemisphere mismatch; + a binary-vs-continuous
  category error).
- The test that "worked" (χ² mass-step reversal: void $\Delta\chi^2{+}94$ / wall ${-}106$) **does
  not use $f_v$ at all** — it splits by `HOST_LOGMASS` (host mass as an environment proxy, a
  weak/unestablished link). It is **non-diagnostic**: the asymmetric $\Delta\chi^2$ is equally
  consistent with "the mass step absorbed an $H^1$ signal" and "the mass step is a real
  astrophysical correction you just broke." And $\Delta\chi^2\approx300$ over $398$ SNe is
  implausibly large for a subtle effect → likely **normalization/baseline-dominated**, not $H^1$.

⟹ Converges with item 24 (operational meaning of $H^3$/$H^1$), from the **cosmology door**.

**Disposition — delegated, not a debt.** This empirical work belongs to the field that owns it:
the Timescape group (Wiltshire et al.) is *already* doing exactly this. The framework's only job
here was to supply a **coordinate** — "*if* the Hubble tension is a void/wall geometric effect,
*then* it sits at $H^1$" — and that coordinate is **invariant to the outcome**: Timescape right →
the coordinate was used by reality; Timescape wrong → a conditional with a false antecedent, the
framework not refuted. So this is **not our open problem**; we'd re-run it only if we *choose* to
care about cosmology. The clean methodology is on record for whoever does: per-SN BBC
$\delta_\text{bias}$ (not uniform $\pm0.03$); same-hemisphere footprint (Pantheon+ north × BOSS
void); continuous $f_v$; permutation significance.

**Keep on record** as the honest *counterweight* to the elegant math (a real attempt that
reported, honestly, no clean signal) — and as the reminder that the framework is a **cartographer,
not a competitor**: the map's position does not change with whether the territory is what we
guessed. The framework earns its keep not here but where a coordinate is non-trivial *and* lands —
QEC substrate-identity (not even conditional) and item 24.

---

## A″. Citation hygiene — shared substrate with the BHQC / finite-geometry program (action, not research)

Lit check 2026-06-14 (see `insight/bhqc_shared_substrate.md`): the framework's substrate
is the *same* body as the Saniga–Lévay–Holweck–de Boutray–Borsten–Duff finite-geometry /
black-hole-qubit program. A **sibling scalar measure, "contextuality degree," is already
computed at n=4,5,6** (arXiv:2105.13798, 2305.10225, 2407.02928). The novel layer survives
(cohomology n_a=δμ / Maslov–Wall + the structural n-dependence theorems are NOT in that
literature — confirmed), but the papers (already on Zenodo) need:
1. cite the contextuality-degree lineage where N_anti is used (primary site: XVII);
   state the N_anti ↔ contextuality-degree relationship.
2. cross-check XVIII/XXI n=4,5,6 numbers vs their published computations (no uncited re-derivation).
3. confirm XIX cites Saniga for the doily; IX for Fano embedding (Saniga–Planat / Lévay).
4. position H^• explicitly as group cohomology of Sp(2n,2), distinct from Veldkamp space
   (theirs) and from Abramsky measurement-sheaf cohomology (item 24 bridge).

Disposition: do on the next paper revision pass; strengthens standing, retracts nothing.

**Progress 2026-06-14 (foundational sites done, compiling clean):**
- ✅ **XVII** — added "Relation to prior work" (SanigaPlanat substrate; LevayPlanatSaniga
  pentagrams/12,096; deBoutray+Muller contextuality degree, N_anti stated as sibling) +
  positioned H^• as group cohomology of Sp(2n,2) vs Veldkamp vs Abramsky (items 1 & 4). +4 bibitems.
- ✅ **XVIII** — "Relation to prior work" (SanigaPlanat + deBoutray+Muller; n=4 quadrics);
  framed N_anti=10 universality as complementary/structural vs their case-by-case degree. +3 bibitems.
- ✅ **XIX** — doily now cited to SanigaPlanat + VeldkampTwoQubits (Saniga–Planat–Pracna–Havlíček) (item 3).
- ✅ **IX** — already cited LevayPlanatSaniga (Fano/pentagram); no change needed.
- Item 2 (number cross-check): addressed in spirit — the new paragraphs state N_anti and
  contextuality degree are *different* invariants (anticommuting pairs vs unsignable contexts),
  so there is no uncited re-derivation; a literal number match is not expected.
- ✅ **XXII** — §7 Mermin–Peres square now cited to Mermin + SanigaPlanat + VeldkampTwoQubits
  (doily Sp(4,2)≅S₆). +3 bibitems.
- ✅ **XXI** — "Relation to prior work" (SanigaPlanat + deBoutray/Muller through n=6); framed
  the master theorem as rigidity + structural n-dependence vs their case-by-case degree;
  positioned H^• as group cohomology of Sp(2n,2) vs Veldkamp vs sheaf. +3 bibitems.

**Status: A″ complete** — XVII, XVIII, XIX, XXI, XXII all edited & compile clean; IX already fine.
All cites anchored on verified arXiv IDs (quant-ph/0612179, 1305.5689, 2105.13798, 2305.10225, 0704.0495).

---

## B. Backlog — mathematically beautiful tangents (Papers VII–IX)

Recorded in `RESEARCH_FRONTIER.md` Part II (items 11–14). Lower physics-relevance to the H³
program, but very rich mathematically; natural addenda if the mood strikes.

### B0. Synthesis 2026-06-19 — both backlogs split along the F₂ ↔ char-0 seam

After the Klein steps 1–3 and the Z/4-Bockstein answer (`supplementary/bockstein/`), the two
"big" backlog lines (Klein/Ramanujan, twistor gerbe) are **clearer**, and the clarification is
that they are **not two more mountains — they are two more views of the one wall already mapped**
(the positivity / F₂→char-0 wall that killed the Amplituhedron and BHQC lines,
`insight/amplituhedron_duality.md`). Each splits cleanly:

| line | **F₂ half** (our side) | **characteristic-0 half** (across the wall) |
|---|---|---|
| Klein / Ramanujan | **DONE** — steps 1–3: W(5,2)→28 bitangents→q₀=[f₃]→spiral q₀→ω→nₐ, all PSL(2,7)-equivariant, lands *in* Direction D | τ-end: 24 cusps of X(7), η²⁴=Δ, mock modular. **Across the wall, no framework leverage.** Tell: the "24" never appears in the finite picture (orbits 7+7+21+28=63; theta chars 64) — it is an index fact of X(7) over ℂ, invisible to W(5,2). |
| Twistor gerbe | **= the family-A class.** The "𝔽₂-linear route" to gerbe non-vanishing IS [nₐ]≠0, already controlled by the master theorem (non-vanishing iff n≠4). *Subsumed into the main line.* | "Escape Kodaira vanishing" = the holomorphic/char-0 Penrose transform. **Across the wall.** |

**Disposition.** The F₂ halves are *harvested* (Klein) or *main-line* (twistor gerbe) — record,
don't re-open. The char-0 halves are **delegated like the Timescape line** (§A′): a recorded
coordinate, not a debt — crossing the wall is not a backlog cleanup but a *new program* (lifting
the framework off 𝔽₂ into characteristic 0 / positivity), to be opened only if deliberately chosen.
**Actionable addenda that are NOT across the wall:** items 13 (higher d_k^eff) and 14 (Φ_*⊣Φ^*
adjunction — dovetails with the forgetful/adjunction reading of Direction D), plus the A2 list.

---

- **Klein quartic / Ramanujan route** (RF item 12; Paper VIII §7, Paper IX). GL(3,𝔽₂)≅PSL(2,7)
  ↪ PSp(6,𝔽₂) via hyperbolic doubling, carrying the Fano plane as isotropic subgeometry of
  W(5,𝔽₂). Chain: W(5,𝔽₂) → PSp(6,𝔽₂) ⊃ PSL(2,7)=Aut(X(7)) → Klein quartic → mock modular
  forms / Ramanujan τ. The "(數學上)很有趣" one. What's needed: the 3-qubit PM-like config
  whose [f₃]∈H¹ is GL(3,𝔽₂)-stabilised; the 3-qubit transgression Φ₃; mock-modular signature.
  **STEP 1 DONE (2026-06-16, `supplementary/klein/`):** built the 168-action on W(5,2)
  (symplectic, 2-transitive on Fano, perfect ⟹ = PSL(2,7) = Aut(X(7))); orbit decomposition
  of the 63 Pauli classes = **7 (Fano) + 7 (dual) + 21 (flags) + 28 (anti-flags = the 28
  BITANGENTS of the Klein quartic, stab order 6)**. The substrate side of the bridge is
  concrete. **STEP 2 DONE (2026-06-16):** hinge tightened to a theorem — explicit
  GL(3,2)-EQUIVARIANT bijection (v↦Q_v=q0+ω(v,·)) from the 28 anti-flags to the 28 odd theta
  characteristics = 28 bitangents (verified all 168 g; stab=S₃). Embedding forced by rep
  theory (only faithful 6-dim symplectic F₂-rep of GL(3,2) is 3⊕3' = Siegel/Levi = curve's
  J[2]). So the 28-orbit IS the Klein bitangents as PSL(2,7)-sets. **STEP 3 DONE (2026-06-16):**
  theta chars (spin structures, H¹-torsor) split 1+7+7+21 (even) + 28 (odd=bitangents); the
  unique GL(3,2)-FIXED theta char = q₀=x·z = [f₃] = the framework's quadratic refinement =
  the Klein quartic's canonical PSL(2,7)-invariant spin structure. Φ₃ verified: polarization
  of q₀ = ω (Weil pairing), GL(3,2)-invariant; with Sq¹ω=na, the D-spiral q₀→ω→na is
  PSL(2,7)-equivariant, based at q₀. **KLEIN LINE MEETS DIRECTION D.** (Caveat: "H¹-level"=
  theta/spin torsor; cross-check Paper IX's exact [f₃].) τ end (24 cusps, η²⁴) = analytic reach.
  **STATUS (B0, 2026-06-19): F₂ core HARVESTED; τ-end across the wall, delegated.**
- **Twistor gerbe non-vanishing** (RF item 11; Paper VIII §4). Escape Kodaira vanishing for the
  twisted Penrose transform — derived category / ambitwistor (Mason–Skinner) / 𝔽₂-linear route.
  **STATUS (B0, 2026-06-19): the 𝔽₂-linear route = the family-A class [nₐ]≠0 (master theorem),
  subsumed into the main line; the Kodaira-escape (holomorphic) route is across the wall.**
- **Higher differentials d_k^eff for n≥3** (RF item 13; Paper VIII §3).
  **STATUS: RESOLVED 2026-06-20 (`supplementary/twistor_cp/`).** d_k^eff exists, but as the
  FAMILY-B cup-power ladder h^k↔ω^k (the Sq² ladder; Thm 2.1 = k=1, PM is family B). The
  FAMILY-A H³ class n_a=Sq¹ω is NOT faithfully realizable on CP^{2ⁿ⁻¹}: that space is
  Sq¹-acyclic (even degree, h=c₁ mod 2), so h↔ω is a ring iso but not Steenrod-natural —
  the obstruction is exactly n_a (= the integral-lift / "ω is not a Chern class" obstruction).
  ⟹ the twistor side hosts Sq² (B), blind to Sq¹ (A): the geometric face of item 24's
  orthogonality and item 23's Sq¹ wall. Obstacle audit: (1) dissolved (pentagram = config),
  (2) redirected (nerve collapses, class on Maslov–Wall S³ not Σ₀⊂CP⁷), (3) resolved
  (target = cup-power h^k=c₁^k, not Chern c_k). The geometric ladder also truncates like the
  arity ceiling: CP⁷ has room for h³..h⁷ but the data realizes only ω,ω² (cf. item 19).
- **Φ_*⊣Φ^* transgression adjunction** (RF item 14; Paper VIII §5).
  **STATUS: RESOLVED 2026-06-20 (`insight/the_adjunction.md`).** Exists in D^b — the only gap
  Paper VIII flagged was τ's adjoint, and τ = the suspension iso (S²=ΣS¹), an equivalence
  (stably Σ⊣Ω); with ι_!⊣ι^*⊣ι_* and ℓ_*⊣ℓ^! the composite Φ_*=ℓ_*τι^* has right adjoint
  Φ^*=ι_*τ⁻¹ℓ^!. The degree shift IS the adjunction, not an obstacle. It's free⊣forgetful =
  𝒬⊣ℬ (Paper V), with ℬ = the one-wall forgetful functor. EQUIVALENCE iff n=4: counit defect
  = forgotten Sq¹ data = n_a, =0 iff n=4 (master theorem) = why_the_ladder §6 (∞-Yoneda free).
  Fulfills the RF item-23 line "saturation + modulus = one adjunction." Existence ✅ rigorous;
  counit-defect=n_a rests on the_one_wall + item 23. No new computation (master theorem is it).

---

## C. Recently RESOLVED (so the map is honest)
- n≥4 cross-context anticommutation (old RF item 15) → XVIII–XXI: N_anti=10 iff n=4.
- "Why H³ and not H⁴" → XXII truncation theorem (arity ceiling; RF item 19).
- Even/odd carrier dichotomy, master rigidity theorem → XXI.
- AdS/CFT / holographic-codes bridge (insight line) → RESOLVED shape-level by computation
  (`supplementary/adscft/`, steps 1–3 [[5,1,3]]→[[8,2]]→[[11,3]]): bulk is a faithful
  W(5,2) carrying H³, but reconstruction is support/geometry-governed and blind to
  contextuality. Real correspondence (shared objects + boundary↛bulk + complementarity +
  wedge nesting), NOT an obstruction-measure identity. See `insight/adscft_holographic_codes.md`.
- Item 24 (operational meaning of H³) → ANSWERED structural-not-operational, by THREE
  orthogonality results (GK / AdS/CFT / MBQC `supplementary/mbqc/`). H³ = classifying
  coordinate + certification depth, orthogonal to every operational axis tested. The
  "framework = coordinates" thesis, earned. See `quantum_applications.md` §7.
- Item 13 (geometric d_k^eff ladder on CP^{2ⁿ⁻¹}) → RESOLVED family-B-only by computation
  (`supplementary/twistor_cp/`): cup-power ladder h^k↔ω^k is family B (Sq²); family-A n_a=Sq¹ω
  unrealizable (CP is Sq¹-acyclic), n_a = the Steenrod obstruction to the realization being
  natural. Twistor face of items 23/24. (See §B bullet for the obstacle audit.)
- Item 14 (Φ_*⊣Φ^* transgression adjunction) → RESOLVED (`insight/the_adjunction.md`): exists
  in D^b (τ=suspension), free⊣forgetful = 𝒬⊣ℬ, adjoint equivalence iff n=4 (counit defect=n_a).
  ℬ = the one-wall functor; gives the wall its left adjoint. (See §B bullet.) ⟹ the entire
  Papers VII–IX twistor backlog conceptual layer (items 13,14) is closed; only item 11's
  holomorphic end remains, across the F₂↔char-0 wall (B0).
- Item 22 (family-B resonance) → RESOLVED (`supplementary/familyB_resonance/`): NO separate
  tower; family B is family A's ω=2 floor (complete r-partite ⟹ clique number r ⟹ clique
  criterion). Q1 collapses into Q2 (item 23). See A2 row for detail.

See [[project-paper22-resonance]], directionD_bridge.md, truncation_vs_ladder.md,
RESEARCH_FRONTIER.md.

=== 2026-06-21 — item 21 positive route (the Steenrod-module attack), from the 23 discussion ===
User's intuition: if Sq1 omega is the unique source, Steenrod structure should forbid arity-5 escape.
Resolved into a CONDITIONAL (the first positive line of attack item 21 has had):
  IF family-A resonance tower is generated by omega as a MODULE OVER THE STEENROD ALGEBRA A (in range)
  THEN Sq1 omega unique indecomposable lift + Sq1Sq1omega=0 => caps at H3 => no arity-5 escape.
So 23 closes the Steenrod-generated front; the ENTIRE residual = the single hypothesis
"tower is omega-generated over A" = exotics get ABSORBED (don't lift to irreducible arity-5/H4).
Concrete test object: Paper XIX's q4 (arity-4 Arf/Dickson exotic). Program: show q4 (+ siblings) is
not an independent generator climbing to H4 -- either subsumed by the omega-orbit, or dies by
c=delta a exact (Paper XXII ceiling). This reframes 21 from "enumerate/rule-out-family" (only nudges
confidence) to "prove a module-generation statement" (structural target, definite shape).
HONEST caveat (recorded in doc): this is a ROUTE not a result; absorption of q4 is unproven;
"omega-generated over A" IS the gap. Steenrod is blind to a fresh exotic generator by definition.
Wrote into RESEARCH_FRONTIER item 21 disposition as "A positive line of attack — the Steenrod-module
route". Front count: 21 went 2-front -> 1-front (the exotic front), weapon identified, front still up.

=== 2026-06-21 — propagation pass: discharge "rests on item 23" caveats (mod Kudo) ===
After 23 closed-mod-Kudo, swept the dependent items. Discipline kept: "discharge" = "rests on the
bridge, closed MODULO the cited Kudo transgression" -- NOT "fully closed".
 - item 14 (adjunction): counit defect = n_a cochain footing now in place (n_a=q-defect proven +
   =Sq1omega mod Kudo). adjoint-equiv-iff-n=4 footed mod same single citation. DISCHARGED-mod-Kudo.
 - item 19 (Z/4-Bockstein, L431): contingency "n_a is Sq1-closed = item 23" discharged mod Kudo;
   beta(n_a)=Sq1Sq1omega=0 no longer conditional on an open item. Exotic caveat (item 21) untouched.
 - item 13 (twistor): obstruction = beta omega = Sq1 omega = n_a now footed mod Kudo. Firmer.
 - item 22: collapse-pointer (Q1->Q2) now lands on resolved-mod-Kudo target. Not a real dependency
   anyway (structural pointer), just confirmed.
 - item 12 (Klein): GUARD -- does NOT ride along. tau end is char-0 (across F2 wall), not 23-dep.
   Stays "steps 1-3 done, tau end open." Explicitly flagged to prevent miscounting as closed.
Also wrote propagation summary into main status line (L533 region).
NET: board consolidated. Lone genuine open frontier = item 21 (exotic arity-5 front), with the
Steenrod-module route as its first positive line of attack (prev commit). Everything else either
resolved or resolved-mod-Kudo; item 12's char-0 tau-end and the backlog char-0 items (11,
amplituhedron) are the other genuinely-open things, all across the F2->char-0 wall.

=== 2026-06-22 — item 21 arity-5 first probe (q5 saturation) + a disposition CORRECTION ===
GROUNDING fix first: my item-21 disposition had mislabelled Paper XIX's q4 as "the arity-4 exotic
(Arf/Dickson)". WRONG. Read Paper19 def:q4: q4 is the natural Maslov/Kashiwara QUADRUPLE bit built
FROM omega (Q4=omega(x,y)+omega(x,z)+omega(y,z), [Q4!=0 on D4]), and it's SATURATED (~99.5% configs,
"no fiber info"). The genuine EXOTIC is the separate ARF invariant of the ray-span, which XIX §arf
RULES OUT as a classifier of N_anti (Arf=0 all cases, parity splits 404/103). Corrected disposition:
arity-4 absorption = (q4 omega-built & saturated) + (Arf exotic ruled out). Both handled at arity 4.

PROBE: built general arity-k Maslov bit q_k (k=4 IS q4). Compared q4 vs q5 SAME configs:
  q4 n=5: 94% inst / 80% configs-full-sat ; n=6: 100%/100%
  q5 n=5: 98% inst / 98% configs ; n=6: 100%/100%
ROBUST (same code/configs): q5 saturates >= q4 at every n => absorption pattern PERSISTS/strengthens
at arity 5. The natural omega-Maslov arity-5 invariant carries no fiber info.
SCOPING (discipline, 4th time): EVIDENCE not proof -- only the omega-generated part; exotic arity-5
(Arf-analog) escape untouched, exactly as q4-saturation left arity-4 Arf to a separate argument.
CALIBRATION CAVEAT: my q4 config-sat 80% (n=5) != XIX's 99.5%. NOT a sampling miss (nonzero F2 quad
form !=0 on >=1/4 pts, 64 samples miss ~1e-8; n=5 q4=0 are genuine Q4=0). Machinery validated by clean
n=6 100% for both. => population/stratum or definitional diff. TO RECONCILE before quoting absolute q5
figures; q5>=q4 ordering immune. Flagged in README + disposition, NOT swept.
NEXT (if continuing 21): (a) reconcile the q4 80%-vs-99.5% calibration (check gen population / proper-
ness / XIX's exact sampling); (b) the real gap = exotic arity-5 (does XIX's Arf-exclusion method
extend to 5 Lagrangians?). (b) is the hard structural core; (a) is bookkeeping.
Files: supplementary/item21_arity5/{qk_saturation.py, README.md}.

=== 2026-06-22 — (a) calibration RECONCILED: q_k machinery is exactly correct ===
Decisive test (calib_q4.py): our kernel-sampled q_k (k=4) vs XIX's EXHAUSTIVE q4_bit, SAME configs:
  agreement 64000/64000 PERFECT (identical per-instance AND per-config).
=> NO bug in our q_k. The 80-vs-99.5 gap is purely DENOMINATOR/POPULATION:
  - on our RAW proper-K5 population, BOTH methods give ~65-87% saturation (varies 65->80 by sampling
    params => population-sensitive).
  - XIX's 99% (maslov_probe.py: 202/204) is over ~204 DEDUPLICATED invariant-buckets
    (rankG, dim radW, n_odd, hg), not raw K5s. Coarser denominator.
Found the surface diff too: maslov_probe uses adj `len(Li&Lj)==2` (lags INCLUDE 0) vs nerve_cochain
`==1` (lags exclude 0) -- same "share one ray", just 0-in-set convention. Not the cause.
NET: machinery validated exactly against XIX. The q5>=q4 ordering (prev probe) stands on validated
code; both ->100% at n=6. Absolute saturation is population/metric-dependent (so don't quote a single
"q5 saturation %"; quote the ordering + n=6 100%).
(a) DONE. Next = (b) the real gap: does XIX's Arf-exclusion extend to an arity-5 exotic? = the
genuine item-21 hard core (handover-doc territory).
Files: supplementary/item21_arity5/calib_q4.py.

=== 2026-06-22 — (b) attack plan written: item21 ATTACK_PLAN.md ===
Wrote the handover for the lone hard core (exotic non-omega arity-5 invariant). Grounded in XIX's
ACTUAL Arf-exclusion (read papers/Paper19 sec:arf):
 - P1: frame-q (q(p,x)=p.x) NOT Sp-invariant (transvection changes q by omega(v,u)q(u), fixes N_anti).
   Lifts verbatim to arity 5.
 - P2: intrinsic-q skeleton (lem:skeleton): rays r_i, Gram G=M Omega M^T, relation space R={a:sum a_i
   r_i=0} dim2, o(a)=sum_{i<j}a_i a_j G_ij quad w/ polarization G, ell=o|ker G linear. intrinsic-q
   exists iff ell|_R=0; N_anti=o(1). Punchline: Arf(Q|W)=0 ALWAYS yet parity splits 404/103 -> Arf
   blind to fiber.
Arity-5 lives at K6/H4: 6 Lagrangians, 15 rays, ray-span W6, Gram G6 (15x15), nerve dDelta^5=S^4.
arity-a = (a-1)-cochain resonates K_{a+1}/H^{a-1}: arity-5 = 4-cochain -> K6/H4.
PROGRAM milestones: M1 c5 exactness <c5,[K6]>=0 (direct H4-analog of <n_a,[K5]>=N_anti; TRACTABLE NOW)
-> M2 K6 skeleton -> M3 frame-q (cheap) -> M4 intrinsic exotic at K6 (computational crux) -> M5
FFT/generation theorem for Sp(2n,F2) on Lagrangian tuples (=actual item21, paper-scale XXIII).
Obstacles O1-O4 (built-from-omega doesn't bound arity; subspaces not vectors no Weyl FFT; char2
exotica in unclassified ring; all-n). Scoping discipline section included (bounded search=evidence;
population-dependent rates; n>=5).
M1-M4 = evidence/scaffold; only M5 closes 21. M1 is the natural next computational step if continuing.
Files: supplementary/item21_arity5/ATTACK_PLAN.md (+ pointer in FRONTIER item 21).

=== 2026-06-22 — M1 grounding catch: M1 is ALREADY a Paper XXII theorem (not open) ===
"M1 看看" -> read Paper22 sec:trunc. M1 (natural arity-5 cochain exact, <c,[K6]>=0) IS Paper XXII
Theorem thm:trunc: c_m = N_anti(face m) = (delta a)_m, so c=delta a, [c]=0 in H^4. PROVEN via the
4-INDEX PARTITION argument (each cross-context pair {v_ij,v_kl} uses exactly 4 indices -> unique
4-subset T -> N_anti(face m)=sum_{T subset face m} a_T). Verified k6_truncation.py: sum_m c_m == 0
(200/200 at n=4,5,6); c_m realize all 32 even-weight patterns (sub-classes live, top dead).
=> My attack plan MISLABELLED M1 as "open, tractable, do first". SECOND grounding error in item-21
work (1st was q4-as-exotic). Pattern: I built the disposition/plan on paraphrases, not the papers.
LESSON (reinforce): ground in the actual paper/script BEFORE writing plan milestones.

VALUE EXTRACTED (the one useful thing): the partition proof works because & only because the datum
is built from 4-INDEX omega-pairings (intrinsically a 3-cochain). So:
  - M1 closes EVERY 4-index-decomposable (= omega-generated) arity-5 cochain. Sharp.
  - M4's opening is EXACTLY a non-4-index-decomposable (exotic) arity-5 invariant -> escapes the
    partition argument -> could be a genuine 4-cochain. Crisp M1/M4 boundary now stated.
q5-saturation probe = value-level shadow of thm:trunc (consistent, not new).
Corrected: ATTACK_PLAN (M1=DONE/XXII, §2, §5, §7, M1/M4 boundary), FRONTIER disposition.
Net: real open frontier confirmed = M4/M5 (exotic), M1-M3 are done/scaffold. No new compute done
(M1 was already verified by XXII; re-running it would be redundant).

=== 2026-06-22 — cross-check pass on the whole item-21 ladder (after M1 turned out done) ===
Applied the lesson (ground every milestone vs sources before labeling open). Result: 3 of 5 already
settled.
 - M1 DONE: Paper XXII thm:trunc (prev entry).
 - M3 DONE-IN-SPIRIT: XIX Prop frameq. Proof uses ONLY "transvection fixes Gram (=> N_anti & every
   omega-invariant fixed) but shifts q by omega(v,u)q(u)" -> ARITY/DIM-AGNOSTIC, lifts verbatim to
   15 rays. No new content; coordinate Arf-type arity-5 killed by same prop.
 - M2 OPEN (confirmed): grep XIX/XXII + all scripts -> NO K6 Gram/relation-skeleton. lem:skeleton is
   K5/10-ray only. Genuinely new scaffold.
 - M4 OPEN (confirmed): NO K6 intrinsic-q/Arf anywhere; all such machinery K5-only. The crux.
 - M5 OPEN: the FFT/generation theorem.
So omega-generated front (M1+M3) entirely settled; real open = M2 (scaffold) + M4 (crux) + M5 (thm).
Pattern note: the plan over-labelled M1 AND M3 as open -> it was written ~1 abstraction level above
the papers. Lesson reinforced & now APPLIED proactively (this cross-check) rather than discovered
mid-build. Cost of grounding paid up-front = cheap; cost paid mid-computation = a wasted loop.
Updated ATTACK_PLAN (§5 M2/M3/M4, §7 grounded-ladder status + M1/M2/M3 rows) + FRONTIER disposition
(grounded ladder). No new compute (M1,M3 already established; M2 is the first new step when resumed).

=== 2026-06-22 — M2 DONE: K6 skeleton (k6_skeleton.py) ===
Extended XIX lem:skeleton (K5/10-ray) to K6/15-ray. Sampled 150/150/120 proper K6 at n=4/5/6.
RESULT 1 (the headline): generic K6 stratum = (2n,2n,0) -- 15 rays SPAN THE FULL F_2^{2n},
Gram NONDEGENERATE, rad W6 = 0. n=4: (8,8,0) 150/150; n=5: (10,10,0) 140/150 + (9,8,1) rare;
n=6: (12,12,0) 97/120 + (11,10,1)/(10,8,2) rare. STRUCTURALLY DIFFERENT from XIX K5 (8,6,2)
(degenerate, rad=2). More rays (15 vs 10) => full span. Once spanning, (2n,2n,0) forced (omega
nondegenerate on V).
RESULT 2: all structural facts hold 100% (R6<=kerG6, o6|kerG6 linear, ker G6/R6 ~ rad W6 via dim
identity, coisotropy). Generic rad=0 => kerG6 = R6, ell6 = o6|R6.
RESULT 3 (M4 hand-off, the important bit): intrinsic-q exists (o6|R6==0): 0/150 (n=4!), 60/150 (n=5,
40%), 37/120 (n=6, 31%). n=4 NEVER => M4 branch (b) [no intrinsic exotic] is REAL, not hypothetical
=> P2 "exists-but-blind" template does NOT lift verbatim; n=4 needs noq_odd-style route. (n=4 anyway
settled by master thm; interesting cases n>=5 where intrinsic-q exists ~30-40%, branches (a)/(c) live.)
IMPLICATION for M4: K6 ray-span is the WHOLE space (no radical), so "intrinsic-q vanishing on rays"
is a TIGHTER condition than at K5 (quad refinement of full omega vanishing on 15 spanning vectors),
and genuinely fails ~60-70% at n>=5. M4 must branch on existence; do NOT assume arity-4 replay.
Scoping: "generic" = empirical (150 configs), not proven-for-all.
Ladder now: M1 done, M2 done, M3 done-in-spirit; OPEN = M4 (crux) + M5 (theorem).
Files: k6_skeleton.py, M2_skeleton_README.md.

=== 2026-06-22 — LITERATURE CHECK (user's instinct): item 21 subfield EXISTS over R,C ===
User: "did we check the literature on Sp(2n,F2)-invariants of Lagrangian tuples?" -> NO, we hadn't.
WebSearch + fetched 2 papers. Findings:
 - Conley-Ovsienko 1812.04271 "Lagrangian configurations and symplectic cross-ratios" (2018-20): THE
   closest. Sp(2n,K)-invariants of Lagrangian configs: continuous CROSS-RATIOS + discrete SIGNS,
   GENERATION theorem, moduli dim n(N-2n-1), first modulus N=2n+2. K=R,C ONLY.
 - MWZ math/9807061 "Symplectic multiple flag varieties of finite type": <=3 Lagrangians finite type,
   >=4 infinite type (modulus). Reduces Sp to GL/quivers (same Sp-orbit iff same GL-orbit).
 - Carlisle-Kropholler/Quillen: ambient modular invariant ring Sp(2n,F2) on vectors (Dickson-type).
CRUX: cross-ratio = ratio of omega-values; over F2 omega in {0,1} => cross-ratio collapses to 1 =>
CONTINUOUS MODULUS DEGENERATES over F2 -> content moves to DISCRETE/cohomological (n_a=Sq1omega, H3,
exotic arity-5). So n/ framework = the CHARACTERISTIC-2 SHADOW of Conley-Ovsienko. Genuinely novel
(char-2 not done by C-O/MWZ) but we've been RE-DERIVING their dictionaries (cross-ratio<->modulus,
Maslov<->sign). Must cite C-O + MWZ going forward.
RECAST item 21 M5: not "invent invariant theory" but "char-2-reduce Conley-Ovsienko" (get their
cross-ratio relations, reduce mod 2, find surviving discrete/exotic residue). Plausibly MORE tractable.
M4 exotic = char-2 residue of the C-O continuous cross-ratio modulus.
LESSON (extends the grounding habit OUTWARD): ground in EXTERNAL literature before grinding a
"new" theorem, not just internal papers. User caught this; should be default for any "is X open" Q.
Wrote: LITERATURE.md, memory reference_item21_priorart.md, updated ATTACK_PLAN (M5 recast) + FRONTIER.
Next concrete: fetch C-O's explicit cross-ratio Pfaffian relations, reduce mod 2.

=== 2026-06-22 — reduce C-O mod 2: ATTEMPTED, shortcut RULED OUT (tempers prev turn) ===
Did the concrete "reduce C-O cross-ratio relations mod 2" (co_reduce.py). Both naive reductions fail
to give the framework's obstruction:
 1. Cross-ratio relation -> TAUTOLOGY. Cross-ratio = ratio of omega in {0,1} -> 1 over F2; hexagon
    relation 1/c0+1/c1+1/c2=1 -> 1+1+1=1 (3=1 mod 2). Vacuous. (by hand)
 2. Pfaffian (polynomial form C-O cite) -> COARSE STRATUM INDICATOR. Pf(ray-Gram) mod2 = [rank G=10].
    n=4: 0 always (dimension-forced, 10 rays can't be nondeg in 2n=8). n=5: ~21% ones, n=6: ~17%.
    rank distribution n=5: {6:1662,8:2951,10:1290,...} (population-dependent, doesn't match XIX's
    (8,6,2) focus -- consistent w/ calib_q4 population sensitivity). It's a stratum indicator, NOT the
    H3 obstruction, and != N_anti (Pf sums perfect MATCHINGS; N_anti sums PAIRS).
 Only C-O's discrete SIGN reduces to the Maslov bit mu (bottom rung).
CONCLUSION: H3/exotic content is ORTHOGONAL to C-O's invariants, not a reduction. So "M5 = reduce C-O,
more tractable" (prev turn) was TOO OPTIMISTIC -- corrected. C-O gives template + mu-dictionary but NOT
the obstruction. M4 route (intrinsic exotic at K6) STANDS as the genuine path; reduction shortcut ruled
out. Same discipline: don't overclaim what a connection gives; verify by attempting it.
This is a clarifying (not purely negative) result: confirms item 21's char-2 content is genuinely
beyond the known R,C theory, so M4 is necessary, not bypassable.
Updated: LITERATURE.md (reduction-attempted section), ATTACK_PLAN (M5 tempered), FRONTIER (prior-art
para tempered), memory reference_item21_priorart (tempered). co_reduce.py added.

=== 2026-06-22 — collaborator cleanup: two un-tempered spots fixed ===
1. M1 entry: "each cross-context pair lies in a unique 4-subset" read like K5 GEOMETRIC/facet
   language, risking the misread that K5 intuition was assumed for K6 (esp. after M2 found K6 stratum
   (2n,2n,0) != K5 (8,6,2)). Checked XXII thm:trunc proof: it IS pure cochain-level — a is a 3-cochain
   because omega(v_ij,v_kl) is INDEXED by the 4-subset {i,j,k,l}; c=delta a on dDelta^N by simplicial
   coboundary, exact since [S^{N-2}] is a cycle. STRATUM-AGNOSTIC; M2's geometry discovery irrelevant
   to M1. Restated at cochain level (§2, §5, §7, FRONTIER) + explicit "M2's (2n,2n,0)!=(8,6,2) does
   not bear on M1". (Collaborator option (b): the proof is already general, so fix the misleading
   facet-language, don't add a re-derive caveat.)
2. §7 M5 row STILL said "plausibly more tractable than feared" + "recast as char-2 reduction" —
   contradicted co_reduce.py. Fixed to: reduction shortcut known NOT to work; M5 difficulty as
   originally estimated; C-O = dictionary for the bottom rung (mu) only, not a route to the exotic.
Lesson: when tempering a claim, grep ALL its propagation sites (I'd missed §7 M5 and the §2/§7/FRONTIER
facet-language). Same as the scoping-propagation discipline.

## M4 DONE for the Arf/P2 candidate (2026-06-23, m4_intrinsic.py)

Built the intrinsic exotic Q6 at K6 (unique quadratic refinement of omega on W6 vanishing on the 15
rays) + its Arf, tested vs the H^4 fiber (c_m=N_anti(face m), M=N_anti(all 6)). The script was DESIGNED
to distinguish (a)/(b)/(c), not to confirm (a). What happened:
  n=4: (b) Q6 does not exist (existence 0%, matches M2). [n=4 settled anyway]
  n=5: (a) Arf identically 0 (constant) -- the XIX K5 "blind" pattern. Rich-signature corroboration
       non-vacuous (2 non-singleton buckets, 0 splits).
  n=6: Arf VARIES {0:39,1:4}. Coarse (c,M) gave a (c)-FLAG (3 split buckets). O1 stress-test (15 four-
       + 6 five-subset N_anti's) collapsed splits to 0 -- BUT rich sig is INJECTIVE at n=6 (all
       singletons) => that statistic is VACUOUS. The decisive argument is STRUCTURAL: Arf is the
       Dickson polynomial in the ray-Gram entries omega(r_ij,r_kl), each <=4-index => Arf in
       F2[arity-<=4 invariants] => REDUCIBLE. Validated basis-independence 0/43 mismatches => the
       n=6 non-constancy is REAL (intrinsic), not a basis artifact.

KEY DISCOVERY: absorption mechanism SHIFTS with n. K5/n=5 kills Arf by CONSTANCY (value-level);
K6/n=6 kills it by REDUCIBILITY (nonconstant polynomial in arity-<=4). The K5 "Arf=0 always" argument
does NOT lift verbatim -- n=6 needs the structural/reducibility form.

SCOPE (held): M4 absorbs ONE candidate (the natural P2 intrinsic Arf), NOT all exotica (O3 unparam).
=> evidence FOR item 21 + completes the P2 lift; does NOT close item 21. The (c) falsification branch
did not occur. M5 (uniform no-exotic FFT, genuinely char-2, no C-O shortcut) is now the LONE open front.

HONESTY NOTES for the writeup: (i) n=6 rich-bucket statistic is vacuous (injective sample) -- foreground
the structural proof, not the bucket count; (ii) the validation (0 mismatches) is what licenses calling
the n=6 variation "real" rather than dismissing it. Both stated in M4_intrinsic_README.md.

Files: m4_intrinsic.py, M4_intrinsic_README.md; ATTACK_PLAN.md (M4 -> DONE-for-Arf), RESEARCH_FRONTIER.md
line 457 updated. inner/ excluded from commit per constraint.

## M5 partial: completeness lemma + ruled-out shortcut (2026-06-23, m5_relations.py)

CONTINUED from M4. Tried to GENERALIZE M4's structural reducibility into a full item-21 proof on the
generic stratum. Got a positive fragment + a clean negative that SHARPENS item 21.

POSITIVE -- Completeness lemma: on generic stratum (2n,2n,0), (G,R) [ray-Gram + relation space] is a
COMPLETE Sp-invariant of the 15 rays. Proof: same G+R+spanning => relabeling map r_i->r_i' is
well-defined (same R), bijective (spanning), omega-preserving (same G) => in Sp. Validated (G,R)
Sp-invariant 140/140 under random transvections. This is a ray-level FIRST FUNDAMENTAL THEOREM =
genuine partial M5.

NEGATIVE (the instructive part) -- "R is arity-<=4-generated" is FALSE. Defect dim R - dim R4
(R4 = span of 4-Lagrangian-local relations) is nonzero almost everywhere, MAXIMAL (7/7) at n=4
(6 rays in 8 dims generically independent => R4=0, dim R=7, all relations global).

KEY LESSON (n=4 CONTROL): n=4 is SETTLED (no H^4) yet has a fully-global R. So global relations =
arity-5 invariants EXIST even where H^4 is provably 0 => arity-irreducibility is NOT equivalent to
item 21. The literal ATTACK_PLAN-§1 reading ("every invariant is a polynomial in arity-<=4
invariants") is TOO STRONG / false at n=4. Item 21 is COHOMOLOGICAL: the 4-cochain is EXACT (M1/M4),
not "no arity-5 invariant exists." Corrected §1 of ATTACK_PLAN.

DISCIPLINE BANKED: n=4 is now the control for any "item 21 <=> X" claim. If X also holds at n=4
(where 21 holds), X cannot be the deciding content. (Same spirit as: a bounded-search failure != a
nonexistence proof; here a structural equivalence is killed by the control case.)

This is the SECOND ruled-out shortcut for M5 (first was co_reduce.py / C-O reduction). M5's open core
stays paper-scale: 2nd FFT (relations among (G,R)), descent ray->Lagrangian invariants, cohomological
truncation. I almost over-claimed "item 21 proven on generic stratum" before the n=4 control caught it
-- glad I ran n=4 as a control rather than only n=5,6.

Files: m5_relations.py, M5_relations_README.md; ATTACK_PLAN.md §1 corrected + §5/§7 + Files;
RESEARCH_FRONTIER.md new paragraph after line 459. inner/ excluded from commit.

## Abstract-H^4 route RULED OUT by n=4 control (2026-06-23, h4_cohomology.py)

CONTINUED "go" -> tried the most ambitious M5 step: compute item 21's answer as H^4 of the abstract
Sp-invariant cochain complex (C^k = functions on (k+1)-Lagrangian (G,R)-orbits; delta = simplicial
coboundary). Completeness lemma + WITT (extends to all strata, removes M4's generic restriction) makes
C^k basis = (G,R) fingerprints, canonicalized over vertex perms. Built delta^3, delta^4, computed
H^4 = |C^4| - rank d4 - rank d3.

VALIDATION delta^2=0 PASSED (machinery sound). But n=4 CONTROL FAILED: abstract H^4 = 2-0-1 = 1, while
master theorem => no H^4 obstruction at n=4. Hand-verified (no arithmetic bug). => WRONG MODEL.

WHY: the abstract complex OVER-COUNTS. The spurious n=4 class is the invariant "is this K5 in orbit #1"
-- a COCYCLE (pairs to 0 on every K6 nerve since delta^4=0) => zero per-config obstruction => no
contextuality content, yet not a coboundary => counted by abstract H^4. The alt reading rank(delta^4)
over-counts the OTHER way: at n=5, ~135 K5-orbits => a K6's 6 faces generically all-distinct =>
orbit-INDICATOR pairs to 1 => spurious "obstruction" that would absurdly falsify item 21 at all n>=5.

CONCLUSION: item 21 is NOT "H^4 of the invariant complex = 0". It is the exactness of the SPECIFIC
natural anticommutation-type arity-5 datum (generalization of N_anti = Sq^1 omega). That's why M1
(N_anti) and M4 (Arf) test NAMED candidates -- the abstract complex is too loose.

PATTERN THIS SESSION: the n=4 control has now ruled out THREE ambitious shortcuts/models:
  1. co_reduce.py    -- char-2-reduce C-O (cross-ratio vacuous, Pfaffian coarse).
  2. m5_relations.py -- "R arity-<=4-generated" (defect 7/7 at n=4, yet n=4 settled).
  3. h4_cohomology.py-- abstract-complex H^4 (=1 at n=4, over-counts).
Discipline that worked every time: RUN n=4 AS A CONTROL. If the proposed reduction/model gives the
wrong answer at n=4 (where item 21 is settled), it's the wrong reduction/model. Bank this hard.

So M5's genuinely-open core is robustly paper-scale and is about SPECIFIC data, not abstract cohomology
or arity-reduction. The positive assets stand: completeness lemma (ray-level FFT), M1 (N_anti exact),
M4 (Arf reducible). Next genuine progress on M5 = the invariant-theoretic 2nd FFT + the specific-datum
truncation, which is insight-bound (XXIII), not another script.

Files: h4_cohomology.py (kept as documented negative/signpost); M5_relations_README.md (3rd-route
section added); ATTACK_PLAN.md (§5 M5 + Files); RESEARCH_FRONTIER.md (M5-partial paragraph extended).
inner/ excluded.

## Descent gap verified: rays determine Lagrangians EXACTLY at n=4 (2026-06-23, descent_gap.py)

CONTINUED. Instead of a 4th speculative script, VERIFIED a load-bearing assertion I'd made in passing:
that the completeness lemma is ray-level and the rays may not determine the Lagrangians at n=6.

Math: r_{ij} in L_i cap L_j; L_i gets N-1=5 isotropic rays; K_i=span{r_{ij}:j} pins L_i iff dim K_i=n;
#Lagrangians containing K_i = prod_{t=1}^{n-dimK_i}(2^t+1).

RESULT (corrected my own over-optimistic prediction of a clean "n<=5 faithful" threshold):
  n=4: dim K_i = 4 = n ALWAYS (1200/1200) -> rays determine the Lagrangians, every config.
  n=5: dim K_i in {3,4,5}; =5 only 556/1200 (~46%) -> rays usually DEPENDENT -> MOSTLY lossy already.
  n=6: dim K_i in {3,4,5}, NEVER 6 (0/720) -> ALWAYS lossy; multiplicity {3,15,135} confirmed.
=> ray<->Lagrangian descent is faithful EXACTLY at n=4 (the universal dimension), partial n=5, never
n>=6. Another face of "n=4 is special" (faithful self-/ray-description only at n=4).

CONSEQUENCE: the ray-level completeness lemma (FFT) is STRICTLY WEAKER than a Lagrangian-tuple FFT for
n>=5. BUT item 21's obstruction is RAY-LEVEL (omega/anticommutation/n_a), so item 21 is properly a
ray-level statement; Lagrangian-invariants-beyond-rays don't enter the H^4 obstruction. Sharpens M5's
descent step; no escape opened.

DISCIPLINE NOTE: good that I VERIFIED rather than asserted -- my "n<=5 faithful" prediction was wrong
(n=5 is mostly lossy). Verify load-bearing claims; report the correction.

Files: descent_gap.py; M5_relations_README.md (descent section); ATTACK_PLAN.md (§5 descent + Files);
RESEARCH_FRONTIER.md (M5-partial paragraph extended). inner/ excluded.

## SESSION ARC (item 21, 2026-06-23) -- where we are
DONE this session: M4 (Arf absorbed, constant->reducible mechanism shift); M5-partial completeness
lemma (ray-level FFT); descent gap (faithful exactly at n=4). RULED OUT (n=4 control x3): C-O reduction,
arity-<=4-generation of R, abstract-complex H^4. NET: M5's open core = 2nd FFT + specific-datum
cohomological truncation, RAY-level, genuinely insight-bound (XXIII), NOT script-reachable. The
computational phase of item 21 is essentially complete; next genuine progress is invariant-theory/paper
work. Positives banked: completeness lemma, M1 (N_anti exact), M4 (Arf reducible), descent=n=4-only.

## M4 CORRECTED -- collaborator caught a value->cochain leap (2026-06-23, m4_cochain.py)

The 小夥伴 caught that M4's n=6 conclusion "Arf is a Dickson polynomial in arity-<=4 Gram entries =>
no H^4 escape" is exactly the value-level -> cochain-level leap that §1's n=4 control DISPROVED
(value-reducibility != cochain-exactness). Correct. Investigating exposed a SECOND error.

ERRORS:
1. WRONG OBJECT/ARITY. M4 computed Arf(Q6) = Arf of the whole 6-Lagrangian config = ARITY-6 (5-cochain
   -> H^5/K7). The item-21 object is the ARITY-5 Arf(Q5) of each 5-Lagrangian FACE, assembled over K6's
   6 facets. The "n=6 non-constant {0:39,1:4} mechanism shift" was an ARITY-6 RED HERRING.
2. VALUE->COCHAIN LEAP. "reducible => exact" was never valid (n=4 control).

CORRECTED (m4_cochain.py, validated: arf() unit-tested PASS; Arf basis-independent 0 mismatches; n=5
reproduces XIX's "Arf=0 essentially always" 533/534 -- KEY: Paper XIX is the n>=5 program, so its
intrinsic-q/Arf results are at n>=5 NOT n=4, which resolves the apparent n=4 disagreement):
  - n=4: intrinsic Q5 NEVER exists (0/2400; dimW=8 spans, consistency fails) -> no Arf cochain (vacuous).
  - n>=5: Arf(Q5) defined ~88-93% faces, ESSENTIALLY ALWAYS 0 (value-level ~const, XIX-consistent),
    rare 1's. Sum_m Arf(face m) mostly 0, sporadic 1's <=> ODD # of faces hit rare Arf=1 -- sporadic
    rare events, NOT a structured H^4 class => NO escape. AND Arf(Q5) is PARTIAL (undefined where Q5
    doesn't exist) => not a total arity-5 cochain => H^4 pairing ill-posed for this candidate.

CORRECTED M4 STATUS: value-level absorbed (Arf(Q5)~0, no H^4 escape), but cochain-level closure NOT
established (partial candidate; "reducibility=>exact" retracted; "constant->reducible mechanism shift"
retracted -- was arity-6). Item 21 (M5) unchanged, open. NO escape (the Sum=1 are sporadic + on a
conditioned partial function, not a class).

DISCIPLINE: this is the 4th time scrutiny/control caught an overclaim this session. The collaborator's
catch was exactly right ("這句結論嚴格來說還沒被現有證據撐住"). Pattern: I keep reaching for cochain-level
conclusions from value-level computations. The ONLY valid cochain-level evidence is a DIRECT Sum=0 test
or explicit delta-witness (M1's standard). For a PARTIAL candidate, even that is ill-posed.

OPEN micro-question (low priority, do NOT chase as escape): the rare Arf(Q5)=1 at n>=5 (1/534) -- bug
or genuine? Basis-independent, so not a basis artifact; either a genuine rare n>=5 value (XIX's "always
0" may be n=4-substratum-specific) or a degenerate-Arf edge case. Either way it's sporadic, forms no
class -> no escape. Not worth chasing unless someone wants the exact XIX cross-check.

Docs fixed: m4_cochain.py (new); M4_intrinsic_README.md (CORRECTION banner); ATTACK_PLAN.md (§0, §0
orientation, §4 item4, §7 ladder+M4+Files); RESEARCH_FRONTIER.md (line 457). inner/ excluded.

## M5 structural reduction: exotic lives in rad(omega|_W) = XIX's modulus (2026-06-23, kerG_reduction.py)

"繼續推 item 21". Pushed M5's core with firewall discipline (value-level vs cochain-level tagged).

VERIFIED (value-level, 1100/1100): R subset ker(G) always; ker(G)/R ~ rad(omega|_W); so
R=ker(G) <=> rad=0. Linear-algebra reason: rays as rows M, G=M Omega M^T, R=leftnull(M); a in R =>
a^T G=0 => R subset ker G.

CONSEQUENCE: on the NONDEGENERATE stratum, R=ker(G) is recovered from G => every arity-5 invariant is
a function of the omega-Gram ALONE (omega-generated). Nondeg fraction: 100% at n=4 (CONTROL passes!),
but only ~21%/17% at n=5/6. So the BULK at n>=5 is degenerate, where the extra-omega datum is exactly
rad(omega|_W) = PAPER XIX's MODULUS ORDER PARAMETER.

So item 21 splits into two cases:
 (1) omega-Gram-functions (nondeg; all of n=4; ~20% at n>=5) -> XXII's resonance domain. Sketch toward
     no-H^4: single atom = <=3-cochain; sum-over-4-subsets = exact (M1); product = degree>=6 (wrong
     degree on S^4). NOT PROVEN (the omega-ring FFT is the gap). [CONJECTURAL cochain-level]
 (2) radical/modulus data (degen bulk, n>=5) = XIX's modulus. Natural exotic = Arf, which corrected M4
     (m4_cochain.py) finds ~0 (value-level, no escape). Full closure needs the radical-data FFT.

NET (value-level, verified): item 21's n>=5 core = "does XIX's radical modulus climb H^3 -> H^4?" =
XXII's ceiling applied to the radical datum. Bottom case (anticommutation) proven by XXII; natural
radical-exotic (Arf) ~0 by M4. So item 21 is now CONNECTED to the XIX(modulus)/XXII(ceiling) machinery
rather than an unparametrized search -- a real localization. Does NOT close item 21 (two FFT gaps,
both cochain-level/insight-bound).

FIREWALLS HELD: n=4 control = 100% nondeg (as expected, ties to n=4-settled); reduction stated
value-level (verified) with every "=> no H^4" flagged cochain-level/conjectural. This is the cleanest
forward step yet -- it doesn't overclaim, and it ties the open core to existing proven machinery.

Files: kerG_reduction.py, M5_kerG_reduction_README.md; ATTACK_PLAN.md (§5 M5 + Files); FRONTIER (M5
para). inner/ excluded.

## SELF-CAUGHT over-reach in the kerG reduction (2026-06-23, same day)

Right after committing b9a9d0c (kerG reduction), ran my own firewall over it before building further --
and caught an over-reach I'd just committed. GOOD (this is the discipline working pre-emptively, not
waiting for 小夥伴).

THE CRACK: I'd framed the reduction as "item 21 splits into (1) nondeg = ω-Gram-functions => XXII
resonance handles it, and (2) radical = XIX modulus." Case (1) is WRONG/vacuous:
 - On the nondeg stratum the orbit IS G (R=ker G), so {functions of G} = {ALL Sp-invariants}, which
   INCLUDES the orbit-indicators that give Sigma=1 (the h4_cohomology over-counting). So "ω-generated"
   is vacuous as a constraint -- does NOT invoke XXII, does NOT exclude indicators.
 - The "product of atoms => degree>=6 cochain" sub-sketch conflated POLYNOMIAL degree (in Gram entries)
   with COCHAIN degree (on the nerve). F(face) is just a number, not a cup product. Loose/wrong.

WHAT SURVIVES [SOLID]: R=ker(G) <=> rad=0 (verified); the ONLY datum beyond the ω-Gram at n>=5 is the
radical rad(ω|_W) = XIX's modulus. That localization is correct and valuable. The reduction does NOT
dispatch either stratum (over-counting + natural-data delimitation untouched) and does NOT close item
21. Corrected README (self-correction section), ATTACK_PLAN §5, FRONTIER.

META: this is the 5th firewall catch this session, and the 1st on my OWN fresh work caught BEFORE the
collaborator. The trap I keep hitting: treating "function of G / ω-generated" as if it were a constraint,
when on the relevant stratum it's everything. The h4_cohomology lesson (functions-of-orbit over-counts)
must be applied to ANY "X is generated by Y" claim: check whether {functions of Y} is actually a proper
subclass or secretly everything. Banked.

NET STATE OF ITEM 21 (unchanged by the correction, just honest): localized to "does XIX's radical
modulus climb H^3->H^4" (= XXII ceiling on the radical), with bottom case proven (XXII) + Arf~0 (M4).
The FFT/natural-data delimitation is the insight-bound crux on BOTH strata. No computational scan
settles it (over-counting). M5 remains paper-scale.

## (a) Paper-math: proof skeleton assembled + Lemma B refuted (2026-06-23, ITEM21_PROOF_SKELETON.md)

User OK'd attempting (a) (not one-shot; will call stop). Switched to paper-math mode (prose/proof,
firewall-tagged). Assembled a STRUCTURAL ARGUMENT for item 21, splitting by the omega/radical dichotomy:

STEP 0 [VERIFIED]: data splits -- omega-Gram G (arity-<=4) + radical rad(omega|_W)=XIX modulus (extra,
n>=5). (kerG_reduction.)

STEP 1 (omega-part): reduces to Lemma A [GAP: omega-Gram invariants = cup-Steenrod subring gen by omega
= char-2 Conley-Ovsienko] + item 23 [PROVEN mod Kudo: only H^4 omega-class is omega^2=decomposable=
family B, no indecomposable H^4]. KEY FIX vs earlier: the right grading is COHOMOLOGICAL degree (cup
raises degree), NOT polynomial-degree-on-nerve. This makes case (1) = item 23 (a real result), not my
earlier flawed "functions of G". omega-part is in GOOD shape.

STEP 2 (radical part): the hard core. Conjectured Lemma B [Arf is the complete non-omega radical
invariant, i.e. (G,Arf) complete on degen strata]. TESTED IT (lemmaB_test.py) -> REFUTED: 15/56
collisions at n=5/6 (distinct orbits share (canon-G, Arf) but differ in R). Reason: Arf~0 (M4) is
nearly constant, can't separate the radical freedom = position of R in ker(G) = XIX's modulus. So the
radical carries MODULUS INVARIANTS BEYOND ARF. M4 closes only the Arf sliver.

CORRECTED TARGET: item 21 = Lemma A + item 23 (omega, good shape) + radical/modulus FFT (classify XIX's
modulus invariants -- only partially done in XIX) + no-climb theorem for them (XXII ceiling for ALL
modulus invariants; n_a done by XXII, Arf~0 by M4, rest OPEN).

FIREWALL WORKED AGAIN (6th catch): tested the load-bearing Lemma B, it FAILED, corrected the skeleton.
The radical part is LARGER than "just Arf" -- this is the honest hard core. Good that I tested rather
than asserted Lemma B.

VALUE OF (a): replaced unparametrized O3 search with a structured target -- the omega-part nearly
closed (mod Lemma A + Kudo), the radical part pinned to XIX's modulus FFT. This is real paper-math
progress even though it didn't close item 21 (and won't one-shot). The genuine remaining theorem:
char-2 generation theorem for the modulus + its ceiling.

Files: ITEM21_PROOF_SKELETON.md (new, the deliverable), lemmaB_test.py (new); FRONTIER + ATTACK_PLAN
updated. inner/ excluded.

## Modulus FFT pushed; reached over-counting wall from inside (2026-06-23, modulus_fine/climb.py)

User: "push on into the modulus FFT." Did two steps.

STEP 1 (modulus_fine.py): IDENTIFY the fine modulus generator beyond (G, Arf). Tried the WEIGHT
ENUMERATOR of R (relation space as binary code in F_2^10; S5-invariant, not a function of G). Result:
it COLLAPSES the (G,Arf) collisions 17->2 (n=5), 80->11 (n=6), and Arf is SUBSUMED ((G, wenum R) alone
= same residual; Arf~0 adds nothing). So the primary fine modulus generator is the relation-code weight
enumerator, NOT Arf. Small residual remains (>=1 more generator). Real FFT progress.

STEP 2 (modulus_climb.py): does the weight-enum generator CLIMB? A_w = (#weight-w codewords in R) mod 2,
test Sum_m A_w(face m). Got Sum != 0 for w=4..10 at n=5,6 (n=4: all 0). LOOKS like item 21 false -- but
it's the h4_cohomology OVER-COUNTING TRAP (7th catch). A_w is a NON-COBOUNDARY invariant that varies
across orbits => pairs !=0 generically (6 faces generically distinct orbits at n>=5), exactly like an
orbit-indicator. N_anti gives Sum=0 ONLY because it's an exact coboundary (delta of arity-4, M1); A_w
isn't. n=4 "control" is WEAK (delta^4=0 for ALL functions at n=4, few orbits). So NOT an escape.

KEY FINDING: even the IDENTIFIED modulus generators over-count. So the modulus no-climb theorem CANNOT
be the naive Sum_m=0 test (it flags all non-coboundaries, natural or not). No-climb needs the natural/
indecomposable-data delimitation = the insight-bound crux. The over-counting wall is reached FROM INSIDE
THE MODULUS now -- 3rd independent confirmation (after h4_cohomology and the kerG self-correction) that
closing item 21 is insight-bound, not computational.

NET (a)-push status: omega-part nearly closed (Lemma A + item 23). Radical part: primary generator =
weight enumerator (FFT progress), but no-climb is provably NOT computational (over-counting from inside).
So item 21's close is genuinely insight-bound: need (Lemma A = char-2 C-O) + (modulus FFT, partly done:
weight enumerator) + (no-climb via natural-data delimitation, which no Sum_m test can do).

I did NOT report "item 21 false" despite the climb test screaming it -- recognized the over-counting
trap (the discipline working). This is a good STOP point for the computational push: every direction
now hits the same insight-bound wall (natural-data delimitation). Further probes will re-hit it.

Files: modulus_fine.py, modulus_climb.py (new); ITEM21_PROOF_SKELETON.md (Step 2 + TODO updated);
FRONTIER. inner/ excluded.

## Lemma A payoff VERIFIED (orthogonal ring, degree 4 skipped) -- 2 self-caught errors (2026-06-23)

User: "take Lemma A, the char-2 C-O generation theorem." Worked it as paper-math + verification. Result:
Lemma A's PAYOFF is verified, after the firewall caught TWO of my own errors.

ERROR 1 (group): I assumed Lemma A is about H*(BV)^{Sp}. WRONG. The framework's omega=[c] is the
QUADRATIC FORM q (q(v)=c(v,v), item 23), which is O-invariant (orthogonal), NOT Sp-invariant (a
transvection shifts q by omega(.,v)(q(v)+1)). Verified: dim H^2(BV)^Sp = 0 (!), dim H^2(BV)^O = 1 (=q).
So n_a = Sq^1 q lives in H*(BV)^O. The relevant ring is ORTHOGONAL, not symplectic. (My initial Sp
computation gave dim H^3^Sp=0, which looked like "n_a not invariant" -- the resolution is the group is O.)

ERROR 2 (bug): fixed_space stacked the COLUMNS (images (T_v-I)(m)) instead of ROWS (equations) when
intersecting ker(T_v-I) over multiple transvections. Column-rank=row-rank only for ONE matrix, so it
broke for multiple generators. Caught by a DIRECT check: q and Sq^1 q are fixed by all O-transvections
(bad=0), contradicting the buggy dim H^3^O=0. Fixed -> correct numbers.

VERIFIED RESULT (n=3,4, stable range covering n>=5; n=2 is small outlier): dim H^4(BV)^O = 1 = <q^2>
(decomposable). Orthogonal generators at degrees 2(q), 3(Sq^1 q = n_a), 5(xi_2), ... = {2} U {1+2^i},
SKIPPING degree 4. So NO indecomposable degree-4 O-invariant => no exotic arity-5/H^4 obstruction from
the omega/q-part. The H^3 ceiling = the orthogonal degree-gap 3->5. (Next obstruction-degree is H^5 =
arity-6 at K7, beyond item 21 -- the ladder degrees are {2,3,5,9,...}.) Dovetails with Steenrod:
<q>-tower = F2[q, Sq^1 q], degree-4 part = <q^2> (item 23).

REMAINING GAP: the ambient<->config BRIDGE (genuine config obstructions = ambient O-classes = item 23's
framework extended). This ALSO resolves the over-counting: config invariants (indicators, weight
enumerators) over-count precisely because they are NOT ambient O-cohomology classes -- only the ambient
O-classes are genuine obstructions. So the natural-data delimitation = "is it an ambient O-class."

STATUS: Step 1 (omega-part) of the proof skeleton is now VERIFIED-payoff + bridge-gap -- a real
advance. Step 2 (radical/modulus) remains the harder open core. This was the most productive (a)-step:
it identified the correct ring (O), verified no-degree-4, and located the bridge as the single remaining
omega-part gap (= the natural-data delimitation, now concretely "ambient O-class or not").

8th firewall catch (group mis-targeting) + 9th (kernel bug) -- both on my own fresh work, caught by
direct checks before building on them. The discipline is the engine here.

Files: sp_invariants.py, LEMMA_A_README.md (new); ITEM21_PROOF_SKELETON.md (Step 1 + assembled +
Files), FRONTIER. inner/ excluded.

## Step 2 DISSOLVED by ambient-O-class criterion; item 21 -> Direction-D bridge (2026-06-23)

User: "push Step 2 with the ambient O-class criterion." The criterion turned out to DISSOLVE Step 2,
not just guide it.

LOGIC: Lemma A gave a concrete "natural data" criterion -- genuine arity-5/H^4 obstruction = nerve-
evaluation of an ambient O-invariant degree-4 cohomology class. The over-counting config invariants
(indicators, weight enumerators) are excluded because they're NOT ambient O-classes. Then:
  - genuine obstructions of BOTH parts (omega-Gram AND radical/modulus) are ambient O-classes;
  - dim H^4(BV)^O = 1 (VERIFIED n=3,4,5 -- pushed to n=5, item 21's smallest case, 64s), spanned by q^2;
  - q^2 is decomposable (cup-square = family B, no independent resonance, item 22) -> not a new/primary
    obstruction;
  => NO indecomposable degree-4 ambient O-class => no exotic arity-5/H^4 obstruction FROM ANY SOURCE.
The modulus FFT (Step 2's hard core) is MOOT: the climbing modulus invariants are over-counting
artifacts (not ambient O-classes), so they need not be classified.

NET: item 21 (n>=5) reduces to a SINGLE remaining gap = the Direction-D bridge (every genuine
obstruction = nerve-eval of an ambient O-class; general, all degrees; item 23 = verified degree-3
instance n_a=Sq^1 q) + the finite verified fact dim H^4^O=1. This replaces the unparametrized O3 exotic
search with a NAMED, GENERAL target (Direction D, already a paper-XXII outlook item).

This is the big payoff of the whole (a) push: item 21 is no longer "search an unparametrized space of
exotica" -- it's "establish the Direction-D characteristic-class bridge, then it follows from a finite
cohomology computation (dim H^4^O=1, done)." The bridge is hard (a real program) but it's the SAME
bridge for all degrees, and degree 3 (item 23) is already verified.

CAVEAT (firewall): the D-bridge is substantial, not a corollary. And it is somewhat close to item 21
in spirit (a "no exotic config obstruction" statement) -- BUT it's general (all degrees) and structural
(spectral sequence), so establishing it once settles the whole ladder, unlike the degree-4-specific
search. Not circular: the bridge is the structural input, the computation is the degree-4 output.

n=5 verification: dim H^2^O=1(q), H^3^O=1(Sq^1 q), H^4^O=1(q^2). Pattern stable n=3,4,5.

Files: ITEM21_PROOF_SKELETON.md (unification section + assembled), LEMMA_A_README.md (n=5 row),
sp_invariants.py (n=5 via one-off), FRONTIER. inner/ excluded.

---
## 2026-06-23 — D-bridge stated generally + transgression tower verified (DBRIDGE.md, bridge_tower.py)

"go D-bridge". Did NOT attempt the full general nerve↔H*(BH) realization (that's item-23-general,
paper-scale, "no finite reduction in hand"). Instead nailed what item 21 ACTUALLY needs, which is
lighter:

- KEY: item 21 needs the CLASSIFICATION direction (config ⟹ ambient), NOT item 23's realization
  direction (ambient ⟹ config). Item 23 = existence (built n_a from Sq¹q). Item 21 = completeness
  (no genuine obstruction escapes the ambient ring). Classification is exactly what kills the
  over-counters (they're the config cochains NOT in the ambient image).
- General form = LHS SS of extra-special extension 1→Z/2→H→V→1: E₂=H*(V)[t] (Quillen), obstructions
  = Kudo transgressions τ(t^{2^k}) = Sq^{2^{k-1}}…Sq¹q at degrees {2}∪{1+2^i}. Degree-4 gap STRUCTURAL
  (t²→3, t⁴→5, nothing→4). Arity-a ↔ deg-(a-1) at K_{a+1}.
- VERIFIED n=2,3,4 (bridge_tower.py): generators ARE the tower, not just dim-matched, THROUGH deg 5.
  T1 q,Sq¹q,Sq²Sq¹q all O-invariant; T2 Sq²q=q² (decomp), Sq¹Sq¹q=0 (Adem) — no deg-4 rung; T3
  Sq²Sq¹q indecomposable + {q·Sq¹q, Sq²Sq¹q} span dim-2 deg-5 O-space.
- The one NEW piece = a [REFRAME] (definitional, justified): genuine obstruction := class pulled from
  H*(BH) = char class of the operator structure, NOT arbitrary Sp-invariant config function. Justified
  bc contextuality is a property of the operator algebra H, not of any Lagrangian-tuple presentation.
  This dissolves over-counting AND the modulus FFT in one move.
- NET: item 21 (n≥5) holds modulo (a) cited Kudo/Quillen, (b) the reframe. Structurally LIGHTER than
  item 23 — negative statement, needs only "obstructions ≤ ambient ring" + verified decomposability of
  H⁴(BV)^O, NOT the hard construction (item 23 link B) of a deg-4 class (there is none to build).

HONEST: the reframe is a definition with justification, not a theorem. The general nerve↔H*(BH)
realization remains the cited/GAP backbone (item 23 = its deg-3 instance). What's genuinely new+solid
this session: (i) the right direction (classification not realization); (ii) the tower=generators
verification through deg 5 (not just dims); (iii) item 21 < item 23 in difficulty. These sharpen the
target; they don't close it from scratch.

Files: DBRIDGE.md (new), bridge_tower.py (new, n=2,3,4 pass), ITEM21_PROOF_SKELETON.md (+pointer),
RESEARCH_FRONTIER.md (+paragraph). inner/ excluded from commit.

---
## 2026-06-23 (cont.) — reframe GROUNDED: over-counters are phase-blind (phase_blind.py)

"continue". Interrogated the one non-theorem piece (the [REFRAME]) in firewall spirit: is excluding
the climbing over-counters principled or arbitrary? -> PRINCIPLED. They're phase-blind.

- A_w (weight enum of relation code R) is computed from R = linear dependencies of the 15 ray vectors,
  NEVER touches omega. So A_w is a function of R => GL(2n,F2)-invariant (GL preserves dependencies).
- n_a = sum omega over disjoint pairs is built from omega => Sp-invariant, NOT GL-invariant (phase).
- VERIFIED n=4,5,6 (phase_blind.py): random g in GL\Sp on a proper K6's 15 rays leaves R and A_w
  EXACTLY unchanged (0/720, 0/720, 0/480) while flipping N_anti ~50%. So A_w is constant precisely
  where contextuality varies => phase-blind => cannot witness contextuality.
- This is the operational meaning of "pulled from H*(BH)": H*(BH) = operator-phase cohomology
  (Sp/O level); GL-invariant incidence combinatorics is a strictly coarser, contextuality-blind layer.
- NET: the reframe's exclusion clause is now a STRUCTURAL fact (where each invariant's data lives),
  not a definitional choice. Main firewall worry about the reframe = closed.

Still open / honest: the reframe's POSITIVE clause (genuine = pulled from H*(BH)) at full generality
is the cited nerve<->H*(BH) realization (item 23 = deg-3 instance). phase_blind closes the EXCLUSION
side (why over-counters aren't genuine), not the inclusion side. But exclusion was the firewall worry;
inclusion is the cited backbone. Good division.

Files: phase_blind.py (new, n=4,5,6 pass), DBRIDGE.md (+grounding para, ledger row, file), FRONTIER
(+para). inner/ excluded.

---
## 2026-06-23 (cont.) — (b) attacked: item 21's negative direction needs Witt, NOT Kudo (witt_fft.py, DBRIDGE.md §4½)

"go (b)". The remaining gap (b) = every genuine obstruction comes from an ambient class. Looked like
the full nerve<->H*(BH) realization (Kudo, "no finite reduction in hand"). KEY: it SPLITS.

- (b-pos) which ambient classes are realized NONZERO = item 23, needs Kudo, = EXISTENCE.
- (b-neg) the BOUND genuine subset of ambient O-ring = item 21 NON-EXISTENCE. Kudo DROPS OUT.

(b-neg) chain:
 1. genuine => phase-derived [phase_blind, done]
 2. phase-derived => function of q/omega-Gram [POLARIZATION (elementary, all-n) + WITT FFT (classical)]
    - polarization: q(sum_S v) = sum q(v_i) + sum_{i<j} omega(v_i,v_j) => Gram determines q on whole span
      => phase data = Gram. witt_fft.py (A): 0 mismatches n=2,3,4.
    - Witt FFT: Gram+relations = complete O-invariant (Witt extension thm). witt_fft.py (B) n=2:
      |O(q)|=72, orbit <=> (Gram,relations), 0 splits. [hit + fixed the O+_4(F2) transvection-generation
      exception -- built O(q) directly, got 72 not 36.]
    - with phase_blind (relations = GL-invariant = phase-blind = not genuine): genuine O-invariants =
      functions of the Gram = ambient H*(BV)^O evaluations.
 3. resonance arity-5 <-> ambient degree-4 [Paper XXII; verified bottom mu<->omega deg2, n_a<->Sq1q deg3]
 4. H^4(BV)^O = <q^2> decomposable [verified n=3,4,5] => only genuine arity-5 = mu^2 (family B), not
    exotic. QED, NO Kudo.

Why Kudo drops out: negative dir needs only CONTAINMENT (genuine ⊆ ambient = Witt+polarization) + target
deg-4 decomposable (verified). Never needs exact transgression VALUES (Kudo) = which classes realized
nonzero = existence/(b-pos) only.

HONEST residual: the one ours-but-relied-upon step = resonance arity<->ambient-degree matching (Paper
XXII, confirmed arities 3,4 by item 23). (b-neg) uses only its containment form. So item 21 dependency
drops from "cited Kudo realization (no finite reduction)" to "Witt + polarization + resonance + verified
finite facts" = strictly firmer.

Subtlety I had to firewall: cochain-degree vs ambient(polynomial)-degree. n_a is a degree-3 cochain but
a SUM of single omega-entries (each ambient degree 2); the +1 to Sq^1omega (ambient deg 3) is the
transgression. For the COUNTING/containment (b-neg) I only need genuine arity-5 <-> ambient deg-4 +
H^4^O=<q^2> decomposable; the exact +1 transgression matching is (b-pos)/Kudo, not needed.

Files: witt_fft.py (new, n=2,3,4 polarization + n=2 Witt), DBRIDGE.md (+§4½, ledger rows, file, §5
rewrite), FRONTIER (+para). inner/ excluded.

---
## 2026-06-23 (cont.) — (b-neg) scrutinized: joint Gram-R loophole resolved; item 21 CONSOLIDATED (ITEM21_CLOSING.md)

"continue". Firewall pass on (b-neg). Found a candidate loophole + resolved it, then consolidated.

LOOPHOLE: last turn said "genuine = function of the Gram (Witt)". But the genuine obstruction could be a
JOINT Gram-R function (sum omega over pairs SELECTED by relations R) -- phase-sensitive (survives
phase_blind) yet not a pure ambient O-class. Would break the Witt step.

RESOLUTION: n_a is (item 23 link A) the polarization defect sum_{i<j} omega(v_i,v_j) over the FIXED
disjoint pairs of K6 combinatorics = fixed linear combo of omega-Gram entries = pure-Gram BY
CONSTRUCTION. An R-selected function uses config-dependent selection = NON-NATURAL cochain, excluded
(cohomology functorial; pure-R also phase-blind). Confirmed: for fixed G, ker(G) fixed but R varies
(ker G/R = rad, kerG_reduction), yet n_a (function of G) constant => R is independent extra data genuine
natural obstructions don't use.

REFINEMENT: (b-neg) needs an explicit [CONDITION]: genuine = natural functorial nerve cochain. Standard
(cohomology functorial), confirmed at bottom (n_a manifestly natural/pure-Gram), but a CONDITION not a
theorem. With the reframe it delimits "genuine."

Important self-correction note: I briefly thought the genuine obstruction was the frustration phi = Q|_R
(charges restricted to cycles, phi(a)=sum_{i in a} q(v_i) by polarization). That's the frustration of
ACTUAL relations/cycles. But n_a is NOT that -- n_a is over the fixed nerve disjoint-pairs (tetrahedra),
generically NOT relations. So n_a is pure-Gram (nerve-combinatorial), distinct from the R-cycle
frustration. The R-cycle frustration would be non-natural. Good that I didn't conflate them in the note.

CONSOLIDATED: ITEM21_CLOSING.md = capstone (like item 23 closing_note). 6-step reduction:
 0 data split (G,R), extra = rad = XIX modulus [VERIFIED]
 A genuine => phase-derived [phase_blind, VERIFIED]
 B genuine natural => pure-Gram [item 23 A + kerG; CONDITION = naturality]
 C pure-Gram => ambient O-eval [witt_fft: polarization + Witt, VERIFIED+CLASSICAL]
 D H^4(BV)^O=<q^2> decomposable [sp_invariants/bridge_tower, VERIFIED n=3,4,5]
 => no exotic. modulo residuals.
(b-pos)/(b-neg) split: Kudo only for existence (b-pos), OFF item 21's critical path.
Two residuals flagged: [CONDITION] naturality; [OURS] resonance arity<->ambient-degree (containment form).

STATUS: item 21 REDUCED not closed. From unparametrized O3 search -> "Witt+polarization+resonance+4
verified computations, modulo a naturality condition." Honest: NOT declaring proven (per memory: item 21
is a genuine open frontier; this is a reduction/skeleton).

Files: ITEM21_CLOSING.md (new), FRONTIER (+para). inner/ excluded.

---
## 2026-06-23 (cont.) — arity-5 resonance COLLAPSES into naturality (gl_invariants.py)

User: "如果是我, 會先選 arity-5 resonance." Did that. Finding: the resonance gap is NOT independent.

- Resonance step = "genuine arity-5 obstruction => degree-4 AMBIENT O-class" (degree-matching).
- Degree-matching follows from REPRESENTABILITY (Yoneda): natural, O-invariant, pointwise-cohomological
  degree-k assignment = element of H^k(BV)^O, degree-matched automatically. So it FOLLOWS from the
  naturality CONDITION (Step B), not a separate input.
- => the TWO residuals collapse to ONE: genuine = natural, pointwise-cohomological nerve cochain.

BONUS (new computation, gl_invariants.py): representability gives a 2nd independent over-counter
exclusion. A_w is GL-invariant (phase_blind). If it were a natural ambient class it'd be in H*(BV)^GL =
Dickson algebra = 0 below degree 2^{2n-1}. VERIFIED H^4(BV)^GL = 0 at n=2,3 (all of deg 1..6 = 0; lowest
Dickson 8 resp 32), vs H^4(BV)^O carrying q^2. So A_w is NOT a natural ambient class -- it's RELATIONAL
(R), not pointwise-cohomological. Over-counters now fail genuineness 2 ways: phase-blind (GL-inv) +
non-representable (relational).

HONEST: representable is slightly stronger than natural (requires pointwise-cohomological, rules out
relational R). But relational over-counters are exactly what fail H^GL=0 AND phase_blind. So the refined
single condition "genuine = natural pointwise-cohomological" is well-motivated: contextuality IS the
pointwise q-defect (n_a = item 23 link A, pointwise). NOT declaring resonance "closed" -- it's REDUCED to
the naturality condition (now the single residual). n=2 is the O-column outlier (2,2,3); n=3 stable
(1,1,1); H^GL=0 everywhere checked.

Updated ITEM21_CLOSING.md (Step D + D', residual section 2->1, ledger row D', files), FRONTIER (+para).
Files: gl_invariants.py (new, n=2,3). inner/ excluded.

---
## 2026-06-24 — last residual grounded OPERATIONALLY: contextuality = fixed-context gluing (ITEM21_CLOSING.md)

"continue". Attacked the single surviving residual (genuine = natural pointwise-cohomological cochain)
from the OPERATIONAL/physics side (value-assignment = Kochen-Specker/AvN/Abramsky-Brandenburger).

Three facts pin the condition to the DEFINITION of a contextuality scenario:
 1. Contextuality is ALWAYS cross-context: within one commuting Lagrangian a consistent lambda always
    exists (shared eigenstates) => every obstruction is a GLUING obstruction = nerve cohomology, built
    from the FIXED context structure = exactly naturality (contexts = fixed scenario data).
 2. Accidental relations R carry NO contextuality: {lambda . a = q-defect(a) : a in R} is ALWAYS solvable
    by lambda = Q (q-charge vector Q_i = q(v_i)), since q-defect(a) = sum_{i in a} q(v_i) = Q . a is LINEAR
    on R (polarization, sum v_i = 0). Operational confirmation of phase_blind + why the modulus is an
    order parameter not a witness.
 3. Gluing signs are q-defects = pointwise q (polarization) = representable = n_a (item 23 link A).

CAUGHT a modeling error en route: first thought the obstruction = within-span relation-sign system. WRONG
-- that's always solvable by lambda=Q. The obstruction is the CROSS-CONTEXT gluing. The catch sharpened
the argument (it's exactly why R carries no contextuality).

So the condition is NOT a free assumption -- it's "the framework's obstruction IS the standard
contextuality obstruction (cross-context value-assignment gluing, fixed contexts, q-defect signs)."
[GAP honest]: this is a MODELING IDENTIFICATION, well-supported, NOT proven in general here. Proving
"framework obstruction = AvN nerve-cohomology obstruction" at all arities = the paper-scale piece (=
nerve<->H*(BH) realization from the contextuality side = (b-pos)). NET: last residual lowered from "assumed
math condition" to "the definition of the contextuality scenario the framework models."

No new script (the key fact -- system solved by lambda=Q -- is algebraic, s=Q|_R linear). Conceptual
grounding resting on existing verified facts + standard contextuality framework.

Files: ITEM21_CLOSING.md (+§grounded operationally), FRONTIER (+para). inner/ excluded.

---
## 2026-06-25 — started Paper 0 (n/ whitepaper for CAID), v0.1 drafted

User confirmed: Overview = a WHITEPAPER (like Bitcoin), one of n/'s whitepapers. Purpose of the whole
series = give mathematical backing to every n/ engineering decision; the obstruction-ladder series backs
the HARDEST one: CAID (coherent self-representation). Must bridge BOTH sides: papers <-> n/ spec.

Drafted research/papers/Paper0_nlang_whitepaper.tex (v0.1, compiles clean, 4pp). Architecture (confirmed
by user): §1 spec side (CAID = engineering decision) -> §2 the dictionary/bridge (semantics->Sp(2n,F2);
contexts->Lagrangians, CAID->Yoneda self-embedding nerve->BH) -> §3 ladder (Bohr/II -> mu/XIII ->
n_a=Sq1w/IX,XX -> resonance ceiling/XXII; one bridge per degree, Kudo self-replication) -> §4 master thm
[n_a]=[dmu]=0 <=> n=4 (CAID dimensionally bounded, selects n=4) -> §5 two faces are one (discovery=realism
about observation-STRUCTURE not values; CAID=Yoneda=cohomology; bottomless reflexivity, n=4=closes at
finite degree) -> §6 honest frontier (item 21 reduced, item 23 secondary/Kudo, bridge never finitely
closes = infty-coherence not gap).

6 \userflag{...} red TODOs left for spec internals I DON'T have (firewall): exact CAID definition/expansion;
spec notion of "context"; per-rung paper attributions to verify; why-n=4 in spec terms (does spec fix 2n=8
independently?); bibliography/Zenodo DOIs + spec pointer. These are genuinely the user's to fill.

v0.1 is complete-through (not stubs) but COMPACT (4pp); expansion to ~12-15pp = flesh each rung, the
dictionary, add refs. Next: user reviews v0.1 + fills the \userflag items, esp §2 dictionary (the crux)
and the CAID definition. inner/ excluded.

---
## 2026-06-25 (cont.) — Paper 0 v0.2: rewritten against the actual spec (SPEC_13 + APP_06)

User had me READ the spec side first. Big correction + a gift:

CORRECTION (firewall): v0.1 misread CAID as "coherent self-representation = Yoneda self-embedding".
WRONG. SPEC_13 §1: CAID = Content Addressable Identifier = projection operator P_A's spectral-geometric
fingerprint (particle Digest + wave Sketch); Yoneda principle here = "object determined by its
RELATIONS" (identity-by-relation, content addressing), NOT self-representation. The self-reference face
is OODP/Ouroboros (銜尾蛇 = the discovery protocol, universe addressing itself).

THE REAL SPEC CHAIN (APP_06, didn't have before): smell-search/LADD needs phase -> EML completeness
needs C + Soler thm (orthomodular lattice + infinite orthogonal seq => field in {R,C,H}) -> choose C ->
FORCED into Hilbert space ("quantization is geometric necessity not style") -> noncommutative ->
Bohrification (observe via commutative contexts) -> P_A fingerprint = CAID. KS = no global section.

THE GIFT: APP_06 §6.5 ALREADY builds the bridge. It defines hbar_n/ = # trust-contexts to describe a
Combo, and states: resonance tower (Paper XXII) IS hbar_n/'s discrete spectrum. arity-a = (a-1)-cochain
at K_{a+1} -> H^{a-1}. Levels: H^1 (arity2 K_3 holonomy) / H^2 (arity3: A=K_4 Maslov, B=K_{3,3} Mermin) /
H^3 (arity4 K_5 pentagram Borromean); CEILING = H^3 (XXII), clique criterion min(omega-2,3). So Paper 0
§2/§3 = connect the spec's own hbar<->resonance-tower correspondence to the series' rigorous proofs, NOT
invent a bridge. Also: the spec's hbar anchor is explicitly NOT via L-S (Vattay comment; L-S is WKB not
exact) but via Bohrification + the series.

REBALANCED: spec actually uses the H^3 CEILING (XXII). n=4 master (XVIII/XXI) is the apex but spec
doesn't directly invoke it -> presented honestly as "the one open hinge" (does spec fix dimension /
2n=8?). Didn't force n=4<->spec.

Also noted: papers = char-2/Pauli SHADOW of the spec's C-Hilbert geometry (where contextuality is
combinatorially exact). Stated in §2.

v0.2: research/papers/Paper0_nlang_whitepaper.tex, compiles clean, 5pp. Title changed to "Forced
Quantization, Bohrification, and the Contextuality Ceiling". 4 \userflag left:
 1. CAID <-> (omega/q-Gram fingerprint) dictionary row = OUR reading not spec words (the one delicate
    entry) -- needs user confirm
 2. per-rung paper attributions verify
 3. the n<->spec hinge (does spec fix dimension for engineering reason?)
 4. bibliography/DOIs/spec pointers

PDF gitignored (committed .tex only). inner/ excluded.

---
## 2026-06-25 (cont.) — Paper 0 v0.3: corrected against README + integration_maps + OpenProblem3

User gave the spec-side ground truth. Key clarifications + fixes:

- My v0.1 wasn't "wrong" -- original n/ jumped between concept nodes; APP_06 is the post-papers logical
  reorder. TRUE causal chain: spectral-geometry (OpenProblem3 smell-search) -> EML -> Bohrification(+KS)
  -> Soler. Added a \remark noting "dependency not chronology"; rooted §1 Decision 2 in OpenProblem3
  (Laplacian-spectrum fingerprint, Weyl stability, Cauchy interlacing).
- spec's CAID is ONLY Paper I-VI level (integration_map.md covers I-VI). So the §2 CAID<->omega/q-Gram
  row IS my interpretation by design (spec has no VII-XII concepts). Reframed the flag: it's the VII-XXII
  EXTENSION of CAID; if adopted, update SPEC_13/REAL_03. (Not "confirm" -- it's correct to interpret.)
- inner/integration_map_VII_XXII.md was written by a PREVIOUS me (post-XXII); APP_06 §6.5 (arity=hbar
  bridge) traces to it. Used its precise VII-XXII<->spec anchors: XI beta = CAID v2 complex-spectrum
  sign/phase; XV Weil rep = Bohrification projection operators; XIX modulus = HOLOGRAPHIC principle
  (boundary arity<=4 underdetermines bulk H^3) -- added as §4 "Holographic reading".
- README numbering is the DEFINITIVE one (early integration_map.md numbering is STALE -- papers got
  reordered). Fixed §3 ladder attributions against README quick-ref: H^1=I, H^2=III(KS)/XIII(Maslov A)/
  X,XVII,XVIII(Mermin B), H^3=IV(predicted),XX(opens), master=XXI, ceiling=XXII, Bohr base=II+Epilogue,
  C-necessity=VI+Epilogue.
- Added §5 "one degree, every engineering layer" (the L_r x E_r matrix from integration_map EPI-GAP-1:
  same H^2 = type conflict L2 / compute-horizon L3 / FLP L4 / governance L5).
- Added a real bibliography (series w/ key DOIs from README, spec github branch=top, EML/Soler/
  Isham-Butterfield/L-S+Vattay). item 23 note now also flags it = the Direction-D comparison map the
  spec's H^3 entries await.

v0.3: 6pp, compiles clean (2 passes for refs). 3 \userflag left:
 1. CAID I-VI vs VII-XXII extension (update spec if adopted) -- now a documented remark, not a blocker
 2. the n<->spec hinge (does spec fix a working dimension / 2n=8?)
 3. bibliography: expand to full per-paper DOI list if desired (optional)

PDF gitignored (committed .tex only). inner/ excluded.

---
## 2026-06-25 (cont.) — Paper 0 v0.4: n=4 hinge RESOLVED (engine vs self-evolution); APP_07 + SPEC_17

User answered flag #2 (the n<->spec hinge). Resolution is clean + IS the whitepaper's thesis:

- OODP engine (CAID+LADD) does NOT fix n=4: it must recognize the WHOLE ladder. APP_07 §4 maps
  H^1=CAP, H^2=FLP, H^3=Byzantine, H^4=Sybil(ORDER_00). Engine is dimension-AGNOSTIC.
- Ouroboros self-evolution (SPEC_17 §4 = self-observational loop, n/ describing/evolving its own %rules
  via truth integral) DOES need n=4: coherent self-representation = [n_a]=0 <=> n=4. = why_the_ladder
  (infty-Yoneda free at n=4). Dimension-SELECTING.
- So hinge resolves: n=4 is NOT the engine's working dimension; it's where the spec's SELF-DESCRIPTION
  closes coherently. Identity-by-relation (CAID) spans the ladder; self-representation (Ouroboros)
  selects the dimension. This is the "Yoneda twice" point sharpened: n=4 belongs to the 2nd (reflexive)
  Yoneda.

CORRECTION I noted: APP_07 §4 ALREADY cites n=4 master theorem -- so I was wrong earlier that "spec
doesn't invoke n=4". It does (APP_07). SPEC_17 describes the self-loop but doesn't yet pin its coherence
to n=4 -> that's a spec-update opportunity (parallel to CAID I-VI/VII-XXII gap).

Also: APP_07 §6 IS the spec's holographic section (matches my §4 XIX holographic add) -> cited it.
APP_07 §5 = the L_r x E_r matrix (matches my §5 add). Both my earlier adds now have spec home.

v0.4 edits: §4 rewritten (two roles/two dimensional behaviors, engine-agnostic vs self-evolution-selects),
abstract n=4 line, §5 "Yoneda twice -> n=4 belongs to reflexive", holographic para cites APP_07 §6, bib
spec entry adds APP_07 + SPEC_17. 6pp, compiles clean.

3 \userflag left -- ALL now documented remarks / optional, NOT open questions:
 1. CAID I-VI vs VII-XXII extension (update spec if adopted)
 2. SPEC_17 should state self-evolution coherence = master theorem (spec-update note)
 3. bibliography: expand to full DOI list (optional)

The n=4 hinge (the last real open question in the draft) is RESOLVED. PDF gitignored. inner/ excluded.

---
## 2026-06-25 (cont.) — Paper 0 v0.5: bib per our own rules; spec write-back listed as parallel task

User decisions on the 3 flags:
- #1 (CAID I-VI->VII-XXII) + #2 (SPEC_17 n=4): ADOPT/update -- this was always the post-series spec
  write-back; Overview just surfaced it mid-stream. Treat as PARALLEL task; list items first.
- #3 (bibliography): don't expand. Use README's own "cite the whole series" format (our own rules).

Done:
- Listed the two spec write-back items as §G in inner/integration_map_VII_XXII.md (G-1 CAID symplectic
  fingerprint -> SPEC_13/REAL_03; G-2 SPEC_17 self-evolution coherence = n=4 master theorem). Noted they
  slot after the existing P1 (2026-06-14 done-but-uncommitted) items; rest of spec updates already in
  the file's [→ SPEC_xx] markers.
- Paper 0 bib: rewrote \bibitem{series} to README's series-citation format (github.com/co-nlang/research,
  "twenty-two-paper series with epilogue", individual papers by Zenodo DOI there). Dropped the inline DOI
  list + flag #3.

Paper 0 now 6pp, 2 \userflag left = the two spec write-back items (G-1, G-2), which are now tracked as a
parallel task in §G. These are no longer blockers on the paper -- they're documented "spec lags papers"
notes with a home. Draft is content-complete; remaining = polish + the parallel spec write-back.

PDF gitignored; inner/ NOT committed (local-only). Committed Paper0 .tex only.

---
## 2026-06-25 (cont.) — (b) spec write-back DONE (SPEC_13 §1.3, SPEC_17 §4.3); Paper 0 flags -> 0

Did the parallel task (b) so integration_map §G + Paper 0 update together.

nlang-spec (branch local, committed, NOT pushed):
- SPEC_13 §1.3 "CAID 的 symplectic 刻畫 (char-2 影子; VII-XXII)": relational fingerprint = ω/q-Gram;
  sign/phase = β/quadratic-refinement (XI); projection operators = Weil rep Sp(6,F2) on C^8 (XV);
  cross-context ω (XVII). Framed as extension of §1.1 (I-VI concept), not replacement; REAL_03 physical
  envelope (complex spectrum) unchanged, symplectic = its math content.
- SPEC_17 §4.3 "自我表示的相干性 = n=4 (master rigidity, XXI)": the engine-vs-self-evolution distinction
  (OODP engine dimension-agnostic, spans whole ladder H^1-H^4 = CAP/FLP/Byzantine/Sybil per APP_07 §4;
  Ouroboros self-evolution selects n=4 = [n_a]=0). = why_the_ladder. Strictness note: identifies the
  self-loop with the self-representation bridge; backing = XXI master + XXII truncation.

Verified APP_06 §6.5 (the ℏ=resonance-tower bridge Paper 0 §3 cites) DOES exist in the spec file (read
earlier, lines ~150-161) -- so the integration_map "未 commit" notes for 2026-06-14 P0/P1 are STALE
(git working tree clean = those were committed since). Good: Paper 0's APP_06/APP_07 citations are real.

integration_map_VII_XXII.md §G: G-1, G-2 marked [✓] DONE with spec section refs.

Paper 0 (research, committed): both \userflag -> resolved cross-refs (SPEC_13 §1.3, SPEC_17 §4.3).
0 flags now, 6pp, compiles clean. Draft content-complete + spec reconciled.

inner/ NOT committed. PDF gitignored.

---
## 2026-06-25 (cont.) — Paper 0 v0.7: polish pass (user + 小夥伴 feedback)

Five expansions, all requested:
- §2: expanded the "context = Lagrangian" dictionary row -- Sp(6,F2) Lagrangian def (n=3: 3 commuting
  Paulis, e.g. <X1,X2,X3>) + n/ MASA/context + schematic `a & b` (commute->one context) vs `a & c`
  (anticommute->_|_/#split). The single identification "same context = commute = share a Lagrangian".
- §3: added "why no arity-5 rung" intuition (4-index partition: omega(v_ij,v_kl) indexed by {i,j,k,l} =
  4-index = deg-3 cochain; on K6 sub-top => c=delta a exact; arity-5 needs a 5-index invariant bilinear
  omega can't supply). Two-sentence version.
- §4: (a) holography->n=4 bridge (user's text: n>=5 holographic reconstruction fails => can't fully
  understand itself => Ouroboros forced to land at n=4 = unique [n_a]=0). (b) "why self-coherence IS a
  cohomology class" (#3): coherent self-description = global section of self-observation nerve;
  obstruction = Cech/sheaf class; top = [n_a] in H^3; so "loop closes" = literally [n_a]=0.
- §5: rewrote "no bottom yet ceiling" para to RESOLVE the §3-vs-§6 apparent conflict (user's point):
  abstract machine (LHS SS + Kudo) is bottomless (gens {2,3,5,9,..}, infinite self-reference); but
  bilinear Pauli data's arity exhausts at 4 => realized obstruction truncates at H^3; even realized rungs
  built infinitely (item 23). Machine infinite / Pauli height finite / rung-construction infty-coherent.
- §6: sharpened item 21 ("reduced, no longer an open search" -> Witt+polarization+single condition+
  verified; condition grounded 2 ways) and item 23 ("closed modulo Kudo") verdicts.

7pp, 0 flags, compiles clean (2 passes), \S\ref{sec:ladder}/{sec:frontier} resolve. Content-complete +
polished. Committed Paper0 .tex. (Optional next: a figure for the ladder/hbar spectrum.)

---
## 2026-06-25 (cont.) — Paper 0 v0.8: added the hbar/resonance ladder figure (§3, fig:ladder)

Added \usepackage{tikz} + a TikZ figure in §3 (after the ladder table). The figure does triple duty
(§3 ceiling / §4 n=4 / §5 reconciliation, + APP_07 §4 dist-systems):
- solid rungs H^1/H^2/H^3 with (hbar, arity, clique) + engineering meaning (CAP/FLP/Byzantine);
- thick CEILING line at H^3 (Paper XXII, c=delta a, no arity-5);
- faded dashed region above: H^4=<q^2> decomposable only (item 21); H^5 (arity 6), H^9,... = abstract
  Steenrod/LHS machine continues but needs non-bilinear data -> visualizes "machine infinite / Pauli
  height finite" (§5);
- blue [n_a]=0 <=> n=4 marker on the H^3 rung; degree=hbar axis on left.
Caption ties it to §5 and the n=4 selection.

Fixed a 6.9pt overfull (verbatim n/ snippet comment too long) by trimming the comments. Now no overfull
>2pt, 0 flags, 7pp, compiles clean (2 passes). Committed Paper0 .tex.

Paper 0 is now content-complete + polished + figured. Remaining = pure language polish (optional) and the
user's read-through. PDF gitignored; inner not committed.

---
## 2026-06-25 (cont.) — Paper N rename (Easter egg) + EML "why" gap-fill; user staggered the figure

- User repositioned the figure rungs into a rising staircase (h1/h2/h3 at x=-2.2/-1.8/-1.4, 12cm boxes,
  diagonal degree axis). Left as-is (their layout). Compiles clean.
- RENAME: "Paper 0" -> "Paper N" in the title, with a \thanks footnote Easter egg: N is n/'s own letter,
  taken from "element zero", so Paper N = the n/ paper = the series' Paper 0 (zeroth/entry). Filename kept
  Paper0_nlang_whitepaper.tex (sorts first as entry point; it IS paper zero) -- title/filename mismatch is
  fine (like other papers' descriptive filenames).
- GAP-FILL (user's example): EML "why does n/ need it?" -- added the semantic-closure motivation: n/ wants
  its math layer semantically closed = generated from a single primitive (math LUCA, SPEC_09) not
  postulated, so it bootstraps its own arithmetic; eml(x,y)=exp(x)-ln(y) is that closure, complete only
  over C. (User noted SPEC_09 mentions math LUCA; semantic closure is the intuitive framing.)

User reading v0.7/0.8 in parallel; flagged EML as one example of small gaps invisible-to-the-expert.
Watch for more on next read-through. 7pp, 0 flags, no overfull. Committed.

---
## 2026-06-25 (cont.) — Paper N v0.9: gap-fill scan applied (G-a/b/c/d/f + 3 glosses; Direction-D removed)

Proactive reader's-eye scan -> user picked G-a/b/c/d/f + G-e's 3 glosses. Applied:
- G-a (§1): "why distance needs phase" -- hashes are mutually orthogonal (no pre-download nearness);
  only interference (=> complex amplitudes/phase) gives nearness before fetching. = APP_06 §2. (The
  load-bearing motivation for the whole forced-C chain; was asserted, now explained.)
- G-b (§2): char-2 shadow LEGITIMACY -- §1 forces C, §2 works over F2; explained it's LOSSLESS for the
  obstruction: KS/Mermin are stabilizer phenomena, Pauli/phase = exactly V=F2^{2n} (omega=commutation,
  q=±1,±i phases); continuous amplitudes irrelevant to the obstruction. Bridges the §1->§2 jump.
- G-c (§3): notation clash -- min(omega-2,3) where omega = clique number collided with omega = symplectic
  form. Fixed to min(omega(G)-2,3), "omega(G) = clique number".
- G-d (§1): Soler's infinite-orthogonal-sequence hypothesis noted (supplied by CAID spectral geometry).
- G-f (§1): "complete only over C" -- why not R/H (R: ln partial; holomorphic completeness needs C; H
  non-commutative breaks it); selects C from Soler's three.
- G-e glosses (3): squaring class (+I vs -I) inline §2; family A/B (Maslov-pentagram / Mermin-square)
  one-liner after §3 table; modulus = order parameter distinguishing n>=5 strata, §4.
- DIRECTION-D removed (user: term only in discussion docs/supplementary, NOT in papers/XXII -> a
  paper-only reader can't find it). Replaced with its meaning: the IV (16-cell/Cech H^3) <-> XX
  (Maslov-Wall H^3) comparison map, same class in two languages.

8pp, 0 flags, no overfull, Direction-D count = 0. Compiles clean (2 passes). Committed. Did NOT do G-g
(P_A/wave-particle gloss) -- user didn't include it.
