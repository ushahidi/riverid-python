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

from config import INFO_URL, MAIL_FROM, NAME, SALT
from datetime import datetime
from mail import Mail
from riverexception import RiverException
from secret import Secret
from riversite import RiverSite
from riveruser import RiverUser
from validator import Validator

class API(object):
    def __init__(self, db):
        self.site = RiverSite(db)
        self.user = RiverUser(db)

    def about(self):
        return dict(info_url=INFO_URL, name=NAME, version='1.0')

    def addusertosite(self, email, session_id, url):
        Validator.email(email)
        Validator.session(session_id)
        Validator.url(url)

        user = self.user.get(email)
        self.user.validate_session(user['session'], session_id)

        if not self.site.exists(url):
            self.site.add_site(url)

        if url in self.site.get_user_urls(user['id']):
            raise RiverException(_('The site has already been added to this user.'))

        self.site.add_user(url, user['id'])

    def changeemail(self, oldemail, newemail, password, mailbody, mailfrom = None, mailsubject = None):
        Validator.email(oldemail)
        Validator.email(newemail)
        Validator.password(password)

        if self.user.get(oldemail)['password'] != Secret.hash(password, SALT):
            raise RiverException(_('The password is incorrect for this user.'))

        if self.user.exists(newemail):
            raise RiverException(_('The new email address has already been registered.'))

        if mailsubject is None:
            mailsubject = _('CrowdmapID Email Change')

        if mailfrom is None:
            mailfrom = MAIL_FROM

        token = Secret.generate(16)

        self.user.update(oldemail, email=newemail, enabled=False, token=token)

        Mail.send(mailfrom, newemail, mailsubject, mailbody, token=token)

    def changepassword(self, email, oldpassword, newpassword):
        Validator.email(email)
        Validator.password(newpassword)

        if self.user.get(email)['password'] != Secret.hash(oldpassword, SALT):
            raise RiverException(_('The old password is incorrect for this user.'))

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
            raise RiverException(_('This email address has already been confirmed.'))

        if user['token'] != token:
            raise RiverException(_('The token is not valid for this email address.'))

        self.user.update(email, enabled=True, token=False)

    def register(self, email, password):
        Validator.email(email)
        Validator.password(password)

        if self.user.exists(email):
            raise RiverException(_('The given email address has already been registered.'))

        user_id = Secret.generate(128)

        self.user.insert(email, enabled=True, id=user_id, password=Secret.hash(password, SALT))

        return user_id

    def registered(self, email):
        Validator.email(email)

        return self.user.exists(email)

    def requestpassword(self, email, mailbody, mailfrom = None, mailsubject = None):
        Validator.email(email)

        token = Secret.generate(16)

        if mailfrom is None:
            mailfrom = MAIL_FROM

        if self.user.exists(email):
            if mailsubject is None:
                mailsubject = _('CrowdmapID: Please confirm your password change.')
            self.user.update(email, token=token)
        else:
            if mailsubject is None:
                mailsubject = _('CrowdmapID: Please confirm your email address.')
            user_id = Secret.generate(128)
            self.user.insert(email, id=user_id, enabled=False, token=token)

        Mail.send(mailfrom, email, mailsubject, mailbody, token=token)

    def sessions(self, email, session_id):
        Validator.email(email)
        Validator.session(session_id)

        sessions = self.user.get(email)['session']
        found = False

        for session in sessions:
            if session['id'] == session_id and 'stop' not in session:
                found = True

        if not found:
            raise RiverException(_('The session is not valid for this account.'))

        return sessions

    def setpassword(self, email, token, password):
        Validator.email(email)
        Validator.token(token)
        Validator.password(password)

        user = self.user.get(email)

        if not user['token']:
            raise RiverException(_('No password change has been requested for this email address.'))

        if user['token'] != token:
            raise RiverException(_('The token is not valid for this email address.'))

        self.user.update(email, enabled=True, token=False, password=Secret.hash(password, SALT))

    def signedin(self, cookies):
        session_id = cookies.get('session_id')
        user_id = cookies.get('user_id')

        return dict(session_id=session_id, user_id=user_id)

    def signin(self, email, password):
        Validator.email(email)
        Validator.password(password)

        user = self.user.get(email)

        if user['enabled'] == False:
            raise RiverException(_('The account is disabled.'))

        if user['password'] != Secret.hash(password, SALT):
            raise RiverException(_('The password is incorrect for this user.'))

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
                    raise RiverException(_('The session has already been ended.'))

                found = True
                session_stop = datetime.utcnow().isoformat()
                self.user.update_array(email, 'session', count, 'stop', session_stop)

        if not found:
            raise RiverException(_('The session is not valid for this account.'))

    def usersites(self, email, session_id):
        Validator.email(email)
        Validator.session(session_id)

        user = self.user.get(email)
        self.user.validate_session(user['session'], session_id)

        return self.site.get_user_urls(user['id'])
