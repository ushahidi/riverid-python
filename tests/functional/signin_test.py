__author__ = "Matthew Kidza-Griffiths"
__copyright__ = "Copyright 2007, Swiftly.org"
__credits__ = ["Matthew Kidza-Griffiths", "Jon Gosier"]
__license__ = "LGPL"
__version__ = "0.0.1"
__maintainer__ = "Matthew Kidza-Griffiths"
__email__ = "mg@swiftly.org"
__status__ = "Development"

import oauth2
import time
import urllib2
import urllib
from urllib2 import URLError

key = u'451ee6b4d98f800700ff6af49c7fa3478783ade4177e1dc5c84796aa'
secret = u'f7fcdeef3a5a0989d31217589599fdd21f1f54acb78571dd1173d913'
url = 'http://localhost:5000/thegateway/validatecredentials'

def build_request(url, method='POST', values={}):
    params = {
        'oauth_timestamp': int(time.time()),
        'oauth_nonce': None,
        'oauth_signature_method':'HMAC-SHA1',
    }
    params.update(values)
    consumer = oauth2.Consumer(key=key,secret=secret)
    req = oauth2.Request(method=method, url=url, parameters=params)
    signature_method = oauth2.SignatureMethod_HMAC_SHA1()
    req.sign_request(signature_method, consumer, None)
    return req

values = {
    'riverid':'test1',
    'password':'password'
}
request = build_request(url, values=values)
data = urllib.urlencode(values)
try :
    req = urllib2.Request(url, headers=request.to_header(), data=data)
    u = urllib2.urlopen(req)
    #u = urllib2.urlopen(request.to_url())
    print u.read()
except URLError, e:
    print e
