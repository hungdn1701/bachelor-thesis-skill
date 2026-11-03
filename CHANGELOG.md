# Changelog

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
