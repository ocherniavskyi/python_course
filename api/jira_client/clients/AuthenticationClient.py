import attr
from api.jira_client.services.AuthenticationService import AuthenticationService


@attr.s(auto_attribs=True)
class AuthenticationClient:

    auth_service: AuthenticationService

    def login(self, username, password):
        return self.auth_service.login(username, password).json()
