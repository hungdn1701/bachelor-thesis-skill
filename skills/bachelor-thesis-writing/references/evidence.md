# Evidence

## Source priority

When sources disagree, the higher one wins. Tell the student about the conflict.

1. Code, schemas, migrations, tests, and observed behavior of the running system
2. Configuration, API definitions, deployment scripts, logs, and measured data
3. READMEs, design documents, comments, and screenshots
4. The student's own explanation
5. Sample theses and templates, for structure and format only, never as facts about this project

Documentation can be out of date. Confirm a stated feature in the code before describing it as implemented.

## Audit before the first draft

Produce this table, then a list of sections that are safe to draft now and a list of what the student must obtain first.

| Evidence | Location | Supports section | State: ok, stale, missing |
|---|---|---|---|

## What each kind of claim needs

| Claim | Needed |
|---|---|
| A feature exists | Code that implements it |
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
- `verified` is the date the student confirmed the value against its source. Leave it empty if you added the row.

## Literature

- Cite only sources the student has read or can read. Never cite from memory.
- Check that each source exists through its DOI, publisher page or official documentation. Ask before sending titles to an external search service.
- If a source cannot be confirmed, write `[MISSING: confirm source]` rather than keeping the citation.
- Prefer peer-reviewed work for claims about research. Official documentation is fine for facts about a technology. Mark preprints as such in the reference list.

## Data about people and systems

Never put credentials, internal addresses, or real names of test participants in the thesis or the register. Anonymize survey and usage data, and check that the school's consent requirements were met.
