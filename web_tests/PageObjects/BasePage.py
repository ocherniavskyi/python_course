from selene.api import s, browser
from conftest import jira_url


class BasePage:
    def __init__(self):
        self.jira_url = jira_url

    @property
    def title(self):
        return browser.title()

    @property
    def profile_button(self):
        return s('#header-details-user-fullname')
