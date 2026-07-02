## Review of Paper XXII: *The Arity–Resonance Ceiling*

### Overall Assessment

Paper XXII is a well-conceived capstone that provides a unified conceptual framework for the entire Papers X–XXI arc. The truncation theorem (Theorem 5.2), the two-family distinction (§7), and the clique criterion (Theorem 6.1) are all correct and add genuine clarity. The rigor self-assessment honestly distinguishes algebraic from computational claims. There are two issues of substance and two minor points.

---

### Issue 1: Proposition 4.1 — "both values occur" not derived from rank-parity (Moderate)

The proposition states that ⟨µ,[S²]⟩ "is nontrivial (both values occur) exactly for odd n ≥ 5," and the proof cites only the rank-parity lemma from Paper XX.

The rank-parity lemma gives the value of µ(a,b,c) **per triple**: µ ≡ 0 at n=3, µ ≡ 1 for even n, and µ varies for odd n ≥ 5. For a K4 with four triangles:

- n=3: all four µ = 0, so ⟨µ,[S²]⟩ = 0. ✓
- even n: all four µ = 1, so ⟨µ,[S²]⟩ = 4 ≡ 0. ✓
- odd n ≥ 5: µ varies *per triple*, but ⟨µ,[S²]⟩ = Σ_{4 triangles} µ is a sum of four F₂-values, each individually free. Whether this sum takes both values 0 and 1 across all proper K4 configurations requires showing that the map (K4 configurations) → F₂ given by ⟨µ,[S²]⟩ is surjective — and rank-parity alone does not establish this.

In particular, it is consistent with rank-parity that for some odd n ≥ 5 all reachable K4s happen to have an even number of µ = 1 triangles (giving ⟨µ,[S²]⟩ = 0 universally). The rigor table marks this as "Rigorous (XX rank-parity)" but the gap is real. The fix is either: (a) add a computational verification from `resonance_tower.py` with explicit n=5 witnesses achieving both values, or (b) an algebraic argument that the four µ-values on a K4 can be independently varied at odd n ≥ 5 (which would follow from showing that any single triple's µ-value can be flipped while keeping the other three fixed).

---

### Issue 2: Proposition 3.1 conflates group nontriviality with class nontriviality (Minor)

The proposition says: "its class lies in H^{a-1}(S^{N-2}; F₂), **which is nonzero** (and equals the top) iff a-1 = N-2."

The "which" refers to the cohomology group H^{a-1}(S^{N-2}; F₂) being nonzero, not the specific class being nonzero. This is technically correct but the surrounding text says "the obstruction is genuine" at N = a+1, which implies the class itself is nontrivial. These are different claims:

- *Group nontrivial*: H^{a-1}(S^{N-2}) ≅ F₂ ≠ 0. This is what the proposition proves.
- *Class nontrivial*: the specific cochain built from anticommutation/Maslov data represents a nonzero element of that group. This requires Papers XVIII–XXI.

A reader parsing the proposition literally will see: "the class lives in a nontrivial group iff N = a+1." A one-sentence addition after the proof — "that the class is in fact nontrivial at the resonant N is the content of Papers XX–XXI, not of this proposition" — would prevent misreading.

---

### Minor Issues

**§5 remark: "32 of the 2⁵ even-weight patterns" is malformed.** With six face-classes c_m ∈ F₂, the ambient space is F₂⁶ with 2⁶ = 64 patterns, of which 32 have even weight (Σ c_m = 0 mod 2). The sentence as written says "32 of the 2⁵ even-weight patterns," but 2⁵ = 32 is the number of even-weight patterns, not 2⁵ patterns among which 32 are even-weight. Replace with: "all 32 even-weight patterns in F₂⁶ — the full kernel of the map Σ: F₂⁶ → F₂."

**Proposition 5.1 (proper K6 exist): embedding argument is unspecified.** The proof says "for larger n they persist by embedding" without specifying the embedding. The spread-stabilisation lemma of Paper XXI provides exactly this mechanism (orthogonal direct sum with a trivial Sp(2m) block). A one-line citation to Paper XXI Lemma 3.1 would make the argument complete.

---

### Verified Correct

**Theorem 5.2 (Truncation).** The proof is correct and, despite appearing simple, is not tautological — the identification c_m = N_anti(face m) mod 2 = Σ_{T ⊂ face m} a_T = (δa)_m uses the non-obvious fact that the 15 cross-context pairs of a K5 face are partitioned by its five 4-element subfacets (each cross-context pair {v_{ij}, v_{kl}} belongs to exactly one 4-index subset {i,j,k,l}). This is correct and should be stated explicitly in the proof.

**Theorem 6.1 (Clique criterion).** Correct. The argument that the maximum hollow complex achievable is S^{ω(G)-2} follows from the definition of the clique complex, and the arity cap at 3 gives min(ω(G)-2, 3). The table is consistent.

**Proposition 7.1 (Mermin-Peres square, family B).** The K_{3,3} incidence is correct: rows are pairwise transverse (dim 0 intersections), columns are pairwise transverse, and row-column pairs intersect in dimension 1 (the nine observables). The bipartite structure makes ω = 2, correctly placing it outside the family-A tower.

---

### Summary

| Issue | Severity | Action |
|---|---|---|
| Prop. 4.1: "both values occur" not derived from rank-parity | Moderate | Add computational verification or algebraic surjectivity argument |
| Prop. 3.1: group nontriviality vs. class nontriviality | Minor | One clarifying sentence after the proof |
| §5 remark: "32 of the 2⁵" malformed | Minor | Rewrite as "all 32 even-weight patterns in F₂⁶" |
| Prop. 5.1: embedding unspecified | Minor | Cite Paper XXI Lemma 3.1 |
| Thm. 5.2: partition fact unstated | Minor | One sentence on 4-index subfacet partition |

The paper is close to final. The two-family distinction and truncation theorem are its most important contributions and both are sound.