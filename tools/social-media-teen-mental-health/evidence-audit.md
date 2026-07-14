# Evidence Audit (v1)
_Generated 2026-07-14. This audit does not count findings (vote-counting double-counts shared sources). It collapses by **source_cluster** and reports independent corroboration per direction, plus standing honesty flags._

## Scored leaf nodes — independent corroboration
`claim_evaluated` is the affirmative proposition; S = evidence FOR it, C = AGAINST. Cells show **distinct source clusters** (independent bodies of work), not raw finding counts.

| node / claim | S clusters | C clusters | X | flags |
|---|---|---|---|---|
| `n_assoc_magnitude` — Heavier social media use is associated with worse depression/anxiety in adolescents at a magnitude that is practically meaningful, not trivially small. | 3 | 2 | 0 | ok |
| `n_assoc_causal` — Social media use causally worsens adolescent mental health. | 2 | 2 | 1 | ok |
| `n_assoc_hetero` — Negative effects of social media are concentrated in specific subgroups and developmental windows (notably girls in early adolescence) rather than spread uniformly. | 3 | 0 | 0 | no independent AGAINST; one-sided |
| `n_assoc_benefits` — Social media provides real mental-health-relevant benefits to some adolescents — community, connection, and support, especially for marginalized youth. | 1 | 0 | 1 | no independent AGAINST; one-sided |
| `n_trend_real` — Adolescent mental health has genuinely deteriorated since ~2010; the rise is not an artifact of changed reporting, screening, or diagnostic practice. | 2 | 0 | 1 | no independent AGAINST; one-sided |
| `n_trend_attrib` — Social media adoption is the principal driver of the post-2010 deterioration in adolescent mental health. | 1 | 2 | 0 | FOR single-cluster: twenge supplies all 2 FOR findings |
| `n_mech_sleep` — Social media and portable-device use displaces or degrades adolescent sleep (quantity and quality). | 1 | 1 | 0 | ok |
| `n_policy_school` — School smartphone bans improve student mental health and academic outcomes. | 2 | 1 | 1 | ok |
| `n_policy_deact` — Individually reducing or deactivating social media use improves subjective wellbeing. | 1 | 2 | 1 | FOR single-cluster: allcott-gentzkow supplies all 2 FOR findings |
| `n_policy_ban` — Age-based platform bans (the Australian under-16 model) effectively reduce under-age social media use. | 0 | 1 | 1 | no qualifying FOR; one-sided |

## Notes on flagged nodes
- **`n_assoc_hetero`** (no independent AGAINST; one-sided). Three independent clusters support concentration of harm (orben-przybylski windows; twenge trend asymmetry; nordic-ban policy-response heterogeneity), but a targeted search found no qualifying non-replication of the age/sex windows. Marked thin rather than padded; the strongest counter-reading (tiny averages) lives on `n_assoc_magnitude` and is crosslinked.
- **`n_assoc_benefits`** (one-sided, single-source FOR). NAS-2024 is the only qualifying FOR cluster; Odgers-review carries the both-directions nuance as COMPLICATES. No credible AGAINST located — flagged thin, not manufactured.
- **`n_trend_real`** (no full AGAINST). The measurement-artifact hypothesis is carried honestly as a COMPLICATES sourced from within a pro-real-increase paper (nordic-trend); a standalone quantitative artifact source did not qualify under the protocol at authoring time. Thin.
- **`n_trend_attrib`** (FOR single-cluster). Both FOR findings are the twenge cluster — the audit treats them as one body of work. Two independent clusters (NAS-2024, odgers-review) push AGAINST. This is the map's most conflation-prone claim and is double-crosslinked to `n_assoc_causal`.
- **`n_policy_ban`** (no qualifying FOR; one-sided). The FOR slot is deliberately empty — no measured evidence that age bans reduce use existed at authoring time. The single AGAINST cluster (aus-ban-eval) is three months of a leaky rollout; the node is scoped to USE, not mental health, and flagged thin.
- **`n_mech_sleep`** (single cluster per direction). Two strong meta-analyses, one per direction (carter-sleep-meta between-person; uq-withinperson-meta within-person). The disagreement is the design contrast itself — typed as an assumption-sensitivity crosslink.
- Counter-signal preserved: `n_assoc_causal` and `n_policy_deact` carry independent clusters AGAINST their own claims (NAS-2024, reduction-rct-pool, antwerp-abstinence-meta) — evidence against was retained, not pruned.

## Source concentration (non-independence)
- Most-used clusters across all 41 findings: NAS-2024 (6), odgers-review (6), twenge (4), allcott-gentzkow (3), reduction-rct-pool (3), orben-przybylski (2).
- The audit collapses to clusters per direction within each node, so e.g. NAS-2024 cannot supply 'independent' corroboration to itself, and the two allcott-gentzkow RCTs count once.
- Cluster note: reduction-rct-pool deliberately spans Ferguson 2024 AND its 2025 reanalysis — they analyze the same experiment pool and must not corroborate each other.

## Source-tier & recency sweep
- Tertiary/aggregator/advocacy-press sources used as evidential basis: **0** (target: 0). Press coverage was used only to LOCATE primary sources during the scan.
- Advocacy/think-tank sources as labelled position evidence: none used. The After Babel critiques of Ferguson are carried inside caveats as a documented dispute, not as findings.
- Sources ≥~10 years old, flagged for refresh review: ['carter-sleep-meta' (2016)].
- Working papers (not yet peer-reviewed at authoring, flagged in caveats): Abrahamsson 2024 (nordic-ban), Figlio & Özek 2025 (nber-florida), Allcott-Gentzkow 2025 (allcott-gentzkow w33697).
- Evidence-type mix: review 18, theoretical 8, observational 8, quasi-experimental 4, experimental 3. Observational findings carry an explicit correlational caveat.
