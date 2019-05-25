from selene.conditions import visible

from web_tests.PageObjects.IssueListPage import IssueListPage
from web_tests.common_fixtures.infrustructure import *
from conftest import *


@pytest.mark.webui
class TestIssuePage:

    def test_create_bug_with_all_mandatory_fields(self, issue_page: IssuePage, generate_summary: str):
        issue_page.create_issue(project, 'Bug', generate_summary)
        text = issue_page.issue_created_popup.text
        assert generate_summary in text

    def test_create_bug_with_empty_summary(self, issue_page: IssuePage):
        issue_page.create_issue(project, 'Bug', '')
        issue_page.page_body.should_be(visible)
        assert issue_page.fields_errors[0].text == 'You must specify a summary of the issue.'

    def test_create_bug_with_256_symbols_summary(self, issue_page: IssuePage):
        summary = 'long '*51 + '1'
        issue_page.create_issue(project, 'Bug', summary)
        issue_page.page_body.should_be(visible)
        assert issue_page.fields_errors[0].text == 'Summary must be less than 255 characters.'

    def test_search_an_issue(self, dashboard_page: DashboardPage, created_bug: dict):
        search_page = dashboard_page.search_issue(created_bug['summary'])
        found_issues = search_page.get_found_issues()
        assert len(found_issues) == 1
        assert found_issues()[0] == created_bug['key']

    def test_search_non_existence_issue(self, dashboard_page):
        search_page : IssueListPage = dashboard_page.search_issue(str(uuid.uuid4()))
        assert search_page.is_empty_list()


