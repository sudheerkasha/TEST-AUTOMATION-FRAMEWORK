from config.settings import BASE_URL
from utils.wait_utils import WaitHelper
from utils.logger import get_logger
from utils.screenshot_utils import take_screenshot


class BasePage:

    def __init__(self, driver):
        self.driver   = driver
        self.wait     = WaitHelper(driver)
        self.logger   = get_logger(self.__class__.__name__)
        self.base_url = BASE_URL

    def open(self, path=""):
        url = f"{self.base_url}{path}"
        self.logger.info(f"GET {url}")
        self.driver.get(url)

    @property
    def current_url(self):
        return self.driver.current_url

    def click(self, locator):
        el = self.wait.until_clickable(locator)
        self.logger.debug(f"click  {locator[1]}")
        el.click()

    def type_text(self, locator, text, clear=True):
        el = self.wait.until_visible(locator)
        if clear:
            el.clear()
        self.logger.debug(f"type   {locator[1]} → '{text}'")
        el.send_keys(text)

    def get_text(self, locator):
        return self.wait.until_visible(locator).text.strip()

    def is_displayed(self, locator, timeout=5):
        return self.wait.is_visible(locator, timeout)

    def find(self, locator):
        return self.wait.until_present(locator)

    def find_all(self, locator):
        try:
            return self.wait.until_all_present(locator)
        except Exception:
            return []

    def refresh(self):
        self.driver.refresh()

    def screenshot(self, name="page"):
        take_screenshot(self.driver, name)
