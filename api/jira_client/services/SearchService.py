from api.jira_client.clients import HttpClient
import attr


@attr.s(auto_attribs=True)
class SearchService:
    
    http_client: HttpClient

    def search_issues(self, jql, fields=None, start_at=None, max_results=None):
        payload = {'jql': jql, 'fields': fields, 'startAt': start_at, 'maxResults': max_results}
        return self.http_client.post('/rest/api/2/search', json=payload)
