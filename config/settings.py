import os

BASE_URL        = os.getenv("BASE_URL",        "https://react-frontend-api-testing.vercel.app")
BROWSER         = os.getenv("BROWSER",         "chrome").lower()
HEADLESS        = os.getenv("HEADLESS",        "false").lower() in ("1", "true", "yes")
EXECUTION_MODE  = os.getenv("EXECUTION_MODE",  "remote")
GRID_URL        = os.getenv("GRID_URL",        "http://127.0.0.1:4444/wd/hub")

DEFAULT_WAIT    = int(os.getenv("DEFAULT_WAIT",   "10"))
PAGE_LOAD_WAIT  = int(os.getenv("PAGE_LOAD_WAIT", "30"))

ADMIN_EMAIL     = os.getenv("ADMIN_EMAIL",    "admin@example.com")
ADMIN_PASSWORD  = os.getenv("ADMIN_PASSWORD", "Admin@123")
USER_EMAIL      = os.getenv("USER_EMAIL",     "user@example.com")
USER_PASSWORD   = os.getenv("USER_PASSWORD",  "User@123")

import pathlib
ROOT_DIR        = pathlib.Path(__file__).resolve().parent.parent
REPORTS_DIR     = ROOT_DIR / "reports"
SCREENSHOTS_DIR = REPORTS_DIR / "screenshots"
LOGS_DIR        = ROOT_DIR / "logs"
ALLURE_DIR      = REPORTS_DIR / "allure-results"

for _d in (SCREENSHOTS_DIR, LOGS_DIR, ALLURE_DIR):
    _d.mkdir(parents=True, exist_ok=True)
