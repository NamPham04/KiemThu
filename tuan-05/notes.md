# Ghi chú tuần 5 – Nhóm App

---

## Phạm Phương Nam

### Điều đã học
Tuần này mình viết được 3 test tự động cho chức năng đăng nhập của app Swag Labs bằng Appium và pytest: đăng nhập thành công, sai mật khẩu và bỏ trống tên đăng nhập. Mình học cách tách code thành các hàm nhỏ (`cho_phan_tu`, `dang_nhap`) để không phải viết lặp lại, và dùng fixture `driver` để mỗi test tự mở app và tự đóng phiên khi xong. Mình cũng hiểu vì sao cần chờ phần tử xuất hiện (`WebDriverWait`) thay vì tìm ngay, vì app cần thời gian để tải màn hình. Ngoài ra, mình viết test case trong `testcases.md` trước rồi đối chiếu với code để hai bên khớp nhau.

### Trả lời câu hỏi phần đọc
- **Làm thế nào để tìm accessibility id của một nút trong ứng dụng?**
  Mở app trên máy ảo hoặc điện thoại, kết nối Appium Inspector, rồi bấm vào nút cần tìm trên màn hình. Inspector hiện các thuộc tính của phần tử, trong đó có `accessibility id` (trên Android chính là thuộc tính `content-desc`). Ví dụ trong bài này là `test-Username`, `test-Password`, `test-LOGIN`.
- **Vì sao trên điện thoại nên ưu tiên accessibility id?**
  Vì id này do lập trình viên đặt riêng cho từng phần tử nên ổn định, không đổi khi giao diện, văn bản hay thứ tự phần tử thay đổi. Nó cũng ngắn gọn và tìm nhanh hơn XPath, và cùng một kiểu định danh dùng được cho cả Android lẫn iOS. XPath dễ hỏng khi cấu trúc màn hình đổi, nên mình chỉ dùng khi không có id (như kiểm tra chữ "PRODUCTS" và các thông báo lỗi).
- **Nếu kết quả thực tế khác mong đợi thì pytest báo gì?**
  Câu `assert` sai sẽ gây `AssertionError`, pytest đánh dấu test là **FAILED** và in ra dòng assert bị sai cùng giá trị thực tế. Trong bài này còn một trường hợp khác: nếu phần tử mong đợi không xuất hiện trong 10 giây thì `WebDriverWait` ném `TimeoutException` và test cũng FAILED (hay gọi là lỗi chứ không phải assert sai).

### Lỗi gặp khi làm và cách sửa
(Phần này bạn tự điền theo lỗi thật mình gặp khi chạy, ví dụ: lỗi kết nối Appium server, không tìm thấy phần tử, sai nội dung thông báo lỗi... và cách mình đã sửa.)

### Dùng AI
- Đã hỏi AI điều gì: Nhờ AI điền nội dung file `testcases.md` dựa trên 3 hàm test trong `test_login.py`, sau đó nhờ AI viết ghi chú tuần này.
- Câu trả lời có đúng không: (Bạn tự điền sau khi kiểm tra. Gợi ý: AI ghi thông báo lỗi sai mật khẩu theo nội dung gốc của Swag Labs, cần chạy thử trên máy để xác nhận đúng chữ.)
- Mình hiểu thêm được gì: (Bạn tự viết bằng lời của mình.)

---