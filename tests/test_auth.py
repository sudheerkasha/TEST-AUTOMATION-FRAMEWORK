import pytest
import allure

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.data_loader import invalid_login_matrix
from config.settings import ADMIN_EMAIL, ADMIN_PASSWORD
from config.locators import LoginLocators


@allure.suite("Authentication")
@allure.title("TC01 - Valid admin login")
@allure.severity(allure.severity_level.BLOCKER)
def test_tc01_valid_admin_login(driver):
    login = LoginPage(driver)
    dash  = DashboardPage(driver)

    with allure.step("Open login page"):
        login.open_login()
        assert login.is_on_login_page()

    with allure.step(f"Login as {ADMIN_EMAIL}"):
        login.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    with allure.step("Wait for redirect away from login"):
        import time
        for _ in range(10):
            if "/login" not in driver.current_url:
                break
            time.sleep(1)

    with allure.step("Assert dashboard loaded"):
        assert dash.is_loaded(), \
            f"Dashboard did not load. URL: {driver.current_url}"

    with allure.step("Assert no error alert"):
        assert not login.is_displayed(LoginLocators.ERROR_ALERT, timeout=2)


@allure.suite("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
    "test_id, email, password, description",
    invalid_login_matrix(),
    ids=[row[0] for row in invalid_login_matrix()]
)
def test_tc02_invalid_login_matrix(driver, test_id, email, password, description):
    allure.dynamic.title(f"TC02 - Invalid login: {description}")

    login = LoginPage(driver)

    with allure.step("Open login page"):
        login.open_login()

    with allure.step(f"Submit email='{email}' password='{password}'"):
        login.login(email, password)

    with allure.step("Assert still on login or error shown"):
        assert login.is_on_login_page() or login.get_error_text() != "", \
            f"Expected login failure for [{description}] but URL: {driver.current_url}"
