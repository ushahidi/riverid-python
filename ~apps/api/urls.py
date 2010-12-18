from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication, OAuthAuthentication
#from piston.doc import documentation_view

from api.handlers import FaceHandler

#auth = HttpBasicAuthentication(realm='My sample API')
auth = OAuthAuthentication(realm="Test Realm")

face = Resource(handler=FaceHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^face\.(?P<emitter_format>.+)', face, name='api_face'),
)
