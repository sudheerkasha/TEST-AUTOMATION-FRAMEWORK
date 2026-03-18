from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import DEFAULT_WAIT


class WaitHelper:

    def __init__(self, driver, timeout=DEFAULT_WAIT):
        self.driver  = driver
        self.timeout = timeout

    def _wait(self, timeout=None):
        return WebDriverWait(self.driver, timeout or self.timeout)

    def until_visible(self, locator, timeout=None):
        return self._wait(timeout).until(EC.visibility_of_element_located(locator))

    def until_present(self, locator, timeout=None):
        return self._wait(timeout).until(EC.presence_of_element_located(locator))

    def until_all_present(self, locator, timeout=None):
        return self._wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def until_clickable(self, locator, timeout=None):
        return self._wait(timeout).until(EC.element_to_be_clickable(locator))

    def until_url_contains(self, partial, timeout=None):
        return self._wait(timeout).until(EC.url_contains(partial))

    def until_alert(self, timeout=None):
        return self._wait(timeout).until(EC.alert_is_present())

    def until_new_window(self, current_count, timeout=None):
        return self._wait(timeout).until(EC.number_of_windows_to_be(current_count + 1))

    def until_frame_and_switch(self, locator, timeout=None):
        return self._wait(timeout).until(EC.frame_to_be_available_and_switch_to_it(locator))

    def until_text_in(self, locator, text, timeout=None):
        return self._wait(timeout).until(EC.text_to_be_present_in_element(locator, text))

    def is_visible(self, locator, timeout=3):
        try:
            self.until_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def is_present(self, locator, timeout=3):
        try:
            self.until_present(locator, timeout)
            return True
        except TimeoutException:
            return False
