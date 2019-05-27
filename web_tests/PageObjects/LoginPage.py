from web_tests.PageObjects.BasePage import BasePage
from selene.api import s, browser


class LoginPage(BasePage):

    def open(self):
        browser.open_url('/login.jsp')
        return self

    def set_username(self, username):
        s('#login-form-username').set(username)
        return self

    def set_password(self, password):
        s('#login-form-password').set(password)
        return self

    def click_login(self):
        s('#login-form-submit').click()
        return self

    def login_as(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    @property
    def wrong_credential_message(self):
        return s('.aui-message-error')

