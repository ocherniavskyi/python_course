from selene.api import s, ss, by
from selene.conditions import visible
from selene.support.conditions import be


class IssueListPage:
    @property
    def issue_list(self):
        return s('.issue-list')

    @property
    def found_issues(self):
        s('.simple-issue-list').should_be(visible)
        #return ss('ol.issue-list li')
        return ss('ol.issue-list li .issue-link-key')

    @property
    def save_as_button(self):
        return s('.save-as-new-filter')

    @property
    def no_issues_found(self):
        return s('.no-results')

    def get_found_issues(self):
        #issues = [x.get_attribute('data-key') for x in self.found_issues()]
        issues = [x.text for x in self.found_issues()]
        return issues

    def at_page(self):
        return self.save_as_button().is_displayed()

    def is_empty_list(self):
        return self.no_issues_found.is_displayed()
