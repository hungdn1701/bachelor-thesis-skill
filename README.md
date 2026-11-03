# Bachelor Thesis Skills

[Tiếng Việt](README.vi.md)

Two agent skills for writing and reviewing a bachelor thesis in engineering. They work with Word, LaTeX, Typst and Markdown, and they do not assume any particular school.

| Skill | What it does |
|---|---|
| `bachelor-thesis-writing` | Asks for your school, thesis type and language, audits your evidence, drafts one section at a time from real data, and keeps your use of AI on record |
| `bachelor-thesis-review` | Reviews a thesis or chapter like a strict advisor, through five gates. It only warns and never edits your text |

You remain the author. These skills help you use AI well; they do not replace your judgment or your advisor's.

## Install

```bash
npx skills add hungdn1701/bachelor-thesis-skill                                  # both skills
npx skills add hungdn1701/bachelor-thesis-skill --skill bachelor-thesis-review   # review only
```

Or copy a folder from `skills/` into your agent's skills directory. The review script needs Python 3.9 or later and nothing else; PyMuPDF is optional and enables PDF checks.

## Use

Ask your agent in plain language, in Vietnamese or English:

- "Help me set up my thesis project."
- "Draft section 5.1 from the data in `data/`."
- "Review chapter 5 before I send it to my advisor."
- "Check my style and format only."

Run the review in a new session, separate from the one that drafted the text.

The skills keep these files in your thesis project:

| File | Purpose |
|---|---|
| `.thesis/config.json` | School, thesis type, language, source files |
| `.thesis/profile.md`, `.thesis/profile.json` | The format basis for your school |
| `evidence/claims.csv` | Each number in the thesis, with its source and the date you verified it |
| `docs/ai-log.md` | When and how AI contributed; the last column is yours |
| `docs/gate-record.md` | Review warnings and your decision on each one |

## The five gates

| Gate | Question |
|---|---|
| Honesty | Is each statement true of the work, and can it be traced? |
| Logic | Does the argument hold from objective to conclusion, at the same strength? |
| Structure | Are all parts present, in order, and doing their job? |
| Format | Does the document follow the format basis for your school? |
| Style | Does it read as plain academic writing, free of hype and chatbot leftovers? |

Gates warn. They never block a build or a submission, and passing them is not an approval: decisions belong to your advisor and committee. The review record lets your advisor see in minutes what was flagged and what you decided.

## What these skills will not do

- Invent numbers, results, citations, signatures or approvals.
- Draft a whole chapter or thesis in one request.
- Report results the AI generated as your own measurements.
- Help you evade AI detectors, plant errors to look human, or hide AI use.
- Tell you that your thesis complies with a school rule.

## Thesis types

- **Build:** the main result is a working system. The chain is objective, requirement, design, implementation, test, result, conclusion.
- **Research:** the main result answers a question. The chain is research question, method, experiment, result, discussion, conclusion.

## Schools

There is no default school. The skill asks for yours, then:

1. If a profile exists in this repository, it uses that profile.
2. If you have a rule, template or defended thesis, it builds a profile from them and separates what is required from what is only inferred.
3. Otherwise it uses cautious defaults, and says so in every report.

A rule from your school, faculty or advisor always overrides a profile. Profiles available now: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) and [generic](skills/bachelor-thesis-writing/profiles/generic.md). Profiles for other schools are welcome.

## About this project

This is a personal contribution by Hung N. Dang (Lecturer & Researcher, PTIT), made first for the students I supervise. I am responsible for the conventions in this repository. It is not a regulation of PTIT or of any other institution. Use it if it helps; nobody is required to. Whether it ever becomes official is a question for later.

## Contributing

Issues and pull requests are welcome, especially school profiles and cases where a skill behaved badly. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

| Part | License |
|---|---|
| Skill text, references, profiles, documentation | [CC BY 4.0](LICENSE) |
| Scripts, tests and evaluation code | [MIT](skills/bachelor-thesis-review/scripts/LICENSE) |

Your thesis is yours: these licenses do not apply to it, and you do not need to credit this repository in it. School names and logos belong to their owners and are not covered by these licenses; no logo is stored here.
