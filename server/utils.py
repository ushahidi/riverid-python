__author__ = "Matthew Kidza-Griffiths"
__copyright__ = "Copyright 2007, Swiftly.org"
__credits__ = ["Matthew Kidza-Griffiths", "Jon Gosier"]
__license__ = "LGPL"
__version__ = "0.0.1"
__maintainer__ = "Matthew Kidza-Griffiths"
__email__ = "mg@swiftly.org"
__status__ = "Development"


from configuration.configuration import config
from domain.utils import validate_riverid_username
from domain.utils import validate_riverid_password
from domain.utils import validate_riverid_emailaddress
from domain.utils import validate_riverid_familyname
from domain.utils import validate_riverid_othernames
from domain.utils import get_riveridobject_by_riverid
import logging.handlers
import logging
import oauth2

#server logging
serverlogging_filename = config.get('logging', 'filename')
serverlogger = logging.getLogger('serverlogger')
formatter = logging.Formatter('%(created)f, %(name)s, %(levelname)s, %(module)s, %(funcName)s, %(lineno)s, %(message)s')
logging_handler = logging.handlers.TimedRotatingFileHandler(serverlogging_filename, when='d', interval=1, backupCount=30, encoding=None, delay=False, utc=False)
logging_handler.setFormatter(formatter)
serverlogger.addHandler(logging_handler)

class OAuthContainer(object):
    pass

def validate_gateway_oauth_credentials(request):
    oauth_server = oauth2.Server(signature_methods={'HMAC-SHA1': oauth2.SignatureMethod_HMAC_SHA1()})
    oauth_server.timestamp_threshold = 50000

    auth_header = {}
    if 'Authorization' in request.headers:
        auth_header = {'Authorization':request.headers['Authorization']}

    req = oauth2.Request.from_request(
        request.method,
        request.url.split('?')[0],
        headers=auth_header,
        parameters=dict([(k,v) for k,v in request.values.iteritems()]))

    auth = OAuthContainer()
    auth.key = config.get('gatewaycredentials', 'oauth_consumer_key')
    auth.secret = config.get('gatewaycredentials', 'oauth_secret')

    try:
        oauth_server.verify_request(req, auth, None)
        return True
    except oauth2.Error, e:
        serverlogger.error("OAUTH REQUEST DENIED, |%s|" % e)
        return False
    except KeyError, e:
        serverlogger.error("OAUTH REQUEST DENIED, |%s|" % e)
        return False
    except AttributeError, e:
        serverlogger.error("OAUTH REQUEST DENIED, |%s|" % e)
        return False

def validate_gateway_register_form(form):
    riverid = form.get('riverid')
    passed, errors = validate_riverid_username(riverid)
    if not passed:
        return False, errors
    
    password = form.get('password')
    passed, errors = validate_riverid_password(password)
    if not passed:
        return False, errors
    
    email_address = form.get('emailaddress')
    passed, errors = validate_riverid_emailaddress(email_address)
    if not passed:
        return False, errors

    family_name = form.get('familyname')
    passed1, errors1 = validate_riverid_familyname(family_name)

    other_names = form.get('othernames')
    passed2, errors2 = validate_riverid_othernames(other_names)

    if not passed1 or not passed2:
        for error in errors2:
            errors1.append(error)
        return False, errors1

    return True, []

def validate_gateway_credentials_form(form):
    riverid = form.get('riverid')
    password = form.get('password')
    errors = []
    if not riverid:
        errors.append('You did not supply your RiverID username')
    if not password:
        errors.append('You did not supply your password')
    if errors:
        return False, errors
    user = get_riveridobject_by_riverid(riverid)
    if not user:
        return False, ['The RiverID you provided could not be found']
    if not user.password == password:
        return False, ['The password you supplied did not match your account']
    return True, []
