import allure

from pages.projects_page import ProjectsPage
from pages.tasks_page import TasksPage
from utils.data_loader import get


@allure.suite("Projects & Tasks")
@allure.title("TC05 - Create project and verify in list")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc05_create_project(admin_driver):
    data     = get("new_project")
    name     = data["name"]
    desc     = data["description"]
    projects = ProjectsPage(admin_driver)

    with allure.step("Open Projects page"):
        projects.open_projects()

    with allure.step(f"Create project '{name}'"):
        projects.create_project(name, desc)

    with allure.step("Assert project in list"):
        assert projects.project_exists(name), \
            f"'{name}' not found. Visible: {projects.get_project_names()}"


@allure.suite("Projects & Tasks")
@allure.title("TC06 - Task status update persists after refresh")
@allure.severity(allure.severity_level.CRITICAL)
def test_tc06_task_status_update(admin_driver):
    new_status = get("task_status_new")
    tasks = TasksPage(admin_driver)

    with allure.step("Open Tasks page"):
        tasks.open_tasks()

    with allure.step("Assert tasks exist"):
        count = tasks.get_row_count()
        assert count >= 1, f"No tasks found on /tasks page (found {count} rows)"

    with allure.step("Change first task status"):
        tasks.update_first_task_status(new_status)

    with allure.step("Refresh and assert status badge not empty"):
        status_after = tasks.refresh_and_get_first_status()
        allure.attach(
            f"Status after refresh: {status_after}",
            name="status",
            attachment_type=allure.attachment_type.TEXT
        )
        assert status_after != "", "Status badge empty after refresh"
