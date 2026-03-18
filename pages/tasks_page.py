import time
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from config.locators import TasksLocators as T


class TasksPage(BasePage):
    PATH = "/tasks"

    def open_tasks(self):
        self.open(self.PATH)
        return self

    def get_row_count(self) -> int:
        # Tasks table takes time to load
        try:
            self.wait.until_present(T.TABLE_ROWS, timeout=10)
        except Exception:
            pass
        return len(self.find_all(T.TABLE_ROWS))

    def update_first_task_status(self, new_status: str):
        rows = self.find_all(T.TABLE_ROWS)
        if not rows:
            return self

        # Click Edit button on first row
        try:
            edit_btn = rows[0].find_element(*T.EDIT_BTN)
            edit_btn.click()
            time.sleep(1)
            self.logger.info("Clicked Edit on first task")
        except Exception as e:
            self.logger.warning(f"No edit button: {e}")
            return self

        # Change status in modal
        try:
            selects = self.driver.find_elements(*T.STATUS_SELECT)
            # Find the status select (3rd select in modal — after Project and before Priority)
            status_sel = None
            for s in selects:
                opts = [o.get_attribute("value") for o in Select(s).options]
                if "todo" in opts or "in_progress" in opts:
                    status_sel = s
                    break
            if status_sel:
                sel = Select(status_sel)
                options = [o.get_attribute("value") for o in sel.options if o.get_attribute("value")]
                self.logger.info(f"Status options: {options}")
                if new_status in options:
                    sel.select_by_value(new_status)
                else:
                    sel.select_by_index(1)
                    new_status = sel.first_selected_option.get_attribute("value")
                self.logger.info(f"Status set to: '{new_status}'")
        except Exception as e:
            self.logger.error(f"Status update failed: {e}")

        # Save
        try:
            saves = self.driver.find_elements(*T.MODAL_SUBMIT)
            if saves:
                saves[0].click()
                time.sleep(1)
        except Exception:
            pass
        return self

    def get_first_task_status(self) -> str:
        rows = self.find_all(T.TABLE_ROWS)
        if not rows:
            return ""
        try:
            return rows[0].find_element(*T.STATUS_BADGE).text.strip()
        except Exception:
            return ""

    def refresh_and_get_first_status(self) -> str:
        self.refresh()
        time.sleep(1)
        return self.get_first_task_status()
