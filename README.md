= RiverID

== Debian 6.0 (Squeeze) Installation Instructions

1. Install the necessary Debian packages:  
`apt-get update`  
`apt-get install apache2 libapache2-mod-wsgi python-pip git`

2. Install the necessary Python packages:  
`pip install flask mongokit`

3. Create a user for RiverID processes to run as:  
`adduser --disabled-password --gecos "" riverid`

4. Clone the RiverID repository:  
`git clone https://github.com/ushahidi/RiverID.git /var/www/riverid`