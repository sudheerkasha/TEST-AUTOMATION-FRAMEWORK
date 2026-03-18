import time
from pages.base_page import BasePage
from config.locators import ProjectsLocators as P


class ProjectsPage(BasePage):
    PATH = "/projects"

    def open_projects(self):
        self.open(self.PATH)
        return self

    def create_project(self, name: str, description: str = ""):
        self.click(P.NEW_BTN)
        # Wait for modal animation to complete
        time.sleep(1)
        self.wait.until_visible(P.NAME_INPUT)
        self.type_text(P.NAME_INPUT, name)
        if description:
            try:
                self.type_text(P.DESC_INPUT, description)
            except Exception:
                pass
        self.click(P.MODAL_SUBMIT)
        time.sleep(1)
        self.logger.info(f"Project created: '{name}'")
        return self

    def get_project_names(self) -> list:
        items = self.find_all(P.PROJECT_NAME)
        return [i.text.strip() for i in items if i.text.strip()]

    def project_exists(self, name: str) -> bool:
        self.wait.until_present(P.PROJECT_ITEMS)
        return any(name.lower() in n.lower() for n in self.get_project_names())
