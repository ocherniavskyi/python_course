import attr
from api.jira_client.constants.IssueTypes import IssueTypes
from api.jira_client.services.IssueService import IssueService


@attr.s(auto_attribs=True)
class IssueClient:
    issue_service: IssueService

    def create_bug(self, project, summary, **kwargs):
        bug = {
            "project": {
                "key": project
            },
            "summary": summary,
            "issuetype": {
                "id": IssueTypes.BUG
            }
        }
        bug.update(kwargs)
        response = self.issue_service.create_issue(bug)
        json = response.json()
        return json

    def delete_issue(self, issue_id):
        return self.issue_service.delete_issue(issue_id)
