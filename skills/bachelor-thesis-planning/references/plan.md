# From a proposal or existing work to a plan

The plan connects each objective to the artifact, the evidence and the section that will carry it. A chapter that answers no objective has no job, and an objective with no evidence cannot be concluded.

## 1. Read what exists

Read the proposal or the assigned topic, then the real files: code, data, models, logs, tests, existing text. Documents can be out of date, so check what they say against the files. Note where they disagree.

## 2. Build the chain

Fill in the table in `docs/plan.md`, one row per objective or requirement.

| Column | Holds |
|---|---|
| Objective | `O1` for a build thesis, `RQ1` for a research thesis |
| Requirement | `R1`, with its threshold if one has a basis |
| Artifact | `A1`: what will show it, its location and version |
| Evaluation and evidence | How it is judged, and the file holding the result |
| Section | Where the thesis says so |
| State | `have`, `partial` or `missing` |

Use `references/structure-build.md` or `references/structure-research.md` to see which chapter does what.

**From an idea:** objectives come first, and the evidence is what you plan to obtain.

**From existing work:** start from what exists and ask which objective each piece serves. Work that serves no objective stays out, or the student explains it. Objectives written after the work are normal here, but say so in the plan, and mark any target set after measuring as `post hoc`.

## 3. Handle targets

For each threshold, ask what it rests on: a real need, a rule, a comparable system. With no basis, write `[MISSING: basis for this target]`. Do not choose a value yourself, even to be helpful, and never one that fits the results.

## 4. List the gaps

Every `partial` or `missing` row goes in the gap list with what is needed and where it would come from. Do not fill a gap with planned text.

## 5. Order the work

Take the riskiest evidence first, since the plan may change if it fails. Requirements come before the chapters that evaluate them. For a group thesis, add an owner to each row and leave the division to the group.

Set milestones backward from the deadline, around meetings with the advisor. If a date is unknown, leave it empty and ask.
