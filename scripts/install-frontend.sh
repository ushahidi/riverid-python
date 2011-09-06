#!/bin/bash

# RiverID Frontend Installation Script
# ====================================
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

# Update Sources
apt-get update

# Upgrade Existing Packages
apt-get upgrade -y

# Install New Packages
apt-get install -y apache2 git

# Clone Repository
git clone https://github.com/ushahidi/riverid.git /var/www/riverid

# Remove Default Apache Configuration
rm -f /etc/apache2/sites-enabled/000-default

# Copy Frontend Configuration
cp /var/www/riverid/config/apache-frontend.conf /etc/apache2/sites-enabled/riverid-frontend.conf

# Reload Apache
/etc/init.d/apache2 reload

# Download Firewall Configuration
wget -O /etc/firewall.conf --no-check-certificate https://raw.github.com/ushahidi/riverid/master/config/firewall-frontend.conf

# Download Firewall Startup Script
wget -O /etc/init.d/firewall --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/firewall.sh

# Flag Firewall Startup Script as Executable
chmod +x /etc/init.d/firewall

# Enable Firewall Startup Script
update-rc.d firewall defaults

# Start Firewall
/etc/init.d/firewall start
