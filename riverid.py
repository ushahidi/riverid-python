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

import flask, json

app = flask.Flask(__name__)

@app.route('/api/<method>')
def api(method):
    parameters = flask.request.args.to_dict()
    if callback in parameters:
        callback = parameters['callback']
        del parameters['callback']
    else:
        callback = False
    result = getattr(interface, method)(**parameters)
    response_data = json.dumps(result)
    if callback:
        response_data = ''.join(callback, '(', response_data, ')')
    flask.make_response(response_data)
    response.headers['Content-Type'] = 'application/javascript; charset=UTF-8' if callback else 'application/json; charset=UTF-8'
    return response

def main():
    app.debug = True
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
