from selene import browser
from selene.support.conditions.be import clickable

from web_tests.PageObjects.BasePage import BasePage
from web_tests.PageObjects.IssueListPage import IssueListPage
from selene.api import s

from web_tests.PageObjects.IssuePage import IssuePage


class DashboardPage(BasePage):

    def open(self):
        #browser.open_url('./secure/Dashboard.jspa')
        return self

    @property
    def create_button(self):
        return s('.create-issue').should_be(clickable)

    @property
    def quick_search_field(self):
        return s('#quickSearchInput')

    def search_issue(self, text_to_search):
        self.quick_search_field.send_keys(text_to_search).press_enter()
        return IssueListPage()

    def open_create_issue_window(self):
        self.create_button.click()
        return IssuePage()
