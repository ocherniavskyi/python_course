from api.jira_client.clients.AuthenticationClient import AuthenticationClient
from api.jira_client.clients.IssueClient import IssueClient
from api.jira_client.clients.SearchClient import SearchClient
from api.jira_client.services.AuthenticationService import AuthenticationService
from api.jira_client.services.IssueService import IssueService
from api.jira_client.services.SearchService import SearchService
from api.jira_client.services.SessionManager import SessionManager


class JiraClient:

    def __init__(self, base_url: str, username: str, password: str):
        session = SessionManager(base_url)
        self.auth: AuthenticationClient = AuthenticationClient(AuthenticationService(session))
        self.issue: IssueClient = IssueClient(IssueService(session))
        self.search: SearchClient = SearchClient(SearchService(session))
        self.auth.login(username, password)


