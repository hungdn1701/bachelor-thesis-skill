# Structure: build thesis

The main result is a working system. The chain that must hold: **objective → requirement → design → implementation → test → result → conclusion**. School rules override these chapter names.

| Part | Job | Must contain | Common failure |
|---|---|---|---|
| Introduction | Why this work, and what counts as done | Problem, measurable objectives (O1, O2…), scope, approach, chapter outline | Objectives that cannot be tested |
| 1. Problem and existing systems | Show the need and the gap | Evidence of the problem, similar systems compared on stated criteria, the gap this work addresses | A list of products with no criteria |
| 2. Background and technology | What the reader needs in order to follow the design | Only concepts and technologies actually used, with reasons and alternatives considered | A textbook summary of each framework |
| 3. Analysis and design | What the system must do and how it is organized | Actors, functional and non-functional requirements with IDs (R1, R2…), architecture, data design, interfaces, decisions with trade-offs | No non-functional targets, so nothing can be evaluated |
| 4. Implementation | What was built and how it differs from the design | Environment, key decisions, difficulties, deviations from design | Code dumps and screenshots with no explanation |
| 5. Testing and evaluation | Whether the system meets its requirements | Test plan mapped to requirements; functional, performance and security tests as relevant; environment, data, sample size; failures included; threats to validity; comparison with objectives | "All tests pass" with no plan or data |
| Conclusion | What was achieved, against the objectives | Each objective with its result, limits, future work. No new claims | Claims that appear nowhere in chapter 5 |

For a group thesis, add a work division stating who did what, and make sure it matches the project history.
