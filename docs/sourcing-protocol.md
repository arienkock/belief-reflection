# Sourcing Protocol (applied at authoring time)
_Frozen 2026-06-30. Binds every (node, direction) findings ticket. The point is that even-handedness is a
*rule applied while authoring*, not something hoped for and checked afterwards._

## Inclusion order (take the highest tier that exists for the exact claim)
1. Systematic review or meta-analysis on the specific claim.
2. National-academy / OECD-tier synthesis.
3. Primary empirical study — quasi-experimental (natural experiment, identification strategy) preferred over plain observational.

## Hard rules
- **No tertiary basis.** Wikipedia, news aggregators and advocacy press releases may NOT be the evidential basis for a finding. (Wikipedia is allowed only as a map to locate primary sources.)
- **Advocacy/think-tank sources** (e.g. CIS, Mercatus, immigration councils) are permitted only to illustrate a stated position, must be labelled as such in the finding `caveat`, and may never be a scored node's sole support.
- **Source-tier rule:** reject a single-study finding where a meta-analysis exists on the same claim.
- **Both directions where they exist:** each scored leaf must include ≥1 good-faith source FOR and AGAINST its claim *if credible evidence in that direction exists*. If it does not, say so plainly and mark the node thin — never pad.
- **Independence:** tag `source_cluster`; the audit collapses by cluster so one report cannot corroborate itself.
- **No fabrication:** if no qualifying source is found, leave the slot empty and flag the node — do not invent or approximate a citation.
- **Recency:** flag sources ≥10 years old for refresh review.

## `source_strength` rubric (editorial, not a computed confidence)
- **strong** — meta-analysis / systematic review / national-academy synthesis, OR population-level administrative census.
- **moderate** — a single well-designed study, or a synthesis with important caveats.
- **thin** — limited, contested, or heavily assumption-dependent evidence.
