import attr
from api.jira_client.services.BaseService import BaseService


@attr.s(auto_attribs=True)
class SearchService(BaseService):

    def search_issues(self, jql, fields=None, start_at=None, max_results=None):
        payload = {'jql': jql, 'fields': fields, 'startAt': start_at, 'maxResults': max_results}
        return self.post('/rest/api/2/search', json=payload)
