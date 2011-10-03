# RiverID

## Synopsis

RiverID is an authentication and identity management system that provides users with a secure central sign-on facility. Third party applications can make use of the integrated OAuth and OpenID endpoints.

## Recommended Application Architecture

![Diagram](https://github.com/ushahidi/riverid/raw/master/diagrams/architecture.png)

## Application Load Balancer

### Software

* [Debian](http://www.debian.org/)
* [Nginx](http://nginx.org/)
* [OpenSSL](http://www.openssl.org/)

### Deployment

1. Run the installation script:  
`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/install-lb.sh | bash`

2. Edit the configuration file at the following location:  
`/etc/nginx/sites-enabled/riverid`

3. Install the SSL certificate at the following location:  
`/etc/nginx/ssl/riverid.in.crt`

4. Install the SSL key at the following location:  
`/etc/nginx/ssl/riverid.in.key`

5. Load the new configuration:  
`/etc/init.d/nginx reload`

## Application Cluster Node

### Software

* [Apache HTTP Server](http://httpd.apache.org/)
* [Debian](http://www.debian.org/)
* [Flask](http://flask.pocoo.org/)
* [Mod_wsgi](http://code.google.com/p/modwsgi/)
* [Postfix](http://www.postfix.org/)
* [Pymongo](http://pypi.python.org/pypi/pymongo/)
* [Python 2.x](http://python.org/)

### Deployment

1. Run the installation script:  
`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/install-app.sh | bash`

2. Edit the configuration file at the following location:  
`/var/www/riverid/api/config.py`

3. Load the new configuration:  
`/etc/init.d/apache2 reload`

## MongoDB Replication Set Node

### Software

* [Debian](http://www.debian.org/)
* [MongoDB](http://www.mongodb.org/)

### Deployment

1. Run the installation script:  
`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/install-mongo.sh | bash`

2. Edit the configuration file at the following location:  
`/etc/mongodb.conf`

3. Load the new configuration:  
`/etc/init.d/mongodb restart`

4. Whitelist the IP address of each Application Server and each other MongoDB Node. Replace `10.1.2.3` and repeat for each:  
`iptables -I INPUT 1 -p tcp --dport 27017 -j ACCEPT -s 10.1.2.3`

5. After whitelisting the IP addresses, save the firewall configuration for restoration after reboot:  
`iptables-save > /etc/firewall.conf`

## Documentation

* [API Documentation](https://github.com/ushahidi/riverid/blob/master/doc/api.md)

## Localisation

* [Transifex](https://www.transifex.net/projects/p/riverid/)

## License

* [GNU Affero General Public License](http://www.gnu.org/licenses/agpl.html)

## Support

* [SwiftRiver Mailing List](http://groups.google.com/group/swiftriver)

## See Also

* [Ushahidi](http://ushahidi.com/)