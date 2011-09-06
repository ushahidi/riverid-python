# RiverID

## Synopsis

RiverID is an authentication and identity management system that provides users with a secure central sign-on facility. Third party applications can make use of the integrated OAuth and OpenID endpoints.

## Supported Operating Systems

* [Debian 6.0](http://www.debian.org/)

## Dependencies

* [Apache HTTP Server](http://httpd.apache.org/)
* [Flask](http://flask.pocoo.org/)
* [mod_wsgi](http://code.google.com/p/modwsgi/)
* [MongoDB](http://www.mongodb.org/)
* [Postfix](http://www.postfix.org/)
* [Python 2.x](http://python.org/)
* [pymongo](http://pypi.python.org/pypi/pymongo/)

## Recommended Architecture

![Diagram](https://github.com/ushahidi/riverid/raw/master/doc/architecture.png)

## Installation

### Root Required

Please remember to execute each of the following as `root`.

### Application Server

1. Run the installation script:  
`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/install-app.sh | bash`

2. Edit the configuration file using a tool such as `vim` or `nano`:  
`vim /var/www/riverid/api/config.py`  
`nano /var/www/riverid/api/config.py`

3. Restart Apache to make sure your new configuration is loaded:  
`/etc/init.d/apache2 restart`

### MongoDB Server

1. Run the installation script:  
`wget -qO- --no-check-certificate https://raw.github.com/ushahidi/riverid/master/scripts/install-mongo.sh | bash`

2. Whitelist the IP addresses which need access to the MongoDB node (replace `10.1.2.3` and repeat for each):  
`iptables -I INPUT 1 -p tcp --dport 27017 -s 10.1.2.3 -j ACCEPT`

3. After whitelisting the IP addresses, save the firewall configuration for restore after reboot:  
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