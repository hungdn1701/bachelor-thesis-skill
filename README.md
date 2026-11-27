# Bachelor Thesis Skills

[![CI](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-555)](https://agentskills.io)
[![skills.sh](https://skills.sh/b/hungdn1701/bachelor-thesis-skill)](https://skills.sh/hungdn1701/bachelor-thesis-skill)

[Tiếng Việt](README.vi.md)

Agent skills that take a bachelor thesis in engineering from an idea to submission. The thesis is the product; code, a model, a dataset or a survey is an artifact, the evidence for what the thesis claims. They work with Word, LaTeX, Typst and Markdown, and do not assume any particular school.

## Quick start

**Any agent.** From your thesis folder, with Node.js 22.20 or later, the open [skills CLI](https://github.com/vercel-labs/skills) installs the skills into the agents it finds, such as Claude Code, Codex, GitHub Copilot, Gemini CLI or Cursor:

```bash
npx skills add hungdn1701/bachelor-thesis-skill          # all three skills
npx skills add hungdn1701/bachelor-thesis-skill --list   # see them before installing
```

Add `--skill bachelor-thesis-review` for one skill, `-a claude-code` for one agent, or `-g` for every project. Update with `npx skills update`.

**Claude Code.** Install it as a plugin, which also adds the commands. Inside Claude Code:

```text
/plugin marketplace add hungdn1701/bachelor-thesis-skill
/plugin install bachelor-thesis@bachelor-thesis-skill
```

Or from a terminal:

```bash
claude plugin install bachelor-thesis --marketplace hungdn1701/bachelor-thesis-skill
```

**By hand.** Copy the folders in `skills/` into your agent's skills directory, such as `.claude/skills/` or `.agents/skills/`. Each folder works on its own.

The review script needs Python 3.9 or later; without it, the review continues by reading only. Then say what you need, for example "Plan my thesis from this code and data."

## Skills

| Skill | Use it to | Steps |
|---|---|---|
| [`bachelor-thesis-planning`](skills/bachelor-thesis-planning/SKILL.md) | Sharpen an idea into a proposal, and connect each objective to an artifact, evidence and a section | Idea, Plan |
| [`bachelor-thesis-writing`](skills/bachelor-thesis-writing/SKILL.md) | Write sections, a chapter or the whole thesis from real evidence, with your use of AI on record | Write |
| [`bachelor-thesis-review`](skills/bachelor-thesis-review/SKILL.md) | Review through five gates, rehearse the defense, and list what is open before submitting | Review, Defense, Final |

## How it works

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

| Step | Command | Or just say | What it does |
|---|---|---|---|
| Idea | `/idea` | "Refine my thesis idea about ..." | Sharpens your idea into a proposal: the problem, directions, objectives, assumptions, what you will not do. It does not pick a topic for you |
| Plan | `/plan` | "Plan my thesis from this code and data." | Connects each objective to an artifact, evidence and a section, budgets the pages, and lists the gaps |
| Write | `/write`, `/write auto`, `/write all` | "Write section 5.1 from `data/`." "Write chapter 5 from the plan in one run." "Write the whole thesis from the plan." | Writes from real evidence and keeps your use of AI on record. Auto runs a chapter of the plan after one clear yes. All runs every chapter on its own branch, one by one or with parallel agents. Both stop at what only you can decide, and report the pages against your limit |
| Review | `/review` | "Review the whole thesis." | A strict advisor's reading through five gates: honesty, logic, structure, format, style. It only warns and never edits, and it says which version and which parts it read |
| Defense | `/defense` | "Rehearse my defense on chapter 5." | A committee that tests your claims against your evidence |
| Final | `/final` | "What is still open before I submit?" | Lists every open item, including changes no review has read. It never says the thesis is ready |

In Claude Code the commands are `/bachelor-thesis:idea` and so on. Other agents have no commands: just ask.

**Two ways in.** Start at `/idea` if you have an idea or only an interest. Start at `/plan` if your topic is assigned or the work is already done. Either way you end up with the same chain from objective to conclusion, and anything set after measuring is marked as such.

**People decide at two points.** Your advisor decides on the proposal. Before you merge, send a version to your advisor or finalize it, you read the changes and add a row to `docs/sign-off.md` yourself.

**Review in a new session, and review the whole thesis before you send it.** A review in the session that wrote the text is only a self-check, and a review of one member's part cannot check the abstract, the conclusion or terms across chapters. The review record keeps the commit each review read, so the checker can tell you what changed since. Building the artifact is up to you and your other tools; for software, [agent-skills](https://github.com/addyosmani/agent-skills) works alongside these.

## What these skills will not do

- Pick your topic, or invent numbers, results, citations, signatures or approvals.
- Write your conclusion, or report results the AI generated as your own measurements.
- Help you evade AI detectors, plant errors to look human, or hide AI use.
- Tell you that your thesis is ready, or that it complies with a school rule.
- Confirm on your behalf, or merge, tag or send a version you have not signed.

## Files in your project

| File | Holds |
|---|---|
| `docs/proposal.md`, `docs/plan.md`, `docs/decisions.md` | The idea, the chain from objectives to sections, the page budget, and the reason behind each choice |
| `.thesis/` | School, thesis type, language, page limits and format basis |
| `evidence/claims.csv` | Each number in the thesis and its source |
| `docs/terms.md` | One name for each concept, shared by everyone who writes |
| `docs/ai-log.md` | Where AI contributed, with a column only you fill in |
| `docs/gate-record.md` | Each review: its commit, scope, warnings, and your decisions |
| `docs/defense-notes.md` | Rehearsal questions |
| `docs/sign-off.md` | What you have read and confirmed, one new row each time |

## Thesis types and schools

There are two thesis types: **build**, where the main result is a working system, and **research**, where the main result answers a question. Group theses are supported: each member signs for their own part, and the body speaks of the group, not of members by name.

There is no default school. The skill asks for yours, then uses its profile if one exists, builds one from your rule, template or defended thesis, or falls back on cautious defaults and says so. A rule from your school, faculty or advisor always overrides a profile. Available now: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) and [generic](skills/bachelor-thesis-writing/profiles/generic.md).

## Supported agents

The skills use the open [Agent Skills](https://agentskills.io) format. They need an agent that can load that format, read and write files in your project, and run commands. Chat apps with no access to a project folder are not a target.

| Status | Agents |
|---|---|
| Used on a real group thesis, and ran the steps tried so far as intended | Claude Code |
| Ran writing and review as intended on v0.1 | GitHub Copilot CLI |
| Ran writing and review, but followed the rules only in part on v0.1 | Antigravity CLI |
| Loads the skills, not yet run | Gemini CLI (trust the folder first) |
| Not yet tried | Codex, Cursor and the [other agents the installer lists](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) |

These come from runs on fictional projects and one real trial ([results](evals/RESULTS.md)). Reports from other agents are welcome.

## Repository layout

```
skills/
  bachelor-thesis-planning/   SKILL.md, references/, assets/
  bachelor-thesis-writing/    SKILL.md, references/, assets/, profiles/
  bachelor-thesis-review/     SKILL.md, references/, assets/, profiles/, scripts/, data/
commands/                     /idea, /plan, /write, /review, /defense, /final for Claude Code
evals/                        pressure scenarios, a fictional project builder, results
tests/                        checks for the review script and the repository
.claude-plugin/               Claude Code marketplace
```

## Evaluation

Each change to a skill comes with a scenario in [`evals/scenarios.json`](evals/scenarios.json), run before and after the change on fictional projects from [`evals/make_fixture.py`](evals/make_fixture.py). The transcripts are read against what the agent must and must not do; [`evals/RESULTS.md`](evals/RESULTS.md) records what changed. Unit tests cover the review script only: `python -m unittest discover -s tests`.

## About this project

This is a personal contribution by Hung N. Dang (Lecturer & Researcher, PTIT), made first for the students I supervise. I am responsible for the conventions in this repository. It is not a regulation of PTIT or of any other institution. Use it if it helps; nobody is required to. Whether it ever becomes official is a question for later. The lifecycle idea is adapted from [agent-skills](https://github.com/addyosmani/agent-skills), rewritten for theses.

## Contributing

Issues and pull requests are welcome, especially school profiles and cases where a skill behaved badly. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Skill text, references, profiles and documentation are under [CC BY 4.0](LICENSE). Scripts, tests and evaluation code are under [MIT](skills/bachelor-thesis-review/scripts/LICENSE). These licenses do not apply to your thesis, and you do not need to credit this repository in it. School names and logos belong to their owners; no logo is stored here.

## Citation

If this repository helps your work on thesis guidance, cite it with [`CITATION.cff`](CITATION.cff), or use GitHub's "Cite this repository" button.
