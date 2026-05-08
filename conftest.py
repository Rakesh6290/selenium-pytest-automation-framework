import pytest
import os
import allure
from utils.driver_factory import get_driver
from utils.config import BASE_URL

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage



def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption(
        "--browser"
    )

    driver = get_driver(browser)

    driver.get(BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def login_page(driver):

    return LoginPage(driver)


@pytest.fixture
def product_page(driver):

    return ProductPage(driver)


@pytest.fixture
def checkout_page(driver):

    return CheckoutPage(driver)


@pytest.fixture
def cart_page(driver):

    return CartPage(driver)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["driver"]

        screenshots_dir = "screenshots"

        os.makedirs(
            screenshots_dir,
            exist_ok=True
        )

        screenshot_name = f"{item.name}.png"

        screenshot_path = os.path.join(
            screenshots_dir,
            screenshot_name
        )

        driver.save_screenshot(
            screenshot_path
        )

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        print(
            f"\nScreenshot saved: {screenshot_path}"
        )