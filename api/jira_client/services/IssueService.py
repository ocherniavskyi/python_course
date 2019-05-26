from api.jira_client.clients.HttpClient import HttpClient
import attr


@attr.s(auto_attribs=True)
class IssueService:
    http_client: HttpClient

    def get_issue(self, issue_id):
        return self.http_client.get(uri=f'/rest/api/2/issue/{issue_id}')

    def delete_issue(self, issue_id):
        return self.http_client.delete(uri=f'/rest/api/2/issue/{issue_id}')

    def create_issue(self, fields, update=None):
        payload = {'fields': fields, 'update': update}
        return self.http_client.post(uri='/rest/api/2/issue', json=payload)
