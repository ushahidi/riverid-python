#!/bin/bash

# RiverID Application Installation Script
# =======================================
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

# Update the sources.
apt-get update

# Upgrade the existing packages.
apt-get upgrade -y

# Install the necessary Debian packages.
apt-get install -y apache2 libapache2-mod-wsgi postfix python-pip git

# Install the necessary Python packages.
pip install Flask pymongo

# Create a user for RiverID processes to run as.
adduser --disabled-password --gecos "" riverid

# Create a local clone of the application.
git clone https://github.com/ushahidi/riverid.git /var/www/riverid

# Remove the default Apache configuration.
rm -f /etc/apache2/sites-enabled/000-default

# Copy the RiverID Apache configuration.
cp /var/www/riverid/config/apache.conf /etc/apache2/sites-enabled/riverid.conf

# Tell Apache to reload its configuration.
/etc/init.d/apache2 reload

# Copy the example RiverID configuration file for customisation.
cp /var/www/riverid/api/config.example.py /var/www/riverid/api/config.py

# Download Firewall Configuration
wget -O /etc/firewall.conf --no-check-certificate https://raw.github.com/ushahidi/riverid/master/config/firewall-app.conf

# Download Firewall Startup Script
wget -O /etc/init.d/firewall --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/firewall.sh

# Flag Firewall Startup Script as Executable
chmod +x /etc/init.d/firewall

# Enable Firewall Startup Script
update-rc.d firewall defaults

# Start Firewall
/etc/init.d/firewall start
