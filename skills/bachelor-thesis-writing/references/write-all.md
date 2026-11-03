# Writing the whole thesis

Use this for `/write all`, or when a student asks for the whole thesis. It only coordinates: each chapter is a run as `references/write-auto.md` describes, and every rule there still holds.

## Before starting

1. **Have a plan.** This needs `docs/plan.md`. Without one, stop and suggest `bachelor-thesis-planning`: a whole thesis cannot be coordinated from a list made on the spot.
2. **Show the size.** List the chapters in order, the number of sections, the evidence state of each, and what will stay open. Say how much the student will have to read.
3. **Get a clear yes.** If the request already approves the plan, that is the yes: show the list and start. Otherwise wait for one. An approval never covers what stays open below.
4. **Work on a branch of its own,** after checking the working tree as `references/write-auto.md` says, so the main branch stays as it was.

## Order

Follow the plan, so that later chapters can rest on earlier ones: requirements and design, then implementation, then evaluation. Write the opening and the conclusion last. Their facts can come from the chapters, but objectives met, contributions and conclusions stay `[MISSING: your reasoning on ...]`.

## Two ways to run

| Mode | Use when |
|---|---|
| **One agent, chapter by chapter** | The default. It works on any agent, and each chapter can use what the last one found |
| **One subagent per chapter** | The student wants speed, the agent can start subagents with their own worktree or branch, and the chapters do not depend on each other's text. Otherwise run one by one |

### Coordinating subagents

Subagents do not inherit this skill, so give each one:

- Its chapter and sections from the plan, and the evidence files.
- The paths to this skill's `SKILL.md`, `references/drafting.md` and `references/write-auto.md`, with the instruction to follow them.
- Its own worktree or branch, for its section commits.
- The instruction to leave `claims.csv`, `ai-log.md` and other chapters alone, and to return its rows, its `[MISSING]` items and anything it stopped on.

Run a chapter that needs another chapter's result after that one finishes. As coordinator, you alone write the shared files and bring the chapter branches together on the thesis branch, then remove their worktrees. Check each result before accepting it: a subagent's report is a claim, so read its text and its rows.

## When a chapter stops

A stop inside a chapter leaves that chapter open, and the others go on unless they depend on it. Stop everything only when the plan no longer matches the files.

## Before closing

Read across the chapters. List, and do not silently fix:

- The same value given differently in two places.
- A term used in two ways.
- A cross-reference to something that does not exist.
- A number with no `claims.csv` row.

## Closing

| Chapter | Sections written | `[MISSING]` | Commits or branch | Stopped on |
|---|---|---|---|---|

Then give what to read first, starting with the chapters that make claims, and three defense questions for each chapter.

A complete draft is not a finished thesis. Next, the student reads it and runs `bachelor-thesis-review` on each chapter in a new session, then signs chapter by chapter in `docs/sign-off.md`. Never merge the branch, tag it or sign.
