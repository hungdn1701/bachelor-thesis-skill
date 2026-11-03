# Contributing

[Tiếng Việt](CONTRIBUTING.vi.md)

Issues and pull requests are welcome. The most useful contributions are school profiles and reports of a skill behaving badly.

## Never include

- Real student data: names, IDs, grades, or unpublished theses.
- Credentials, internal addresses, or anything private to a school or company.
- Private conversations. Describe the problem instead.

## Add a school profile

1. Add `<id>.md` and `<id>.json` to `skills/bachelor-thesis-writing/profiles/`, using [`ptit.md`](skills/bachelor-thesis-writing/profiles/ptit.md) as the model.
2. Give a public source for every value. Mark values without a written rule as common practice.
3. Put only values from a written rule, or values you state as a proposal, in the JSON file. The checker reports against them.
4. Set `status` to `official` only if the school has confirmed it. Otherwise use `community`.
5. Copy both files to `skills/bachelor-thesis-review/profiles/`. A test checks that the two folders match.

## Report a skill behaving badly

Use the issue template. Include the request, what the skill did, and what you expected. Use made-up thesis content.

## Change a skill

A change to a `SKILL.md` or a reference file needs evidence that it helps:

1. Add or pick a scenario in [`evals/scenarios.json`](evals/scenarios.json) that shows the problem.
2. Run it with a fresh agent, before and after your change, as [`evals/README.md`](evals/README.md) describes.
3. Say what changed in the pull request. Keep `SKILL.md` short and move detail into `references/`.

Keep instructions general. Do not add rules that fit only one school, one thesis or one incident.

## Change a script

Add a test first, then run:

```bash
python -m unittest discover -s tests
```

Scripts use the Python standard library only, and always exit 0 when they could run: gates warn, they do not block.

## Style

Skills are written in English. The material for students and contributors is written in both Vietnamese and English; update both. Keep files in UTF-8 without a BOM.

By contributing, you agree that your contribution is licensed under the same terms as the part you change, as described in the [README](README.md#license).
