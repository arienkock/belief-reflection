# Proposal: Ultra-Processed Foods and Health

_Proposed 2026-07-15. Status: **draft — pre-Phase-1**. The dimension sketch
below is the pre-freeze draft; once nodes are frozen it will be superseded by
`nodes.json` and `phase1-to-phase2-handoff.md`, and where they differ the
frozen tree and the handoff's decision log govern._

## Working title and scope

**Ultra-processed foods and health.** One sentence: what does the evidence
actually show about the health effects of ultra-processed foods (UPF, as
defined by the NOVA classification) in adults — is the observed harm
attributable to *processing itself* or to the nutrients and dietary patterns
that processing travels with, and what would UPF-specific policy measurably
change?

## Why this topic (selection rationale)

Chosen as the third tool (after Immigration and Social Media & Teen Mental
Health) for three reasons:

1. **Public salience is at a peak and policy is being written right now.**
   The US FDA and USDA opened a joint process in 2025 to define "ultra-
   processed food" for the first time (>5,000 public comments), with a
   federal definition targeted for 2026 that would flow into school-food
   rules, procurement, warning labels, and dietary guidance under the "Make
   America Healthy Again" agenda. The 2025–2030 Dietary Guidelines pointedly
   declined to name UPF. The *Lancet* published a three-paper UPF Series in
   November 2025. Governments are legislating a category whose scientific
   status is openly contested.
2. **The evidence base is genuinely two-sided at high tiers — and the
   dispute is a conflation the tool format is built to separate.** There are
   umbrella reviews of millions of participants linking UPF to mortality and
   chronic disease (Lane et al., *BMJ* 2024), a tightly-controlled inpatient
   RCT showing processing *causes* ~500 kcal/day of excess intake (Hall et
   al., *Cell Metabolism* 2019) and a 2025 *Nature Medicine* crossover trial
   finding more weight loss on minimally-processed diets — set against
   large cohorts whose associations *attenuate* once diet quality is
   controlled (Fang et al., *BMJ* 2024), poor inter-rater reliability of the
   NOVA classification itself (Braesco et al., Fleiss' κ ≈ 0.3), and a US
   advisory committee that reviewed the same literature and found it
   **insufficient** to make a UPF-specific recommendation. Every scored leaf
   can be sourced in both directions.
3. **The evidence base changed recently.** The first long-duration
   real-world UPF-vs-minimally-processed RCT (2025), the first UMBRELLA-level
   synthesis (2024), the DGAC's explicit non-recommendation (2024), and the
   Lancet Series (2025) all postdate older reviews — a snapshot now captures
   a live turning point.

### Why this topic was previously deferred — and why that no longer holds

The Social Media tool's proposal explicitly deferred UPF: *"high salience,
but the leaf claims are harder to make falsifiable-in-principle (definitional
fights over the NOVA classification would dominate), partially failing the
'not primarily definitional' test."* That concern was correct and is met
head-on here rather than waved away:

- The definitional problem is promoted to **its own scored leaf**
  (`n_concept_reliable`: can NOVA be applied consistently?), where the poor
  inter-rater reliability is the evidence the participant rates — instead of
  being an unscored fog hanging over every other claim. Isolating the
  definitional question is exactly what this tool format does well.
- The genuinely empirical claims are **separable from** the definitional
  one. Controlled-feeding RCTs (Hall 2019; Dicken 2025) manipulate
  processing directly and measure intake/weight; they are falsifiable-in-
  principle regardless of whether NOVA is a tidy taxonomy. So is "does the
  cohort association survive adjustment for nutrients?" and "do warning
  labels change purchases?"
- The residual values/definitional matter — *should* there be a UPF category
  in policy at all — is handled as a coverage-note scope boundary, not
  scored.

In short, the property that made UPF a poor fit for a single up-or-down tool
is the property this multi-leaf tool is designed to exploit.

**Alternatives considered and deferred this session** (not rejected —
candidates for later iterations):

- *School vouchers / education savings accounts* — strong, genuinely
  contested tree (test-score effects, fiscal impact on public schools,
  competitive effects, pop-up-provider quality) and very high 2026 salience
  (universal ESAs, 200+ state bills). Deferred mainly because a chunk of the
  live dispute is values (parental-choice rights, public-vs-private
  purpose), which risks the "not primarily moral" criterion; strong
  candidate for a future session that scopes tightly to the empirical
  leaves.
- *Return-to-office mandates and productivity* — high salience, but the
  productivity evidence is currently lopsided (no RCTs; observational and
  quasi-experimental work largely finds no productivity gain from RTO), so
  several leaves would be thin-AGAINST rather than genuinely two-sided. Same
  young-literature weakness flagged for "remote work" in the prior proposal.
- *Minimum-wage employment effects* and *nuclear energy safety/cost* —
  carried over as deferred from the Social Media proposal; salience lower or
  leaves one-sided at high tiers.

## Fit against the candidate-topic criteria

- **Splits into an honest question tree** — "are ultra-processed foods bad
  for you?" hides at least five separately-measured questions: (a) is the
  NOVA category even reliably applicable; (b) how large is the observational
  association with disease; (c) does that association reflect *processing* or
  the nutrients/patterns it correlates with; (d) does controlled evidence
  show processing itself causes harm; (e) what would UPF-specific policy
  change. These have *different* answers and *different* evidence quality —
  the point of the tool.
- **A scored leaf can go either way on the literature** — see the
  [source scan](source-scan.md): every draft leaf has credible tier-1/tier-2
  sourcing in both directions except where flagged thin (and those flags are
  named in advance).
- **Not primarily moral or definitional** — the *definitional* dispute is
  real, so rather than pretend it away it is scored as one leaf and bounded
  by scope notes. The core of the topic is measured effects (intake, weight,
  mortality, purchases). Two traps handled in scope notes: (a) "processed"
  ≠ "ultra-processed" — canned beans and fresh bread are processed but not
  NOVA-4; findings must state the exposure definition used; (b) whether a
  UPF category *should* drive policy is partly a values question — the tool
  scores only what policies measurably change, not whether they are
  justified.

## Draft root question

> **What does the evidence show about ultra-processed foods and health — and
> is it the processing, or the nutrients the processing carries?**

(Simple register: *Are ultra-processed foods bad for you?*)

Root `depends_on`: "bad for you" is not one measurable quantity. The
literature separately measures whether the UPF category is reliably
definable, the size of the observational disease association, whether that
association is about processing or about nutrients/lifestyle, whether
controlled trials show processing itself causes harm, and what UPF policy
changes — with sharply different degrees of consensus. Public and political
debate routinely lets confidence on one of these stand in for all of them.

## Expected dimensions (draft, not frozen)

1. **`d_concept` — Is "ultra-processed" a valid, usable category?**
   - NOVA can be applied consistently/reliably (inter-rater reliability).
   - UPF status predicts harm *beyond* what conventional nutrient profiling
     (sugar/salt/sat-fat/energy density) already captures.
2. **`d_assoc` — Observational association with disease.**
   - Higher UPF consumption is associated with worse health outcomes
     (all-cause mortality, cardiometabolic disease) at a meaningful
     magnitude.
   - The association reflects processing rather than being explained away by
     nutrient quality / confounding / healthy-user bias.
   - Harms are concentrated in specific UPF subgroups (processed meats,
     sugary drinks) rather than uniform across all UPF.
3. **`d_cause` — Does processing itself cause harm? (controlled trials)**
   - Ultra-processed diets cause excess energy intake / weight gain
     independent of nutrient composition.
4. **`d_policy` — What would UPF-specific policy change?**
   - The evidence is strong enough to justify UPF-specific dietary guidance
     (vs. nutrient-based guidance).
   - Front-of-pack warning labels reduce purchases of targeted products.

Roughly 8 scored leaves across 4 dimensions — comparable to the prior tools
(10–11 leaves / 4 dimensions).

## Coverage note (what this map deliberately leaves out)

DELIBERATELY NOT COVERED (invisible to this tool): "food addiction" as a
clinical construct (its own contested literature — Gearhardt vs. critics);
specific additives and their individual toxicology (emulsifiers, nitrites,
non-sugar sweeteners) as separate scored claims; environmental and food-
system sustainability arguments; children/adolescents as a separate
population (the map is adult-focused, mirroring where the RCT and cohort
evidence sits); eating-disorder outcomes; food-industry political-economy
and marketing-to-children (touched only where a policy finding carries it);
and whether restricting UPF is *justified all things considered* — a values
question the tool records no verdict on. Absence is a scope choice, not
evidence of no effect. Two definitional boundaries to hold: "processed" is
not "ultra-processed" (NOVA group 3 vs 4), and nutrient-targeted policy
(e.g. sugar labels) is not the same as processing-targeted policy — findings
must not silently swap them.

## Known sourcing hazards (flag at authoring time)

- **The originators are advocates.** The NOVA/UPF concept's principal
  authors (Monteiro and colleagues) are also its leading policy advocates
  (the 2025 Lancet Series). Their syntheses are permitted as position
  evidence but must be labelled, and may not be a scored node's sole
  support — mirror the Immigration/Twenge handling.
- **Self-reported diet.** Almost all cohort evidence rests on food-frequency
  questionnaires; associations and their attenuation both inherit that
  measurement error. State the design on every observational finding.
- **Attenuation-after-adjustment cuts both ways.** Reviews disagree on
  whether UPF associations "remain unchanged" or "substantially attenuate"
  after diet-quality adjustment; the pivotal `n_assoc_confound` leaf must
  carry both, not pick a side.
- **Nutrient-label ≠ UPF-label.** The strongest policy evidence (Chile)
  concerns *nutrient* warning labels, not NOVA-processing labels — its
  transportability to UPF-specific policy is an assumption, flagged as a
  mandatory crosslink.
- **RCTs are small/short and their generalisability is contested.** Hall
  2019 (n=20, 2 weeks) and Dicken 2025 (n=55) are the causal backbone;
  Nature Medicine published formal critiques of the latter. Carry the
  disputes.

## Why now

A federal UPF definition is being drafted in 2026 that will trigger
labelling, procurement, and guidance downstream, while the strongest US
advisory synthesis declined to recommend limiting UPF and the NOVA category
fails inter-rater reliability tests — yet cohort and controlled-trial
evidence of real harm also exists. The public conversation treats "UPF is
associated with disease," "processing itself is the cause," "the category is
well-defined," and "UPF policy will work" as one claim. That is precisely
the conflation this tool format exists to pull apart, and the policy window
is open now.

## Next step

Phase 1 node authoring: freeze the node tree (root, dimensions, leaf
`claim_evaluated` wording) per `../../docs/README.md`, then open per-leaf
findings tickets under `../../docs/sourcing-protocol.md`. The
[source scan](source-scan.md) is the raw material for those tickets, not a
substitute for them.
