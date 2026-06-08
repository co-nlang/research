# Paper XIX supplementary — n≥5 deformation of Mermin K₅s

Computational backing for Paper XIX (Structure & Obstruction): in Sp(2n,F₂) with
n ≥ 5 the n=4 rigidity (Paper XVIII) softens into a **modulus**. The central result
is negative — no relative-position invariant up to arity 4 classifies the fiber.
The paper also contains a positive theorem: **rankG=4 ⟹ N_anti=6** (rigorous,
via Sylvester + doily dichotomy + C5 non-lifting argument).

Full graded claim ledger: `../../inner/paper19_data.md`.

## Scripts

| Script | Establishes |
|---|---|
| `nge5_probe.py` | Original landscape probe: rankG distribution, radW order parameter, (8,6,2) split. |
| `lowrank_rigidity.py` | Exhaustive 2¹⁵ Petersen-subgraph upper-bound ladder (rankG=4⟹N_anti≤6, rigorous) + multi-seed deterministic strata (rankG∈{0,2,4}). |
| `maslov_probe.py` | Triple-Maslov bit + μ S₃-symmetry self-check; `n_odd≤5 ⟹ N_anti even`; purity ladder (stalls); **the modulus witness** (same arity-≤4 data, opposite parity). |
| `quad_refine.py` | Arf ruled out: frame-q non-Sp-invariance; intrinsic-q is generic (~91%, brute-verified — corrects an earlier 6.3% estimate) + unique; its Arf does not separate (8,6,2) parity. |
| `noq_odd_proof.py` | Structural skeleton for the (8,6,2) no-q stratum: W coisotropic, R⊆kerG, o linear on kerG ⟹ intrinsic-q exists ⟺ ℓ\|_R≡0; N_anti=o(𝟙); sharp empirical: no-q ⟹ N_anti=9 exactly (Petersen−6 anti-graph). |
| `reduction_frame.py` | Radical-quotient reduction frame (proven): W̄=W/rad(ω\|_W) is non-deg symplectic of dim rankG; each L_a → isotropic L̄_a in Sp(rankG,2). Forced-stratum table; negative: forcing is dimension-stratified — (9,8,1) splits across all refinements. |
| `doily_rank4.py` | Exhaustive over Sp(4,2)≅S₆ doily GQ(2,2): all C(15,5)=3003 5-syntheme subsets satisfying spanning+rank-4 axioms → 132 configs, exactly 2 S₅-classes: C5 meeting-pentagon (N_anti=5) and (22233)-degree (N_anti=6). Proper K₅ realises only the 6-class. |
| `rank4_lemmas.py` | Conditional proof of rankG=4⟹N_anti=6 via (I) ℓ\|_R≡0 and (II) radW spanned by inner rays; (I)∧(II)⟹q̄ exists⟹doily forces N_anti=6 (rigorous); (I),(II) verified 176/176. |
| `rank4_lemmaII.py` | Anatomy of condition (II): verifies Lemma lem:3term — the only F₂ dependency among 3 distinct rays of a proper K₅ is a Fano star (2369/2369 dependent triples are stars); confirms C6 and tree anti-graph types avoid stars ⟹ (II) holds. |

## Run

```
python3 nge5_probe.py       5 3000 400  6
python3 lowrank_rigidity.py 5 3000 600  8
python3 maslov_probe.py     5 2500 350  8
python3 quad_refine.py      5 2500 350  6
python3 noq_odd_proof.py    5 4000 600  8
python3 reduction_frame.py  5 4000 500 10
python3 doily_rank4.py
python3 rank4_lemmas.py     5 4000 500 10
python3 rank4_lemmaII.py    5 4000 400  8
```

Args: `n n_lag max_k5 seeds` (except `doily_rank4.py` which is exhaustive, no args).
Pure Python 3, no dependencies. Seeds are disjoint across scripts so cross-script
agreement is not a seed artifact.
