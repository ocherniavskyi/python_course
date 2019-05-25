import pytest
from selene.browser import driver
import uuid

from web_tests.PageObjects.DashboardPage import DashboardPage
from web_tests.PageObjects.IssuePage import IssuePage
from web_tests.PageObjects.LoginPage import LoginPage
from conftest import *


@pytest.fixture(scope='session')
def jira_client():
    return JiraClient(jira_url, username, password)


@pytest.fixture()
def login_page():
    return LoginPage().open()


@pytest.fixture()
def dashboard_page(login_page):
    login_page.login_as(username=username, password=password)
    page = DashboardPage().open()
    return page


@pytest.fixture()
def issue_page(dashboard_page: DashboardPage):
    page = dashboard_page.open_create_issue_window()
    return page


@pytest.fixture(autouse=True)
def refresh_after_test():
    yield
    driver().close()


@pytest.fixture(autouse=True, scope='session')
def clear_issues_after_run(jira_client):
    yield
    issues_to_delete = jira_client.search.search_issues_by_comment(issue_tag)
    for issue_id in issues_to_delete:
        jira_client.issue.delete_issue(issue_id)


@pytest.fixture()
def generate_summary():
    return f'{issue_tag} {str(uuid.uuid4())}'


@pytest.fixture()
def created_bug(jira_client: JiraClient, generate_summary):
    bug = jira_client.issue.create_bug(project, generate_summary)
    bug['summary'] = generate_summary
    return bug

