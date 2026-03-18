import pytest
import allure
import time

from utils.driver_factory import DriverFactory
from utils.screenshot_utils import take_screenshot, attach_page_source
from utils.logger import get_logger
from config.settings import ADMIN_EMAIL, ADMIN_PASSWORD, USER_EMAIL, USER_PASSWORD

logger = get_logger("conftest")


@pytest.fixture(scope="function")
def driver(request):
    drv = DriverFactory.get_driver()
    logger.info("Driver created")
    yield drv
    drv.quit()
    logger.info("Driver quit")


@pytest.fixture(scope="function")
def admin_driver(driver):
    from pages.login_page import LoginPage
    lp = LoginPage(driver)
    lp.open_login()
    lp.login(ADMIN_EMAIL, ADMIN_PASSWORD)
    # Wait for redirect away from /login
    for _ in range(10):
        if "/login" not in driver.current_url:
            break
        time.sleep(1)
    logger.info(f"Admin session ready: {ADMIN_EMAIL} | URL: {driver.current_url}")
    return driver


@pytest.fixture(scope="function")
def user_driver(driver):
    from pages.login_page import LoginPage
    lp = LoginPage(driver)
    lp.open_login()
    lp.login(USER_EMAIL, USER_PASSWORD)
    time.sleep(2)
    logger.info(f"User login attempted: {USER_EMAIL} | URL: {driver.current_url}")
    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report  = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = (item.funcargs.get("driver")
               or item.funcargs.get("admin_driver")
               or item.funcargs.get("user_driver"))
        if drv:
            name = item.name.replace("[", "_").replace("]", "").replace(" ", "_")
            take_screenshot(drv, f"FAIL_{name}")
            attach_page_source(drv, f"source_{name}")
            logger.error(f"FAILED: {item.name}")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
