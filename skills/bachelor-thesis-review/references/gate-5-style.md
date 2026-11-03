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

## Patterns (`low`)

Report these only when they recur:

- Every paragraph shaped the same; lists of exactly three everywhere.
- "Không chỉ… mà còn…", "not only… but also" as a habit.
- Dashes used for asides, and semicolons chaining clauses.
- Bold lead-ins on every list item, and lists where a paragraph would argue better.
- Several names for one concept in a paragraph.
- Sentences too long to read aloud.

## Language

- **Vietnamese:** no "bạn", "mình" or "chúng ta" in the body. Standard technical terms may stay in English, but do not mix languages inside a descriptive phrase.
- **English:** one spelling convention, formal register.

## Keep these

- Bounding words: "có thể", "trong điều kiện thử nghiệm", "suggests", "in this test". Removing them turns an observation into a stronger claim.
- Scope statements and stated limits.
- An AI-use disclosure required by the school.
- A tool name when the tool is the subject of the thesis.
- Terms of art that look like jargon, and "state of the art" when describing the literature.
- Introductory roadmap sentences, where the school's convention expects them.
