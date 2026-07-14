# Evidence Audit (v2)
_Generated 2026-06-30. This audit no longer counts findings (vote-counting double-counts shared sources). It collapses by **source_cluster** and reports independent corroboration per direction, plus standing honesty flags._

## Scored leaf nodes — independent corroboration
`claim_evaluated` is the affirmative proposition; S = evidence FOR it, C = AGAINST. Cells show **distinct source clusters** (independent bodies of work), not raw finding counts.

| node / claim | S clusters | C clusters | X | flags |
|---|---|---|---|---|
| `n_econ_wages_overall` — Immigration lowers wages/employment for native-born workers overall. | 1 | 1 | 1 | ok |
| `n_econ_wages_lowskill` — Immigration lowers wages/employment for low-skilled natives and prior immigrants. | 2 | 1 | 1 | ok |
| `n_econ_gdp_pc` — Immigration raises GDP per capita, not merely aggregate GDP. | 1 | 1 | 1 | ok |
| `n_fiscal_highskill` — High-skilled immigrants are net fiscal contributors. | 1 | 0 | 1 | no independent AGAINST; one-sided/single-source |
| `n_fiscal_lowskill` — Low-skilled immigrants are a net fiscal drain. | 1 | 1 | 1 | ok |
| `n_fiscal_horizon` — Counting descendants and the long run, immigration is fiscally positive. | 1 | 1 | 1 | ok |
| `n_innov_share` — Immigrants contribute disproportionately to patents and entrepreneurship. | 2 | 0 | 1 | no independent AGAINST |
| `n_innov_complement` — High-skilled immigrants complement rather than crowd out native innovators. | 2 | 1 | 0 | ok |
| `n_social_crime` — Immigration increases crime. | 1 | 3 | 1 | ok |
| `n_social_trust` — Immigration / ethnic diversity erodes social trust and cohesion. | 2 | 2 | 1 | ok |
| `n_social_integration` — Immigrants and their descendants integrate over generations. | 1 | 1 | 1 | ok |

## Notes on flagged nodes
- **`n_fiscal_highskill`** (no independent AGAINST; one-sided/single-source). FOR is corroborated by two independent clusters (Dallas Fed reading of NAS; OECD). The lack of an AGAINST is genuine near-consensus, carried honestly as the public-goods COMPLICATES caveat, not a manufactured challenge.
- **`n_innov_share`** (no independent AGAINST). The descriptive over-representation is corroborated across independent clusters (Diamond; Kerr/NBER). The live dispute is about *why* (composition), carried as COMPLICATES. No AGAINST exists because the descriptive count is not seriously contested.
- Counter-signal preserved: `n_econ_wages_lowskill` and `n_fiscal_lowskill` carry independent clusters AGAINST their own claim — evidence against the node's proposition was retained, not pruned.

## Source concentration (non-independence)
- Most-used clusters across all 46 findings: NAS-2016 (16), OECD-migration (7), Dinesen-2020 (4), DallasFed-2017 (3), Borjas-2016 (2).
- The audit above neutralises this by collapsing to clusters per direction, so e.g. NAS-2016 cannot supply 'independent' corroboration to itself within a node.

## Source-tier & recency sweep
- Tertiary/aggregator/advocacy-press sources used as evidential basis: **0** [] (target: 0).
- Advocacy/think-tank sources (permitted only as labelled position evidence): ['F-wl-2', 'F-inn-1', 'F-is-3'] — each flagged in its finding `caveat`.
- Sources ≥~10 years old, flagged for refresh review: ['CIS-2016', 'Hunt-2010', 'NAS-2016', 'Putnam-2007'].
- Evidence-type mix: observational 17, review 14, model-based 7, theoretical 6, quasi-experimental 2. Observational findings carry an explicit correlational caveat.