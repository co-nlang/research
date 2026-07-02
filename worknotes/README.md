# worknotes/ — The Working Documents, As They Were

*Selected files from the project's internal working directory (`inner/`), published verbatim.*

## What this is

The papers show the results; these files show the work. They are the actual working
documents of the human + LLM collaboration that produced the series — planning,
dead ends, refuted lemmas, self-caught errors, session logs — kept **append-only**
and published **unedited** (original internal jargon included; decoder below).

If you are curious what collaborative research with LLM agents looks like day to
day, this is a live demonstration. The division of labor: the human sets direction,
taste, and the methodological **firewalls**; the agents derive, compute, review, and
log. The discipline that makes it work is visible on every page:

- negative results are recorded, not deleted (ruled-out shortcuts stay ruled out);
- corrections never overwrite — they are appended, with the error named
  ("self-caught", "collaborator-flagged");
- every load-bearing claim carries a status tag (`[PROVEN]`, `[VERIFIED n=...]`,
  `[CONDITION]`, `[GAP, honest]`, `[OURS]`, `[CLASSICAL]`);
- before believing any new model of the problem, run the settled case as a control
  (here: $n=4$) — three wrong routes were killed by that control in a single session.

## The files

### A paper's life cycle — the Paper XXII chain (read in order)

1. **[`if_not_ladder.md`](if_not_ladder.md)** — the post-XXI brainstorm menu:
   four candidate directions (A–D) for what to do after the master theorem, plus a
   ranked, brutally honest assessment. Origin of the "Direction A/B/C/D" jargon;
   its predictions can now be scored against what happened (B became Paper XXII;
   D became the capstone).
2. **[`paper22_idea.md`](paper22_idea.md)** — Direction B growing from a one-line
   thesis into the paper's actual skeleton: the resonance-tower table, the lateral
   test that discovered the family-A/B split *mid-note* (the "BIG REFRAME"), the
   clique criterion. The header block is the outcome log — drafted, reviews
   addressed, readability pass — prepended as it happened.
3. *(the draft itself: [`papers/Paper22_resonance_ceiling.tex`](../papers/Paper22_resonance_ceiling.tex))*
4. **[`paper22_review.md`](paper22_review.md)** — a cross-review by an independent
   agent: one genuine rigor gap caught (Prop. 4.1's "both values occur" was *not*
   derivable from rank-parity alone), a group-vs-class conflation, an action table.
   Its counterpart is the "REVIEW ADDRESSED" log atop the idea file — including one
   instance where the *reviewer's* suggested fix was itself wrong ("polynomial in
   pairwise ω ⇒ arity ≤ 4" is false — products span ≥ 5 indices) and was rejected
   with a counterexample. Review is symmetric here: everyone gets checked.

### The long-running instruments

- **[`open_problems.md`](open_problems.md)** — the living roadmap ("the pit list").
  Starts as a difficulty-audited backlog after Paper XXII; becomes an append-only
  session log. The per-entry "Files: … inner/ excluded" footers are the agent's own
  commit notes (`inner/` was local-only at the time; this publication changes that
  for these files).
- **[`directionD_bridge.md`](directionD_bridge.md)** — a single problem's complete
  working file: "Direction D" from first strike (2026-06-13) through negative
  results, ruled-out formula families, the closed form, to closure-mod-Kudo
  (= RESEARCH_FRONTIER item 23). Read top to bottom for the honest shape of a
  proof search.

### Connect-the-dots, caught on camera

- **[`twistor_theory.md`](twistor_theory.md)** (中文) — a raw connect-the-dots
  session on twistor theory: layer-by-layer correspondence tables, a bold
  conjecture (the googly problem as an $H^2$ obstruction; the $SO(3)\to SU(2)$
  central-extension analogy), self-assigned rigor grades (🟢/🟡/🔴 per claim), and
  an appended second-opinion evaluation that fixed the logical order ($\Phi$ must
  exist *before* $d_2\neq0$ can be inherited). This one jumped the fence: instead
  of settling into `insight/` it became the **seed of Paper VII** — the
  demonstrated payoff of the standing rule ("keep the dots; label the lines").

## Decoder ring (internal jargon)

These files predate the public naming and were deliberately not adjusted. The map:

| internal term | public meaning |
|---|---|
| Direction A | "the physical meaning of $H^3$" — became **item 24** (answered: structural, not operational) |
| Direction B | "other configurations / horizontal extension" — became **Paper XXII** (arity–resonance ceiling) |
| Direction C | the even/odd dichotomy of Paper XXI: **C-odd** (Wall/metaplectic, the $H^2\to H^3$ seam) was absorbed into the Direction-D line; **C-even** (equidistribution) = **item 20**, deprioritized |
| Direction D | "back to Postnikov / unify the tower" — became the transgression bridge / **self-representation map** = **item 23**, and the ambient-class bridge inside item 21 |
| item $N$ | entry $N$ of [`RESEARCH_FRONTIER.md`](../RESEARCH_FRONTIER.md) Part II |
| family A / family B | Maslov-pentagram type / Mermin-square type — the two $H^2$-rung flavors (Paper N §3) |
| the modulus | Paper XIX's order parameter $\mathrm{rad}(\omega|_W)$ — the $n\ge5$ degree of freedom no arity-$\le4$ datum sees |
| FFT / SFT | first / second fundamental theorem (invariant theory) — *not* Fourier |
| M1–M5 | milestones of the item-21 attack plan (`supplementary/item21_arity5/ATTACK_PLAN.md`) |
| (b-pos) / (b-neg) | the two halves of the D-bridge: *realization* (which classes are nonzero; needs Kudo) vs the *classification bound* (genuine ⊆ ambient; needs only Witt + polarization) |
| over-counters | config invariants (orbit indicators, weight enumerators) that pair $\neq0$ without being genuine obstructions — the phase-blind / non-representable layer |
| firewall | the standing discipline: value ≠ cochain; $n=4$ as control; total vs partial functions; degree bookkeeping |
| 附論 | companion note — an LsNote-style addendum, smaller than a paper |
| 小夥伴 | "the buddies" — the other LLM agents used for cross-review (see the AI Collaboration Disclosure in the main [README](../README.md)) |

## Provenance & caveats

- **Verbatim snapshots.** They may reference sibling `inner/` files not (yet)
  published here; those references dangle by design — more files may be curated in
  as the mood strikes.
- **Point-in-time.** Statuses inside may lag the frontier;
  [`RESEARCH_FRONTIER.md`](../RESEARCH_FRONTIER.md) is authoritative.
- **License:** same as the papers (CC BY 4.0).
