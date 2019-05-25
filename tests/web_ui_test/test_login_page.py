import allure
from selene.conditions import visible, text
from web_tests.common_fixtures.infrustructure import *
from conftest import *


@pytest.mark.webui
class TestLoginPage:

    def test_login_with_valid_username(self, login_page):
        login_page.set_username(username)
        login_page.set_password(password)
        login_page.click_login()

        login_page.profile_button.should_be(visible)

    @pytest.mark.parametrize("wrong_credentials", [
        {'username': username, 'password': 'abracadabra'},
        {'username': 'abracadabra', 'password': password}])
    def test_login_with_wrong_username(self, wrong_credentials, login_page):
        login_page.set_username(wrong_credentials['username'])
        login_page.set_password(wrong_credentials['password'])
        login_page.click_login()

        login_page.wrong_credential_message.should(visible)
        login_page.wrong_credential_message.should_have(text(
            'Sorry, your username and password are incorrect - please try again.'))




