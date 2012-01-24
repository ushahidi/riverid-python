# RiverID Mail Class
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

from email.mime.text import MIMEText
from smtplib import SMTP

class Mail(object):
    @staticmethod
    def send(sender, recipient, subject, body, **values):
        if len(body) > 0:
            for key in values:
                body = body.replace('%%%s%%' % key, values[key])
        else:
            for key in values:
                body += "%s=%s\n" % (key, values[key])

        message = MIMEText(body)
        message['From'] = sender
        message['To'] = recipient
        message['Subject'] = subject
        
        smtp = SMTP('localhost')
        smtp.sendmail(sender, [recipient], message.as_string())
        smtp.quit()
