# Gate 2: Logic

Question: does the argument hold from start to finish, at the same strength?

## Build the chain

Fill in this table in the report, with one row per objective or research question.

**Build thesis:**

| Objective | Requirement | Design | Implementation | Test | Result | Conclusion | Same strength? |
|---|---|---|---|---|---|---|---|

**Research thesis:**

| Research question | Method | Experiment | Result | Discussion | Conclusion | Same strength? |
|---|---|---|---|---|---|---|

For a partial review, fill in only what the provided text covers and say so.

## Failure modes

| Failure | Test |
|---|---|
| Undelivered objective | An objective or question has no result |
| Orphan result | A result no objective asked for |
| Widened abstract | The abstract claims more than the results chapter |
| Conclusion drift | A conclusion that appears nowhere in the results |
| Unmeasured criterion | "Meets the requirement" with no stated target |

## Claim audit

Read every sentence that contains a word such as *always, never, all, any, only, proves, guarantees* or *luôn, mọi, tất cả, duy nhất, chứng minh, đảm bảo, hoàn toàn*, and ask what was actually tested.

| Error | Example | Correct form |
|---|---|---|
| General claim from limited tests | "handles every load level" | "handled up to 200 concurrent users on the test machine" |
| Method claim from one implementation | "the approach achieves" | "this implementation achieved, in the tested configuration" |
| No failures seen, so none exist | "has no errors" | "no errors were observed in N runs" |
| Correlation stated as cause | "because X, performance improved" | State the association; state a cause only if it was tested |
| Significance without a test | "significantly better" | Name the test, or give the numbers |
| Comparison without a basis | "outperforms similar systems" | Same measure, same conditions, with a source |

## Contradictions

Read these pairs side by side: abstract and conclusion; text and table; text and figure caption; described method and actual configuration; stated limits and later claims; related work and claimed novelty.

## Strongest objection

Write the single strongest objection a committee member could raise, then find where the thesis answers it. If it does not, report that as `medium`.

## Keep these

Do not flag scope statements, explicit non-claims, or bounding words such as "in this test" or "suggests". They make a claim accurate.
