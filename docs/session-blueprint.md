# Session blueprint: taking a topic from idea to published tool

_Written 2026-07-14, after the second tool (Social Media & Teen Mental
Health) was built end-to-end in one working session. Part 1 records the
process as actually practiced; Part 2 records where it was weaker than it
should have been and what a future session should do differently. The
improvements are numbered so a future session can cite which ones it
adopted._

---

## Part 1 — The process as practiced

### Stage 0: Absorb the repo before deciding anything

Read, in order: `README.md`, `research/README.md`, `docs/README.md`,
`docs/sourcing-protocol.md`, and the most recent tool's artifacts —
`data/nodes.json`, `data/findings.json`, `data/crosslinks.json`,
`evidence-audit.md`, `build-notes/phase1-to-phase2-handoff.md`. The prior
tool is the de-facto spec: its field values (e.g. the exact
`source_type` / `evidence_type` / `source_strength` vocabularies, the
`evidence_quality` values, the tension `kind` set) are conventions to
extract programmatically, not to guess.

### Stage 1: Topic selection with documented alternatives

Web-search current public salience; select against the three
candidate-topic criteria in `research/README.md` (honest question tree;
literature that can go either way per leaf; not primarily moral or
definitional). Record the alternatives considered *and why they were
deferred* in the proposal — the selection reasoning is part of the
project's transparency, not scaffolding to discard.

Strong selection signals: policy is currently outrunning evidence; the
evidence base changed recently; the public debate visibly conflates
sub-questions the tree can pull apart.

### Stage 2: Preliminary source scan, both directions, before freezing anything

For each draft leaf, search for the best available tier of source FOR and
AGAINST (inclusion order from the sourcing protocol). Two disciplines that
paid off:

- **⚠ VERIFY tags.** Anything located only via title, press release, or
  secondary coverage gets an explicit flag with what exactly is
  unconfirmed (venue, direction, magnitude). Nothing unverified silently
  hardens into a finding later.
- **Name the expected thin flags now.** If a leaf's AGAINST side can't be
  sourced at scan time, write that down as an expected audit flag rather
  than discovering it during authoring and being tempted to pad.

### Stage 3: Proposal (`research/<slug>/proposal.md`)

Working title + one-sentence scope; draft root question and dimensions;
coverage note (what is deliberately out of scope); why now; known sourcing
hazards; alternatives considered. Commit and push — each pipeline stage is
a separate commit so the history reads as the pipeline.

### Stage 4: Phase 1 freeze with a decision log

Author `nodes.json` in the established schema (registers, `depends_on`
guards targeting the topic's signature conflations, coverage notes), then
validate the tree programmatically: parent/child symmetry, every leaf
scored with a `claim_evaluated`, no orphans. Write the
`phase1-to-phase2-handoff.md` with one ticket per scored leaf, sourcing
leads pointing into the scan, and — critically — a **decision log**: which
draft leaves were cut or rescoped and why (e.g. mechanism pathways not
scored to avoid manufacturing false balance; the age-ban leaf scoped to
USE because no mental-health outcome data exists to source either way).
Future change requests argue with the log, not with a guess about intent.

### Stage 5: Resolve every ⚠ VERIFY before authoring

A dedicated verification pass, one targeted search per flag, resolving
venue, direction, and headline magnitudes. The drop rule: a source whose
direction cannot be confirmed is dropped or thin-flagged, never guessed.
(In practice: one meta-analysis was dropped this way.)

### Stage 6: Author findings and crosslinks

Graduate the topic (`git mv` research/<slug> content into
`tools/<slug>/data` and `tools/<slug>/build-notes`). Author
`findings.json` per ticket — both registers, effect sizes as numbers where
they exist, caveats that carry disputes (a contested meta-analysis is
citable only WITH its published critique attached and never as sole
support). Author `crosslinks.json` with typed tensions, including the
tensions the handoff marked mandatory.

Treat `crosslinks.json` as the single source of truth for
`tension_with`: backfill the per-finding field programmatically so the two
can never disagree. (This caught a hand-written inconsistency
immediately.)

### Stage 7: Scripted audit and derived artifacts

One idempotent compose script (rerunnable after any edit) that:

1. backfills `tension_with` from crosslinks;
2. collapses findings by `source_cluster` per node per direction;
3. computes the audit flags (one-sided, FOR-single-cluster,
   single-source-heavy) and writes `evidence-audit.md` (table +
   hand-written notes on each flagged node);
4. backfills `evidence_quality` and `evidence_caveats` into `nodes.json`;
5. renders `evidence-map.md`;
6. generates the tool's `BeliefEngine.tsx` from the reference tool's
   component by swapping only the inline `DATA` constant;
7. writes `participant-state.example.json`.

The audit is not paperwork — expect it to change the published quality
labels. Honest thin flags on one-sided leaves are the product working as
designed.

### Stage 8: Webapp, registration, verification

`index.html` + `main.tsx` per the reference tool; add the entry to
`tools.json`. Then verify at two levels: `npm run build` (Vite
auto-discovers `tools/<slug>/index.html`), and a headless-browser smoke
test against the production build that (a) loads the tool page, (b)
checks real content renders, (c) exercises at least one navigation step,
and (d) compares behavior against the reference tool rather than assuming
what "correct" looks like — the reference settles disputes about expected
behavior.

### Stage 9: Commit, push, report

Commit per stage with messages that state what was verified, not just
what was added. Report failures and skipped steps plainly.

---

## Part 2 — Improvements for the next session

Ordered by how much they would have raised quality this session.

**I1. Full-text verification for load-bearing findings.** This session
verified citations, venues, directions, and headline numbers via targeted
search, but did not read the underlying papers — a weaker standard than
the handoff itself demanded. Next session: define a finding as
*load-bearing* if it quotes an effect size OR is a node's sole support in
its direction, and fetch/read the actual paper (or at minimum its
abstract + results section) for every load-bearing finding before
authoring. Budget: this roughly doubles Stage 5 and is worth it.

**I2. An independent review pass before publishing.** Every editorial
judgment — tree framing, claim wording, direction calls, strength
ratings, quality labels — was single-pass this session. Next session, add
a review stage between Stage 7 and Stage 8: a reviewer (human, or a fresh
agent context given only the sourcing protocol and the data files, not
the author's reasoning) adversarially checks a random sample plus all
flagged nodes for: direction misassignment, strength inflation,
research-to-simple register drift, and claims a cited source does not
actually make. File the outcome as `build-notes/review-<date>.md`. The
pipeline's step 6 ("reframe under review") still applies after real
outside review arrives; this internal pass is a floor, not a substitute.

**I3. Structured extraction between verification and authoring.** Findings
were written from search-result summaries held in working memory. Next
session: during Stage 5, build a small extraction table per source
(verified claims, numbers, population, design, limitations, quotable
conclusions) and author findings only from that table. This narrows the
gap where paraphrase drift enters.

**I4. Promote the compose script into the repo.** This session's script
lived in session scratchpad and is gone. It has been reconstructed as the
process above, but next session should commit it (e.g.
`scripts/compose-tool.py`, parameterized by slug) so audits are
reproducible by anyone and CI could run the structural checks (tree
validity, tension symmetry, schema vocabularies) on every push.

**I5. Decide the shared-component question deliberately.** The engine is
currently duplicated per tool by design (self-contained tool
directories), regenerated from the reference tool. This is fine at two
tools and wrong at five. Next session that touches the engine should
either extract it to a shared module that takes `data` as a prop, or
re-affirm duplication in writing — but not drift.

**I6. Log the search trail.** Queries used during scan and verification
were not recorded. Append them to `build-notes/source-scan.md` as run —
it makes the "no qualifying source found" claims auditable and spares the
next researcher re-running dead-end searches.

**I7. Register-fidelity spot-check.** The simple register is a
translation, and translations drift toward vividness. Add to the review
pass (I2) an explicit check that each simple paraphrase asserts nothing
stronger than its research counterpart — the failure mode is a punchy
simple sentence quietly upgrading "associated with" to "causes".

**I8. Pin the fast-moving sources.** For topics where policy evidence is
months old (this one), record in each affected finding's caveat the
authoring date and add a standing re-search instruction to the audit
("re-run the Australia-ban search before any republish"). Recency flags
exist for old sources; fast-moving topics need the mirror-image flag for
new ones.

---

## Adoption log

_A dated record of which improvements each subsequent session actually
adopted, so the list above stays honest about what has been tried._

**2026-07-15 — Ultra-Processed Foods and Health (third tool).** Adopted
**I1** (read the primary source or its abstract/results for every
load-bearing finding — Braesco κ, Lane umbrella grades, Fang cohort
attenuation, Hall/Dicken magnitudes, Chile −23.7%), **I2** (independent
review pass in a fresh agent context given only the protocol + data files,
filed as `tools/ultra-processed-foods/build-notes/review-2026-07-15.md`;
five findings applied, including two direction re-typings a single-pass
author had missed), **I3** (`build-notes/source-extraction.md` table
authored before findings), **I4** (compose pipeline promoted to
`scripts/compose-tool.py`, parameterized by slug, with per-tool editorial
input in `build-notes/compose-config.json`), **I6** (search trail logged in
the source scan), **I7** (register-fidelity was the review's most useful
catch — an "association"→"harm" drift in the subgroup leaf's simple
register), and **I8** (fast-moving policy sources pinned with a re-search
instruction for the FDA/USDA 2026 UPF definition). **I5** was addressed in
writing (`build-notes/engine-decision-I5.md`): duplication re-affirmed but
made script-generated from the canonical reference component, with a stated
trigger (a fifth tool, or the next engine-logic change) to extract a shared
module. New wrinkle worth carrying forward: making the definitional dispute
its own scored leaf let a topic the prior session had deferred as "too
definitional" become tractable — consider that move for other deferred
definitional topics.

**2026-07-15 — Microplastics: Origin and Effects (fourth tool).** Adopted
**I1** (read the primary source or its abstract/results for every
load-bearing finding — Marfella NEJM HR 4.53, Leslie blood 17/22, Ragusa
placenta 4/6, VAMAS 84-lab reproducibility, Boucher–Friot 15–31%/35%/28%/2%,
Foley 2018, Bucci–Rochman 17%, Koelmans HC5/exceedance, the measured
microbead reduction), **I2** (independent review pass filed as
`build-notes/review-2026-07-15.md` — it caught two no-fabrication failures a
single-pass author had let through: a wrong author/year on the microbead-ban
citation and fabricated page numbers on the NEJM correspondence; both fixed
and recomposed), **I3** (`build-notes/source-extraction.md` table authored
before findings), **I4** (reused `scripts/compose-tool.py` unchanged except a
genuine generalisation — see below), **I6** (search trail logged in the
source scan), **I7** (register-fidelity framed as the topic's central
discipline: the "presence is not harm" rule, enforced so detection findings
never read as harm findings in either register), and **I8** (fast-moving
sources pinned: the EU/UN plastics-treaty policy, the single-study Marfella
association, and measurement standardisation each carry a re-search
instruction). **I5** was untouched (no engine-logic change; duplication
remains script-generated from the reference component, per the UPF decision).

Two things worth carrying forward. (a) **The presence/harm split as the tree
spine.** This topic's signature conflation is not two sub-questions of equal
strength (as in prior tools) but a *strong* side (the particles are real,
measurable, human-made, and in our bodies) vouching for a *weak* side (they
harm us). Building the tree so the well-evidenced presence leaves and the
thin harm leaves sit together, with the root `depends_on` and a manual caveat
stating the asymmetry outright, is a reusable move for any "X is everywhere,
therefore X is dangerous" topic. (b) **A leaked hardcoded string in the
"generic" compose script.** The advocacy-note line in `write_audit` still
carried UPF-specific text (the Lancet UPF Series), which printed — falsely —
into the microplastics audit. Fixed by moving it to an `advocacy_note` config
key (UPF audit output byte-identical afterward). Lesson for the next session:
when reusing the compose script, grep its output for the *previous* tool's
proper nouns before trusting the audit — I4's "promote the script" is not
done until the script is verified free of per-topic constants.
