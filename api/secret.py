# RiverID Secret Class
# ====================
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

from hashlib import sha512
from random import choice
from string import ascii_letters, digits

class Secret(object):
    @staticmethod
    def hash(string, salt):
        return sha512(salt + string).hexdigest()

    @staticmethod
    def generate(length=64):
        characters = ascii_letters + digits
        return ''.join([choice(characters) for i in range(length)])
