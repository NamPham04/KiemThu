import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    # Khai báo máy Android và ứng dụng Swag Labs cần mở
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = True

    # Tên máy lấy bằng lệnh `adb devices`; đặt biến môi trường ANDROID_UDID nếu có nhiều máy
    udid = os.environ.get("ANDROID_UDID")
    if udid:
        options.udid = udid

    # Kết nối tới Appium server đang chạy trên máy (mặc định cổng 4723)
    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv  # đưa driver cho bài test dùng
    drv.quit()  # đóng phiên sau khi test xong


def test_smoke(driver):
    # Chờ tối đa 10 giây cho tới khi ô nhập tên đăng nhập xuất hiện
    o_username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))
    )

    # Kiểm tra ô đó đang hiển thị trên màn hình
    assert o_username.is_displayed()
