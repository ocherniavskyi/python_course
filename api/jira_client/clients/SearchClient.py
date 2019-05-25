import attr
from api.jira_client.services.SearchService import SearchService


@attr.s(auto_attribs=True)
class SearchClient:
    search_service: SearchService

    def search_issues_by_comment(self, text):
        jql = f'text ~ "{text}"'
        response = self.search_service.search_issues(jql=jql, fields=['id'])
        json = response.json()

        ids = [x['id'] for x in json['issues']]
        return ids
