# Evaluating the skills

[`scenarios.json`](scenarios.json) lists requests that put pressure on a skill: a deadline, a request for invented numbers, a request to mark everything as passed. The thesis project they use is fictional, and its defects are planted.

## Run a scenario

1. Create a separate copy of the project for each run:

   ```bash
   python evals/make_fixture.py /tmp/evals run1
   python evals/make_fixture.py /tmp/evals --research run2   # scenarios with "fixture": "research"
   ```

2. Start a new agent session in that folder, with the skill available, and send the scenario's `prompt` as written.
3. Read the transcript and the changed files against `must` and `must_not`.

To test a change, run the same scenario before and after it. Without a before run, you cannot tell whether the change did anything.

## Reading the results

Read what the agent actually did. Unit tests and script output do not show whether a skill holds up under pressure. When a new excuse appears, add a counter to the skill and run the scenarios again.
