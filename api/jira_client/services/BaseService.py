import attr
from api.jira_client.services.SessionManager import SessionManager


@attr.s(auto_attribs=True)
class BaseService:

    session: SessionManager

    def get(self, uri, params=None):
        return self.session.get(uri, params=params)

    def post(self, uri, json=None, data=None):
        return self.session.post(uri, data=data, json=json)

    def put(self, uri, json=None, data=None):
        return self.session.put(uri, data=data, json=json)

    def delete(self, uri):
        return self.session.delete(uri)
