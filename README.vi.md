# Bộ skill đồ án tốt nghiệp đại học

[![CI](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue)](LICENSE)

[English](README.md)

Các agent skill giúp viết và rà đồ án tốt nghiệp đại học ngành kỹ thuật. Bộ skill dùng được với Word, LaTeX, Typst và Markdown, không mặc định bất kỳ trường nào.

| Skill | Làm gì |
|---|---|
| `bachelor-thesis-writing` | Hỏi trường, loại đồ án và ngôn ngữ; kiểm kê bằng chứng; viết nháp từng mục từ dữ liệu thật |
| `bachelor-thesis-review` | Rà đồ án hoặc từng chương như một giảng viên khó tính qua năm gate. Skill chỉ cảnh báo, không sửa bài |

Tác giả vẫn là sinh viên. Bộ skill giúp dùng AI cho đúng cách, không thay cho nhận định của sinh viên hay giảng viên hướng dẫn.

## Cài đặt

Claude Code:

```bash
claude plugin install bachelor-thesis --marketplace hungdn1701/bachelor-thesis-skill
```

Các agent khác, chạy trong thư mục đồ án (cần Node.js 22.20 trở lên):

```bash
npx skills add hungdn1701/bachelor-thesis-skill
```

Hoặc chép các thư mục trong `skills/` vào thư mục skill của agent, ví dụ `.claude/skills/` hay `.agents/skills/`. Script rà cần Python 3.9 trở lên; nếu không có Python, việc rà vẫn tiếp tục bằng cách đọc văn bản.

## Các agent được hỗ trợ

Bộ skill dùng định dạng mở [Agent Skills](https://agentskills.io). Agent cần nạp được định dạng này, đọc và ghi được tệp trong dự án, và chạy được lệnh. Các ứng dụng chat không truy cập được thư mục dự án không nằm trong phạm vi hỗ trợ.

| Tình trạng | Agent |
|---|---|
| Đã chạy cả hai skill đúng như thiết kế | Claude Code, GitHub Copilot CLI |
| Đã chạy, nhưng chỉ tuân theo một phần quy tắc | Antigravity CLI |
| Nạp được skill, chưa chạy thử | Gemini CLI (cần tin cậy thư mục trước) |
| Chưa thử | Codex, Cursor và [các agent khác trong danh sách của công cụ cài](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) |

Kết quả này đến từ vài lượt chạy trên dự án giả tưởng ([chi tiết](evals/RESULTS.md)). Rất mong nhận báo cáo khi dùng với các agent khác.

## Cách dùng

Nói với agent bằng tiếng Việt hoặc tiếng Anh, ví dụ:

- "Thiết lập giúp em dự án đồ án."
- "Viết nháp mục 5.1 từ dữ liệu trong `data/`."
- "Rà Chương 5 trước khi em gửi thầy."
- "Chỉ kiểm tra văn phong và trình bày."

Nên chạy phần rà trong một phiên mới, tách khỏi phiên đã viết nháp. Trước khi gộp, gửi giảng viên hoặc chốt một phiên bản, sinh viên tự đọc phần thay đổi và tự ký vào `docs/sign-off.md`.

Bộ skill lưu tệp trong dự án đồ án: `.thesis/` (trường, loại đồ án, ngôn ngữ, căn cứ trình bày), `evidence/claims.csv` (từng con số và nguồn), `docs/ai-log.md` (phần AI đã tham gia), `docs/gate-record.md` (cảnh báo và quyết định của sinh viên) và `docs/sign-off.md` (phần sinh viên đã đọc và xác nhận).

Phần rà chạy năm gate: trung thực, logic, bố cục, trình bày và văn phong. Gate chỉ cảnh báo, và không có cảnh báo cũng không có nghĩa là được duyệt: quyền quyết định thuộc giảng viên và hội đồng.

## Những việc bộ skill không làm

- Bịa số liệu, kết quả, trích dẫn, chữ ký hay xác nhận.
- Viết nguyên một chương hoặc cả quyển trong một yêu cầu.
- Coi kết quả do AI tự tạo là số đo của sinh viên.
- Giúp né công cụ phát hiện AI, cố tình thêm lỗi cho giống người viết, hay giấu việc dùng AI.
- Khẳng định đồ án đã đúng quy định của trường.
- Xác nhận thay sinh viên, hoặc gộp, gắn tag, gửi một phiên bản sinh viên chưa ký.

## Loại đồ án và các trường

Có hai loại đồ án: **xây dựng**, kết quả chính là một hệ thống chạy được; và **nghiên cứu**, kết quả chính là câu trả lời cho một câu hỏi.

Không có trường mặc định. Skill hỏi trường của sinh viên, rồi dùng hồ sơ của trường nếu đã có, dựng hồ sơ từ quy định, mẫu hoặc đồ án đã bảo vệ, hoặc dùng bộ mặc định thận trọng và nói rõ điều đó. Quy định của trường, khoa hoặc giảng viên hướng dẫn luôn được ưu tiên hơn hồ sơ. Hiện có: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) và [generic](skills/bachelor-thesis-writing/profiles/generic.md).

## Về dự án này

Đây là đóng góp cá nhân của tôi, Đặng Ngọc Hùng (giảng viên, PTIT), trước hết để hỗ trợ sinh viên nhóm tôi hướng dẫn. Tôi chịu trách nhiệm về các quy ước trong repo. Repo không phải văn bản của PTIT hay bất kỳ đơn vị nào. Ai thấy phù hợp thì dùng, không bắt buộc. Sau này có trở thành chính thức hay không sẽ tính sau.

## Đóng góp

Rất mong nhận issue và pull request, nhất là hồ sơ trường và các trường hợp skill xử lý chưa tốt. Xem [CONTRIBUTING.vi.md](CONTRIBUTING.vi.md).

## Bản quyền

Nội dung skill, tài liệu tham chiếu, hồ sơ trường và tài liệu dùng [CC BY 4.0](LICENSE). Script, test và mã đánh giá dùng [MIT](skills/bachelor-thesis-review/scripts/LICENSE). Các giấy phép này không áp dụng cho đồ án của sinh viên, và sinh viên không cần ghi nguồn repo này trong đồ án. Tên và logo của các trường thuộc về chủ sở hữu; repo không lưu logo nào.
