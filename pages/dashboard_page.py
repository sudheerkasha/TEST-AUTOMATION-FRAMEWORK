from pages.base_page import BasePage
from config.locators import DashboardLocators as D, NavLocators as N


class DashboardPage(BasePage):

    def is_loaded(self) -> bool:
        return (
            "/login" not in self.current_url
            and self.is_displayed(D.HEADING, timeout=10)
        )

    def get_heading(self) -> str:
        if self.is_displayed(D.HEADING, timeout=5):
            return self.get_text(D.HEADING)
        return ""

    def logout(self) -> None:
        self.logger.info("Logging out")
        if self.is_displayed(N.LOGOUT, timeout=4):
            self.click(N.LOGOUT)
        else:
            # Fallback: navigate directly which will trigger app logout
            self.open("/login")

    def nav_links(self) -> list:
        links = self.find_all(N.ALL_NAV_LINKS)
        return [l.text.strip() for l in links if l.text.strip()]
