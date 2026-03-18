from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config.settings import BROWSER, EXECUTION_MODE, GRID_URL, HEADLESS, PAGE_LOAD_WAIT


class DriverFactory:

    @staticmethod
    def get_driver():
        if EXECUTION_MODE == "remote":
            return DriverFactory._create_remote_driver()
        return DriverFactory._create_local_driver()

    @staticmethod
    def _create_local_driver():
        if BROWSER == "chrome":
            driver = webdriver.Chrome(options=DriverFactory._chrome_options())
        elif BROWSER == "firefox":
            driver = webdriver.Firefox(options=DriverFactory._firefox_options())
        else:
            raise Exception(f"Unsupported browser: {BROWSER}")
        driver.maximize_window()
        driver.set_page_load_timeout(PAGE_LOAD_WAIT)
        driver.implicitly_wait(0)
        return driver

    @staticmethod
    def _create_remote_driver():
        if BROWSER == "chrome":
            options = DriverFactory._chrome_options()
        elif BROWSER == "firefox":
            options = DriverFactory._firefox_options()
        else:
            raise Exception(f"Unsupported browser: {BROWSER}")
        driver = webdriver.Remote(command_executor=GRID_URL, options=options)
        driver.maximize_window()
        driver.set_page_load_timeout(PAGE_LOAD_WAIT)
        driver.implicitly_wait(0)
        return driver

    @staticmethod
    def _chrome_options():
        opts = ChromeOptions()
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--disable-extensions")
        if HEADLESS:
            opts.add_argument("--headless=new")
        return opts

    @staticmethod
    def _firefox_options():
        opts = FirefoxOptions()
        if HEADLESS:
            opts.add_argument("--headless")
        return opts
