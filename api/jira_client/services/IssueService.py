import attr
from api.jira_client.services.BaseService import BaseService


@attr.s(auto_attribs=True)
class IssueService(BaseService):

    def get_issue(self, issue_id):
        return self.get(uri=f'/rest/api/2/issue/{issue_id}')

    def delete_issue(self, issue_id):
        return self.delete(uri=f'/rest/api/2/issue/{issue_id}')

    def create_issue(self, fields, update=None):
        payload = {'fields': fields, 'update': update}
        return self.post(uri='/rest/api/2/issue', json=payload)
