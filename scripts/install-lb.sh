#!/bin/bash

# RiverID Load Balancer Installation Script
# =========================================
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
apt-get install -y nginx openssl

# Remove Default Nginx Configuration
rm -f /etc/nginx/sites-enabled/default

# Download Custom Nginx Configuration
wget -O /etc/nginx/sites-enabled/riverid --no-check-certificate https://raw.github.com/ushahidi/riverid/master/config/nginx-lb.conf

# Create SSL Directory
mkdir /etc/nginx/ssl
