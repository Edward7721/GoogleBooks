import requests
import json
from lib.utils import Config

class Api(object):
    def __init__(self ):
        self.config = Config()
        self.base_url = self.config.uri

    def get(self, q = None,  maxResults = None):
        search_payload = {'q':q, 'maxResults':maxResults}
        resp = requests.get(self.base_url,params = search_payload)
        print 'Response Status Code:', resp.status_code

        if resp.status_code == 200:
            return resp.text
        return resp
