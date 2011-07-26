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
from flask import Flask, make_response, request
from inspect import getargspec
from json import dumps

app = Flask(__name__)

@app.route('/api/<method_name>')
def api(method_name):
    api = API()
    method = getattr(api, method_name)
    method_parameters = getargspec(method).args
    request_parameters = request.args.to_dict()

    if callback in request_parameters:
        callback = request_parameters['callback']
        del request_parameters['callback']
    else:
        callback = False

    result = method(**request_parameters)
    response_data = dumps(result)

    if callback:
        response_data = ''.join(callback, '(', response_data, ')')

    response = make_response(response_data)
    response.headers['Content-Type'] = 'application/javascript; charset=UTF-8' if callback else 'application/json; charset=UTF-8'

    return response

def main():
    app.debug = True
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
