Overview
--------
TBC

Change Log
----------

* v0.1.0 - Initial stable release of the software


Dependencies
------------
# database:
	
mongodb (download from mongodb.org the stable version)
quickstart: http://www.mongodb.org/display/DOCS/Quickstart+OS+X

# python stuff:
	
python 2.6+ (if python 2.5, please install simplejson)
django 1.2+
pymongo 1.7+
	
(can use "easy_install package_name" for easy installation )

other dependencies are loaded at runtime and can be found in
~apps and ~libs directories

above dependencies can be downloaded and safely put in 
~libs directory

Instructions
-------------------------
# settings.py:
	
if mongodb has username and password
update "mongoengine.connect()" in settings.py
	
# run django as standard:

Please note that mongodb must be running before django
type 'mongod' in terminal
	
cd into riverid folder
type 'python manage.py runserver'
	
RiverID then is running at http://127.0.0.1:8000
	
# fishing for fun

to add initial data:
go to http://127.0.0.1:8000/feedfish (only if there is no user)
	
then login with user/user or admin/admin or dev/dev (username/password)
		
to clear data:
go to http://127.0.0.1:8000/killoil (need admin access)
	
# testing oauth

cd into riverid folder
type 'python oauth_client.py'
	
just following prompts in the terminal
	
in oauth_client.py API key and secret are preconfigured based on
the initial key added in by "feeding fish"
	
if you want to test with other combinations, please change accordingly
	
# dev notes

search for #m instances for modificaitons, to-dos and notes
	
# thanks tons to 

Harry Marr (http://hmarr.com) of MongoEngine and for great base layout
Jesper Noehr (http://noehr.org/) of Django Piston
Django Team
MongoDB Team

Ushahidi, Swift & Google for this opportunity
	
	my eldest youngest sister and my parents