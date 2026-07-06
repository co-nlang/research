# The ℏ Spectrum Is Sparse: Degree 4 Is a Hole Sealed Twice

*Status: the core is a theorem (Paper XXII) plus a verified-mod-reframe tower fact;
the closing self-similarity conjecture is ⚠️ a label-counting heuristic, stated to
be shot at. Bookkeeping convention throughout: ℏ_{n/} = cohomological degree =
arity − 1 = clique − 2.*

---

## 1. The claim

The degrees at which primary obstruction data can resonate are not dense. They are

$$\{2\} \cup \{1 + 2^i \mid i \ge 1\} = 2,\ 3,\ 5,\ 9,\ 17,\ \dots$$

— the degrees of the Kudo transgression tower: $q$ (deg 2), $\mathrm{Sq}^1 q$ (deg 3),
$\mathrm{Sq}^2\mathrm{Sq}^1 q$ (deg 5), $\mathrm{Sq}^4\mathrm{Sq}^2\mathrm{Sq}^1 q$ (deg 9), ….
The framework has *realized* degrees {2, 3} (the KS/K₄ and Borromean/K₅ rungs; the
ceiling of Paper XXII). **Degree 4 is a hole, and it is sealed twice:**

1. **Seal (i) — arity truncation (theorem).** Paper XXII: an arity-$a$ datum is an
   $(a-1)$-cochain resonating at $K_{a+1}$; the framework has no irreducible arity-5
   primitive, so $K_6/H^4$ truncates ($c = \delta a$ exact). Bilinear (stabilizer)
   phase data tops out at $H^3$.
2. **Seal (ii) — the tower skips 4 (verified mod reframe).** The transgression
   tower's rungs jump $t^2 \to$ deg 3, $t^4 \to$ deg 5; there is no rung at 4.
   This leg goes through the ambient-class reframe (the naturality CONDITION of
   frontier item 21), so its honest label is *verified-mod-reframe*, not theorem:
   Lemma A checked $n = 3, 4, 5$ by hand plus classical Kudo (internal ledger;
   the Direction-D bridge notes are published verbatim in
   `worknotes/directionD_bridge.md`).

Most of this was already sitting in the internal ledgers. The increment of this
note is to **name it as a falsifiable prediction and put it on the public face**:

> **Prediction.** Any future extension of the framework that carries genuinely new
> phase data gets its next primary rung at $H^5$ (arity 6, $K_7$) — **never at
> $H^4$**. The dashed rungs in Paper N's ladder figure follow $1+2^i$; the gap at
> 4 is structural, not an artifact of "we haven't looked yet."

What would kill it: exhibiting a primary obstruction carried at $H^4$ inside the
framework's ambient class. (Note the firewall: item 20 already showed the $n\ge5$
modulus IS an $H^3$ class — the ladder's known content lives at {2, 3}. The
prediction is about where the *next* rung can appear.)

## 2. ⚠️ The self-similarity conjecture (the spectrum of the spectrum)

Label counting suggests the *allowed arities* follow the same sequence as the
degrees. A $k$-linear datum acts on rays; each ray carries 2 Lagrangian labels;
so a $k$-linear datum touches at most $2k$ labels ⟹ it is a $(2k-1)$-cochain
(arity $2k$, resonating at $K_{2k+1}$). Matching $2k - 1 = 1 + 2^i$ gives
$k = 1 + 2^{i-1}$ — **the linearity degrees that have a rung to resonate with are
themselves $k \in \{2, 3, 5, 9, \dots\}$**:

| $k$ (linearity) | arity $2k$ | cochain deg $2k{-}1$ | clique | tower rung at that deg? | status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2 (bilinear) | 4 | 3 | $K_5$ | $\mathrm{Sq}^1 q$ ✓ | ✅ realized — XXII's $n_a=\delta\mu$ at $K_5/H^3$ |
| 3 (trilinear) | 6 | 5 | $K_7$ | $\mathrm{Sq}^2\mathrm{Sq}^1 q$ ✓ | ⚠️ the predicted "next rung" — same statement as §1's prediction |
| 4 (quadrilinear) | 8 | 7 | $K_9$ | **none** | ❌ predicted forbidden: quadrilinear phase data cannot carry a primary obstruction |
| 5 | 10 | 9 | $K_{11}$ | $\mathrm{Sq}^4\mathrm{Sq}^2\mathrm{Sq}^1 q$ ✓ | allowed in principle |

(The base rung deg 2 — Maslov/KS at $K_4/H^2$, arity 3 — is the standalone $\{2\}$
part: it is $q$ itself, below the $k$-linear regime.)

Two consistency checks make this more than numerology: the $k=2$ row *is* Paper
XXII's realized ceiling, and the $k=3$ row lands exactly on the independently
predicted next rung. If the alignment is not a coincidence, the arity spectrum is
**self-similar**: the sequence of allowed $k$ is again $1 + 2^j$.

**Status: ⚠️ heuristic.** The $2k$-label count is a worst-case simplex-counting
sketch, not a construction. To promote it, one needs:

1. the map "$k$-linear datum ⟹ degree-$(2k-1)$ cochain" made precise (does every
   such datum factor through the tower at that degree?);
2. a realization check at $k = 3$: does some trilinear datum actually hit the
   $\mathrm{Sq}^2\mathrm{Sq}^1 q$ rung? (Realization side = the Kudo machinery of
   item 23 — the b-pos branch.)

What would kill it: a $k$-linear datum carrying a primary obstruction at degree
$\ne 2k-1$, or a realized rung whose $k$ falls outside the sequence.

## 3. Relation to the binarity contract (design-side echo)

This note and the binarity design contract (XXII read in reverse: n/'s safety
property "contextuality ceilinged at $H^3$, $n=4$ self-description coherent" is
conditional on all relational primitives being bilinear) are one story. The
contract keeps the language at $k = 2$. The sparse spectrum adds: even *lifting*
the contract only ever opens rungs at $k \in \{3, 5, 9, \dots\}$ — the next
checkpoint is trilinear/$K_7$, and quadrilinear is structurally empty. Language
extensions that add phase-carrying primitives can be audited against this table.

*Cross-refs: Paper XXII (ceiling theorem); frontier items 20, 21 (reframe
CONDITION), 23 (realization); `worknotes/directionD_bridge.md` (tower ledger);
Paper N ladder figure (dashed rungs).*
