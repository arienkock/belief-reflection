# Phase 1 → Phase 2 Handoff: Frozen Question List (v2)
_Frozen 2026-06-30._

Nodes are frozen. Each scored leaf is an independent ticket: gather evidence FOR and AGAINST its `claim_evaluated` under the sourcing protocol (4–8 findings). Do not add/rename nodes while researching; file a change request to Phase 1 instead.

## Scored leaf tickets

### `n_econ_wages_overall` — Does immigration lower wages or employment for native-born workers overall?
- claim to evaluate: **Immigration lowers wages/employment for native-born workers overall.**
- evidence_quality: **well-evidenced**
- standing caveats: single-source-heavy: NAS-2016 supplies 2/3 findings here, US-centric evidence — external validity to other destinations not established
- findings authored: 3

### `n_econ_wages_lowskill` — Does immigration lower wages or employment for low-skilled natives and prior immigrants?
- claim to evaluate: **Immigration lowers wages/employment for low-skilled natives and prior immigrants.**
- evidence_quality: **well-evidenced**
- standing caveats: single-source-heavy: NAS-2016 supplies 3/4 findings here, US-centric evidence — external validity to other destinations not established
- findings authored: 4

### `n_econ_gdp_pc` — Does immigration raise GDP per capita (not just total GDP)?
- claim to evaluate: **Immigration raises GDP per capita, not merely aggregate GDP.**
- evidence_quality: **well-evidenced**
- standing caveats: single-source-heavy: OECD-migration supplies 3/3 findings here
- findings authored: 3

### `n_fiscal_highskill` — Are high-skilled immigrants net fiscal contributors?
- claim to evaluate: **High-skilled immigrants are net fiscal contributors.**
- evidence_quality: **well-evidenced**
- standing caveats: single-source-heavy: DallasFed-2017 supplies 2/2 findings here, US-centric evidence — external validity to other destinations not established
- findings authored: 2

### `n_fiscal_lowskill` — Are low-skilled immigrants a net fiscal drain?
- claim to evaluate: **Low-skilled immigrants are a net fiscal drain.**
- evidence_quality: **THIN — flag honestly**
- standing caveats: US-centric evidence — external validity to other destinations not established
- findings authored: 3

### `n_fiscal_horizon` — Does the fiscal picture turn positive once you count descendants and the long run?
- claim to evaluate: **Counting descendants and the long run, immigration is fiscally positive.**
- evidence_quality: **THIN — flag honestly**
- standing caveats: single-source-heavy: NAS-2016 supplies 2/3 findings here, US-centric evidence — external validity to other destinations not established
- findings authored: 3

### `n_innov_share` — Do immigrants contribute disproportionately to patents and entrepreneurship?
- claim to evaluate: **Immigrants contribute disproportionately to patents and entrepreneurship.**
- evidence_quality: **well-evidenced**
- standing caveats: US-centric evidence — external validity to other destinations not established, mostly correlational — causal interpretation is not licensed
- findings authored: 3

### `n_innov_complement` — Do high-skilled immigrants complement (rather than crowd out) native innovators?
- claim to evaluate: **High-skilled immigrants complement rather than crowd out native innovators.**
- evidence_quality: **well-evidenced**
- standing caveats: US-centric evidence — external validity to other destinations not established, mostly correlational — causal interpretation is not licensed
- findings authored: 3

### `n_social_crime` — Does immigration increase crime?
- claim to evaluate: **Immigration increases crime.**
- evidence_quality: **well-evidenced**
- standing caveats: mostly correlational — causal interpretation is not licensed
- findings authored: 5

### `n_social_trust` — Does immigration / ethnic diversity erode social trust and cohesion?
- claim to evaluate: **Immigration / ethnic diversity erodes social trust and cohesion.**
- evidence_quality: **THIN — flag honestly**
- standing caveats: single-source-heavy: Dinesen-2020 supplies 3/5 findings here, mostly correlational — causal interpretation is not licensed
- findings authored: 5

### `n_social_integration` — Do immigrants and their descendants integrate over generations?
- claim to evaluate: **Immigrants and their descendants integrate over generations.**
- evidence_quality: **THIN — flag honestly**
- standing caveats: single-source-heavy: NAS-2016 supplies 2/3 findings here, US-centric evidence — external validity to other destinations not established, mostly correlational — causal interpretation is not licensed
- findings authored: 3

## Non-scored structural nodes
- `n_root` (topic) → n_econ, n_fiscal, n_innov, n_social
- `n_econ` (dimension) → n_econ_wages_overall, n_econ_wages_lowskill, n_econ_gdp_pc
- `n_fiscal` (dimension) → n_fiscal_highskill, n_fiscal_lowskill, n_fiscal_horizon
- `n_innov` (dimension) → n_innov_share, n_innov_complement
- `n_social` (dimension) → n_social_crime, n_social_trust, n_social_integration