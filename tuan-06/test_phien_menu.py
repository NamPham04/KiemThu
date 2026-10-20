import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

XPATH_PRODUCTS = '//android.widget.TextView[@text="PRODUCTS"]'


@pytest.fixture
def driver():
    # Capabilities: khai báo thiết bị và ứng dụng cho phiên làm việc
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = False

    # webdriver.Remote gửi yêu cầu tới Appium server để mở một phiên mới
    drv = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield drv
    drv.quit()


def cho(driver, by, value):
    # Chờ tối đa 10 giây cho tới khi phần tử xuất hiện
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((by, value)))


def dang_nhap(driver):
    cho(driver, AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    try:
        driver.hide_keyboard()
    except Exception:
        pass
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()
    cho(driver, AppiumBy.XPATH, XPATH_PRODUCTS)


def test_phien_appium(driver):
    # Mỗi phiên có một session_id riêng do Appium server cấp
    print("session_id:", driver.session_id)
    print("platformName:", driver.capabilities.get("platformName"))
    print("deviceName:", driver.capabilities.get("deviceName"))
    assert driver.session_id
    assert driver.capabilities.get("platformName", "").lower() == "android"


def test_menu_va_back(driver):
    dang_nhap(driver)
    # Mở menu bằng nút menu trên màn hình PRODUCTS
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Menu").click()
    # Chờ menu hiện ra (mục ALL ITEMS)
    muc_menu = cho(driver, AppiumBy.ACCESSIBILITY_ID, "test-ALL ITEMS")
    assert muc_menu.is_displayed()
    # Bấm ALL ITEMS để quay về danh sách PRODUCTS
    muc_menu.click()
    san_pham = cho(driver, AppiumBy.XPATH, XPATH_PRODUCTS)
    assert san_pham.is_displayed()


def test_nut_back(driver):
    dang_nhap(driver)
    # Mở menu rồi bấm Back của Android
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Menu").click()
    cho(driver, AppiumBy.ACCESSIBILITY_ID, "test-ALL ITEMS")
    driver.back()
    # Sau khi Back, menu đóng và vẫn ở màn hình PRODUCTS
    san_pham = cho(driver, AppiumBy.ACCESSIBILITY_ID, "test-PRODUCTS")
    assert san_pham.is_displayed()  