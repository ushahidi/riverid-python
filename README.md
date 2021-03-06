# RiverID

## Synopsis

RiverID is an authentication and identity management system that provides users with a secure central sign-on facility.

## Architecture

![Diagram](https://github.com/ushahidi/riverid/raw/master/diagrams/architecture.png)

## Application Load Balancer

### Software

* [Ubuntu](http://www.ubuntu.com/)
* [Nginx](http://nginx.org/)
* [OpenSSL](http://www.openssl.org/)

### Deployment

1. Run the installation script:  
`wget -qO- https://raw.github.com/ushahidi/riverid/master/scripts/install-lb.sh | bash`

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
* [Ubuntu](http://www.ubuntu.com/)
* [Flask](http://flask.pocoo.org/)
* [Mod_wsgi](http://code.google.com/p/modwsgi/)
* [Postfix](http://www.postfix.org/)
* [Pymongo](http://pypi.python.org/pypi/pymongo/)
* [Python 2.x](http://python.org/)

### Deployment

1. Run the installation script:  
`wget -qO- https://raw.github.com/ushahidi/riverid/master/scripts/install-app.sh | bash`

2. Edit the configuration file at the following location:  
`/var/www/riverid/api/config.py`

3. Load the new configuration:  
`/etc/init.d/apache2 restart`

## MongoDB Replication Set Node

### Software

* [Ubuntu](http://www.ubuntu.com/)
* [MongoDB](http://www.mongodb.org/)

### Deployment

1. Run the installation script:  
`wget -qO- https://raw.github.com/ushahidi/riverid/master/scripts/install-mongo.sh | bash`

2. Whitelist the IP address of each Application Cluster Node and each other MongoDB Node. Replace `10.1.2.3` and repeat for each:  
`iptables -I INPUT 1 -p tcp --dport 27017 -j ACCEPT -s 10.1.2.3`

3. After whitelisting the IP addresses, save the firewall configuration for restoration after reboot:  
`iptables-save > /etc/firewall.conf`

4. Configure the [Replication Set](http://www.mongodb.org/display/DOCS/Replica+Sets).

## Content Delivery Network

* `http://c290918.r18.cf1.rackcdn.com/`
* `https://c290918.ssl.cf1.rackcdn.com/`

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
