import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Cấu hình kết nối tới Appium server và máy ảo Android
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.udid = "emulator-5556"     # đổi thành số hiệu máy ảo của bạn
    options.no_reset = False           # reset app mỗi lần chạy

    # Kết nối tới Appium server đang chạy trên máy
    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv
    drv.quit()


def nhap_dang_nhap(driver, username, password):
    """Hàm phụ trợ: nhập username, password rồi nhấn LOGIN"""
    # Chờ ô username xuất hiện (tối đa 10 giây)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Username"))
    ).send_keys(username)

    # Nhập password
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys(password)

    # Nhấn nút LOGIN
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()


def lay_text_loi(driver):
    """Hàm phụ trợ: lấy text thông báo lỗi từ khung test-Error message"""
    # Chờ khung thông báo lỗi xuất hiện
    error_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-Error message"))
    )

    # Lấy text từ element con TextView bên trong khung
    error_text = error_container.find_element(
        AppiumBy.XPATH, ".//android.widget.TextView"
    ).text

    return error_text


# ==================== BÀI 1: ĐĂNG NHẬP THÀNH CÔNG ====================
def test_login_success(driver):
    # Nhập standard_user / secret_sauce
    nhap_dang_nhap(driver, "standard_user", "secret_sauce")

    # Chờ màn hình Products xuất hiện (tối đa 10 giây)
    products = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS"))
    )

    # Kiểm tra màn hình Products có hiển thị
    assert products.is_displayed()


# ==================== BÀI 2: TÀI KHOẢN BỊ KHÓA ====================
def test_login_locked_user(driver):
    # Nhập locked_out_user / secret_sauce
    nhap_dang_nhap(driver, "locked_out_user", "secret_sauce")

    # Lấy text thông báo lỗi
    error_text = lay_text_loi(driver)

    # Kiểm tra nội dung thông báo có chứa "locked out"
    assert "locked out" in error_text.lower()


# ==================== BÀI 3: BỎ TRỐNG MẬT KHẨU ====================
def test_login_empty_password(driver):
    # Nhập standard_user, để trống password
    nhap_dang_nhap(driver, "standard_user", "")

    # Lấy text thông báo lỗi
    error_text = lay_text_loi(driver)

    # Kiểm tra nội dung thông báo có chứa "Password is required"
    assert "Password is required" in error_text