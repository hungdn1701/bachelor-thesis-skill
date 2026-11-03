# Bachelor Thesis Skills

[![CI](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue)](LICENSE)

[Tiếng Việt](README.vi.md)

Agent skills for writing and reviewing a bachelor thesis in engineering. They work with Word, LaTeX, Typst and Markdown, and do not assume any particular school.

| Skill | What it does |
|---|---|
| `bachelor-thesis-writing` | Asks for your school, thesis type and language, audits your evidence, and drafts one section at a time from real data |
| `bachelor-thesis-review` | Reviews a thesis or chapter like a strict advisor, through five gates. It only warns and never edits your text |

You remain the author. These skills help you use AI well; they do not replace your judgment or your advisor's.

## Install

Claude Code:

```bash
claude plugin install bachelor-thesis --marketplace hungdn1701/bachelor-thesis-skill
```

Other agents, from your thesis folder (needs Node.js 22.20 or later):

```bash
npx skills add hungdn1701/bachelor-thesis-skill
```

Or copy the folders in `skills/` into your agent's skills directory, such as `.claude/skills/` or `.agents/skills/`. The review script needs Python 3.9 or later; without it, the review continues by reading only.

## Supported agents

The skills use the open [Agent Skills](https://agentskills.io) format. They need an agent that can load that format, read and write files in your project, and run commands. Chat apps with no access to a project folder are not a target.

| Status | Agents |
|---|---|
| Ran both skills as intended | Claude Code, GitHub Copilot CLI |
| Ran, but followed the rules only in part | Antigravity CLI |
| Loads the skills, not yet run | Gemini CLI (trust the folder first) |
| Not yet tried | Codex, Cursor and the [other agents the installer lists](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) |

These come from a few runs on fictional projects ([results](evals/RESULTS.md)). Reports from other agents are welcome.

## Use

Ask your agent in plain language, in Vietnamese or English:

- "Help me set up my thesis project."
- "Draft section 5.1 from the data in `data/`."
- "Review chapter 5 before I send it to my advisor."
- "Check my style and format only."

Run the review in a new session, separate from the one that drafted the text. Before you merge, send a version to your advisor or finalize it, read the changes and sign `docs/sign-off.md` yourself.

The skills keep their files in your project: `.thesis/` (school, thesis type, language, format basis), `evidence/claims.csv` (each number and its source), `docs/ai-log.md` (where AI contributed), `docs/gate-record.md` (warnings and your decisions) and `docs/sign-off.md` (what you have read and confirmed).

The review runs five gates: honesty, logic, structure, format and style. Gates only warn, and having no warnings is not an approval: decisions belong to your advisor and committee.

## What these skills will not do

- Invent numbers, results, citations, signatures or approvals.
- Draft a whole chapter or thesis in one request.
- Report results the AI generated as your own measurements.
- Help you evade AI detectors, plant errors to look human, or hide AI use.
- Tell you that your thesis complies with a school rule.
- Confirm on your behalf, or merge, tag or send a version you have not signed.

## Thesis types and schools

There are two thesis types: **build**, where the main result is a working system, and **research**, where the main result answers a question.

There is no default school. The skill asks for yours, then uses its profile if one exists, builds one from your rule, template or defended thesis, or falls back on cautious defaults and says so. A rule from your school, faculty or advisor always overrides a profile. Available now: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) and [generic](skills/bachelor-thesis-writing/profiles/generic.md).

## About this project

This is a personal contribution by Hung N. Dang (Lecturer & Researcher, PTIT), made first for the students I supervise. I am responsible for the conventions in this repository. It is not a regulation of PTIT or of any other institution. Use it if it helps; nobody is required to. Whether it ever becomes official is a question for later.

## Contributing

Issues and pull requests are welcome, especially school profiles and cases where a skill behaved badly. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Skill text, references, profiles and documentation are under [CC BY 4.0](LICENSE). Scripts, tests and evaluation code are under [MIT](skills/bachelor-thesis-review/scripts/LICENSE). These licenses do not apply to your thesis, and you do not need to credit this repository in it. School names and logos belong to their owners; no logo is stored here.
