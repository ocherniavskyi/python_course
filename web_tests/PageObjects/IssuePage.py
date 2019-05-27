from selene import browser
from selene.support.conditions import be

from web_tests.PageObjects.BasePage import BasePage
from selene.api import s, ss


class IssuePage(BasePage):

    @property
    def page_body(self):
        return s('#create-issue-dialog')

    @property
    def summary_field(self):
        return s('#summary').should(be.clickable)

    @property
    def fields_errors(self):
        return ss('.error')

    @property
    def issue_created_popup(self):
        return s('#aui-flag-container')

    @property
    def create_button(self):
        return s('#create-issue-submit')

    @property
    def cancel_button(self):
        return s('.cancel')#.should(be.clickable)

    @property
    def issue_type_list(self):
        return s('#issuetype-field').should(be.clickable)

    @property
    def projects_list(self):
        return s('#project-field').should(be.clickable)

    def open(self):
        browser.open_url('/secure/CreateIssue.jspa')
        return self

    def create_issue(self, project, issue_type, summary):
        self.select_project(project)
        self.select_issue_type(issue_type)
        self.set_summary(summary)
        self.click_create()

    def select_project(self, project):
        self.projects_list.set(project).press_enter()

    def select_issue_type(self, issue_type):
        self.issue_type_list.set(issue_type).press_enter()

    def set_summary(self, summary):
        self.summary_field.set(summary)

    def click_create(self):
        self.create_button.click()

    def click_cancel(self):
        self.cancel_button.click()

