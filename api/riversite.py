# RiverID Site Class
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

class RiverSite(object):
    def __init__(self, db):
        self.db = db
    
    def add_site(self, url):
        self.db.site.insert({'url': url})

    def add_user(self, url, user_id):
        self.db.site.update({'url': url}, {'$push': {'user_id': user_id}})

    def exists(self, url):
        return self.db.site.find_one({'url': url}) != None

    def get_user_urls(self, user_id):
        urls = []
        for site in self.db.site.find({'user_id': user_id}):
            urls.append(site['url'])
        return urls
