# RiverID User Class
# ==================
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

from riverexception import RiverException

class RiverUser(object):
    def __init__(self, db):
        self.db = db
    
    def add(self, email, array, **item):
        self.db.user.update({'email': email}, {'$push': {array: item}})

    def delete(self, email):
        self.db.user.remove({'email': email})

    def exists(self, email):
        return self.db.user.find_one({'email': email}) != None

    def get(self, email):
        user = self.db.user.find_one({'email': email})
        if not user:
            raise RiverException(_('The email address does not appear to be registered.'))
        return user

    def insert(self, email, **values):
        values['email'] = email
        self.db.user.insert(values)

    def update(self, email_id, **values):
        self.db.user.update({'email': email_id}, {'$set': values})
    
    def update_array(self, email, array, count, key, value):
        self.db.user.update({'email': email}, {'$set': {''.join((array, '.', str(count), '.', key)): value}})

    def validate_session(self, sessions, session_id):
        valid = False
        for session in sessions:
            if session['id'] == session_id and 'stop' not in session:
                valid = True
        if not valid:
            throw new RiverException(_('The session is no longer valid; please sign back into the system.'))
