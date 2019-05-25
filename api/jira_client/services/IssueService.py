from api.jira_client.clients import HttpClient
import attr


@attr.s(auto_attribs=True)
class IssueService:

    http_client: HttpClient

    def delete_issue(self, issue_id):
        return self.http_client.delete(f'/rest/api/2/issue/{issue_id}')

    def create_issue(self, fields, update=None):
        payload = {'fields': fields,
                   'update': update}
        return self.http_client.post('/rest/api/2/issue', json=payload)

