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






"""
auth = json.loads(post_response.text)
login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
"""

"""
If q=None
{
 "error": {
  "errors": [
   {
    "domain": "global",
    "reason": "queryRequired",
    "message": "Missing query.",
    "locationType": "parameter",
    "location": "q"
   }
  ],
  "code": 400,
  "message": "Missing query."
 }
}
"""