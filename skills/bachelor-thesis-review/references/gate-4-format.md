# Gate 4: Format

Question: does the document follow the format basis that was chosen?

## Basis first

Read `.thesis/profile.md`. If it does not exist, ask for the school, then:

- If `profiles/<school>.md` exists, use it after the student confirms it.
- If the student has a rule, template or defended thesis, build `.thesis/profile.md` as `references/setup.md` in `bachelor-thesis-writing` describes. Sort each value into required, inferred or unspecified.
- Otherwise use `profiles/generic.md`.

Open the report by naming the basis and its status. A profile is not an official rule unless the school says so. Without a written rule, do not present common practice as a requirement: report those items as `low`, labelled "common practice, not a rule of this school". Never state or confirm that the document complies; send the student to the advisor or faculty for that.

## Checks

| Item | How |
|---|---|
| Paper, margins, base font and size | Script for `.docx` and PDF. It compares only the values the profile sets; otherwise it lists the actual values for you to report |
| Line and paragraph spacing, indents | Inspect the document; a `.docx` may override styles directly |
| Page numbers: position, style change between front matter and body | Inspect the PDF pages |
| Cover and title page fields | Compare with the profile. Check that placeholders are gone |
| Order of front matter | Compare with the profile |
| Captions: tables above, figures below, numbering by chapter | Sample every chapter |
| Equations | Numbered and consistent |
| Reference style | One style throughout; every entry complete |
| Headings use real heading styles, so the table of contents can update | Script reports heading structure in `.docx` |
| Markdown symbols or draft marks left in the document | Script |

## Limits

- Say what you checked and how. If you could only read the file structure, say the file should also be opened in its own editor, because display can differ.
- If there is no PDF, say that page-level checks were skipped.
- Inspect a page of each kind: cover, front matter, chapter opening, body with figure, references, appendix.
