# Test case Đăng nhập – Swag Labs (Nhóm App)


## TC1: Đăng nhập thành công
- Các bước:
  1. Mở ứng dụng Swag Labs, màn hình Đăng nhập hiển thị
  2. Nhập tên đăng nhập vào ô Username
  3. Nhập mật khẩu vào ô Password
  4. Bấm nút LOGIN
- Dữ liệu nhập: tên đăng nhập = standard_user, mật khẩu = secret_sauce
- Kết quả mong đợi: Đăng nhập thành công, chuyển sang màn hình danh sách sản phẩm và hiển thị tiêu đề "PRODUCTS"

## TC2: Đăng nhập thất bại – Sai mật khẩu
- Các bước:
  1. Mở ứng dụng Swag Labs, màn hình Đăng nhập hiển thị
  2. Nhập tên đăng nhập hợp lệ vào ô Username
  3. Nhập mật khẩu sai vào ô Password
  4. Bấm nút LOGIN
- Dữ liệu nhập: tên đăng nhập = standard_user, mật khẩu = sai_mat_khau
- Kết quả mong đợi: Không đăng nhập được, vẫn ở màn hình Đăng nhập và hiển thị thông báo lỗi chứa nội dung "Username and password do not match any user in this service"

## TC3: Đăng nhập thất bại – Bỏ trống tên đăng nhập
- Các bước:
  1. Mở ứng dụng Swag Labs, màn hình Đăng nhập hiển thị
  2. Để trống ô Username
  3. Nhập mật khẩu hợp lệ vào ô Password
  4. Bấm nút LOGIN
- Dữ liệu nhập: tên đăng nhập = (để trống), mật khẩu = secret_sauce
- Kết quả mong đợi: Không đăng nhập được, vẫn ở màn hình Đăng nhập và hiển thị thông báo lỗi "Username is required"