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
from mail import Mail
from riverexception import RiverException
from secret import Secret
from riveruser import RiverUser
from validator import Validator

class API(object):
    def __init__(self, db):
        self.user = RiverUser(db)

    def changeemail(self, oldemail, newemail, password):
        Validator.email(oldemail)
        Validator.email(newemail)
        Validator.password(password)

        if self.user.get(oldemail)['password'] != Secret.hash(password, SALT):
            raise RiverException('The password is incorrect for this user.')
        
        token = Secret.generate(16)

        self.user.update(oldemail, email=newemail, enabled=False, token=token)

        Mail.send(MAIL_FROM, newemail, 'RiverID Email Change', token)

    def changepassword(self, email, oldpassword, newpassword):
        Validator.email(email)
        Validator.password(oldpassword)
        Validator.password(newpassword)

        if self.user.get(email)['password'] != Secret.hash(oldpassword, SALT):
            raise RiverException('The old password is incorrect for this user.')

        self.user.update(email, password=Secret.hash(newpassword, SALT))

    def checkpassword(self, email, password):
        Validator.email(email)
        Validator.password(password)

        return self.user.get(email)['password'] == Secret.hash(password, SALT)
    
    def confirmemail(self, email, token):
        Validator.email(email)
        Validator.token(token)

        user = self.user.get(email)

        if not user['token']:
            raise RiverException('This email address has already been confirmed.')

        if user['token'] != token:
            raise RiverException('The token is not valid for this email address.')

        self.user.update(email, enabled=True, token=False)

    def registered(self, email):
        Validator.email(email)

        return self.user.exists(email)

    def requestpassword(self, email):
        Validator.email(email)

        token = Secret.generate(16)

        if self.user.exists(email):
            subject = 'RiverID: Please confirm your password change.'
            self.user.update(email, token=token)
        else:
            subject = 'RiverID: Please confirm your email address.'
            user_id = Secret.generate(128)
            self.user.insert(email, id=user_id, enabled=False, token=token)

        Mail.send(MAIL_FROM, email, subject, token)
    
    def sessions(self, email, session_id):
        Validator.email(email)
        Validator.session(session_id)

        sessions = self.user.get(email)['session']
        found = False

        for session in sessions:
            if session['id'] == session_id and 'stop' not in session:
                found = True
        
        if not found:
            raise RiverException('The session is not valid for this account.')
        
        return sessions

    def setpassword(self, email, token, password):
        Validator.email(email)
        Validator.token(token)
        Validator.password(password)

        user = self.user.get(email)

        if not user['token']:
            raise RiverException('No password change has been requested for this email address.')

        if user['token'] != token:
            raise RiverException('The token is not valid for this email address.')

        self.user.update(email, enabled=True, token=False, password=Secret.hash(password, SALT))

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

        user = self.user.get(email)

        if user['enabled'] == False:
            raise RiverException('The account is disabled.')
        
        if user['password'] != Secret.hash(password, SALT):
            raise RiverException('The password is incorrect for this user.')

        session_id = Secret.generate(64)
        session_start = datetime.utcnow().isoformat()

        self.user.add(email, 'session', id=session_id, start=session_start)

        return dict(user_id=user['id'], session_id=session_id)

    def signout(self, email, session_id):
        Validator.email(email)
        Validator.session(session_id)

        sessions = self.user.get(email)['session']
        found = False

        for count, session in enumerate(sessions):
            if session['id'] == session_id:
                if 'stop' in session:
                    raise RiverException('The session has already been ended.')

                found = True
                session_stop = datetime.utcnow().isoformat()
                self.user.update_array(email, 'session', count, 'stop', session_stop)
        
        if not found:
            raise RiverException('The session is not valid for this account.')
