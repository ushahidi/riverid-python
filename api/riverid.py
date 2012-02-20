# RiverID Controller
# ==================
#
# This file is part of RiverID.
#
# RiverID is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RiverID is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with RiverID.  If not, see <http://www.gnu.org/licenses/>.

import os, sys
sys.path.append(os.path.dirname(__file__))

from api import API
from config import MONGODB_SERVERS
from flask import abort, Flask, make_response, request
from inspect import getargspec
from json import dumps
from pymongo import Connection
from riverexception import RiverException
from validator import Validator

import gettext
localedir = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'locale'))
gettext.bindtextdomain('api', localedir)
gettext.textdomain('api')
_ = gettext.gettext

languages = {}
for lang in os.listdir(localedir):
    languages[lang] = gettext.translation('api', localedir, [lang])
languages['en_ZA'].install()

application = Flask(__name__)

@application.route('/api/<method_name>', methods=['GET', 'POST'])
def api(method_name):
    db = Connection(MONGODB_SERVERS).riverid
    api = API(db)

    # Get a reference to the actual method in the API object to call
    method = getattr(api, method_name, False)

    # If the method could not be returned, it does not exist in the API
    if method == False:
        abort(404)

    # Use reflection to retrieve the list of defined parameters of the method
    method_parameters = getargspec(method).args
    method_parameters.remove('self')

    # Read the given parameters out of the post body if available, otherwise use the querystring
    # Use to_dict because every parameter key can only have one associated value
    if request.method == 'POST':
        request_parameters = request.form.to_dict()
    else:
        request_parameters = request.args.to_dict()

    # Special treatment for the callback parameter as that is used for JSONP
    if 'callback' in request_parameters:
        callback = request_parameters['callback']
        Validator.callback(callback)
    else:
        callback = False

    # Special treatment for the lang parameter as that is used for GNU Gettext
    if 'lang' in request_parameters:
        if request_parameters['lang'] in languages:
            languages[request_parameters['lang']].install()
        else:
            languages['en_ZA'].install()
    else:
        languages['en_ZA'].install()

    # Pass the cookies object to the method if the method has a parameter called "cookies"
    if 'cookies' in method_parameters:
        request_parameters['cookies'] = request.cookies

    # Check if there are any missing parameters
    for key in method_parameters:
        if key not in request_parameters:
            abort(400)

    # Remove extra parameters in the request that are not needed by the method
    unused_parameters = []
    for key in request_parameters:
        if key not in method_parameters:
            unused_parameters.append(key)
    for key in unused_parameters:
        del request_parameters[key]

    # Start building the object to be serialised and returned to the client
    result = dict(method=method_name, request=request_parameters)

    # Attempt to execute the API method with the given parameters
    try:
        result['response'] = method(**request_parameters)
        result['success'] = True
    except RiverException as (error,):
        result['success'] = False
        result['error'] = error

    # Serialise the response data
    json = dumps(result)

    # If the callback has been specified, return as JSONP, otherwise as straight JSON
    if callback:
        javascript = '%s(%s);\n' % (callback, json)
        response = make_response(javascript)
        response.headers['Content-Type'] = 'application/javascript; charset=UTF-8'
    else:
        response = make_response(json + '\n')
        response.headers['Content-Type'] = 'application/json; charset=UTF-8'

    return response

def main():
    application.debug = True
    application.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
