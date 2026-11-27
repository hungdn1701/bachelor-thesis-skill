# Drafting a section

## Steps

1. **Find the section's job** in the structure file for this thesis type.
2. **Collect its evidence** and list what is missing. If nothing supports the section, return the gap list instead of prose.
3. **Ask for the student's reasoning** when the section explains a choice, a contribution or a conclusion. A sentence or two from them is enough to work from.
4. **Check the terms.** Read `docs/terms.md` if it exists, and use its names. A concept that is new to the thesis gets one name; add it there and tell the student.
5. **Write the section**, in the student's chosen format and using their existing labels and citation keys.
6. **Close with the outputs** listed in `SKILL.md`.

## Writing rules

- Open a paragraph with its point, then give the evidence.
- State the conditions of every result: "at 200 concurrent users on the test machine", not "under load".
- Report failed tests and negative results. Leaving them out misleads the reader.
- Separate what was measured from what it may mean. Use "suggests" or "is consistent with" unless a mechanism was tested.
- Use one term per concept across the whole thesis, in the text, tables and figure labels. Define each abbreviation at first use.
- Introduce each figure and table in the text before it appears, and interpret it afterwards.
- Refer to sections, figures and tables through the format's cross-references, not typed numbers, so a renumbering cannot leave them wrong.
- Describe and draw only what the version described actually runs. Code that is present but disabled, or replaced, is not part of the system.
- Do not paste large blocks of code. Explain the decision and show only the lines needed.
- Keep the thesis about the work, not about how the text was produced. Prose must not contain phrases such as "based on the code you sent", file paths used only for your own reference, commit hashes, or the names of AI tools, unless such a tool is the subject of the thesis or ran a test the thesis reports. Name measurement and test tools such as k6, since they are part of the method. AI use belongs in `ai-log.md` and in any disclosure the school requires.
- Do not write sentences about what the text leaves out or will not judge, such as "this section does not say whether the objective is met". Those rules are for you, not for the reader.

## Say a shared fact once

Some facts apply to a whole chapter or the whole thesis. Repeated in every section, they bury the result, and the student ends up deleting them by hand.

| Fact | Where it goes |
|---|---|
| Limits every test shares: one run, one machine, a small sample, tests an AI tool ran | Once at the start of the evaluation chapter, and again where results are set against the objectives |
| A limit of one test only | In that test's section |
| Work the student inherited from others | Once in the introduction and the scope or system overview |

Gathering limits never removes them. Every bad result, failed attempt and unmeasured point stays somewhere in the thesis.

## What only the student writes

- **Acknowledgements, the declaration, a personal preface.** Ask what they want to say, then write it from their words. Do not leave `[MISSING]` inside them.
- **Assessments, contributions, conclusions.** Ask first, as rule 8 says. In a run that cannot stop, follow `references/write-auto.md`: one mark for the section, not one in every cell, and the questions at the end.
- **Evidence that may not exist.** Do not write `[MISSING: evidence, if the student has any]`. Write what the evidence supports, and ask.

## Group thesis

- In the body, write about the work. When a sentence needs an actor, it is the group ("nhóm", "the team"), never a member by name: not "according to Lan", not "the backend built by Minh".
- Names appear only where the school expects them: the cover, the declaration, and the table that divides the work.
- That table lists what each member confirms as theirs. Commits help them remember; they do not decide it.
- A member's recollection is evidence of the weakest kind. Say so in the text, as the group's: "the group recalls; no log was kept".

## Revising after a review

Apply one finding at a time, and check each against its source before changing the text. A pass that fixes many places at once tends to add a new error. Commit in small groups, so that each change can be read and undone.

## Vietnamese

- Use impersonal academic prose: "đồ án đề xuất", "hệ thống được kiểm thử". Do not write "bạn", "mình" or "chúng ta" in the body. "Em", or "chúng em" for a group, appears only in the declaration and acknowledgements, if the school expects it.
- Keep standard technical terms in English when that is normal in the field, and write the rest in Vietnamese. Do not mix the two inside a descriptive phrase.
- Write decimals with a comma: `3,1%`.

## English

- Use formal technical English. Use the passive for procedure and "this thesis" for claims.
- Keep one spelling convention throughout.

## Second-language abstract

Translate from the final abstract. Mark it for the student to check, since it carries the same claims.
