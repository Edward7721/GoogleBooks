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
        status = resp.status_code
        print 'Response Status Code:', status
        if  status== 200:
            return resp.text, status
        return resp, status

def nice_print_out( r):
    header_string = ''
    for key in r.request.headers:
        header_string += '-H "%s: %s" ' % (key, r.request.headers[key])
    if r.request.body:
        print('Curl is:\n curl %s "%s" -d \'%s\' -X %s' % (header_string, r.request.url, r.request.body,
                                                           r.request.method))
    else:
        print('Curl is:\n curl %s "%s" -X %s' % (header_string, r.request.url, r.request.method))
    print('\nResponse status code: %s' % r.status_code)
    if r.json != 'NoJSON':
        try:
            print('\nResponse body:\n %s' % json.dumps(r.json, indent=2))
            print"============================================"
            print json.dumps(r.json)
        except TypeError:
            print('\nResponse body:\n %s' % r.json)
    else:
        print('\nNo body in the response.')
