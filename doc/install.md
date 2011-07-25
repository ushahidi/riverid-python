# RiverID Generic Installation Instructions

## Dependencies

* [Apache HTTP Server](http://httpd.apache.org/)
* [Flask](http://flask.pocoo.org/)
* [mod_wsgi](http://code.google.com/p/modwsgi/)
* [MongoDB](http://www.mongodb.org/)
* [Python 2.x](http://python.org/)
* [pymongo](http://pypi.python.org/pypi/pymongo/)

## Apache Configuration

    <VirtualHost *:80>
     Alias /static/ /var/www/riverid/static/
     AliasMatch ^/$ /var/www/riverid/static/index.html
     WSGIDaemonProcess riverid user=riverid group=riverid threads=5
     WSGIScriptAlias / /var/www/riverid/api/wsgi.py
    </VirtualHost>

* If your application is installed in a different directory than `/var/www/riverid`, remember to modify the path accordingly.
* You need a user set up for the RiverID process to run as. In the above, we assume both the user and group will be `riverid`.