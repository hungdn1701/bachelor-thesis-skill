# Bộ skill đồ án tốt nghiệp đại học

[![CI](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/hungdn1701/bachelor-thesis-skill/actions/workflows/ci.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue)](LICENSE)

[English](README.md)

Các agent skill đưa một đồ án tốt nghiệp đại học ngành kỹ thuật đi từ ý tưởng đến lúc nộp. Quyển đồ án là sản phẩm; mã nguồn, mô hình, bộ dữ liệu hay khảo sát là artifact, tức bằng chứng cho những gì đồ án khẳng định. Bộ skill dùng được với Word, LaTeX, Typst và Markdown, không mặc định bất kỳ trường nào.

```
  Ý TƯỞNG      KẾ HOẠCH       VIẾT          RÀ         BẢO VỆ      BẢN CUỐI
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ Câu hỏi │─▶│Luận điểm│─▶│Từng mục │─▶│ Năm gate│─▶│Hội đồng │─▶│ Chữ ký  │
│Đề cương │  │Artifact │  │ Số liệu │  │Cảnh báo │  │ Câu hỏi │  │Việc còn │
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
   /idea        /plan       /write       /review     /defense      /final
                  ▲            ▲            │
                  │            └──── sửa ───┘
           Đã có artifact
```

## Các bước

| Bước | Lệnh | Hoặc nói | Làm gì |
|---|---|---|---|
| Ý tưởng | `/idea` | "Tinh chỉnh giúp em ý tưởng đồ án về ..." | Làm rõ ý tưởng của sinh viên thành đề cương: vấn đề, các hướng, mục tiêu, giả định, phần không làm. Không chọn đề tài thay sinh viên |
| Kế hoạch | `/plan` | "Lập kế hoạch đồ án từ code và dữ liệu này." | Nối từng mục tiêu với artifact, bằng chứng và mục viết, rồi liệt kê phần còn thiếu |
| Viết | `/write`, `/write auto`, `/write all` | "Viết mục 5.1 từ `data/`." "Viết Chương 5 theo kế hoạch trong một lượt." "Viết cả quyển theo kế hoạch." | Viết từ bằng chứng thật và ghi lại phần AI đã tham gia. Chế độ auto chạy một chương của kế hoạch sau một lần đồng ý rõ ràng. Chế độ all chạy mọi chương trên một nhánh riêng, tuần tự hoặc bằng nhiều agent song song. Cả hai dừng ở những gì chỉ sinh viên quyết định được |
| Rà | `/review` | "Rà Chương 5." | Đọc như một giảng viên khó tính qua năm gate: trung thực, logic, bố cục, trình bày, văn phong. Chỉ cảnh báo, không sửa bài |
| Bảo vệ | `/defense` | "Luyện bảo vệ Chương 5." | Hội đồng giả, kiểm tra các khẳng định bằng chính bằng chứng của sinh viên |
| Bản cuối | `/final` | "Trước khi nộp còn thiếu gì?" | Liệt kê mọi việc còn mở. Không bao giờ nói đồ án đã sẵn sàng |

Trên Claude Code, lệnh có dạng `/bachelor-thesis:idea`. Các agent khác không có lệnh, chỉ cần nói yêu cầu.

**Hai điểm vào.** Có ý tưởng hoặc mới chỉ có mối quan tâm thì bắt đầu ở `/idea`. Đã được giao đề tài hoặc đã làm xong phần việc thì bắt đầu ở `/plan`. Cả hai đều đi về cùng một chuỗi từ mục tiêu đến kết luận, và phần nào đặt sau khi đo đều được ghi rõ.

**Hai chốt của con người.** Giảng viên quyết định về đề cương. Trước khi gộp, gửi giảng viên hoặc chốt một phiên bản, sinh viên tự đọc phần thay đổi và tự ký vào `docs/sign-off.md`.

Nên chạy phần rà trong một phiên mới, tách khỏi phiên đã viết. Việc làm ra artifact là của sinh viên và các công cụ khác; với phần mềm, có thể dùng [agent-skills](https://github.com/addyosmani/agent-skills) song song.

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

| Skill | Các bước |
|---|---|
| `bachelor-thesis-planning` | Ý tưởng, Kế hoạch |
| `bachelor-thesis-writing` | Viết |
| `bachelor-thesis-review` | Rà, Bảo vệ, Bản cuối |

## Các agent được hỗ trợ

Bộ skill dùng định dạng mở [Agent Skills](https://agentskills.io). Agent cần nạp được định dạng này, đọc và ghi được tệp trong dự án, và chạy được lệnh. Các ứng dụng chat không truy cập được thư mục dự án không nằm trong phạm vi hỗ trợ.

| Tình trạng | Agent |
|---|---|
| Đã chạy các bước đã thử đúng như thiết kế | Claude Code |
| Đã chạy phần viết và rà đúng như thiết kế ở v0.1 | GitHub Copilot CLI |
| Đã chạy phần viết và rà, nhưng chỉ tuân theo một phần quy tắc ở v0.1 | Antigravity CLI |
| Nạp được skill, chưa chạy thử | Gemini CLI (cần tin cậy thư mục trước) |
| Chưa thử | Codex, Cursor và [các agent khác trong danh sách của công cụ cài](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) |

Kết quả này đến từ vài lượt chạy trên dự án giả tưởng ([chi tiết](evals/RESULTS.md)). Rất mong nhận báo cáo khi dùng với các agent khác.

## Những việc bộ skill không làm

- Chọn đề tài thay sinh viên, hoặc bịa số liệu, kết quả, trích dẫn, chữ ký hay xác nhận.
- Viết kết luận thay sinh viên, hoặc coi kết quả do AI tự tạo là số đo của sinh viên.
- Giúp né công cụ phát hiện AI, cố tình thêm lỗi cho giống người viết, hay giấu việc dùng AI.
- Nói đồ án đã sẵn sàng, hay đã đúng quy định của trường.
- Xác nhận thay sinh viên, hoặc gộp, gắn tag, gửi một phiên bản sinh viên chưa ký.

## Các tệp trong dự án

`docs/proposal.md`, `docs/plan.md` và `docs/decisions.md` (ý tưởng, chuỗi luận điểm, lý do của từng lựa chọn), `.thesis/` (trường, loại đồ án, ngôn ngữ, căn cứ trình bày), `evidence/claims.csv` (từng con số và nguồn), `docs/ai-log.md` (phần AI đã tham gia), `docs/gate-record.md` (cảnh báo và quyết định của sinh viên), `docs/defense-notes.md` (câu hỏi luyện bảo vệ) và `docs/sign-off.md` (phần sinh viên đã đọc và xác nhận).

## Loại đồ án và các trường

Có hai loại đồ án: **xây dựng**, kết quả chính là một hệ thống chạy được; và **nghiên cứu**, kết quả chính là câu trả lời cho một câu hỏi.

Không có trường mặc định. Skill hỏi trường của sinh viên, rồi dùng hồ sơ của trường nếu đã có, dựng hồ sơ từ quy định, mẫu hoặc đồ án đã bảo vệ, hoặc dùng bộ mặc định thận trọng và nói rõ điều đó. Quy định của trường, khoa hoặc giảng viên hướng dẫn luôn được ưu tiên hơn hồ sơ. Hiện có: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) và [generic](skills/bachelor-thesis-writing/profiles/generic.md).

## Về dự án này

Đây là đóng góp cá nhân của tôi, Đặng Ngọc Hùng (giảng viên, PTIT), trước hết để hỗ trợ sinh viên nhóm tôi hướng dẫn. Tôi chịu trách nhiệm về các quy ước trong repo. Repo không phải văn bản của PTIT hay bất kỳ đơn vị nào. Ai thấy phù hợp thì dùng, không bắt buộc. Sau này có trở thành chính thức hay không sẽ tính sau. Ý tưởng về vòng đời được phỏng theo [agent-skills](https://github.com/addyosmani/agent-skills) và viết lại cho đồ án.

## Đóng góp

Rất mong nhận issue và pull request, nhất là hồ sơ trường và các trường hợp skill xử lý chưa tốt. Xem [CONTRIBUTING.vi.md](CONTRIBUTING.vi.md).

## Bản quyền

Nội dung skill, tài liệu tham chiếu, hồ sơ trường và tài liệu dùng [CC BY 4.0](LICENSE). Script, test và mã đánh giá dùng [MIT](skills/bachelor-thesis-review/scripts/LICENSE). Các giấy phép này không áp dụng cho đồ án của sinh viên, và sinh viên không cần ghi nguồn repo này trong đồ án. Tên và logo của các trường thuộc về chủ sở hữu; repo không lưu logo nào.
