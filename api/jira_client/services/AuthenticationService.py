import attr
from api.jira_client.services.BaseService import BaseService


@attr.s
class AuthenticationService(BaseService):

    def login(self, username, password):
        payload = {'username': username, 'password': password}
        return self.post(uri='/rest/auth/1/session', json=payload)
