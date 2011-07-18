from hashlib import sha512
from user import User

class API(object):
    def changeemail(oldemail, newemail, password:
        pass

    def changepassword(email, oldpassword, newpassword):
        pass

    def checkpassword(email, password):
        pass

    def confirmemail(email, token):
        pass

    def currentsessions(session):
        pass

    def recoverpassword(email):
        pass

    def register(email, password):
        user = User()
        user.email = email
        user.password = sha512(password).digest()

    def signin(email, password):
        pass

    def signout(session):
        pass
