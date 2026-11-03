# Bachelor Thesis Skills

[![CI](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue)](LICENSE)

[Tiếng Việt](README.vi.md)

Agent skills that take a bachelor thesis in engineering from an idea to submission. The thesis is the product; code, a model, a dataset or a survey is an artifact, the evidence for what the thesis claims. They work with Word, LaTeX, Typst and Markdown, and do not assume any particular school.

```
   IDEA         PLAN         WRITE       REVIEW       DEFENSE       FINAL
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ Question│─▶│ Claims  │─▶│Sections │─▶│  Five   │─▶│Committee│─▶│Signature│
│Proposal │  │Evidence │  │ Numbers │  │  gates  │  │Questions│  │Open list│
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
   /idea        /plan       /write       /review     /defense      /final
                  ▲            ▲            │
                  │            └──── fix ───┘
            Existing work
```

## Steps

| Step | Command | Or just say | What it does |
|---|---|---|---|
| Idea | `/idea` | "Refine my thesis idea about ..." | Sharpens your idea into a proposal: the problem, directions, objectives, assumptions, what you will not do. It does not pick a topic for you |
| Plan | `/plan` | "Plan my thesis from this code and data." | Connects each objective to an artifact, evidence and a section, and lists the gaps |
| Write | `/write`, `/write auto` | "Write section 5.1 from `data/`." "Write chapter 5 from the plan in one run." | Writes from real evidence and keeps your use of AI on record. Auto runs a chapter of the plan after one clear yes, and stops at what only you can decide |
| Review | `/review` | "Review chapter 5." | A strict advisor's reading through five gates: honesty, logic, structure, format, style. It only warns and never edits |
| Defense | `/defense` | "Rehearse my defense on chapter 5." | A committee that tests your claims against your evidence |
| Final | `/final` | "What is still open before I submit?" | Lists every open item. It never says the thesis is ready |

In Claude Code the commands are `/bachelor-thesis:idea` and so on. Other agents have no commands: just ask.

**Two ways in.** Start at `/idea` if you have an idea or only an interest. Start at `/plan` if your topic is assigned or the work is already done. Either way you end up with the same chain from objective to conclusion, and anything set after measuring is marked as such.

**People decide at two points.** Your advisor decides on the proposal. Before you merge, send a version to your advisor or finalize it, you read the changes and sign `docs/sign-off.md` yourself.

Run reviews in a new session, separate from the one that wrote the text. Building the artifact is up to you and your other tools; for software, [agent-skills](https://github.com/addyosmani/agent-skills) works alongside these.

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

| Skill | Steps |
|---|---|
| `bachelor-thesis-planning` | Idea, Plan |
| `bachelor-thesis-writing` | Write |
| `bachelor-thesis-review` | Review, Defense, Final |

## Supported agents

The skills use the open [Agent Skills](https://agentskills.io) format. They need an agent that can load that format, read and write files in your project, and run commands. Chat apps with no access to a project folder are not a target.

| Status | Agents |
|---|---|
| Ran the steps tried so far as intended | Claude Code |
| Ran writing and review as intended on v0.1 | GitHub Copilot CLI |
| Ran writing and review, but followed the rules only in part on v0.1 | Antigravity CLI |
| Loads the skills, not yet run | Gemini CLI (trust the folder first) |
| Not yet tried | Codex, Cursor and the [other agents the installer lists](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) |

These come from a few runs on fictional projects ([results](evals/RESULTS.md)). Reports from other agents are welcome.

## What these skills will not do

- Pick your topic, or invent numbers, results, citations, signatures or approvals.
- Write your conclusion, or report results the AI generated as your own measurements.
- Help you evade AI detectors, plant errors to look human, or hide AI use.
- Tell you that your thesis is ready, or that it complies with a school rule.
- Confirm on your behalf, or merge, tag or send a version you have not signed.

## Files in your project

`docs/proposal.md`, `docs/plan.md` and `docs/decisions.md` (the idea, the chain, the reasons behind each choice), `.thesis/` (school, thesis type, language, format basis), `evidence/claims.csv` (each number and its source), `docs/ai-log.md` (where AI contributed), `docs/gate-record.md` (warnings and your decisions), `docs/defense-notes.md` (rehearsal questions) and `docs/sign-off.md` (what you have read and confirmed).

## Thesis types and schools

There are two thesis types: **build**, where the main result is a working system, and **research**, where the main result answers a question.

There is no default school. The skill asks for yours, then uses its profile if one exists, builds one from your rule, template or defended thesis, or falls back on cautious defaults and says so. A rule from your school, faculty or advisor always overrides a profile. Available now: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) and [generic](skills/bachelor-thesis-writing/profiles/generic.md).

## About this project

This is a personal contribution by Hung N. Dang (Lecturer & Researcher, PTIT), made first for the students I supervise. I am responsible for the conventions in this repository. It is not a regulation of PTIT or of any other institution. Use it if it helps; nobody is required to. Whether it ever becomes official is a question for later. The lifecycle idea is adapted from [agent-skills](https://github.com/addyosmani/agent-skills), rewritten for theses.

## Contributing

Issues and pull requests are welcome, especially school profiles and cases where a skill behaved badly. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Skill text, references, profiles and documentation are under [CC BY 4.0](LICENSE). Scripts, tests and evaluation code are under [MIT](skills/bachelor-thesis-review/scripts/LICENSE). These licenses do not apply to your thesis, and you do not need to credit this repository in it. School names and logos belong to their owners; no logo is stored here.
