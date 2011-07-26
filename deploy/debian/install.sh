#!/bin/bash
#
# RiverID Debian Deployment Script
# ================================
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
apt-get install -y apache2 libapache2-mod-wsgi postfix mongodb-server python-pip git

# Install the necessary Python packages.
pip install Flask pymongo

# Create a user for RiverID processes to run as.
adduser --disabled-password --gecos "" riverid

# Create a local clone of the application.
git clone https://github.com/ushahidi/RiverID.git /var/www/riverid

# Replace the default Apache configuration with the bundled one.
cp /var/www/riverid/deploy/debian/apache.conf /etc/apache2/sites-enabled/000-default

# Tell Apache to reload its configuration.
/etc/init.d/apache2 reload

# Copy the example RiverID configuration file for customisation.
cp /var/www/riverid/api/config.example.py /var/www/riverid/api/config.py
