from config import MAIL_FROM, SALT
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
        user = self.db.users.find_one({'email': email})
        if not user:
            raise Exception('The email address has not been registered.')
        if user.token != token:
            raise Exception('The token does not match with the email address provided.')
        self.db.users.update({'email': email}, {'token': False})
        return {'email': email}

    def currentsessions(self, session):
        Validator.session(session)

    def recoverpassword(self, email):
        Validator.email(email)

    def register(self, email, password):
        Validator.email(email)
        Validator.password(password)
        if self.db.users.find_one({'email': email}):
            raise Exception('The email address has already been registered.')
        token = Secret.generate(16)
        self.db.users.insert({'email': email, 'password': Secret.hash(password, SALT), 'token': token})
        Mail.send(MAIL_FROM, email, 'RiverID Email Confirmation', token)
        return {'email': email}

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

    def signout(self, session):
        Validator.session(session)
