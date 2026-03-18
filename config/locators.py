from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL         = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD      = (By.CSS_SELECTOR, "input[type='password']")
    SUBMIT        = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_ALERT   = (By.CSS_SELECTOR, "div.alert")


class NavLocators:
    ALL_NAV_LINKS = (By.CSS_SELECTOR, "a.nav-link")
    LOGOUT        = (By.CSS_SELECTOR, "a[href='/logout'], a.nav-link[href*='logout'], button[class*='logout']")
    USER_INFO     = (By.CSS_SELECTOR, ".navbar .navbar-text, .navbar span.nav-link")


class DashboardLocators:
    HEADING       = (By.CSS_SELECTOR, "h2.fw-bold")
    MAIN_CARD     = (By.CSS_SELECTOR, ".card, .container")


class UsersLocators:
    ACCESS_DENIED = (By.CSS_SELECTOR, "div.alert.alert-warning")
    TABLE         = (By.CSS_SELECTOR, "table.table")
    TABLE_ROWS    = (By.CSS_SELECTOR, "table.table tbody tr")


class ProjectsLocators:
    NEW_BTN       = (By.CSS_SELECTOR, "button.btn.btn-primary")
    MODAL         = (By.CSS_SELECTOR, ".modal.show")
    NAME_INPUT    = (By.CSS_SELECTOR, ".modal.show input.form-control")
    DESC_INPUT    = (By.CSS_SELECTOR, ".modal.show textarea.form-control")
    MODAL_SUBMIT  = (By.CSS_SELECTOR, ".modal.show button[type='submit']")
    PROJECT_ITEMS = (By.CSS_SELECTOR, "table.table tbody tr")
    PROJECT_NAME  = (By.CSS_SELECTOR, "td:nth-child(2) .fw-semibold")
    SEARCH_INPUT  = (By.CSS_SELECTOR, "input[type='search']")


class TasksLocators:
    NEW_BTN       = (By.CSS_SELECTOR, "button.btn.btn-primary")
    MODAL         = (By.CSS_SELECTOR, ".modal.show")
    TITLE_INPUT   = (By.CSS_SELECTOR, ".modal.show input.form-control")
    PROJECT_SELECT= (By.CSS_SELECTOR, ".modal.show select.form-select")
    MODAL_SUBMIT  = (By.CSS_SELECTOR, ".modal.show button[type='submit']")
    TABLE_ROWS    = (By.CSS_SELECTOR, "table.table tbody tr")
    STATUS_BADGE  = (By.CSS_SELECTOR, "td:nth-child(4) .badge")
    EDIT_BTN      = (By.CSS_SELECTOR, "button.btn-outline-primary.btn-sm")
    STATUS_SELECT = (By.CSS_SELECTOR, ".modal.show select.form-select")


class TestScenariosLocators:
    ALERT_BTN      = (By.ID, "btn-simple-alert")
    CONFIRM_BTN    = (By.ID, "btn-confirm")
    PROMPT_BTN     = (By.ID, "btn-prompt")
    CONFIRM_RESULT = (By.ID, "confirm-result")
    PROMPT_RESULT  = (By.ID, "prompt-result")
    IFRAME         = (By.CSS_SELECTOR, "iframe")
    IFRAME_BODY_TEXT = (By.CSS_SELECTOR, "body, p, h1, h2, div")
    NEW_TAB_BTN    = (By.CSS_SELECTOR, "button[id*='tab'], a[target='_blank']")
    POPUP_BTN      = (By.CSS_SELECTOR, "button[id*='popup'], button[id*='window']")
