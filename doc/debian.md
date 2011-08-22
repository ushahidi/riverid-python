# RiverID Debian 6.0 (Squeeze) Installation Instructions

## Automatic

Run the following at the command line:

`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/riverid/master/deploy/debian/install.sh | sudo bash`

## Manual

1. Install the necessary Debian packages.  
`apt-get install apache2 libapache2-mod-wsgi postfix mongodb-server python-pip git`

2. Install the necessary Python packages.  
`pip install Flask pymongo`

3. Create a user for RiverID processes to run as.  
`adduser --disabled-password --gecos "" riverid`

4. Create a local clone of the application.  
`git clone https://github.com/ushahidi/RiverID.git /var/www/riverid`

5. Replace the default Apache configuration with the bundled one.  
`cp /var/www/riverid/deploy/debian/000-default /etc/apache2/sites-enabled/`

6. Tell Apache to reload its configuration.  
`/etc/init.d/apache2 reload`

7. Copy the example RiverID configuration file for customisation.  
`cp /var/www/riverid/api/config.example.py /var/www/riverid/api/config.py`