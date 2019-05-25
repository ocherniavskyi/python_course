from api.jira_client.clients.HttpClient import HttpClient
from api.jira_client.clients.IssueClient import IssueClient
from api.jira_client.clients.SearchClient import SearchClient
from api.jira_client.services.IssueService import IssueService
from api.jira_client.services.SearchService import SearchService


class JiraClient:

    def __init__(self, base_url: str, username: str, password: str):
        self.http_client: HttpClient = HttpClient(base_url, username, password)
        self.issue: IssueClient = IssueClient(IssueService(self.http_client))
        self.search: SearchClient = SearchClient(SearchService(self.http_client))
