from requests import Session


class SessionManager(Session):
    def __init__(self, url_base=None):
        super(SessionManager, self).__init__()
        self.url_base = url_base

    def request(self, method, url, **kwargs):
        modified_url = self.url_base + url
        return super(SessionManager, self).request(method, modified_url, **kwargs)
