import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

XPATH_PRODUCTS = '//android.widget.TextView[@text="PRODUCTS"]'
XPATH_SAN_PHAM = '//*[@content-desc="test-Item"]'


@pytest.fixture
def driver():
    # Khai báo thiết bị và ứng dụng cho phiên làm việc
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.swaglabsmobileapp"
    options.app_activity = "com.swaglabsmobileapp.MainActivity"
    options.no_reset = False

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


def lay_san_pham(driver):
    # Chờ cho tới khi có ít nhất một sản phẩm, rồi trả về cả danh sách
    return WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((AppiumBy.XPATH, XPATH_SAN_PHAM))
    )


def lay_rong(driver):
    # Chiều rộng của sản phẩm đầu tiên (size trả về dict có width và height)
    return lay_san_pham(driver)[0].size["width"]


def cho_on_dinh(driver, so_lan=3, nghi=0.5, toi_da=10):
    # Chờ tới khi chiều rộng giữ nguyên qua `so_lan` lần đọc liên tiếp,
    # tức là giao diện đã vẽ xong, rồi trả về giá trị ổn định đó.
    het_gio = time.time() + toi_da
    gan_nhat, dem = None, 0
    while time.time() < het_gio:
        try:
            rong = lay_rong(driver)
        except (StaleElementReferenceException, TimeoutException):
            gan_nhat, dem = None, 0
            time.sleep(nghi)
            continue
        if rong == gan_nhat:
            dem += 1
            if dem >= so_lan - 1:
                return rong
        else:
            gan_nhat, dem = rong, 0
        time.sleep(nghi)
    raise TimeoutException("Chiều rộng sản phẩm không ổn định sau %s giây" % toi_da)


def bam_toggle(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Toggle").click()


def cho_rong_khac(driver, rong_cu):
    # Sau khi bấm Toggle, giao diện đổi chậm nên chờ tới khi chiều rộng khác đi
    WebDriverWait(driver, 10, ignored_exceptions=(StaleElementReferenceException,)).until(
        lambda d: lay_rong(d) != rong_cu
    )


def bam_toggle_va_cho(driver, rong_cu):
    # Bấm Toggle, chờ chiều rộng đổi, rồi chờ nó đứng yên hẳn và trả về giá trị cuối
    bam_toggle(driver)
    cho_rong_khac(driver, rong_cu)
    return cho_on_dinh(driver)


def test_toggle_doi_bo_cuc(driver):
    dang_nhap(driver)
    rong_truoc = cho_on_dinh(driver)
    print("so san pham:", len(driver.find_elements(AppiumBy.XPATH, XPATH_SAN_PHAM)))

    rong_sau = bam_toggle_va_cho(driver, rong_truoc)
    print("truoc:", rong_truoc, "| sau:", rong_sau)
    # Đổi chế độ lưới / danh sách thì chiều rộng mỗi sản phẩm phải khác đi
    assert rong_sau != rong_truoc


def test_toggle_hai_lan_tro_ve(driver):
    dang_nhap(driver)
    rong_goc = cho_on_dinh(driver)          # lấy mốc SAU KHI giao diện đã ổn định

    rong_luoi = bam_toggle_va_cho(driver, rong_goc)
    assert rong_luoi != rong_goc

    rong_ve = bam_toggle_va_cho(driver, rong_luoi)
    print("goc:", rong_goc, "| luoi:", rong_luoi, "| ve:", rong_ve)
    # Bấm Toggle hai lần thì phải về đúng bố cục ban đầu
    assert rong_ve == rong_goc
