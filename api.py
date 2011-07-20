from utils.mail import Mail
from utils.secret import Secret
from utils.validator import Validator

class API(object):
    def __init__(self, db):
        self.db = db

    def changeemail(self, oldemail, newemail, password):
        Validator.email(oldemail)
        Validator.email(newemail)
        Validator.password(password)

    def changepassword(self, email, oldpassword, newpassword):
        Validator.email(email)
        Validator.password(oldpassword)
        Validator.password(newpassword)

    def checkpassword(self, email, password):
        Validator.email(email)
        Validator.password(password)

    def confirmemail(self, email, token):
        Validator.email(email)
        Validator.token(token)

    def currentsessions(self, session):
        Validator.session(session)

    def recoverpassword(self, email):
        Validator.email(email)

    def register(self, email, password):
        Validator.email(email)
        Validator.password(password)
        if self.db.users.find_one({'email': email}):
            raise Exception('The email address has already been registered.')
        self.db.users.insert({'email': email, 'password': Secret.hash(password)})
        return {'email': email}

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

    def signout(self, session):
        Validator.session(session)
