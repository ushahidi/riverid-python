from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$','direct_to_template', {'name': 'home', 'template': 'pages/home.html'}, name='home'),
    url(r'^api/about/$','direct_to_template', {'name': 'api', 'template': 'pages/api.html'}, name='api'),
    
    #m to-do check why login_required decorator is directing to this place
    #m (r'^accounts/login/$', 'redirect_to', {'url': '/account/login/', 'permanent': True}),
)

urlpatterns += patterns('',
	(r'^accounts/', include('registration.backends.default.urls')),
    (r'^api/', include('api.urls')),
    
    # versioning of api is pretty easy, though old handlers need to work with the new data "schema"
    #(r'^api/0.01', include('api.urls')),
    
    (r'^profile/', include('face.urls')),
    (r'^apikey/', include('key.urls')),	
)

urlpatterns += patterns('piston.authentication',
    url(r'^oauth/request_token/$','oauth_request_token', name='oauth_request_token'),
    url(r'^oauth/authorize/$','oauth_user_auth', name='oauth_user_auth'),
    url(r'^oauth/access_token/$','oauth_access_token', name='oauth_access_token'),
)

#m fish for fun (mongoengine doesn't support django fixtures, so here we are)
urlpatterns += patterns('fish.views',
    url(r'^feedfish/$','feedfish', name='fish_feedfish'),
    url(r'^killoil/$','killoil', name='fish_killoil'),
)

if settings.DEBUG:
    # make sure to serve static folder on django dev server
    urlpatterns += patterns('', 
        (r'^' + settings.MEDIA_URL.lstrip('/') + r'(.*)$', 
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )