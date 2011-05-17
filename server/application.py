__author__ = "Matthew Kidza-Griffiths"
__copyright__ = "Copyright 2007, Swiftly.org"
__credits__ = ["Matthew Kidza-Griffiths", "Jon Gosier"]
__license__ = "LGPL"
__version__ = "0.0.1"
__maintainer__ = "Matthew Kidza-Griffiths"
__email__ = "mg@swiftly.org"
__status__ = "Development"


from flask import Flask, request, jsonify
from domain.models import RiverID
from domain.utils import con
from server.utils import validate_gateway_oauth_credentials
from server.utils import validate_gateway_register_form
from server.utils import validate_gateway_credentials_form

app = Flask(__name__)

@app.route('/thegateway/register', methods=['POST'])
def register_from_the_gateway():
    if not validate_gateway_oauth_credentials(request):
        return jsonify(status='Failed', errorcomponent='gateway', errors=['The oauth credentials supplied were inaccurate.'])
    passed, errors = validate_gateway_register_form(request.form)
    if not passed:
        return jsonify(status='Failed', errorcomponent='user',  errors=errors)
    riverid = con.RiverID()
    riverid.riverid = request.form.get('riverid')
    riverid.password = request.form.get('password')
    riverid.email_address = request.form.get('emailaddress')
    riverid.family_name = request.form.get('familyname')
    riverid.other_names = request.form.get('othernames')
    riverid.save()
    return jsonify(status='Succeeded')
    return;

@app.route('/thegateway/validatecredentials', methods=['POST'])
def validate_credentials_from_the_gateway():
    if not validate_gateway_oauth_credentials(request):
        return jsonify(status='Failed', errorcomponent='gateway',  errors=['The oauth credentials supplied were inaccurate.'])
    passed, errors = validate_gateway_credentials_form(request.form)
    if not passed:
        return jsonify(status='Failed', errorcomponent='user',  errors=errors)
    return jsonify(status='Succeeded')

