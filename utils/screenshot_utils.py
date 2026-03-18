import allure
from datetime import datetime
from config.settings import SCREENSHOTS_DIR
from utils.logger import get_logger

logger = get_logger(__name__)


def take_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filepath  = SCREENSHOTS_DIR / f"{name}_{timestamp}.png"
    try:
        driver.save_screenshot(str(filepath))
        logger.info(f"Screenshot → {filepath.name}")
        with open(filepath, "rb") as f:
            allure.attach(f.read(), name=name, attachment_type=allure.attachment_type.PNG)
    except Exception as exc:
        logger.warning(f"Screenshot failed: {exc}")
    return filepath


def attach_page_source(driver, name="page_source"):
    try:
        allure.attach(driver.page_source, name=name, attachment_type=allure.attachment_type.HTML)
    except Exception as exc:
        logger.warning(f"Page source attach failed: {exc}")
