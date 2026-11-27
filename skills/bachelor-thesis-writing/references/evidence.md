# Evidence

## Source priority

When sources disagree, the higher one wins. Tell the student about the conflict.

1. Code, schemas, migrations, tests, and observed behavior of the running system
2. Configuration, API definitions, deployment scripts, logs, and measured data
3. READMEs, design documents, comments, screenshots, and the student's own papers and drafts
4. The student's own explanation
5. Sample theses and templates, for structure and format only, never as facts about this project

Documentation can be out of date. Confirm a stated feature in the code before describing it as implemented. A paper or a document often reports one version or run, while the thesis may describe another: take each value from the source of the version the sentence is about.

## Audit before the first draft

Produce this table, then a list of sections that are safe to draft now and a list of what the student must obtain first.

| Evidence | Location | Supports section | State: ok, stale, missing |
|---|---|---|---|

## What each kind of claim needs

| Claim | Needed |
|---|---|
| A feature exists | Code that implements it and, for a deployed system, configuration that enables it in the version described. Code that is present but switched off is not a feature |
| A setting, a size or a count, such as a hyperparameter or the size of a dataset | The configuration file, script or data of that version, not a document that mentions it. When the project has several versions, the text names the version |
| What a label, status or field in a result means | The code that sets it. Without that code, ask the student; never infer the meaning from the name |
| A formula | The code that computes it, so that the text says what the code does |
| A test passed | The test, the command, date, version or commit, and the output |
| A performance figure | Tool, load, environment, duration, number of runs, raw output |
| A comparison | The same measure on both sides, under stated conditions |
| A survey result | The original questionnaire, sample size, date, and how people were recruited |
| A statement from the literature | A source the student has read, cited at the claim |

## Claims register

`evidence/claims.csv` has one row per number used in the thesis.

```csv
id,value,source,verified
latency-200-users,612 ms,data/load-test.csv#avg_response_ms,2026-11-03
slowdown-100-to-200,2.48 times,"derived: 612 / 247, data/load-test.csv",2026-11-03
```

- `source` is a path, a path with a column (`data/runs.csv#accuracy`), a path with a column and row (`data/runs.csv#accuracy (baseline)`), `other-repo@commit:path`, or `derived:` with the formula.
- `verified` is the date the student confirmed the value against its source, as `YYYY-MM-DD`. Leave it empty if you added the row.
- If you change the value or the source of a row the student has verified, empty its `verified` date and tell them: their confirmation was for the old value.
- Derive a new number only from values that have rows of their own.

## Results a tool produced

When the student asks you, or another tool, to run a test or a measurement:

- Before acting on a live system that people use, have the consent of the person responsible for it, and record it in `ai-log.md`.
- Keep the raw output in the project, and give its rows an empty `verified` date until the student reruns the test and gets the same result.
- If such results go into the thesis, say once, at the start of the evaluation chapter, which tests a tool ran and which the student reran. That is a fact about the method, not a confession, and it is not repeated in each section.

## Literature

- Cite only sources the student has read or can read. Never cite from memory.
- Check that each source exists through its DOI, publisher page or official documentation. Ask before sending titles to an external search service.
- If a source cannot be confirmed, write `[MISSING: confirm source]` rather than keeping the citation.
- Prefer peer-reviewed work for claims about research. Official documentation is fine for facts about a technology. Mark preprints as such in the reference list.
- An access date is the day the student read the page. If they do not remember it, give the month; never make up a day.

## Data about people and systems

Never put credentials, internal addresses, or real names of test participants in the thesis or the register. Anonymize survey and usage data, and check that the school's consent requirements were met.
