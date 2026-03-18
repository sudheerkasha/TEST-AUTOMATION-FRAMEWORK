from pages.base_page import BasePage
from config.locators import TestScenariosLocators as T


class ScenariosPage(BasePage):
    PATH = "/test-scenarios"

    def open_scenarios(self):
        self.open(self.PATH)
        return self

    def trigger_alert_and_accept(self) -> str:
        self.click(T.ALERT_BTN)
        alert = self.wait.until_alert()
        text  = alert.text
        alert.accept()
        return text

    def trigger_confirm_and_accept(self) -> str:
        self.click(T.CONFIRM_BTN)
        alert = self.wait.until_alert()
        text  = alert.text
        alert.accept()
        return text

    def trigger_confirm_and_dismiss(self) -> str:
        self.click(T.CONFIRM_BTN)
        alert = self.wait.until_alert()
        text  = alert.text
        alert.dismiss()
        return text

    def trigger_prompt_and_submit(self, input_text: str) -> str:
        self.click(T.PROMPT_BTN)
        alert = self.wait.until_alert()
        text  = alert.text
        alert.send_keys(input_text)
        alert.accept()
        return text

    def get_confirm_result(self) -> str:
        return self.get_text(T.CONFIRM_RESULT)

    def get_prompt_result(self) -> str:
        return self.get_text(T.PROMPT_RESULT)

    def get_iframe_body_text(self) -> str:
        try:
            self.wait.until_frame_and_switch(T.IFRAME)
            content = self.driver.find_element(*T.IFRAME_BODY_TEXT).text.strip()
            return content
        except Exception as exc:
            self.logger.error(f"iFrame error: {exc}")
            return ""
        finally:
            self.driver.switch_to.default_content()

    def open_new_tab_and_switch(self) -> dict:
        original = self.driver.window_handles
        self.click(T.NEW_TAB_BTN)
        self.wait.until_new_window(len(original))
        new = [h for h in self.driver.window_handles if h not in original][0]
        self.driver.switch_to.window(new)
        return {"url": self.driver.current_url, "title": self.driver.title}

    def close_current_tab_and_return(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def open_popup_and_switch(self) -> dict:
        original = self.driver.window_handles
        self.click(T.POPUP_BTN)
        self.wait.until_new_window(len(original))
        popup = [h for h in self.driver.window_handles if h not in original][0]
        self.driver.switch_to.window(popup)
        return {"url": self.driver.current_url, "title": self.driver.title}

    def switch_to_main_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
