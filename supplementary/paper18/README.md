# Paper XVIII: Supplementary Computational Scripts

## Scripts

### `recheck_paper18.py`

Primary verification script for the transversal property (B0 + B1 + B2).
Checks all universal sub-steps of the elementary proof at the K₄ level.

**Steps:**
1. B0 no-3-term: verify no Fano vertex in proper K₄ (24,000 K₄s, 3 seeds)
2. B0 structured: exhaustive search over all 15⁴ Lagrangian completions of canonical Fano plane
3. Cor. no-3-term: check all context-ray triples in 300 proper K₅s
4. B1 implication: pairing=0 ⇒ others=1 (1,500 instances)
5. proper K₄ anti-count: 20,000 standalone K₄s, all have exactly 2 anticommuting pairs
6. B2 collapse/dim checks: 400 proper K₄s
7. All-anti Gram nonsingular: algebraic check of block matrix

**Runtime:** ~60 seconds

**Usage:** `python3 recheck_paper18.py`

**Requirements:** Python 3, NumPy

---

### `verify_sigma.py`

Verifies Σ_m uniformity: all five matching parities Σ_m are equal for every K₅,
and Σ_m = 0 for n = 4. Also tests n = 3, 5, 6 for the landscape table.

**Steps:**
1. Generate proper K₅s for specified n
2. Compute all 5 Σ_m values
3. Verify uniformity (all Σ_m equal) and value (0 for n=4)

**Runtime:** varies by n (~30 seconds for n=4, 500 K₅s)

**Usage:** `python3 verify_sigma.py [n=4] [n_lag=500] [max_k5=200] [seed=42]`

---

### `check_k5_random_n.py`

General-n K₅ sampler: computes N_anti and Σ_m distributions for any
Sp(2n,F₂). Generates Table 1 rows for n = 3, 4, 5, 6.

**Usage:** `python3 check_k5_random_n.py [n=5] [n_lag=2000] [max_k5=500] [seed=42]`

---

### `study_fano_count.py`

Counts Fano Lagrangians (w_a = 0) per K₅. Discovers the 0-or-1 Fano property
and the Type I / Type II split.

**Runtime:** ~15 seconds (500 K₅s default)

**Usage:** `python3 study_fano_count.py [n_k5=500] [seed=42]`

---

### `study_type_correspondence.py`

Verifies the correspondence: n_fano = 1 ↔ Type I (non-PM commuting graph),
n_fano = 0 ↔ Type II (perfect matching commuting graph). Referenced in Table 2.

**Steps:**
1. Generate proper K₅s, compute Fano count and commuting-pairs graph
2. Classify commuting graph as perfect matching (PM) or non-PM
3. Cross-tabulate Fano count vs PM/non-PM

**Runtime:** ~20 seconds (500 K₅s default)

**Usage:** `python3 study_type_correspondence.py [n_k5=500] [seed=42]`

---

### `verify_graph_structure.py`

Verifies the Petersen graph structure: for Type II K₅s, the 5 commuting pairs
form a perfect matching of K(5,2) and the 10 anticommuting pairs form two
disjoint 5-cycles. Referenced in Proposition 5.7 and Table 2.

**Steps:**
1. Generate proper K₅s, identify Type II (0 Fano Lagrangians)
2. Check if commuting pairs graph is a perfect matching
3. Check if anticommuting pairs graph decomposes into two 5-cycles

**Runtime:** ~20 seconds (200 K₅s default)

**Usage:** `python3 verify_graph_structure.py [n=4] [n_lag=500] [max_k5=200] [seed=42]`

---

### `explore_solution_space.py`

Key Lemma verification (Gram rank route, now optional): among the 4 candidate ω-vectors
in the constraint coset, identifies which have Gram rank in {0,8} and shows these are
exactly the ones with Σ_m = 0 for all m.

**Steps:**
1. Generate proper K₅ in Sp(8,F₂) via random Lagrangian sampling
2. Compute null space of 10×8 ray matrix M (rank=8 → 2 relations → 4 candidates)
3. Build constraint system: ω(v_k, R_α) = 0 for each relation R_α (rank-13 system)
4. Enumerate 4 candidate ω-vectors in the constraint coset
5. Compute Gram matrix G_x for each candidate; record rank and Σ_m values
6. Verify: rank(G_x) ∈ {0,8} ↔ Σ_m = 0 for all m

**Runtime:** ~10 seconds (50 K₅s default)

**Usage:** `python3 explore_solution_space.py [n_k5=50] [seed=42]`

---

### `check_3term.py`

Verifies that no 3-term relation v_{ij} + v_{ik} + v_{il} = 0 ever occurs among
context rays of any Lagrangian in a proper K₅.

**Steps:**
1. Generate proper K₅s in Sp(8,F₂)
2. For each Lagrangian L_a, check all C(4,3) = 4 triples of context rays
3. Count K₅s with any 3-term relation

**Runtime:** ~15 seconds (500 K₅s default)

**Usage:** `python3 check_3term.py [n_k5=500] [seed=42]`

---

### `check_lower_bound.py`

Verifies that each Mermin matching has at least 1 commuting pair (N_anti ≤ 10).

**Steps:**
1. Generate proper K₅s and compute all 15 cross-context ω-values
2. For each of the 5 Mermin matchings, check if all 3 pairs anticommute (0 commuting)
3. Count "all-anticommuting matching" exceptions

**Runtime:** ~15 seconds (500 K₅s default, 2500 matchings)

**Usage:** `python3 check_lower_bound.py [n_k5=500] [seed=42]`

---

### `compute_relations.py`

Computes the 2 F₂-linear relations among the 10 context rays for each K₅.
Classifies relations by support size (4,6), (5,5), (6,6).

**Steps:**
1. Generate proper K₅s and compute rank of 10×8 ray matrix
2. Find null space generators (the 2 relations)
3. Classify by number of nonzero entries in each relation

**Runtime:** ~5 seconds (10 K₅s default)

**Usage:** `python3 compute_relations.py [n_k5=10] [seed=42]`

---

### `check_k5_4qubit.py`

Initial exploration for n=4: discovers that K₅s in Sp(8,F₂) exist with
N_anti ≠ 15. Motivated the investigation leading to Paper XVIII.

**Runtime:** ~30 seconds

**Usage:** `python3 check_k5_4qubit.py [full]`

---

### `check_k5_5qubit.py` / `check_k5_5qubit_random.py`

K₅ parity sampling in Sp(10,F₂) (n=5). Contributes to Table 1 (n=5 landscape row).

---

### `study_wvectors.py`

Exploratory study of Fano-failure vectors w_a and their symplectic pairings.

---

### `strategy_a_v2.py` – `strategy_a_v5.py`

Development scripts from the proof search phase. Not directly cited in the
paper; retained for provenance.

---

## Key Results

### Transversal Property (Main Line — Fully Algebraic)

| Fact | Check | Result |
|------|-------|--------|
| B0 no-3-term (random) | 24,000 proper K₄ (3 seeds) | 0 Fano vertices |
| B0 no-3-term (structured/exhaustive) | all 15⁴ Lagrangian completions of canonical Fano plane | 0 all-Fano K₄ |
| Cor. no-3-term | 300 proper K₅, all context-ray triples | 0 violations |
| B1 implication: pairing=0 ⇒ others=1 | 1,500 instances | 0 violations |
| proper K₄ anti-count | 20,000 standalone K₄ | all = 2 (never 0/1/3) |
| B2 collapse: dim(L_a+L_b)=7 | 400 proper K₄ | 0 failures |
| B2 contradiction: (L_a+L_b)⊥ = ⟨v_ab⟩ | 400 proper K₄ | 0 failures |
| All-anti Gram nonsingular | block matrix det = 1 | exact |

### Gram Rank Selection (Alternative Route — Optional)

| Script | Claim | Result |
|--------|-------|--------|
| `explore_solution_space.py` | rank(G_x) ∈ {0,8} ↔ Σ_m = 0 (Key Lemma) | 210 K₅ × 4 candidates = 840/840 ✓ |
| `check_3term.py` | No 3-term relation in any proper K₅ | 0/500 exceptions ✓ |
| `compute_relations.py` | Exactly 2 relations, types (4,6)/(5,5)/(6,6) | Verified (10 K₅s) ✓ |
| `check_lower_bound.py` | No matching is all-anticommuting | 0/2500 exceptions ✓ |
| `study_type_correspondence.py` | n_fano=1 ↔ Type I, n_fano=0 ↔ Type II | 500/500 K₅s ✓ |
| `verify_graph_structure.py` | Type II: commuting = PM, anticommuting = 2×C₅ | 75/75 Type II ✓ |
| `verify_sigma.py` | Σ_m = 0 for all m, all n=4 proper K₅s | 200/200 K₅s ✓ |
| `check_k5_random_n.py` | N_anti landscape: universal for n∈{3,4}, mixed n≥5 | 500+ K₅s per n ✓ |

All scripts use `seed=42` as default; robustness confirmed with additional seeds.

### Cross-Context Anticommutation (Theorem 1.1)

For every proper K₅ in Sp(8,F₂): N_anti = 10 and Σ_m = 0 for all m.

**Main proof (transversal):** B0 (no Fano vertex) + B1 (≤ 1 commuting per matching)
+ B2 (≥ 1 commuting per matching) ⇒ exactly 1 commuting per matching ⇒ N_anti = 10.
Fully algebraic, K₄-level, independent of rank=8 theorem.

**Alternative proof (Gram rank):** rank = 8 (algebraic) → 4-candidate coset →
Gram rank 8 ↔ Σ_m = 0 (Key Lemma, computational) → non-degeneracy selects
rank-8 candidate → N_anti = 10 by counting. Key Lemma is computationally verified
(840/840) with algebraic proof open.
