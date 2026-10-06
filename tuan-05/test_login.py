import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    # Xóa dữ liệu app mỗi lần chạy để luôn bắt đầu từ màn hình đăng nhập
    options.no_reset = False

    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv
    drv.quit()


def cho_phan_tu(driver, by, value):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((by, value))
    )


def dang_nhap(driver, ten, mat_khau):
    # Nhập tên đăng nhập và mật khẩu rồi bấm LOGIN
    cho_phan_tu(driver, AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys(ten)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys(mat_khau)
    try:
        driver.hide_keyboard()
    except Exception:
        pass  # bàn phím không hiện thì bỏ qua
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()


def test_dang_nhap_thanh_cong(driver):
    dang_nhap(driver, "standard_user", "secret_sauce")
    tieu_de = cho_phan_tu(
        driver, AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]'
    )
    assert tieu_de.is_displayed()


def test_sai_mat_khau(driver):
    dang_nhap(driver, "standard_user", "sai_mat_khau")
    loi = cho_phan_tu(
        driver, AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "do not match")]'
    )
    assert loi.is_displayed()


def test_bo_trong_ten_dang_nhap(driver):
    dang_nhap(driver, "", "secret_sauce")
    loi = cho_phan_tu(
        driver, AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Username is required")]'
    )
    assert loi.is_displayed()
