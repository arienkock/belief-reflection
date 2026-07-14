# Preliminary source scan: Social Media and Adolescent Mental Health

_Compiled 2026-07-14 as raw material for Phase 2 findings tickets. This is a
scan, not a findings file: nothing below has been authored into a finding,
verified against full text, or audited by cluster yet. Every entry was
located via live search on the compile date; entries marked ⚠ VERIFY were
identified but not confirmed in enough detail to state their direction or
venue with confidence — check the full text before use. The sourcing
protocol (`../../docs/sourcing-protocol.md`) binds at findings-authoring
time, not here — but the no-fabrication rule is already in force: nothing
in this file is cited from memory alone._

Draft leaf IDs refer to the draft tree in [proposal.md](proposal.md).

---

## d_assoc — association and causation in individuals

### Leaf: heavier use is associated with worse depression/anxiety (magnitude)

**FOR (association exists, small-to-moderate):**
- Dose–response meta-analysis, *Time Spent on Social Media and Risk of
  Depression in Adolescents* (2022, PMC9103874) — per-hour dose–response on
  depression risk. Tier 1. Cluster hint: `dose-response-meta`.
- Systematic review + meta-analysis of 2020–2024 evidence, *Behavioral
  Sciences* 15(11):1450 (MDPI, 2025) — pooled r ≈ 0.22 between
  social-networking-site risk exposure and mental-health problems. Tier 1.
- Meta-analysis of problematic social media use, *JMIR Mental Health* 2022
  (9(4):e33450) — depression r = 0.27, anxiety r = 0.35. Tier 1. CAVEAT:
  "problematic use" is a clinical-adjacent construct, not time-spent — do
  not present as a time-use finding.

**AGAINST (association is trivially small / analysis-dependent):**
- Orben & Przybylski 2019, *Nature Human Behaviour* — specification-curve
  analysis across three large datasets; digital-technology use explains at
  most ~0.4% of variance in adolescent well-being; defensible analytic
  choices can produce positive, negative, or null. Tier 3 (methodological
  primary), strong within its claim. Cluster hint: `orben-przybylski`.
- Orben & Przybylski 2019, *Psychological Science* — time-use-diary
  replication of the above; same cluster (do NOT count as independent
  corroboration).
- CAVEAT for the whole leaf: associations measured from device logs run
  substantially weaker than self-report; every finding must state its
  measurement basis.

### Leaf: social media causally worsens adolescent mental health

**FOR:**
- Braghieri, Levy & Makarin 2022, *American Economic Review* 112(11):
  3660–3693, "Social Media and Mental Health" — staggered Facebook rollout
  across US colleges as a natural experiment; worsened student mental
  health; mechanism evidence points to unfavorable social comparison.
  Tier 3 quasi-experimental, strong identification. CAVEAT: college
  students circa 2004–2006, one platform — transportability to
  2020s adolescents not established. Cluster hint: `econ-quasiexp`.
- Allcott, Braghieri, Eichmeyer & Gentzkow 2020, *AER* 110(3), "The Welfare
  Effects of Social Media" — RCT, n≈2,743; four-week Facebook deactivation
  raised subjective well-being. CAVEAT: adults, not adolescents; overlapping
  author team with Braghieri et al. — consider shared cluster membership at
  audit time.

**AGAINST / COMPLICATES:**
- National Academies of Sciences, Engineering, and Medicine 2024, *Social
  Media and Adolescent Health* — consensus report: the committee's review
  "did not support the conclusion that social media causes changes in
  adolescent health at the population level," while affirming that specific
  design features can harm some young people. Tier 2 (national-academy
  synthesis), strong. Cluster hint: `NAS-2024`. NOTE: this source cuts
  differently on different leaves — attribution AGAINST here, benefits FOR
  below. Do not let one report dominate the audit (Immigration's
  single-source-heavy flags are the precedent).
- Ferguson, C.J. — meta-analysis of 27 social-media reduction experiments;
  pooled d ≈ 0.09 with CI including zero. ⚠ VERIFY venue and exact citation
  before use. MANDATORY CAVEAT: publicly disputed — Rausch & Haidt (SSRN
  5224958, 2025) allege factual errors in effect sizes, sample sizes, and
  inclusion criteria. If used, the finding must carry the dispute; it may
  not stand as a scored node's sole AGAINST support.
- Odgers & Jensen 2020 (review, *J. Child Psychology & Psychiatry*) —
  ⚠ VERIFY full citation; widely referenced position that associations are
  small and causal evidence limited.

### Leaf: effects are concentrated in vulnerable subgroups / developmental windows

**FOR:**
- Orben, Przybylski, Blakemore & Kievit 2022, *Nature Communications*
  13:1649, "Windows of developmental sensitivity to social media" — two UK
  datasets (n = 84,011; longitudinal n = 17,409): higher use predicts lower
  life satisfaction one year later specifically for girls at 11–13, boys at
  14–15, both sexes at 19. Tier 3, large-sample longitudinal. NOTE: same
  `orben-przybylski` cluster as the null-leaning association work — an
  instructive within-cluster nuance, not a contradiction.

**AGAINST:** not yet located in this scan — targeted Phase 2 search needed
(candidate framing: studies failing to replicate age/sex-specific windows).
If none is found, mark the leaf thin per protocol; do not pad.

---

## d_trend — the population trend

### Leaf: adolescent mental health genuinely deteriorated since ~2010

**FOR:**
- Twenge, Joiner, Rogers & Martin 2018, *Clinical Psychological Science* —
  US adolescent depressive symptoms, suicide-related outcomes, and suicide
  rates rose after 2010, especially among girls; rises include objectively
  measured outcomes (suicide), resisting a pure reporting-artifact reading.
  Tier 3. Cluster hint: `twenge`. CAVEAT: advocacy-adjacent author position;
  correlational trend work.
- Norwegian measurement-invariance study, *Psychological Medicine* (2024,
  PMC11578914), "Time trends in adolescent depressive symptoms from 2010 to
  2019 in Norway: real increase or artifacts of measurements?" — instrument
  found measurement-invariant across time; latent-mean rise among girls from
  2014 supports a real increase. Tier 3, directly answers the artifact
  objection. Cluster hint: `nordic-trend`.

**AGAINST (artifact / reporting-change hypothesis):**
- The artifact position is actively debated (the Norwegian paper exists
  because of it) but this scan did not capture a strong standalone source
  arguing it. Phase 2 targeted search needed (candidates: diagnostic-code
  and help-seeking-change studies). If the best available AGAINST is weak,
  flag honestly rather than padding.

### Leaf: social media adoption is the principal driver of the deterioration

**FOR:**
- Twenge et al. 2018 (above) — links the timing to new-media screen time.
  Same `twenge` cluster; may not corroborate itself across leaves.
- Twenge 2020, *Psychiatric Research and Clinical Practice* — mechanism
  review for the post-2012 rise. Same cluster.

**AGAINST:**
- NAS 2024 consensus report (above) — declines population-level causal
  attribution. Tier 2.
- Orben & Przybylski association-magnitude work (above) — an exposure this
  weakly associated at the individual level is hard to scale into the
  principal population driver without further assumptions. CAVEAT: this is
  an inference, not a stated conclusion of the papers — findings text must
  not overstate it.
- EXPECTED AUDIT FLAG: FOR side of this leaf is currently single-cluster
  (`twenge`). This is the most conflation-prone leaf in the whole map —
  in public debate it inherits confidence from the association leaf. Keep
  the claims separate.

---

## d_mech — mechanisms

### Leaf: social media use displaces or degrades adolescent sleep

**FOR:**
- Carter, Rees, Hale et al. 2016, *JAMA Pediatrics* 170(12):1202–08 —
  meta-analysis: portable-device access or use associated with reduced
  sleep quantity and quality in 6–19-year-olds; effect present even for
  device *access without use*. Tier 1. RECENCY FLAG: ≥10 years old in 2026 —
  refresh-review required by protocol.
- Updated systematic review + meta-analysis, *J. Medical Internet Research*
  2024 (26:e48356), electronic media use and sleep quality. Tier 1 —
  candidate refresh for Carter. ⚠ VERIFY adolescent subgroup and direction
  detail against full text.

**AGAINST / COMPLICATES:**
- Within-person meta-analysis, *JAMA Pediatrics* (2025?, article 2845524),
  "Within-Person Association Between Daily Screen Use and Sleep in Youth" —
  ⚠ VERIFY direction; within-person designs typically shrink between-person
  associations, which is the credible AGAINST framing here.
- CAVEAT for leaf: most of this literature is *screens/devices*, not social
  media specifically — the leaf claim must either say "screens incl. social
  media" or the mismatch must be a standing caveat.

### Leaf: social comparison / algorithmic amplification is the operative pathway

**FOR:**
- Braghieri et al. 2022 mechanism evidence (unfavorable social comparison).
- NAS 2024 — identifies algorithmically driven amplification and design
  features as plausible harm channels.

**AGAINST:** displacement-hypothesis alternatives; not yet sourced —
Phase 2 search needed. Consider whether this leaf survives Phase 1 at all:
mechanism claims may be better handled as `depends_on` text plus crosslinks
than as a scored leaf. DECISION FOR PHASE 1.

---

## d_policy — what restriction measurably changes

### Leaf: school smartphone bans improve mental health and academic outcomes

**FOR:**
- Abrahamsson 2024, "Smartphone Bans, Student Outcomes and Mental Health"
  (NHH Discussion Paper 01/2024; SSRN 4735240) — Norwegian school-level ban
  timing as causal identification; reports improvements. ⚠ VERIFY headline
  magnitudes and the commonly-cited concentration among girls against full
  text; working paper — check for a peer-reviewed version by Phase 2.
  Cluster hint: `nordic-ban`.
- NBER Working Paper 34388, "The Impact of Cellphone Bans in Schools on
  Student Outcomes" — ⚠ VERIFY direction and outcomes before assigning.

**AGAINST:**
- Goodyear et al. 2025, *Lancet Regional Health – Europe* (SMART Schools) —
  cross-sectional, 1,227 adolescents / 30 English schools: no difference in
  mental wellbeing between restrictive and permissive school phone policies.
  Tier 3. CAVEAT: cross-sectional; contrasts school *policy*, i.e. a few
  school-hours of exposure difference, not total use — a null here is
  consistent with total-use effects. Published methodological criticism
  exists (advocacy-adjacent, e.g. awayfortheday.org — position illustration
  only, never evidential basis).
- Companion commentary, *Lancet Regional Health – Europe* 2025, "Smartphone
  use and mental health: going beyond school restriction policies" — argues
  restriction-policy evidence is thin relative to policy momentum. Same
  Lancet cluster as SMART Schools for audit purposes — check authorship
  overlap.

### Leaf: individual deactivation/reduction improves subjective wellbeing

**FOR:**
- Allcott et al. 2020 *AER* deactivation RCT (above; adult-sample caveat).
- Large-scale 2025 Stanford-affiliated deactivation replication reported at
  n≈35,000 — ⚠ VERIFY: located only via secondary coverage (PetaPixel);
  find the primary paper before any use.

**AGAINST / NULL:**
- Ferguson reduction-experiment meta-analysis (above, with mandatory
  dispute caveat).
- "The effects of social media abstinence on affective well-being and life
  satisfaction: a systematic review and meta-analysis," *Scientific Reports*
  2025 — ⚠ VERIFY direction; abstinence-RCT metas commonly find small or
  mixed effects.
- "The effects of social media restriction: meta-analytic evidence from
  randomized controlled trials" (ScienceDirect, 2025) — ⚠ VERIFY.
- LEAF-LEVEL CAVEAT: short-run abstinence RCTs measure days-to-weeks of
  individual withdrawal-plus-substitution; they do not estimate the effect
  of never-adopting or of population-wide restriction (general-equilibrium
  point — crosslink candidate to the ban leaves, type
  `context-transportability`).

### Leaf: age-based platform bans reduce under-age use and harm (Australia)

**FOR:** no credible early evidence of use reduction located yet. If Phase 2
confirms, this side is thin-by-honesty at authoring time — say so.

**AGAINST (early implementation evidence):**
- BMJ-published early evaluation (June 2026): three months after Australia's
  December 2025 under-16 restrictions, >85% of under-16s still using major
  platforms; little change at 12–13, slight decrease at 14–15, increase at
  16+; circumvention (borrowed/fake accounts, age-check bypass) widespread.
  ⚠ VERIFY exact citation (journal, authors) — located via BMJ Group press
  release and syndicated coverage (techxplore.com, phys.org). Tier 3.
- STANDING CAVEAT for leaf: outcome measured is *use and circumvention*,
  not mental health, over one quarter of a chaotic rollout. An early null
  on use-reduction is not evidence about mental-health effects of a
  well-enforced ban — this is the mirror image of the pro-ban conflation
  and deserves an explicit crosslink (`scope-aggregation`).

---

## Cross-cutting benefits (placement decided in Phase 1)

### Candidate leaf: social media provides real benefits (community for marginalized youth)

**FOR:**
- NAS 2024 — names community formation for marginalized youth (incl. LGBTQ+
  adolescents) and everyday social connection as genuine benefits. Tier 2.

**AGAINST:** not yet sourced. Phase 2 search needed; if the contrary
literature is thin, flag it — the both-directions rule cuts this way too.

---

## Candidate crosslinks (typed per `crosslinks.json` conventions)

1. Orben/Przybylski tiny-association ↔ Braghieri causal harm —
   `assumption-sensitivity` (self-report cross-sectional variance-explained
   vs. quasi-experimental adoption effects can both be true; they answer
   different questions).
2. Deactivation-RCT gains ↔ abstinence-meta nulls — `empirical-contradiction`
   (pending ⚠ VERIFY on the metas).
3. Abrahamsson Norway benefits ↔ Goodyear England null —
   `context-transportability` (different countries, designs, and policy
   dosages).
4. Australia early circumvention ↔ ban-rationale claims —
   `scope-aggregation` (use-reduction ≠ mental-health outcome).
5. Twenge trend attribution ↔ NAS population-level agnosticism —
   `empirical-contradiction`.
6. Individual-level causal harm ↔ population-trend attribution —
   `scope-aggregation` (the public debate's central conflation; make it
   explicit in the tool).

## Known gaps after this scan (Phase 2 to-do)

- A strong standalone AGAINST source for the "real deterioration" leaf
  (artifact hypothesis).
- Any AGAINST for developmental-windows heterogeneity.
- Any AGAINST for the benefits leaf.
- Primary citations for every ⚠ VERIFY entry above.
- Non-Anglosphere evidence generally — current scan is US/UK/Norway/Australia
  heavy; expect a standing `caveat` mirroring Immigration's "US-centric"
  flags.
