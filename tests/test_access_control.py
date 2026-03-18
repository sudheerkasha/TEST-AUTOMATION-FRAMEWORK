import allure

from pages.users_page import UsersPage


@allure.suite("Access Control")
@allure.title("TC03 - Admin can access Users page")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc03_admin_users_page_access(admin_driver):
    users = UsersPage(admin_driver)

    with allure.step("Navigate to /users"):
        users.open_users()

    with allure.step("Assert users table visible"):
        assert users.is_table_visible(), \
            f"Users table not found at {admin_driver.current_url}"

    with allure.step("Assert at least 1 row"):
        assert users.get_row_count() >= 1, "Users table is empty"


@allure.suite("Access Control")
@allure.title("TC04 - Non-admin cannot access Users page")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc04_non_admin_access_restriction(user_driver):
    users = UsersPage(user_driver)

    with allure.step("Navigate to /users as normal user"):
        users.open_users()

    with allure.step("Assert access is restricted"):
        url        = user_driver.current_url
        redirected = "/login" in url
        denied     = users.is_access_denied_shown()
        assert redirected or denied, \
            f"Expected restriction but URL is: {url}"

    with allure.step("Assert users table NOT visible"):
        assert not users.is_table_visible(), \
            "Users table should not be visible to non-admin"
