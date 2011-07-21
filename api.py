from config import MAIL_FROM, SALT
from util.mail import Mail
from util.secret import Secret
from util.user import User
from util.validator import Validator

class API(object):
    def __init__(self, db):
        self.user = User(db)

    def changeemail(self, oldemail, newemail, password):
        Validator.email(oldemail)
        Validator.email(newemail)
        Validator.password(password)

        if user.get(oldemail)['password'] != Secret.hash(password):
            raise Exception('The password is incorrect for this user.')

        self.user.update(oldemail, email=newemail)

    def changepassword(self, email, oldpassword, newpassword):
        Validator.email(email)
        Validator.password(oldpassword)
        Validator.password(newpassword)

        if user.get(email)['password'] != Secret.hash(oldpassword):
            raise Exception('The old password is incorrect for this user.')

        self.user.update(email, password=Secret.hash(newpassword))

    def checkpassword(self, email, password):
        Validator.email(email)
        Validator.password(password)

    def confirmemail(self, email, token):
        Validator.email(email)
        Validator.token(token)
        user = self.user.get(email)
        if not user['token']:
            raise Exception('The email address has already been confirmed.')
        if user.token != token:
            raise Exception('The token is not valid for this email address.')
        self.user.update(email, token=False)
        return {'email': email}

    def currentsessions(self, session):
        Validator.session(session)

    def recoverpassword(self, email):
        Validator.email(email)

    def register(self, email, password):
        Validator.email(email)
        Validator.password(password)
        if self.user.exists(email):
            raise Exception('The email address has already been registered.')
        token = Secret.generate(16)
        self.user.insert(email, password=Secret.hash(password, SALT), token=token)
        Mail.send(MAIL_FROM, email, 'RiverID Email Confirmation', token)
        return {'email': email}

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

    def signout(self, session):
        Validator.session(session)
