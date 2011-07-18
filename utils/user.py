from datetime import datetime
from mongokit import *
from pymongo.binary import Binary

class User(Document):
    structure = {
        'email': unicode,
        'password': Binary,
        'token': unicode,
        'created': datetime,
        'sessions': [unicode]
    }
