# Kiểm thử tự động – Nhóm App

Bài kiểm thử đầu tiên (smoke test) cho ứng dụng Swag Labs trên Android, dùng Python + pytest + Appium.

## Yêu cầu cài đặt
- Node.js
- Appium 2.x: `npm install -g appium`
- Driver UiAutomator2: `appium driver install uiautomator2`
- JDK 17 và Android Studio (đặt biến môi trường `JAVA_HOME`, `ANDROID_HOME`)
- Python 3 và thư viện: `pip install pytest Appium-Python-Client`
- Một máy ảo Android (tạo trong Android Studio → Device Manager) hoặc điện thoại Android thật bật USB debugging
- File `.apk` của Swag Labs (tải ở trang Releases của Swag Labs Sample App), cài vào máy ảo bằng cách kéo thả hoặc `adb install ten_file.apk`

## Cách chạy
1. Bật máy ảo, kiểm tra thiết bị đã nhận: `adb devices`
2. Mở một cửa sổ terminal, chạy Appium server: `appium`
3. Mở cửa sổ terminal khác, chạy bài test: `pytest tuan-04/test_smoke.py`

Thấy `1 passed` là bài test chạy thành công.

## Cấu trúc
- `tuan-04/test_smoke.py`: bài kiểm thử đầu tiên
- `tuan-04/anh/`: ảnh chụp màn hình chạy thành công của từng thành viên
- `tuan-04/notes.md`: ghi chú tuần của từng thành viên
