# Proposal: Social Media and Adolescent Mental Health

_Proposed 2026-07-14. Status: **Phase 1 complete — nodes frozen 2026-07-14**;
see [`nodes.json`](nodes.json) and
[`phase1-to-phase2-handoff.md`](phase1-to-phase2-handoff.md). The dimension
sketch below is the pre-freeze draft, kept for the record; where it differs
from `nodes.json` (e.g. the mechanism-pathway leaf was cut), the frozen tree
and the handoff's decision log govern._

## Working title and scope

**Social media and adolescent mental health.** One sentence: what does the
evidence actually show about the effects of social media use on the mental
health of adolescents (roughly ages 10–19) in high-income countries, and what
do restriction policies (school phone bans, deactivation, age-based platform
bans) demonstrably change?

## Why this topic (selection rationale)

Chosen as the next iteration after Immigration for three reasons:

1. **Public salience is at a peak and policy is outrunning evidence.**
   Australia's world-first under-16 platform ban took effect December 2025;
   France, the UK, Denmark, Greece, and Malaysia announced or passed similar
   measures in late 2025 / 2026. Governments are legislating now, while
   researchers publicly dispute whether the causal evidence supports the
   intervention at all.
2. **The evidence base is genuinely contested in both directions at high
   tiers.** This is not a manufactured "both sides": there are
   quasi-experimental studies finding real harm (Braghieri et al., *American
   Economic Review* 2022), large RCTs finding wellbeing gains from
   deactivation (Allcott et al., *AER* 2020), specification-curve analyses
   finding near-zero associations (Orben & Przybylski, *Nature Human
   Behaviour* 2019), meta-analyses whose confidence intervals include zero
   (Ferguson 2024) that are themselves under published attack for factual
   errors, and a National Academies consensus report (2024) that explicitly
   declined to endorse a population-level causal conclusion. Every scored
   leaf can be sourced in both directions without padding.
3. **The evidence base has changed recently.** Post-ban natural experiments
   are now arriving (first evaluations of the Australian ban published June
   2026; Norwegian and English school-phone-ban studies 2024–2025), so a
   snapshot now captures a live turning point that older syntheses miss.

**Alternatives considered and deferred** (not rejected — candidates for later
iterations):

- *Minimum wage employment effects* — excellent contested literature
  (Card/Krueger vs. Neumark traditions) but salience is currently lower and
  the debate is largely stable; less "why now."
- *Ultra-processed foods and health* — high salience, but the leaf claims are
  harder to make falsifiable-in-principle (definitional fights over the NOVA
  classification would dominate), partially failing the "not primarily
  definitional" test.
- *Nuclear energy safety and cost* — strong question tree, but several leaves
  are one-sided at high tiers (e.g. deaths/TWh) and would mostly get flagged
  thin-AGAINST rather than genuinely contested.
- *Remote work and productivity* — viable, but the literature is young,
  heavily working-paper based, and firm-outcome-centric; weaker fit for the
  sourcing protocol's tier ordering.

## Fit against the candidate-topic criteria

- **Splits into an honest question tree** — "is social media bad for teens?"
  hides at least four separately-measured questions: the size of the
  cross-sectional association, whether the effect is causal, whether it
  explains the population-level trend since ~2010, and whether restriction
  policies work. These have *different* answers with *different* evidence
  quality, which is exactly the point of the tool.
- **A scored leaf can go either way on the literature** — see the
  [source scan](source-scan.md): every draft leaf has credible tier-1/tier-2
  sourcing in both directions except where flagged thin.
- **Not primarily moral or definitional** — the core dispute is about
  measured effects. Two definitional traps must be handled in scope notes
  rather than argued: (a) "screen time" ≠ "social media use" — the map is
  about social media and must not import general-screen-time findings as if
  equivalent; (b) whether an age ban is *justified* is a values question
  (autonomy, proportionality) — the tool scores only the empirical claims
  about what bans measurably change.

## Draft root question

> **What does the evidence say about social media's effects on adolescent
> mental health — and on which question, exactly?**

(Simple register: *Is social media harming teenagers?*)

Root `depends_on`: "harmful" is not one measurable quantity. The literature
measures (at least) association, causation, trend attribution, mechanism, and
policy response separately, and the degree of consensus differs sharply
between them. High confidence on one leaf does not transfer to its
neighbours — this topic is unusually prone to exactly that transfer error in
public debate.

## Expected dimensions (draft, not frozen)

1. **`d_assoc` — Association and causation in individuals.** Draft leaves:
   - Heavier social media use is associated with worse depression/anxiety in
     adolescents (magnitude of the correlational association).
   - Social media use *causally* worsens adolescent mental health
     (quasi-experimental / experimental evidence).
   - Effects are concentrated in vulnerable subgroups (girls, specific
     developmental windows) rather than uniform.
2. **`d_trend` — The population trend.** Draft leaves:
   - Adolescent mental health has genuinely deteriorated since ~2010 (vs.
     reporting/measurement artifact).
   - Social media adoption is the principal driver of that deterioration.
3. **`d_mech` — Mechanisms.** Draft leaves:
   - Social media use displaces or degrades adolescent sleep.
   - Social comparison / algorithmic amplification is the operative harm
     pathway (vs. displacement of other activities).
4. **`d_policy` — What restriction measurably changes.** Draft leaves:
   - School smartphone bans improve student mental health and academic
     outcomes.
   - Individual deactivation/reduction improves subjective wellbeing.
   - Age-based platform bans reduce under-age use and harm (the
     Australian test case).

Roughly 10 scored leaves across 4 dimensions — comparable in size to the
Immigration tool (11 leaves / 4 dimensions).

## Coverage note (what this map deliberately leaves out)

DELIBERATELY NOT COVERED (invisible to this tool): content-specific harms
with their own distinct literatures (cyberbullying prevalence, grooming and
exploitation, CSAM, pro-eating-disorder and self-harm content exposure);
"problematic use"/addiction as a clinical construct; effects on *adults*;
benefits and harms to civic life, polarization, and attention/academics
beyond what the policy leaves capture; physical-health outcomes (obesity,
myopia); platform-by-platform design comparisons; and privacy/data-rights
harms. Also out of scope: whether age bans are *justified all things
considered* — that is a values question the tool records no verdict on.
Absence is a scope choice, not evidence of no effect. One inclusion to note:
the *benefits* direction (community for marginalized youth, e.g. LGBTQ+
adolescents) is inside scope and must be sourced good-faith, not treated as
an afterthought — the National Academies report treats it as a real finding.

## Known sourcing hazards (flag at authoring time)

- **Advocacy-adjacent secondary literature on both sides.** The After Babel
  Substack (Haidt/Rausch) and equivalent skeptic blogs are position
  illustrations under the protocol, never evidential basis — even though
  both routinely cite primary work worth chasing.
- **Contested meta-analyses.** Ferguson (2024) has published corrections/
  critiques against it (Rausch & Haidt, SSRN 2025); if used, the caveat must
  carry the dispute. Conversely, abstinence-RCT meta-analyses pooling
  heterogeneous durations/outcomes have the mirror-image problem.
- **Self-report inflation.** Associations shrink substantially when use is
  measured from device logs rather than self-report; findings should state
  the measurement basis.
- **Fast-moving policy evidence.** Australian-ban evaluations are months
  old, preprint-adjacent, and measure *use/circumvention*, not yet mental
  health. Early nulls on use-reduction must not be laundered into "bans
  don't affect mental health."

## Why now

Multiple governments are implementing bans in 2026 on a stated
mental-health rationale while the strongest available syntheses decline to
endorse population-level causation — the public conversation is treating
"the association exists," "it's causal," "it explains the trend," and "bans
will fix it" as one claim, which is precisely the conflation this tool
format exists to pull apart. The first post-ban outcome data will land over
the next 12–18 months; a map built now can absorb it leaf-by-leaf.

## Next step

Phase 1 node authoring: freeze the node tree (root, dimensions, leaf
`claim_evaluated` wording) per `docs/README.md`, then open per-leaf
findings tickets under `docs/sourcing-protocol.md`. The
[source scan](source-scan.md) is the raw material for those tickets, not a
substitute for them.
