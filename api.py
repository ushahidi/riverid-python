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

        if user.get(oldemail)['password'] != Secret.hash(password, SALT):
            raise Exception('The password is incorrect for this user.')

        self.user.update(oldemail, email=newemail)

        return dict(oldemail=oldemail, newemail=newemail)

    def changepassword(self, email, oldpassword, newpassword):
        Validator.email(email)
        Validator.password(oldpassword)
        Validator.password(newpassword)

        if user.get(email)['password'] != Secret.hash(oldpassword, SALT):
            raise Exception('The old password is incorrect for this user.')

        self.user.update(email, password=Secret.hash(newpassword, SALT))

        return dict(email=email)

    def checkpassword(self, email, password):
        Validator.email(email)
        Validator.password(password)

        return dict(email=email, valid=self.user.get(email)['password'] == Secret.hash(password, SALT)}

    def currentsessions(self, email, session):
        Validator.email(email)
        Validator.session(session)

        return dict(email=email, sessions=self.user.get(email)['sessions'])

    def requestpassword(self, email):
        Validator.email(email)

        token = Secret.generate(16)

        if self.user.exists(email):
            self.user.update(email, token=token)
        else:
            self.user.insert(email, token=token)

        Mail.send(MAIL_FROM, email, 'RiverID Password Change', token)

        return dict(email=email)

    def setpassword(self, email, token, password):
        Validator.email(email)
        Validator.token(token)
        Validator.password(password)

        user = self.user.get(email)

        if not user['token']:
            raise Exception('No password change has been requested.')

        if user['token'] != token:
            raise Exception('The token is not valid for this email address.')

        self.user.update(email, token=False, password=Secret.hash(password, SALT))

        return dict(email=email)

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

    def signout(self, email, session):
        Validator.email(email)
        Validator.session(session)