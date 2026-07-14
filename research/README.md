# Research

Candidate topics that aren't a published tool yet — the pipeline stage before
`tools/<slug>/`. A topic lives here while its node tree and scope are still
being worked out; it graduates to `tools/` once nodes are frozen and Phase 2
evidence-gathering starts (see [`../docs/README.md`](../docs/README.md) for
the pipeline).

## What makes a good candidate topic

- **Splits into an honest question tree**, not one contested yes/no. If the
  topic really is a single up-or-down empirical question, it likely doesn't
  need this tool — the value here is surfacing that "is X good?" usually
  hides several separately-measured dimensions with different evidence
  quality (see the Immigration root node's `coverage_note` and `depends_on`
  for what that split looks like in practice).
- **Has a literature to be sourced from a scored leaf can go either way on**
  — a claim with essentially no credible evidence on one side should be
  flagged thin, not forced into this tool to manufacture false balance.
- **Is not primarily a moral or definitional dispute.** If the disagreement
  is about values or word-meaning rather than what the evidence shows, this
  tool format won't resolve it and shouldn't pretend to.

## Proposing a topic

Open an issue or a PR adding `research/<slug>/proposal.md` with:

- **Working title and one-sentence scope.**
- **Draft root question** and the dimensions you expect it to split into.
- **Coverage note** — what you already know this topic-map will deliberately
  leave out, and why.
- **Why now** — what makes this a useful addition (public salience, evidence
  base recently changed, gap in existing tools, etc).

A maintainer or reviewer will weigh in before it moves to Phase 1 node
authoring. This is a public repository — proposals, sourcing, and framing are
all open to scrutiny; see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
