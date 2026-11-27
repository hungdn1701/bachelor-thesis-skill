# Gate 5: Style

Question: does it read as plain academic writing about the work?

The aim is clarity, not hiding AI use. AI involvement is disclosed in `ai-log.md` and wherever the school requires. Do not advise on detector scores.

The word lists in `data/style-terms.json` give candidates. A hit is a reason to read the sentence, not a defect. Never bulk-replace terms.

## Leftovers from a chat or a workflow (`high`)

- Assistant phrases: "Chắc chắn rồi!", "Dưới đây là", "Certainly!", "Here is the".
- Text addressed to someone: "như bạn yêu cầu", "code bạn đã gửi", "as you requested".
- Draft marks: `TODO`, `[MISSING]`, Markdown symbols in a Word file.
- Process notes: file paths, commit hashes or tool names that serve the writer rather than the reader.

## Inflated claims (`medium`)

Words such as *vượt trội, đột phá, tối ưu, toàn diện, mạnh mẽ, hoàn hảo; outperforms, robust, optimal, seamless* are claims. Each needs its measurement, or the word goes. Suggest the plain form, with its number if there is one.

## Empty phrases (`low`)

- Openers with no content: "Trong bối cảnh…", "Ngày nay, với sự phát triển mạnh mẽ của…", "Có thể nói rằng…", "It is important to note that…".
- Stock wording: "đóng vai trò then chốt", "nền tảng vững chắc", "bức tranh toàn cảnh", "plays a crucial role", "delve into".
- Metaphors: "chìa khóa", "đòn bẩy", "hành trình", "xương sống", "landscape", "tapestry".

## Terms across the thesis (`medium`)

Build a list of the thesis's key terms: from `docs/terms.md` if it exists, otherwise from definitions, the abbreviation list and the headings. Then look for each concept under other names, in the text, table headers and figure labels; read a figure's source or the image when its labels are text you can reach. Report each concept that has two names, with every location, and suggest the name already used most, or the one in `docs/terms.md`. In a group thesis, check across the parts of different writers. A partial review checks only its own scope: say so.

## Patterns (`low`)

Report these only when they recur:

- Every paragraph shaped the same; lists of exactly three everywhere.
- "Không chỉ… mà còn…", "not only… but also" as a habit.
- Dashes used for asides, and semicolons chaining clauses.
- Bold lead-ins on every list item, and lists where a paragraph would argue better.
- Several names for one concept in a paragraph.
- The same limit stated again in section after section, instead of once for the chapter.
- Sentences about what the text does not do, such as "this section does not judge whether the objective is met".
- A member of a group named in the body, such as "according to Lan".
- Sentences too long to read aloud.

## Language

- **Vietnamese:** no "bạn", "mình" or "chúng ta" in the body. Standard technical terms may stay in English, but do not mix languages inside a descriptive phrase.
- **English:** one spelling convention, formal register.

## Keep these

- Bounding words: "có thể", "trong điều kiện thử nghiệm", "suggests", "in this test". Removing them turns an observation into a stronger claim.
- Scope statements and stated limits, said once where they belong. When a repeated limit is removed, it must still be stated somewhere.
- An AI-use disclosure required by the school.
- A tool name when the tool is the subject of the thesis.
- Terms of art that look like jargon, and "state of the art" when describing the literature.
- Introductory roadmap sentences, where the school's convention expects them.
