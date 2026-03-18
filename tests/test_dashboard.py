import allure

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage


@allure.suite("Dashboard")
@allure.title("Dashboard loads after admin login")
@allure.severity(allure.severity_level.CRITICAL)
def test_dashboard_loads_after_login(admin_driver):
    dash = DashboardPage(admin_driver)

    with allure.step("Assert heading visible and not on login page"):
        assert dash.is_loaded(), \
            f"Dashboard not loaded. URL: {admin_driver.current_url}"

    with allure.step("Attach heading text"):
        allure.attach(dash.get_heading(), name="heading", attachment_type=allure.attachment_type.TEXT)


@allure.suite("Dashboard")
@allure.title("Sidebar nav links present")
@allure.severity(allure.severity_level.NORMAL)
def test_dashboard_nav_links_present(admin_driver):
    dash = DashboardPage(admin_driver)

    with allure.step("Collect nav links"):
        links = dash.nav_links()
        allure.attach("\n".join(links), name="nav links", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Assert at least 2 links"):
        assert len(links) >= 2, f"Expected nav links, got: {links}"


@allure.suite("Dashboard")
@allure.title("Logout redirects to login")
@allure.severity(allure.severity_level.CRITICAL)
def test_dashboard_logout(admin_driver):
    dash  = DashboardPage(admin_driver)
    login = LoginPage(admin_driver)

    with allure.step("Confirm dashboard loaded"):
        assert dash.is_loaded(), "Dashboard not loaded before logout"

    with allure.step("Click logout"):
        dash.logout()

    with allure.step("Assert on login page"):
        # App may go to /logout then redirect, so check both
        import time
        for _ in range(5):
            if login.is_on_login_page():
                break
            time.sleep(1)
        assert login.is_on_login_page(), \
            f"Expected /login after logout but got: {admin_driver.current_url}"
