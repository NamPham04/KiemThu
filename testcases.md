# Test case Đăng nhập – Swag Labs (Android)

| Mã | Tên test case | Các bước | Dữ liệu | Kết quả mong đợi |
|----|---------------|----------|---------|------------------|
| TC1 | Đăng nhập thành công | 1. Mở ứng dụng Swag Labs<br>2. Nhập tên đăng nhập<br>3. Nhập mật khẩu<br>4. Bấm LOGIN | Tên: `standard_user`<br>Mật khẩu: `secret_sauce` | Vào được màn hình PRODUCTS |
| TC2 | Đăng nhập sai mật khẩu | 1. Mở ứng dụng<br>2. Nhập tên đăng nhập<br>3. Nhập mật khẩu sai<br>4. Bấm LOGIN | Tên: `standard_user`<br>Mật khẩu: `sai_mat_khau` | Hiện thông báo lỗi "Username and password do not match any user in this service", vẫn ở màn hình đăng nhập |
| TC3 | Bỏ trống tên đăng nhập | 1. Mở ứng dụng<br>2. Để trống tên đăng nhập<br>3. Nhập mật khẩu<br>4. Bấm LOGIN | Tên: (trống)<br>Mật khẩu: `secret_sauce` | Hiện thông báo lỗi "Username is required" |
