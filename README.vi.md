# Bộ skill đồ án tốt nghiệp đại học

[English](README.md)

Hai agent skill giúp viết và rà đồ án tốt nghiệp đại học ngành kỹ thuật. Bộ skill dùng được với Word, LaTeX, Typst và Markdown, không mặc định bất kỳ trường nào.

| Skill | Làm gì |
|---|---|
| `bachelor-thesis-writing` | Hỏi trường, loại đồ án và ngôn ngữ; kiểm kê bằng chứng; viết nháp từng mục từ dữ liệu thật; ghi lại phần AI đã tham gia |
| `bachelor-thesis-review` | Rà đồ án hoặc từng chương như một giảng viên khó tính qua năm gate. Skill chỉ cảnh báo, không sửa bài |

Tác giả vẫn là sinh viên. Bộ skill giúp dùng AI cho đúng cách, không thay cho nhận định của sinh viên hay giảng viên hướng dẫn.

## Cài đặt

```bash
npx skills add hungdn1701/bachelor-thesis-skill                                  # cả hai skill
npx skills add hungdn1701/bachelor-thesis-skill --skill bachelor-thesis-review   # chỉ phần rà
```

Hoặc chép một thư mục trong `skills/` vào thư mục skill của công cụ AI đang dùng. Script rà chỉ cần Python 3.9 trở lên; PyMuPDF là tùy chọn, dùng để kiểm tra PDF.

## Cách dùng

Nói với công cụ AI bằng tiếng Việt hoặc tiếng Anh, ví dụ:

- "Thiết lập giúp em dự án đồ án."
- "Viết nháp mục 5.1 từ dữ liệu trong `data/`."
- "Rà Chương 5 trước khi em gửi thầy."
- "Chỉ kiểm tra văn phong và trình bày."

Nên chạy phần rà trong một phiên mới, tách khỏi phiên đã viết nháp.

Bộ skill lưu các tệp sau trong dự án đồ án:

| Tệp | Mục đích |
|---|---|
| `.thesis/config.json` | Trường, loại đồ án, ngôn ngữ, các tệp nguồn |
| `.thesis/profile.md`, `.thesis/profile.json` | Căn cứ trình bày của trường |
| `evidence/claims.csv` | Từng con số trong đồ án, kèm nguồn và ngày sinh viên kiểm chứng |
| `docs/ai-log.md` | AI đã tham gia khi nào, ra sao; cột cuối do sinh viên viết |
| `docs/gate-record.md` | Cảnh báo khi rà và quyết định của sinh viên với từng cảnh báo |

## Năm gate

| Gate | Câu hỏi |
|---|---|
| Trung thực | Mỗi điều nêu ra có đúng với công việc đã làm và truy được nguồn không? |
| Logic | Lập luận có giữ được từ mục tiêu đến kết luận, cùng một mức khẳng định không? |
| Bố cục | Có đủ các phần, đúng thứ tự, mỗi phần làm đúng việc của nó không? |
| Trình bày | Tài liệu có theo căn cứ trình bày của trường không? |
| Văn phong | Có phải văn học thuật giản dị, không cường điệu, không sót dấu vết chatbot không? |

Gate chỉ cảnh báo, không chặn build hay chặn nộp, và không có cảnh báo cũng không có nghĩa là được duyệt: quyền quyết định thuộc giảng viên và hội đồng. Biên bản rà giúp giảng viên thấy trong vài phút những gì bị cảnh báo và sinh viên đã quyết định ra sao.

## Những việc bộ skill không làm

- Bịa số liệu, kết quả, trích dẫn, chữ ký hay xác nhận.
- Viết nguyên một chương hoặc cả quyển trong một yêu cầu.
- Coi kết quả do AI tự tạo là số đo của sinh viên.
- Giúp né công cụ phát hiện AI, cố tình thêm lỗi cho giống người viết, hay giấu việc dùng AI.
- Khẳng định đồ án đã đúng quy định của trường.

## Hai loại đồ án

- **Xây dựng:** kết quả chính là một hệ thống chạy được. Mạch: mục tiêu, yêu cầu, thiết kế, triển khai, kiểm thử, kết quả, kết luận.
- **Nghiên cứu:** kết quả chính là câu trả lời cho một câu hỏi. Mạch: câu hỏi nghiên cứu, phương pháp, thực nghiệm, kết quả, bàn luận, kết luận.

## Các trường

Không có trường mặc định. Skill hỏi trường của sinh viên, rồi:

1. Nếu repo đã có hồ sơ của trường, dùng hồ sơ đó.
2. Nếu sinh viên có quy định, mẫu hoặc đồ án đã bảo vệ, dựng hồ sơ từ các tài liệu này và phân biệt phần bắt buộc với phần chỉ suy ra.
3. Nếu không có gì, dùng bộ mặc định thận trọng và nói rõ điều đó trong mọi báo cáo.

Quy định của trường, khoa hoặc giảng viên hướng dẫn luôn được ưu tiên hơn hồ sơ. Hiện có: [PTIT](skills/bachelor-thesis-writing/profiles/ptit.md) và [generic](skills/bachelor-thesis-writing/profiles/generic.md). Rất mong nhận thêm hồ sơ của các trường khác.

## Về dự án này

Đây là đóng góp cá nhân của tôi, Đặng Ngọc Hùng (giảng viên, PTIT), trước hết để hỗ trợ sinh viên nhóm tôi hướng dẫn. Tôi chịu trách nhiệm về các quy ước trong repo. Repo không phải văn bản của PTIT hay bất kỳ đơn vị nào. Ai thấy phù hợp thì dùng, không bắt buộc. Sau này có trở thành chính thức hay không sẽ tính sau.

## Đóng góp

Rất mong nhận issue và pull request, nhất là hồ sơ trường và các trường hợp skill xử lý chưa tốt. Xem [CONTRIBUTING.vi.md](CONTRIBUTING.vi.md).

## Bản quyền

| Phần | Giấy phép |
|---|---|
| Nội dung skill, tài liệu tham chiếu, hồ sơ trường, tài liệu | [CC BY 4.0](LICENSE) |
| Script, test và mã đánh giá | [MIT](skills/bachelor-thesis-review/scripts/LICENSE) |

Đồ án là của sinh viên: các giấy phép này không áp dụng cho đồ án, và sinh viên không cần ghi nguồn repo này trong đồ án. Tên và logo của các trường thuộc về chủ sở hữu, không thuộc phạm vi các giấy phép này; repo không lưu logo nào.
