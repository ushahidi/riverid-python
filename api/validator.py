# RiverID Validator Class
# =======================
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

from re import match, IGNORECASE
from riverexception import RiverException

class Validator(object):
    @staticmethod
    def callback(string):
        if match(r'^[a-zA-Z][a-zA-Z0-9_]*$', string) == None:
            raise RiverException(_('Please provide a valid callback function name.'))

    @staticmethod
    def email(string):
        if match(r'(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)', string, IGNORECASE) == None:
            raise RiverException(_('Please provide a valid email address.'))

    @staticmethod
    def password(string):
        if not 8 <= len(string) <= 128:
            raise RiverException(_('Please provide a password between 8 and 128 characters in length.'))

    @staticmethod
    def session(string):
        if match(r'^[a-zA-Z0-9]{64}$', string) == None:
            raise RiverException(_('Please provide a valid session identifier.'))

    @staticmethod
    def token(string):
        if match(r'^[a-zA-Z0-9]{16}$', string) == None:
            raise RiverException(_('Please provide a valid token.'))
