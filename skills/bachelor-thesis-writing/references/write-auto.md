# Writing several sections in one run

Use this for `/write auto`, or whenever a request covers more than one section. The human stops stepping between sections; every section still clears the same bar.

## Before starting

1. **Know the sections.** Follow `docs/plan.md`. With no plan, list the sections and the evidence for each, and suggest `bachelor-thesis-planning`.
2. **Get a clear yes** to that list and to where you will stop. "Do not ask again" counts for the list, not for anything under Stop below. A deadline is not a yes.
3. **Take one chapter per run.** That is what a student can read and sign. Run again for the next one, or use `references/write-all.md` for the whole thesis.
4. **Check the working tree.** If thesis files have uncommitted changes, ask how to handle them, so that a section's commit never absorbs the student's own edits. Without git, write to new files.

## For each section, in plan order

1. Collect its evidence.
2. Write it, as `references/drafting.md` describes. Each gap becomes `[MISSING: what is needed, where it would come from]`.
3. Add its `claims.csv` rows and its `ai-log.md` row.
4. Commit before moving on, with only that section's changes and its name in the message, so the student can read and undo each one. Do this even when all the sections share one file: write one section, commit, then add the next.

## Stop

**Leave the section open and go on:**

- It needs a result that does not exist. Write `[MISSING: ...]`.
- Sources disagree on something inside this section, such as a count. Use neither number, write `[MISSING: ...]` naming both, and list it at the end.
- It is an assessment, a contribution, a rationale or a conclusion. Do not write it: leave one `[MISSING: your reasoning on ..., see the questions at the end]` for the section, not one in every cell of a table, and list what you would ask. Writing "the system meets its needs" for them is writing their conclusion.
- It is the acknowledgements or the declaration. Leave it for the student, and list it at the end.

**Stop the run and ask,** only when going on would make the other sections wrong:

- Sources disagree about what the system or the study is.
- The plan no longer matches the files.

A gap is not a reason to stop. Stopping with nothing written, the night before a deadline, helps less than a chapter with its gaps marked.

These stand however the request is worded: never invent a value, run an experiment to fill a gap, merge, tag or sign.

## Closing the run

- Sections written and their commits.
- Every `[MISSING]` item, with what each needs, and the questions for the student.
- New `claims.csv` rows, and the `ai-log.md` rows whose last column is still empty.
- Pages: build the PDF if the project can, and give its page count against `pages` in `.thesis/config.json` and the chapter's share in `docs/plan.md`. If the project cannot build, say so and give the chapter's word count. Say plainly when the draft is over the limit, since cutting at the end costs more than writing to size.
- What to read first, starting with the sections that make claims.
- Three defense questions for each section.
- Next: `bachelor-thesis-review` in a new session, then the student signs for the chapter in `docs/sign-off.md`.
