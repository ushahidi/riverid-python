from datetime import datetime
from mongokit import *

class User(Document):
    structure = {
        'email': unicode,
        'password': unicode,
        'token': unicode,
        'created': datetime,
        'sessions': [unicode]
    }
