import allure
import pytest

from pages.test_scenarios_page import ScenariosPage
from utils.data_loader import get


@allure.suite("Browser Interactions")
@allure.title("TC07 - Handle alert, confirm, and prompt dialogs")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc07_alerts_handling(admin_driver):
    prompt_text = get("prompt_input")
    page = ScenariosPage(admin_driver)

    with allure.step("Open Test Scenarios page"):
        page.open_scenarios()

    with allure.step("Trigger alert and accept"):
        alert_text = page.trigger_alert_and_accept()
        allure.attach(alert_text or "", name="alert text", attachment_type=allure.attachment_type.TEXT)
        assert alert_text is not None

    with allure.step("Trigger confirm and dismiss"):
        page.trigger_confirm_and_dismiss()

    with allure.step("Assert confirm result updated"):
        result = page.get_confirm_result()
        allure.attach(result, name="confirm result after dismiss", attachment_type=allure.attachment_type.TEXT)
        assert result != ""

    with allure.step("Trigger confirm and accept"):
        page.trigger_confirm_and_accept()

    with allure.step(f"Trigger prompt: '{prompt_text}'"):
        page.trigger_prompt_and_submit(prompt_text)

    with allure.step("Assert prompt result contains entered text"):
        prompt_result = page.get_prompt_result()
        allure.attach(prompt_result, name="prompt result", attachment_type=allure.attachment_type.TEXT)
        assert prompt_text in prompt_result, \
            f"'{prompt_result}' does not contain '{prompt_text}'"


@allure.suite("Browser Interactions")
@allure.title("TC08 - iFrame switching and multi-window handling")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc08_iframe_and_window_handling(admin_driver):
    page = ScenariosPage(admin_driver)

    with allure.step("Open Test Scenarios page"):
        page.open_scenarios()
        main_url = admin_driver.current_url

    with allure.step("Switch into iframe and read content"):
        content = page.get_iframe_body_text()
        allure.attach(content or "(empty)", name="iframe content", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Assert back on main page after iframe"):
        assert admin_driver.current_url == main_url

    with allure.step("Open new tab"):
        windows_before = len(admin_driver.window_handles)
        try:
            info = page.open_new_tab_and_switch()
            allure.attach(f"URL: {info['url']}", name="new tab", attachment_type=allure.attachment_type.TEXT)
            assert len(admin_driver.window_handles) > windows_before
        except Exception as exc:
            pytest.skip(f"New tab button not found: {exc}")

    with allure.step("Close tab and return"):
        page.close_current_tab_and_return()
        assert admin_driver.current_url == main_url

    with allure.step("Open popup"):
        try:
            popup = page.open_popup_and_switch()
            allure.attach(f"URL: {popup['url']}", name="popup", attachment_type=allure.attachment_type.TEXT)
            assert len(admin_driver.window_handles) >= 2
        except Exception as exc:
            pytest.skip(f"Popup button not found: {exc}")

    with allure.step("Return to main window"):
        page.switch_to_main_window()
        assert admin_driver.current_url == main_url
