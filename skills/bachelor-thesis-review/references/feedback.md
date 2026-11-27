# Reporting a problem with these skills

Use this when the student, or their advisor, wants to tell the authors of these skills that one of them did something wrong, unhelpful or missing. The report goes to the public issue tracker of the skills, so it must hold nothing from the thesis.

## Steps

1. **Find what happened.** From this session, or from what the student describes: which skill and step (setup, idea, plan, write, write auto, write all, review, defense, final, or the checker script), what they asked, what the skill did, and what they expected. If it happened in another session, ask the student to describe it; do not guess.
2. **Find the versions.** The skill version is the `version` under `metadata` in that skill's `SKILL.md`. Add the agent and its version, and the model if known.
3. **Strip the thesis out.** Describe the behavior, not the content: "left `[MISSING]` in every cell of the objectives table", not the table. Replace names, topics, systems, numbers and file paths from the project with made-up ones, and say they are made up. Nothing from the thesis, its data, its people or its school's internal documents goes in.
4. **Let the student write the summary.** Draft the other fields, then ask the student for two or three sentences in their own words on what went wrong. A report is the student's, not yours.
5. **Show it and ask before anything leaves the machine.** Never post a report yourself without a clear yes for that exact text.
6. **Hand it over.** Give a link that opens the form with the fields filled in, so that the student submits it from their own account:

   `https://github.com/hungdn1701/bachelor-thesis-skill/issues/new?template=skill-behavior.yml&title=<title>&skill=<skill>&step=<step>&version=<version>&agent=<agent>&request=<request>&actual=<actual>&expected=<expected>&summary=<summary>`

   Encode each value for a URL and keep the link under about 6,000 characters; if it is longer, give the fields as text to paste instead. For an idea or a missing step rather than a fault, use `template=idea.yml` with the fields `idea`, `today` and `version`. If the student prefers the command line and has GitHub CLI signed in, `gh issue create --repo hungdn1701/bachelor-thesis-skill --label behavior --title ... --body-file ...` also works, after the same yes.
7. **Point to the trial record, if there is one.** If the advisor set up a feedback log in the project, such as a trial form in `docs/`, remind the student to add the same row there and the issue number once it exists. You stay read-only: do not write it for them.

## Field ids of the forms

| Form | Fields |
|---|---|
| `skill-behavior.yml` | `skill`, `step`, `version`, `agent`, `request`, `actual`, `expected`, `severity`, `summary` |
| `idea.yml` | `idea`, `today`, `version` |

Text fields fill in from the link. Dropdowns (`skill`, `step`, `severity`) may not, so tell the student which option to pick: the skill's name or `check_thesis.py`; the step; `blocks the work`, `annoying` or `minor`.
