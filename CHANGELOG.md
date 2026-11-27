# Changelog

## 0.3.1 (unreleased)

- Feedback: ask the agent to "report a problem with the thesis skills", or run `/feedback`, and the review skill drafts a report with the thesis left out, asks the student for a summary in their own words, and hands over a link to the filled-in form; nothing is sent without a clear yes, and the student submits it from their own account.
- Issue forms: the behavior form adds the planning skill, the step, the skill version, the agent and model, a severity, the student's own summary, and checks for thesis content and duplicates; a new form for ideas; blank issues off, with a link to the README's feedback section. The labels the forms use now exist.
- README: a Feedback section in both languages, linked from the quick start.
- Evals: the fixture builder skips an empty project name instead of deleting its base folder.

## 0.3.0 (unreleased)

From the first trial on a real group thesis, and the student group's report on it.

- Writing: a limit the whole chapter shares is stated once, at the start of the evaluation chapter and where results meet the objectives, instead of in every section; bad results still stay in the thesis. `[MISSING]` marks only a missing number or source; acknowledgements and assessments are asked for, with one mark per section in a run. No sentences about what the text does not do.
- Evidence: values come from the configuration or script of the version described, not from documents or papers that report another one. Labels, statuses and formulas are read from the code that produces them. A component counts only if the deployed configuration enables it. Rules for tests a tool ran: consent before touching a live system, one statement in the evaluation chapter, rows unverified until the student reruns. Access dates are never made up.
- Group theses: the body speaks of the group, not of members by name; the division table lists what members confirm; revisions after a review go one finding at a time.
- Length: setup asks for the page limits, the plan budgets pages per chapter, and each run reports pages against the limit. The checker warns when the PDF is over the maximum, counting pages without PyMuPDF.
- Terms: a shared `docs/terms.md`, read before drafting and checked by the style gate across chapters, tables and figure labels.
- Sign-off: the template and the reminder spell out a new row each time, the real date, the current section numbers and the commit read; the student makes that commit. A question about how to sign, merge or send now loads the writing skill, which holds the rule.
- The student's columns: every turn names the `ai-log.md` rows and record warnings still waiting for the student, who alone fills them in.
- Review coverage: each review records its commit and scope; a review in the drafting session is a self-check; a partial review lists the whole-thesis checks it could not make. The checker reports changes since the last review in a new session, and a signed version that contains changes no review covered. `/final` lists them.
- Gates: honesty opens the source of key results and checks its version, and reads the code behind labels and formulas; logic maps every finding in the abstract and conclusion to the table, figure or section that shows it; style checks terms across the thesis and flags repeated limits and members named in the body.
- README: install first, with the skills CLI, the Claude Code marketplace or by hand; a table of skills, the project files, the repository layout, evaluation and citation.

## 0.2.0 (unreleased)

- From an idea to submission: `/idea`, `/plan`, `/write`, `/review`, `/defense`, `/final`.
- New `bachelor-thesis-planning` skill: refine the student's idea, write a proposal, connect objectives, artifacts, evidence and sections, and keep a decision log. Work can start from an idea or from existing work.
- `/write all` coordinates the whole thesis from a plan, chapter by chapter or with parallel agents, on its own branch. Each chapter follows the same rules as `/write auto`.
- `bachelor-thesis-writing` no longer limits a request to one section. Every section clears the same bar, and a run over several sections needs a clear yes, stops at what only the student can decide, and commits each section separately.
- `bachelor-thesis-review` also rehearses the defense and lists what is open before submitting, without a verdict.

## 0.1.0 (unreleased)

- First version of `bachelor-thesis-writing` and `bachelor-thesis-review`.
- Five warn-only gates: honesty, logic, structure, format, style.
- Build and research thesis types; Vietnamese and English.
- School profiles: PTIT (community proposal) and generic.
- Mechanical checker for Word, LaTeX, Typst and Markdown sources.
- Checker reads Typst and LaTeX projects from the main file, resolves citation keys against `.bib` files, and measures margins and body size on the PDF.
- Sign-off: the student reads and signs before a merge, a release or sending to an advisor; the skills never sign for them, and the checker warns about unsigned or changed versions.
- Install as a Claude Code plugin, with `npx skills add`, or by copying a folder.
- Frontmatter carries the license, requirements, author and source, so they travel with an installed skill.
