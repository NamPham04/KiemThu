import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    # Mở ứng dụng Swag Labs trên máy Android
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = False  # mỗi bài test bắt đầu từ trạng thái sạch (chưa đăng nhập)

    udid = os.environ.get("ANDROID_UDID")
    if udid:
        options.udid = udid

    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv
    drv.quit()


def tim(driver, accessibility_id):
    # Hàm phụ: chờ tối đa 10 giây rồi trả về phần tử theo accessibility id
    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
    )


def dang_nhap(driver, ten, mat_khau):
    # Hàm phụ: nhập tên, mật khẩu rồi bấm nút LOGIN
    tim(driver, "test-Username").send_keys(ten)
    tim(driver, "test-Password").send_keys(mat_khau)
    tim(driver, "test-LOGIN").click()


def test_dang_nhap_thanh_cong(driver):
    # TC1: tài khoản đúng thì vào được màn hình PRODUCTS
    dang_nhap(driver, "standard_user", "secret_sauce")
    tieu_de = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("PRODUCTS")')
        )
    )
    assert tieu_de.is_displayed()


def test_sai_mat_khau(driver):
    # TC2: sai mật khẩu thì hiện thông báo lỗi
    dang_nhap(driver, "standard_user", "sai_mat_khau")
    loi = tim(driver, "test-Error message")
    assert "do not match" in loi.text


def test_bo_trong_ten_dang_nhap(driver):
    # TC3: để trống tên đăng nhập thì báo "Username is required"
    tim(driver, "test-Password").send_keys("secret_sauce")
    tim(driver, "test-LOGIN").click()
    loi = tim(driver, "test-Error message")
    assert "Username is required" in loi.text
