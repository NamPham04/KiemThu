import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


@pytest.fixture
def driver():
    # Khai báo thiết bị và ứng dụng cần mở
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = True

    # Kết nối tới Appium server đang chạy trên máy
    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv
    drv.quit()


def test_smoke(driver):
    # Tìm ô nhập tên đăng nhập trên màn hình đăng nhập
    o_username = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Username")

    # Kiểm tra ô đó có hiển thị
    assert o_username.is_displayed()
