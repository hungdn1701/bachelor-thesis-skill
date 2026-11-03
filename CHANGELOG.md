# Changelog

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
