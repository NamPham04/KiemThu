# Kiểm thử tự động Swag Labs (Android) – Nhóm App

## Cài đặt
1. Cài Python 3, Node.js, JDK 17, Android Studio.
2. Tạo môi trường ảo và cài thư viện:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   pip install pytest Appium-Python-Client
   ```
3. Cài Appium và driver:
   ```
   npm install -g appium
   appium driver install uiautomator2
   ```
4. Tạo máy ảo Android trong Android Studio (Device Manager), hoặc cắm điện thoại Android thật có bật USB debugging.
5. Cài file `.apk` Swag Labs vào máy: `adb install ten-file.apk`.

## Chạy
1. Kiểm tra máy đã nhận: `adb devices`.
2. Mở một cửa sổ lệnh, chạy Appium server: `appium`.
3. Mở cửa sổ lệnh khác, chạy bài test:
   ```
   pytest tuan-04/test_smoke.py -v
   pytest tuan-05/test_login.py -v
   ```
   Nếu có nhiều máy, đặt trước biến `ANDROID_UDID` bằng tên máy lấy từ `adb devices`.
