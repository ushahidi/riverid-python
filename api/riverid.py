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

from api import API
from flask import abort, Flask, make_response, request
from inspect import getargspec
from json import dumps

app = Flask(__name__)

@app.route('/api/<method_name>')
def api(method_name):
    api = API()
    method = getattr(api, method_name, False)

    if method == False:
        abort(404)

    method_parameters = getargspec(method).args
    request_parameters = request.args.to_dict()

    if callback in request_parameters:
        callback = request_parameters['callback']
        del request_parameters['callback']
    else:
        callback = False

    for key in method_parameters:
        if key not in request_parameters:
            abort(400)
        
    for key in request_parameters:
        if key not in method_parameters:
            del request_parameters[key]

    try:
        result = method(**request_parameters)
        result['status'] = 'success'
    except Exception as message:
        result = {'status': 'error', 'parameters': request_parameters, 'message': message}

    json = dumps(result)

    if callback:
        javascript = ''.join(callback, '(', json, ')')
        response = make_response(javascript)
        response.headers['Content-Type'] = 'application/javascript; charset=UTF-8'
    else:
        response = make_response(json)
        response.headers['Content-Type'] = 'application/json; charset=UTF-8'

    return response

def main():
    app.debug = True
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
