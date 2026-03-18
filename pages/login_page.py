from pages.base_page import BasePage
from config.locators import LoginLocators as L


class LoginPage(BasePage):
    PATH = "/login"

    def open_login(self):
        self.open(self.PATH)
        return self

    def login(self, email, password):
        self.logger.info(f"Logging in as '{email}'")
        self.type_text(L.EMAIL, email)
        self.type_text(L.PASSWORD, password)
        self.click(L.SUBMIT)
        return self

    def get_error_text(self):
        if self.is_displayed(L.ERROR_ALERT, timeout=5):
            return self.get_text(L.ERROR_ALERT)
        return ""

    def is_on_login_page(self):
        return "/login" in self.current_url or self.is_displayed(L.SUBMIT, timeout=3)

    def is_login_failed(self):
        return self.is_displayed(L.ERROR_ALERT, timeout=5) or self.is_on_login_page()
