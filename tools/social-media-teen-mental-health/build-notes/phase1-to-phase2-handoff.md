# Phase 1 → Phase 2 Handoff: Frozen Question List (v1)
_Frozen 2026-07-14. Topic: Social Media and Adolescent Mental Health._

Nodes are frozen — see [`nodes.json`](nodes.json). Each scored leaf below is
an independent ticket: gather evidence FOR and AGAINST its `claim_evaluated`
under [`../../docs/sourcing-protocol.md`](../../docs/sourcing-protocol.md)
(target 3–6 findings per leaf). Do not add/rename nodes while researching;
file a change request to Phase 1 instead. `evidence_quality` and
`evidence_caveats` in `nodes.json` are placeholders (`pending-phase2`) —
Phase 2 findings plus the source-cluster audit fill them.

Sourcing leads per ticket refer to sections of
[`source-scan.md`](source-scan.md); every ⚠ VERIFY entry there must be
confirmed against full text before it becomes a finding.

## Phase 1 decisions (and why)

1. **Mechanism pathways are not scored leaves.** Sleep displacement is
   independently measurable and gets a leaf; social comparison and
   algorithmic amplification are evidenced as embedded mechanism findings
   (e.g. inside Braghieri et al. 2022) and expert synthesis, not as claims
   with good-faith evidence on both sides. Scoring them would manufacture
   false balance. They stay visible as findings and crosslinks on
   `n_assoc_causal`, and the decision is recorded in `n_mech.coverage_note`.
   Revisit if the mechanism literature matures.
2. **The benefits leaf lives under `n_assoc`,** not a separate dimension:
   it is the same individual-level literature read in the other direction,
   and separating it would imply an evidence base it doesn't yet have.
3. **The age-ban leaf is scoped to USE, not mental health.** No
   mental-health outcome data from any national ban exists yet (July 2026).
   A leaf claiming "bans improve mental health" would be unsourceable in
   both directions; a leaf on use-reduction is testable today. The
   `depends_on` text guards against the null-on-use → "bans don't help"
   laundering in both directions.
4. **The association leaf keeps "practically meaningful" in the claim.**
   Existence of some association is not in serious dispute; magnitude is
   the live question. The `depends_on` text requires findings to report
   numbers, not adjectives, so the participant judges the threshold.
5. **Trend dimension split in two** (`n_trend_real`, `n_trend_attrib`) so
   that "it's real" evidence cannot silently carry the attribution claim —
   the central conflation in public debate, flagged in both nodes'
   `depends_on`.

## Scored leaf tickets

### `n_assoc_magnitude` — Is heavier social media use meaningfully associated with worse adolescent depression and anxiety?
- claim to evaluate: **Heavier social media use is associated with worse depression/anxiety in adolescents at a magnitude that is practically meaningful, not trivially small.**
- sourcing leads: source-scan §d_assoc/magnitude — dose–response meta (PMC9103874), Behavioral Sciences 2025 meta (r≈0.22), JMIR 2022 problematic-use meta FOR; Orben & Przybylski 2019 (NHB + Psych Science, one cluster) AGAINST.
- expected flags: self-report vs. device-log measurement caveat on every finding; problematic-use construct must not be presented as time-spent.

### `n_assoc_causal` — Does social media use causally worsen adolescent mental health?
- claim to evaluate: **Social media use causally worsens adolescent mental health.**
- sourcing leads: source-scan §d_assoc/causal — Braghieri et al. AER 2022, Allcott et al. AER 2020 FOR (check author-overlap for cluster assignment); NAS-2024, Ferguson meta (⚠ disputed — carry the dispute in the caveat, never sole support), Odgers & Jensen 2020 (⚠ VERIFY) AGAINST.
- expected flags: transportability caveats (2000s college students; adult RCT samples); NAS-2024 must not dominate the audit.

### `n_assoc_hetero` — Are harms concentrated in vulnerable subgroups and developmental windows?
- claim to evaluate: **Negative effects are concentrated in specific subgroups and developmental windows (notably girls in early adolescence) rather than spread uniformly.**
- sourcing leads: source-scan §d_assoc/heterogeneity — Orben et al. Nature Communications 2022 FOR (same `orben-przybylski` cluster as the null-leaning magnitude work — instructive, not contradictory).
- expected flags: AGAINST side not yet located — run the targeted search (non-replications of age/sex windows); if none qualifies, mark THIN honestly, do not pad.

### `n_assoc_benefits` — Does social media provide real mental-health-relevant benefits to some adolescents?
- claim to evaluate: **Social media provides real mental-health-relevant benefits to some adolescents — community, connection, and support, especially for marginalized youth.**
- sourcing leads: source-scan §benefits — NAS-2024 FOR.
- expected flags: single-cluster FOR at scan time; AGAINST unsourced — both-directions rule cuts this way too. Likely THIN.

### `n_trend_real` — Has adolescent mental health genuinely deteriorated since ~2010?
- claim to evaluate: **Adolescent mental health has genuinely deteriorated since ~2010; the rise is not an artifact of changed reporting, screening, or diagnostic practice.**
- sourcing leads: source-scan §d_trend/real — Twenge et al. 2018 (incl. objectively measured outcomes), Norwegian measurement-invariance study (Psychological Medicine 2024) FOR.
- expected flags: standalone artifact-hypothesis source still missing — Phase 2 search (reporting-change, diagnostic-practice studies). Anglosphere+Nordic heavy.

### `n_trend_attrib` — Is social media adoption the principal driver of the post-2010 deterioration?
- claim to evaluate: **Social media adoption is the principal driver of the post-2010 deterioration in adolescent mental health.**
- sourcing leads: source-scan §d_trend/attribution — Twenge 2018/2020 FOR (single `twenge` cluster, advocacy-adjacent caveat); NAS-2024 AGAINST; magnitude-inference AGAINST framing only if stated without overreach.
- expected flags: FOR side single-cluster at scan time — expected audit flag. The map's most conflation-prone leaf; crosslink to `n_assoc_causal` (`scope-aggregation`) is mandatory.

### `n_mech_sleep` — Does social media / device use displace or degrade adolescent sleep?
- claim to evaluate: **Social media and portable-device use displaces or degrades adolescent sleep (quantity and quality).**
- sourcing leads: source-scan §d_mech/sleep — Carter et al. JAMA Pediatrics 2016 (RECENCY FLAG: ≥10y in 2026 — refresh review required; JMIR 2024 meta is the refresh candidate) FOR; within-person JAMA Pediatrics meta (⚠ VERIFY direction) AGAINST/COMPLICATES.
- expected flags: screens-vs-social-media measurement mismatch is a standing caveat on the whole leaf.

### `n_policy_school` — Do school smartphone bans improve student mental health and academic outcomes?
- claim to evaluate: **School smartphone bans improve student mental health and academic outcomes.**
- sourcing leads: source-scan §d_policy/school — Abrahamsson 2024 (⚠ VERIFY magnitudes & girls-concentration; check for peer-reviewed version), NBER w34388 (⚠ VERIFY direction) FOR; Goodyear et al. Lancet Regional Health – Europe 2025 AGAINST (cross-sectional + school-hours-dose caveats; the awayfortheday.org critique is advocacy — position illustration only).
- expected flags: `context-transportability` crosslink Norway↔England; design mismatch must be foregrounded, not averaged away.

### `n_policy_deact` — Does individually reducing or deactivating social media improve wellbeing?
- claim to evaluate: **Individually reducing or deactivating social media use improves subjective wellbeing.**
- sourcing leads: source-scan §d_policy/deactivation — Allcott et al. 2020 FOR (adult sample caveat; find the reported n≈35k 2025 replication's primary paper before use — ⚠ VERIFY); Ferguson meta (disputed), Scientific Reports 2025 abstinence meta (⚠ VERIFY), ScienceDirect 2025 restriction meta (⚠ VERIFY) AGAINST/NULL.
- expected flags: rival meta-analyses of the same RCT pool — if both are used, their mutual dispute must be a typed crosslink (`empirical-contradiction`), not silently averaged. General-equilibrium caveat: short-run individual withdrawal ≠ never-adoption ≠ population-wide restriction.

### `n_policy_ban` — Do age-based platform bans actually reduce under-age social media use?
- claim to evaluate: **Age-based platform bans (the Australian under-16 model) effectively reduce under-age social media use.**
- sourcing leads: source-scan §d_policy/age-ban — BMJ-published June 2026 early evaluation (⚠ VERIFY exact citation; >85% of under-16s still using, circumvention widespread) AGAINST; FOR side expected THIN at authoring time — say so plainly.
- expected flags: one quarter of a leaky rollout; outcome is use, not mental health — `scope-aggregation` crosslink to the ban-rationale claims is mandatory. Fast-moving: re-search immediately before authoring.

## Non-scored structural nodes
- `n_root` (topic) → n_assoc, n_trend, n_mech, n_policy
- `n_assoc` (dimension) → n_assoc_magnitude, n_assoc_causal, n_assoc_hetero, n_assoc_benefits
- `n_trend` (dimension) → n_trend_real, n_trend_attrib
- `n_mech` (dimension) → n_mech_sleep
- `n_policy` (dimension) → n_policy_school, n_policy_deact, n_policy_ban

## Candidate crosslinks carried from the scan
See source-scan §candidate-crosslinks — six typed candidates, of which two
are mandatory per the tickets above (`n_trend_attrib`↔`n_assoc_causal`
scope-aggregation; `n_policy_ban`↔ban-rationale scope-aggregation).

## Graduation
Per [`../README.md`](../README.md), this topic graduates to
`tools/social-media-teen-mental-health/` when Phase 2 evidence-gathering
starts: move `nodes.json` into `tools/<slug>/data/`, this file into
`tools/<slug>/build-notes/`, and author `findings.json` /
`crosslinks.json` there under the protocol.
