import attr
import requests


@attr.s(auto_attribs=True)
class BaseService:
    base_url: str
    username: str
    password: str

    def get(self, uri, params=None):
        return requests.get(self.base_url + uri, auth=self.get_auth(), params=params)

    def post(self, uri, json=None, data=None):
        #headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        return requests.post(self.base_url + uri, auth=self.get_auth(), data=data, json=json)#, headers=headers)

    def put(self, uri, json=None, data=None):
        return requests.put(self.base_url + uri, auth=self.get_auth(), data=data, json=json)

    def delete(self, uri):
        return requests.delete(self.base_url + uri, auth=self.get_auth())
    
    def get_auth(self):
        return self.username, self.password
