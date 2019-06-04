from api.jira_client.services.AuthenticationService import AuthenticationService
from api.jira_client.services.SessionManager import SessionManager
from web_tests.common_fixtures.infrustructure import *
from conftest import *


@pytest.mark.api
class TestLogin:

    def test_auth_with_valid_credentials(self):
        auth = AuthenticationService(SessionManager(jira_url))
        response = auth.login(username, password)
        payload = response.json()
        assert response.status_code == 200
        assert len(payload['session']['value']) > 0

    @pytest.mark.parametrize("wrong_credentials", [
        {'username': username, 'password': 'abracadabra'},
        {'username': 'abracadabra', 'password': password}])
    def test_login_with_wrong_credentials(self, wrong_credentials):
        auth = AuthenticationService(SessionManager(jira_url))
        response = auth.login(wrong_credentials['username'], wrong_credentials['password'])
        assert response.status_code == 401
        payload = response.json()
        assert payload['errorMessages'][0] == 'Login failed'


@pytest.mark.api
class TestIssueCreation:

    def test_create_bug_with_all_mandatory_fields(self, jira_client: JiraClient, generate_summary: str):
        payload = jira_client.issue.create_bug(project, generate_summary)
        assert payload.get('key')

    def test_create_bug_with_empty_summary(self, jira_client: JiraClient):
        payload = jira_client.issue.create_bug(project, '')
        assert payload['errors']['summary'] == 'You must specify a summary of the issue.'

    def test_create_bug_with_256_symbols_summary(self, jira_client: JiraClient):
        summary = 'long ' * 51 + '1'
        payload = jira_client.issue.create_bug(project, summary)
        assert payload['errors']['summary'] == 'Summary must be less than 255 characters.'


@pytest.mark.api
class TestIssueSearch:
    def test_search_an_issue(self, jira_client: JiraClient, created_bug: dict):
        payload = jira_client.search.search_issues_by_comment(created_bug['summary'])
        assert created_bug['id'] == payload[0]


    def test_search_non_existence_issue(self, jira_client: JiraClient):
        payload = jira_client.search.search_issues_by_comment(str(uuid.uuid4()))
        assert len(payload) == 0
