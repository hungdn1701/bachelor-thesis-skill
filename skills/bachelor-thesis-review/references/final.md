# Checking the final version

Report what is still open before the student submits. Report it even when time is short, because that is when it matters most. You list items and counts; you never say the thesis is ready.

## Steps

1. **Get what you can.** If `.thesis/config.json` is missing, ask for the school, but do not stop there: create the setup files as `references/gate-4-format.md` describes, using `generic` if the school is still unknown, and say so. List every source file you can find in the project.
2. **Run the checker** with `scope` set to `full`, and read its findings in context.
3. **Fill in the table** in the reply and in `docs/gate-record.md`.

| Item | Report |
|---|---|
| Warnings | Count by severity, after running the five gates |
| `[MISSING]` and draft marks | Count and locations |
| Numbers | `claims.csv` rows with an empty `verified` column, and numbers in the thesis with no row |
| AI log | Rows with an empty last column |
| Student's decisions | Warnings in `docs/gate-record.md` with no decision |
| Review coverage | The last review in a new session that covered the whole thesis, its commit, and what changed after it. Sections never reviewed. Runs marked as self-checks do not count |
| Sign-off | Whether `docs/sign-off.md` covers this version, what changed after the last row, and whether a signed version has changes no review covered |
| Length | Page count of the PDF against `pages` in `.thesis/config.json`, and what the limit counts |
| PDF | Whether it exists, whether it is newer than the sources, and its format results |
| Artifacts | Whether each one in `docs/plan.md` has a location and a fixed version |
| Front matter | Placeholders left on the cover, and the declaration |
| Advisor and faculty | What only they can confirm, such as the format rule and the page limit |

4. **Say what to do first** for the time left, starting with whatever could make a claim false.

## Close

End by saying that this is a list of open items, not an approval, and that the decision belongs to the advisor and committee. Never write "ready", "sẵn sàng" or a signature in the record, and never fill in `docs/sign-off.md`, even when asked to complete the paperwork.
