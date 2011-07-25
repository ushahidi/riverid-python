# RiverID API Class
# =================
#
# This file is part of RiverID.
#
# RiverID is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# RiverID is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with RiverID.  If not, see <http://www.gnu.org/licenses/>.

from config import MAIL_FROM, SALT
from datetime import datetime
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

        if self.user.get(oldemail)['password'] != Secret.hash(password, SALT):
            raise Exception('The password is incorrect for this user.')
        
        token = Secret.generate(16)

        self.user.update(oldemail, email=newemail, enabled=False, token=token)

        Mail.send(MAIL_FROM, newemail, 'RiverID Email Change', token)

        return dict(oldemail=oldemail, newemail=newemail)

    def changepassword(self, email, oldpassword, newpassword):
        Validator.email(email)
        Validator.password(oldpassword)
        Validator.password(newpassword)

        if self.user.get(email)['password'] != Secret.hash(oldpassword, SALT):
            raise Exception('The old password is incorrect for this user.')

        self.user.update(email, password=Secret.hash(newpassword, SALT))

        return dict(email=email)

    def checkpassword(self, email, password):
        Validator.email(email)
        Validator.password(password)

        return dict(email=email, valid=self.user.get(email)['password'] == Secret.hash(password, SALT)}
    
    def confirmemail(self, email, token):
        Validator.email(email)
        Validator.token(token)

        user = self.user.get(email)

        if not user['token']:
            raise Exception('This email address has already been confirmed.')

        if user['token'] != token:
            raise Exception('The token is not valid for this email address.')

        self.user.update(email, enabled=True, token=False)

        return dict(email=email)

    def currentsessions(self, email, session):
        Validator.email(email)
        Validator.session(session)

        return dict(email=email, sessions=self.user.get(email)['sessions'])

    def registered(self, email):
        Validator.email(email)

        return dict(email=email, registered=self.user.exists(email))

    def requestpassword(self, email):
        Validator.email(email)

        token = Secret.generate(16)

        if self.user.exists(email):
            subject = 'RiverID Change Password'
            self.user.update(email, token=token)
        else:
            subject = 'RiverID Registration'
            self.user.insert(email, enabled=False, token=token)

        Mail.send(MAIL_FROM, email, subject, token)

        return dict(email=email)

    def setpassword(self, email, token, password):
        Validator.email(email)
        Validator.token(token)
        Validator.password(password)

        user = self.user.get(email)

        if not user['token']:
            raise Exception('No password change has been requested for this email address.')

        if user['token'] != token:
            raise Exception('The token is not valid for this email address.')

        self.user.update(email, enabled=True, token=False, password=Secret.hash(password, SALT))

        return dict(email=email)

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

        session_id = Secret.generate(64)
        session_start = datetime.utcnow().isoformat()

        self.user.add(email, 'session', id=session_id, start=session_start)

        return dict(email=email, session_id=session_id, session_start=session_start)

    def signout(self, email, session_id):
        Validator.email(email)
        Validator.session(session_id)

        session_stop = datetime.utcnow().isoformat()

        self.user.update_sub(email, 'session', 'id', session_id, id=False, stop=session_stop)

        return dict(email=email, session_id=session_id, session_stop=session_stop)