__author__ = "Matthew Kidza-Griffiths"
__copyright__ = "Copyright 2007, Swiftly.org"
__credits__ = ["Matthew Kidza-Griffiths", "Jon Gosier"]
__license__ = "LGPL"
__version__ = "0.0.1"
__maintainer__ = "Matthew Kidza-Griffiths"
__email__ = "mg@swiftly.org"
__status__ = "Development"


from mongokit import *
from domain.utils import con

@con.register
class RiverID(Document):

    #The MongoDB collection to store these object in
    __collection__ = 'riverids'

    #The database used for all objects in this project
    __database__ = 'swift_riverid'

    #Allow access to properties via dot notation
    use_dot_notation = True

    #The JSON structure of this object
    structure = {
        'riverid': unicode,
        'password': unicode,
        'email_address': unicode,
        'family_name': unicode,
        'other_names': unicode,
    }

    #Indices
    indexes = [
        {'fields': 'riverid', 'unique': True,}
    ]    