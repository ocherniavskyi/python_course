from selene.api import s
from selene import browser


class IssueDetailsPage:

    @property
    def summary_selector(self):
        return s('#summary-val')

    @property
    def summary(self):
        return s('#summary')

    @property
    def priority_selector(self):
        return s('#priority-val')

    @property
    def priority(self):
        return s('#priority-field')

    @property
    def assignee_selector(self):
        return s('#assignee-val')

    @property
    def assignee(self):
        return s('#assignee-field')

    @property
    def edit_button(self):
        return s('#edit-issue')

    @property
    def submit_button(self):
        return s('.submit')

    def open_issue_details(self, issue_id):
        browser.open_url(f'/browse/{issue_id}')
        return self

    def update_priority(self, priority):
        self.priority_selector.click()
        self.priority.set(priority).press_enter().press_enter()
        #self.submit_button.click()

    def update_summary(self, summary):
        self.summary_selector.click()
        self.summary.click().set(summary)#.press_enter()
        self.submit_button.click()

    def update_assignee(self, assignee_name):
        self.assignee_selector.click()
        self.assignee.click().set(assignee_name)
        self.submit_button.click()