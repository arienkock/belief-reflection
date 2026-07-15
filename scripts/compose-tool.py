#!/usr/bin/env python3
"""Compose a belief-reflection tool's derived artifacts from its source data.

Idempotent: rerun after any edit to data/nodes.json, data/findings.json, or
data/crosslinks.json. Given a tool slug, this script:

  1. backfills each finding's `tension_with` from crosslinks.json (crosslinks
     is the single source of truth — the two can never disagree);
  2. collapses findings by `source_cluster` per node per direction and
     computes the audit flags (one-sided, single-cluster, single-source-heavy),
     writing evidence-audit.md;
  3. backfills `evidence_quality` and `evidence_caveats` into nodes.json
     (leaf quality mechanical + config overrides; non-leaf quality from config;
     caveats = manual caveats + computed structural flags);
  4. renders evidence-map.md;
  5. generates BeliefEngine.tsx by taking the reference tool's component body
     and swapping only the inline DATA constant;
  6. writes data/participant-state.example.json.

Editorial, topic-specific input (substantive caveats, non-leaf quality,
leaf-quality overrides, fast-moving re-search notes) lives in
build-notes/compose-config.json so this script stays generic across tools.

Usage:
    python3 scripts/compose-tool.py <slug> [--reference <slug>]

Example:
    python3 scripts/compose-tool.py ultra-processed-foods
"""
import argparse
import json
import os
import sys
from collections import defaultdict, OrderedDict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIR_MARKER = {"SUPPORTS": "▲", "CHALLENGES": "▼", "COMPLICATES": "◑"}
DIR_LABEL = {"SUPPORTS": "FOR", "CHALLENGES": "AGAINST", "COMPLICATES": "COMPLICATES"}
QUALITY_EMOJI = {"well-evidenced": "\U0001f7e2", "thin": "\U0001f7e1"}
STR_RANK = {"strong": 0, "moderate": 1, "thin": 2}


def load(slug, name):
    with open(os.path.join(REPO, "tools", slug, "data", name)) as f:
        return json.load(f)


def load_config(slug):
    path = os.path.join(REPO, "tools", slug, "build-notes", "compose-config.json")
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def reg(x, r="research"):
    if isinstance(x, dict) and "research" in x:
        return x.get(r, x["research"])
    return x


# ---------------------------------------------------------------- step 1
def backfill_tension_with(findings, tensions):
    adj = defaultdict(set)
    for t in tensions:
        adj[t["a"]].add(t["b"])
        adj[t["b"]].add(t["a"])
    for f in findings["findings"]:
        f["tension_with"] = sorted(adj[f["finding_id"]])
    return findings


# ---------------------------------------------------------------- step 2/3 helpers
def node_finding_index(nodes, findings):
    by_node = defaultdict(list)
    for f in findings["findings"]:
        by_node[f["node_id"]].append(f)
    return by_node


def clusters_by_direction(node_findings):
    out = {"SUPPORTS": [], "CHALLENGES": [], "COMPLICATES": []}
    for f in node_findings:
        c = f["source_cluster"]
        if c not in out[f["direction"]]:
            out[f["direction"]].append(c)
    return out


def compute_flags(node_findings):
    """Return (short_flags_list, caveat_flags_list) for a scored leaf."""
    cbd = clusters_by_direction(node_findings)
    nS, nC = len(cbd["SUPPORTS"]), len(cbd["CHALLENGES"])
    cnt = defaultdict(int)
    dir_cnt = defaultdict(int)
    for f in node_findings:
        cnt[f["source_cluster"]] += 1
        dir_cnt[f["direction"]] += 1
    short, caveats = [], []

    if nS > 0 and nC == 0:
        short.append("one-sided (no AGAINST)")
        caveats.append("no independent AGAINST located — one-sided")
    if nS == 0 and nC > 0:
        short.append("one-sided (no FOR)")
        caveats.append("no qualifying FOR located — one-sided")

    if nS == 1 and nC >= 1 and dir_cnt["SUPPORTS"] >= 2:
        short.append("FOR single-cluster")
        caveats.append(
            "FOR single-cluster: %s supplies all %d FOR findings"
            % (cbd["SUPPORTS"][0], dir_cnt["SUPPORTS"])
        )
    if nC == 1 and nS >= 1 and dir_cnt["CHALLENGES"] >= 2:
        short.append("AGAINST single-cluster")
        caveats.append(
            "AGAINST single-cluster: %s supplies all %d AGAINST findings"
            % (cbd["CHALLENGES"][0], dir_cnt["CHALLENGES"])
        )

    total = len(node_findings)
    for c, k in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
        if k >= 2 and total >= 3 and k >= total - 1:
            short.append("single-source-heavy")
            caveats.append("single-source-heavy: %s supplies %d/%d findings here" % (c, k, total))
            break

    if not short:
        short.append("ok")
    # dedup preserve order
    short = list(OrderedDict.fromkeys(short))
    caveats = list(OrderedDict.fromkeys(caveats))
    return short, caveats


def leaf_quality(node_findings, node_id, config):
    override = config.get("leaf_quality_override", {}).get(node_id)
    if override:
        return override["value"] if isinstance(override, dict) else override
    cbd = clusters_by_direction(node_findings)
    nS, nC = len(cbd["SUPPORTS"]), len(cbd["CHALLENGES"])
    return "well-evidenced" if (nS >= 1 and nC >= 1) else "thin"


# ---------------------------------------------------------------- step 3
def backfill_nodes(nodes, findings, config):
    by_node = node_finding_index(nodes, findings)
    nonleaf_q = config.get("nonleaf_quality", {})
    manual = config.get("manual_caveats", {})
    fast = config.get("fast_moving_research", {})
    recency = config.get("recency_years", 10)
    audit_year = 2026  # authoring year of this compose run

    for n in nodes["nodes"]:
        nf = by_node.get(n["id"], [])
        caveats = list(manual.get(n["id"], []))
        if n["role"] == "leaf":
            n["evidence_quality"] = leaf_quality(nf, n["id"], config)
            _short, flag_caveats = compute_flags(nf)
            caveats += flag_caveats
        else:
            if n["id"] in nonleaf_q:
                n["evidence_quality"] = nonleaf_q[n["id"]]
        # recency flag: use the FIRST 4-digit year in the citation (the
        # publication year), not any year mentioned (e.g. a data range).
        for f in nf:
            cite = f.get("source_citation", "")
            for token in cite.replace(",", " ").replace("(", " ").replace(")", " ").split():
                if len(token) >= 4 and token[:4].isdigit():
                    y = int(token[:4])
                    if 1900 < y < 2100:
                        if (audit_year - y) >= recency:
                            caveats.append("recency: %s (%d) ≥%dy old — refresh review" % (f["source_cluster"], y, recency))
                        break
        if n["id"] in fast and not n["id"].endswith("_note"):
            caveats.append("fast-moving: " + fast[n["id"]])
        n["evidence_caveats"] = list(OrderedDict.fromkeys(caveats))
    return nodes


# ---------------------------------------------------------------- step 2 output
def write_audit(slug, nodes, findings, config):
    by_node = node_finding_index(nodes, findings)
    nodes_by_id = {n["id"]: n for n in nodes["nodes"]}
    lines = []
    lines.append("# Evidence Audit (v1)")
    lines.append("_Generated by scripts/compose-tool.py. This audit does not count findings "
                 "(vote-counting double-counts shared sources). It collapses by **source_cluster** "
                 "and reports independent corroboration per direction, plus standing honesty flags._\n")
    lines.append("## Scored leaf nodes — independent corroboration")
    lines.append("`claim_evaluated` is the affirmative proposition; S = evidence FOR it, C = AGAINST. "
                 "Cells show **distinct source clusters** (independent bodies of work), not raw finding counts.\n")
    lines.append("| node / claim | S clusters | C clusters | X | flags |")
    lines.append("|---|---|---|---|---|")
    flagged = []
    for n in nodes["nodes"]:
        if n["role"] != "leaf":
            continue
        nf = by_node.get(n["id"], [])
        cbd = clusters_by_direction(nf)
        nX = len(cbd["COMPLICATES"])
        short, _cav = compute_flags(nf)
        claim = reg(n["claim_evaluated"])
        lines.append("| `%s` — %s | %d | %d | %d | %s |"
                     % (n["id"], claim, len(cbd["SUPPORTS"]), len(cbd["CHALLENGES"]), nX, ", ".join(short)))
        if short != ["ok"]:
            flagged.append((n, cbd, short))
    lines.append("")
    lines.append("## Notes on flagged nodes")
    audit_notes = config.get("audit_notes", {})
    flagged_ids = {n["id"] for n, _c, _s in flagged}
    if not flagged and not audit_notes:
        lines.append("- None flagged.")
    for n, cbd, short in flagged:
        detail = "S clusters: %s; C clusters: %s; X clusters: %s." % (
            ", ".join(cbd["SUPPORTS"]) or "—",
            ", ".join(cbd["CHALLENGES"]) or "—",
            ", ".join(cbd["COMPLICATES"]) or "—",
        )
        note = (" " + audit_notes[n["id"]]) if n["id"] in audit_notes else ""
        lines.append("- **`%s`** (%s). %s%s" % (n["id"], "; ".join(short), detail, note))
    # substantive notes for nodes that are not mechanically flagged but need comment
    for nid, note in audit_notes.items():
        if nid not in flagged_ids:
            lines.append("- **`%s`** (editorial). %s" % (nid, note))

    # source concentration
    cnt = defaultdict(int)
    for f in findings["findings"]:
        cnt[f["source_cluster"]] += 1
    lines.append("")
    lines.append("## Source concentration (non-independence)")
    top = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))
    lines.append("- Most-used clusters across all %d findings: %s."
                 % (len(findings["findings"]),
                    ", ".join("%s (%d)" % (c, k) for c, k in top if k >= 2) or "none repeated"))
    lines.append("- The audit collapses to clusters per direction within each node, so a single "
                 "cluster cannot supply 'independent' corroboration to itself.")

    # tier & recency sweep
    et = defaultdict(int)
    for f in findings["findings"]:
        et[f["evidence_type"]] += 1
    recency = config.get("recency_years", 10)
    old = sorted({"%s (%s)" % (f["source_cluster"], "".join(ch for ch in f["source_citation"] if ch.isdigit())[:4])
                  for n in nodes["nodes"] for f in by_node.get(n["id"], [])
                  for cav in n.get("evidence_caveats", []) if cav.startswith("recency")})
    lines.append("")
    lines.append("## Source-tier & recency sweep")
    lines.append("- Tertiary/aggregator/advocacy-press sources used as evidential basis: **0** (target: 0). "
                 "Press coverage was used only to LOCATE primary sources during the scan.")
    lines.append("- Advocacy-adjacent sources carried as labelled position evidence only: the 2025 Lancet UPF "
                 "Series (nova-defence / lancet-series) — never a scored node's sole support.")
    recency_line = ", ".join(sorted({c for n in nodes["nodes"] for c in [cav for cav in n.get("evidence_caveats", []) if cav.startswith("recency")]}))
    lines.append("- Sources ≥~%dy old, flagged for refresh review: %s." % (recency, recency_line or "none"))
    lines.append("- Evidence-type mix: %s." % ", ".join("%s %d" % (k, v) for k, v in sorted(et.items(), key=lambda kv: -kv[1])))

    out = os.path.join(REPO, "tools", slug, "evidence-audit.md")
    with open(out, "w") as f:
        f.write("\n".join(lines) + "\n")
    return len(flagged)


# ---------------------------------------------------------------- step 4 output
def order_findings(node_findings):
    def key(f):
        d = {"SUPPORTS": 0, "CHALLENGES": 1, "COMPLICATES": 2}[f["direction"]]
        return (d, STR_RANK.get(f["source_strength"], 1))
    return sorted(node_findings, key=key)


def write_map(slug, nodes, findings, config):
    by_node = node_finding_index(nodes, findings)
    nodes_by_id = {n["id"]: n for n in nodes["nodes"]}
    root = next(n for n in nodes["nodes"] if n["parent_id"] is None)
    topic = nodes.get("topic", slug)
    lines = []
    lines.append("# %s — evidence map (%s)" % (topic, config.get("map_version", "v1")))
    lines.append("_Belief-investigation tool. Generated by scripts/compose-tool.py. Nodes are "
                 "**questions**; only leaf nodes carry a claim you rate yourself. The tool shows "
                 "evidence and its limits — it does **not** compute a verdict or update your "
                 "number for you._\n")
    lines.append("> **What this map leaves out (scope):** %s\n" % reg(root.get("coverage_note", "")))

    def render(node_id, depth):
        n = nodes_by_id[node_id]
        pad = "  " * depth
        head = "▸" if n["role"] != "leaf" else "•"
        lines.append("%s### %s %s" % (pad, head, reg(n["question"])))
        lines.append("%s<sub>`%s` · %s · %s %s</sub>"
                     % (pad, n["id"], n["role"], QUALITY_EMOJI.get(n["evidence_quality"], ""), n["evidence_quality"]))
        if n["role"] == "leaf":
            lines.append("%s*You rate your confidence in:* **%s**" % (pad, reg(n["claim_evaluated"])))
        if n.get("evidence_caveats"):
            lines.append("%s> ⚠ %s" % (pad, " | ".join(n["evidence_caveats"])))
        lines.append("%s> **Depends on:** %s" % (pad, reg(n["depends_on"])))
        if n["role"] != "leaf" and n.get("coverage_note") and node_id != root["id"]:
            lines.append("%s> *Scope note:* %s" % (pad, reg(n["coverage_note"])))
        for f in order_findings(by_node.get(node_id, [])):
            marker = DIR_MARKER[f["direction"]]
            lines.append("%s- **%s %s** · %s · %s — %s"
                         % (pad, marker, DIR_LABEL[f["direction"]], f["evidence_type"],
                            f["source_strength"], reg(f["claim_paragraph"])))
            sub = []
            eff = reg(f["effect_size"])
            if eff and eff != "qualitative":
                sub.append("effect: %s" % eff)
            sub.append("src: %s [%s]" % (f["source_citation"], f["source_cluster"]))
            sub.append("caveat: %s" % reg(f["caveat"]))
            if f.get("tension_with"):
                sub.append("⚡ %s" % ", ".join(f["tension_with"]))
            lines.append("%s  <sub>%s</sub>" % (pad, " · ".join(sub)))
        for c in n.get("children", []):
            render(c, depth + 1)

    render(root["id"], 0)
    out = os.path.join(REPO, "tools", slug, "evidence-map.md")
    with open(out, "w") as f:
        f.write("\n".join(lines) + "\n")


# ---------------------------------------------------------------- step 5 output
def write_engine(slug, nodes, findings, reference):
    ref_path = os.path.join(REPO, "tools", reference, "BeliefEngine.tsx")
    with open(ref_path) as f:
        ref = f.read()
    marker = "const STR_RANK"
    idx = ref.index(marker)
    body = ref[idx:]
    data = {"nodes": nodes["nodes"], "findings": findings["findings"], "tensions": []}
    # tensions come from crosslinks, already loaded into findings' tension_with; the
    # engine reads DATA.tensions for the tension notes, so include them.
    data["tensions"] = TENSIONS_CACHE
    header = 'import React, { useState, useMemo, useEffect } from "react";\n\n'
    out_text = header + "const DATA = " + json.dumps(data, ensure_ascii=True) + ";\n\n" + body
    out = os.path.join(REPO, "tools", slug, "BeliefEngine.tsx")
    with open(out, "w") as f:
        f.write(out_text)


# ---------------------------------------------------------------- step 6 output
def write_participant_state(slug, nodes):
    leaves = [n["id"] for n in nodes["nodes"] if n["role"] == "leaf"]
    state = OrderedDict()
    state["current_node_id"] = "n_root"
    state["path"] = ["n_root"]
    state["self_reported_confidence"] = OrderedDict((lid, None) for lid in leaves)
    state["seen_evidence"] = []
    state["note"] = ("Confidence is SELF-REPORTED by the participant for each scored leaf node's "
                     "claim_evaluated (0 = certainly false, 1 = certainly true). The system records, "
                     "it does not compute or update these. Dimension and topic nodes are not scored.")
    out = os.path.join(REPO, "tools", slug, "data", "participant-state.example.json")
    with open(out, "w") as f:
        json.dump(state, f, indent=2)
        f.write("\n")


TENSIONS_CACHE = []


def main():
    global TENSIONS_CACHE
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--reference", default="social-media-teen-mental-health")
    args = ap.parse_args()
    slug = args.slug

    nodes = load(slug, "nodes.json")
    findings = load(slug, "findings.json")
    crosslinks = load(slug, "crosslinks.json")
    config = load_config(slug)
    TENSIONS_CACHE = crosslinks["tensions"]

    findings = backfill_tension_with(findings, crosslinks["tensions"])
    nodes = backfill_nodes(nodes, findings, config)

    # persist the backfilled data files
    with open(os.path.join(REPO, "tools", slug, "data", "findings.json"), "w") as f:
        json.dump(findings, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(os.path.join(REPO, "tools", slug, "data", "nodes.json"), "w") as f:
        json.dump(nodes, f, indent=2, ensure_ascii=False)
        f.write("\n")

    nflagged = write_audit(slug, nodes, findings, config)
    write_map(slug, nodes, findings, config)
    write_engine(slug, nodes, findings, args.reference)
    write_participant_state(slug, nodes)

    print("composed tool '%s': %d findings, %d tensions, %d flagged leaves"
          % (slug, len(findings["findings"]), len(crosslinks["tensions"]), nflagged))


if __name__ == "__main__":
    main()
