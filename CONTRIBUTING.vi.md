# Đóng góp

[English](CONTRIBUTING.md)

Rất mong nhận issue và pull request. Hữu ích nhất là hồ sơ trường và báo cáo về các trường hợp skill xử lý chưa tốt.

## Tuyệt đối không đưa vào

- Dữ liệu sinh viên thật: tên, mã sinh viên, điểm, đồ án chưa công bố.
- Thông tin đăng nhập, địa chỉ nội bộ, hoặc nội dung riêng của trường hay công ty.
- Trao đổi riêng tư. Hãy mô tả vấn đề thay vì chép lại.

## Thêm hồ sơ trường

1. Thêm `<id>.md` và `<id>.json` vào `skills/bachelor-thesis-writing/profiles/`, theo mẫu [`ptit.md`](skills/bachelor-thesis-writing/profiles/ptit.md).
2. Nêu nguồn công khai cho từng thông số. Thông số không có văn bản quy định thì ghi là thông lệ.
3. Chỉ đưa vào tệp JSON các giá trị từ văn bản quy định, hoặc giá trị được nêu rõ là đề xuất. Script sẽ đối chiếu theo các giá trị này.
4. Chỉ đặt `status` là `official` nếu trường đã xác nhận; còn lại dùng `community`.
5. Chép cả hai tệp sang `skills/bachelor-thesis-review/profiles/`. Có test kiểm tra hai thư mục phải giống nhau.

## Báo skill xử lý chưa tốt

Dùng mẫu issue. Ghi yêu cầu, skill đã làm gì và mong đợi điều gì. Hãy dùng nội dung đồ án giả định.

## Sửa skill

Thay đổi `SKILL.md` hoặc tệp tham chiếu cần có bằng chứng là giúp ích:

1. Thêm hoặc chọn một tình huống trong [`evals/scenarios.json`](evals/scenarios.json) thể hiện vấn đề.
2. Chạy với một agent mới, trước và sau khi sửa, theo [`evals/README.md`](evals/README.md).
3. Nêu những gì đã thay đổi trong pull request. Giữ `SKILL.md` ngắn và chuyển chi tiết sang `references/`.

Giữ chỉ dẫn ở mức tổng quát. Không thêm quy tắc chỉ hợp với một trường, một đồ án hay một sự cố.

## Sửa script

Viết test trước, rồi chạy:

```bash
python -m unittest discover -s tests
```

Script chỉ dùng thư viện chuẩn của Python và luôn thoát với mã 0 khi chạy được: gate chỉ cảnh báo, không chặn.

## Quy ước

Nội dung skill viết bằng tiếng Anh. Tài liệu cho sinh viên và người đóng góp có cả tiếng Việt và tiếng Anh; khi sửa cần cập nhật cả hai. Tệp dùng UTF-8 không BOM.

Khi đóng góp, bạn đồng ý rằng phần đóng góp theo cùng giấy phép với phần được sửa, như mô tả trong [README](README.vi.md#bản-quyền).
