from tests.web_ui_test.UiTest import UiTest


class TestLoginPage(UiTest):

    def test_login_with_valid_username(self, login_page):
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login()

        login_page.profile_button.should_be(visible)