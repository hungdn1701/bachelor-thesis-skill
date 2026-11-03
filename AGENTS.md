# AGENTS.md

Instructions for AI assistants working on this repository. To use the skills on a thesis, install them instead; see `README.md`.

## What this repository is

Two agent skills for bachelor theses, in `skills/`, with their public evaluation scenarios in `evals/`. The audience is students and advisors at any school, so keep content general and public.

## Rules

- Never add real student data, private conversations, internal project names, credentials, or text that exists only for one school's internal use.
- A change to a `SKILL.md` or a reference needs a scenario in `evals/` that shows the problem, run before and after the change.
- Keep `SKILL.md` short. Use `references/` for detail. A skill's `description` says when to use it, not how it works.
- Keep the two `profiles/` folders identical. `tests/test_repo.py` checks this.
- Keep the gates warn-only and the review skill read-only. These are design decisions, not omissions.
- Scripts use the Python standard library only and exit 0 when they could run. PyMuPDF stays optional.
- Student-facing and contributor documents exist in Vietnamese and English; update both.
- Files are UTF-8 without a BOM.

## Check before finishing

```bash
python -m unittest discover -s tests
```

Script results and tests are not evidence that a skill behaves well. For that, run the scenarios and read the transcript.
