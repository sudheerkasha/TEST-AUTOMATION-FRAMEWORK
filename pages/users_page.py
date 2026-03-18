import time
from pages.base_page import BasePage
from config.locators import UsersLocators as U


class UsersPage(BasePage):
    PATH = "/users"

    def open_users(self):
        self.open(self.PATH)
        time.sleep(2)
        return self

    def is_table_visible(self) -> bool:
        return self.is_displayed(U.TABLE, timeout=8)

    def get_row_count(self) -> int:
        return len(self.find_all(U.TABLE_ROWS))

    def is_access_denied_shown(self) -> bool:
        return self.is_displayed(U.ACCESS_DENIED, timeout=8)

    def get_access_denied_text(self) -> str:
        if self.is_access_denied_shown():
            return self.get_text(U.ACCESS_DENIED)
        return ""
