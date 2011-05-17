__author__ = "Matthew Kidza-Griffiths"
__copyright__ = "Copyright 2007, Swiftly.org"
__credits__ = ["Matthew Kidza-Griffiths", "Jon Gosier"]
__license__ = "LGPL"
__version__ = "0.0.1"
__maintainer__ = "Matthew Kidza-Griffiths"
__email__ = "mg@swiftly.org"
__status__ = "Development"


from mongokit import *
from configuration.configuration import config

con = Connection(config.get('mongodb', 'host'), config.getint('mongodb', 'port'))

from domain.models import *
import re


################################################################################
# RiverID Access Methods                                                       #
################################################################################
def get_riveridobject_by_riverid(riverid):
    return con.RiverID.find_one({'riverid':riverid.lower()})

################################################################################
# Validation functions for RiverID objects                                     #
################################################################################
def validate_riverid_username(riverid):
    if not riverid:
        return False, ["You must supply a RiverID"]
    errors = []
    if not riverid.islower():
        errors.append('Your RiverID must be lower case')
    rule = re.compile(r'^\w{4,20}$', re.IGNORECASE)
    if not bool(rule.match(riverid)):
        errors.append('Your RiverID must contain only letters and between 4 and 50 characters')
    if len(errors):
        return False, errors
    existing_user = con.RiverID.find_one({'riverid':riverid})
    if existing_user:
        errors.append('Sorry, that RiverID is already taken')
    return len(errors) == 0, errors

def validate_riverid_password(password):
    if not password:
        return False, ["You must supply a password"]
    rule = re.compile(r'^\w{6,20}$', re.IGNORECASE)
    if not bool(rule.match(password)):
        return False, ['Your password must be lower case, contain only letters, number and underscores and between 6 and 20 characters']
    return True, []

def validate_riverid_emailaddress(email):
    if not email:
        return False, ["You must supply an email address"]
    rule = re.compile(r"(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)",re.IGNORECASE)
    if not bool(rule.match(email)):
        return False, ["The email you entered doesn't look like and email address"]
    existing_user = con.RiverID.find_one({'email_address':email.lower()})
    if existing_user:
        return False, ['Sorry, that email address is already associated with a RiverID']
    return True, []

def validate_riverid_familyname(family_name):
    if not family_name:
        return True, []
    rule = re.compile(r'^\w+$', re.IGNORECASE)
    if not bool(rule.match(family_name)):
        return False, ['Your family name must contain only letters']
    return True, []

def validate_riverid_othernames(other_names):
    if not other_names:
        return True, []
    rule = re.compile(r'^\w+$', re.IGNORECASE)
    if not bool(rule.match(other_names)):
        return False, ['Your other names must contain only letters']
    return True, []

