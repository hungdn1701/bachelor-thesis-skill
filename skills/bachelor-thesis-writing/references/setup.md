# Setup

Run once per thesis. Ask only what is missing, and do not move the student to another writing tool.

## 1. Ask

- **School and faculty.** There is no default school.
- **Thesis type:** `build` (the main result is a system) or `research` (the main result answers a research question through experiments or analysis). If both apply, choose by what the conclusion claims.
- **Language:** `vi` or `en`.
- **Sources:** the files that hold the thesis text, such as `.docx`, `.tex`, `.typ` or `.md`, and the exported PDF if any. If they are obvious from the folder, list them and tell the student rather than asking.

## 2. Choose the format basis

| Situation | Action | Report wording |
|---|---|---|
| A profile for this school exists in `profiles/` | Copy `<id>.md` and `<id>.json` to `.thesis/profile.md` and `.thesis/profile.json`. Ask whether the faculty has its own rule | "Based on the community profile for <school>, not an official rule" |
| No profile, but the student has a rule, template or defended thesis | Build a profile from those documents, as below | "Based on <documents>" |
| Nothing is available right now | Copy `generic.md` and `generic.json`, carry on, and ask the student to request a rule, template or defended thesis from the faculty | "No school rule; format not checked against one" |

A rule from the faculty or advisor overrides any profile. Never tell a student that a thesis complies with a school rule; only an advisor or faculty can confirm that.

## 3. Build a profile from documents

Read the student's documents and sort every value:

| Class | Meaning | Script checks it? |
|---|---|---|
| `required` | Written in a rule or official template | Yes, put it in `profile.json` |
| `inferred` | Seen in a defended thesis, with no written rule | No, list it in `profile.md` as guidance |
| `unspecified` | Not stated anywhere | No, write "not specified" and do not guess |

`profile.md` follows `profiles/ptit.md`, with a source for each value. After setup, tell the student that the profile can be contributed back through a pull request if it contains no personal data.

## 4. Create the files

Create these in the thesis project, without overwriting existing ones:

| File | From |
|---|---|
| `.thesis/config.json` | `assets/config.json`, filled in |
| `.thesis/profile.md`, `.thesis/profile.json` | Step 2 or 3 |
| `evidence/claims.csv` | `assets/claims.csv` |
| `docs/ai-log.md` | `assets/ai-log.md` |

In `config.json`, set `scope` to `partial` while chapters are missing and to `full` for the complete thesis.
