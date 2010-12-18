from django.conf.urls.defaults import *

urlpatterns = patterns('key.views',
    url(r'^add/$', 'add_consumer', name='key_add'),
    url(r'^delete/$', 'delete_consumer', name='key_delete'),
    url(r'^edit/(\w+)/$', 'edit_consumer', name='key_edit'),
    url(r'^list/$', 'list_consumers', name='key_list'), 
    url(r'^tokens/$', 'list_tokens', name='key_tokens'), 
    
    url(r'^admin/delete/$', 'delete_consumer_admin', name='key_delete_admin'),   
    url(r'^admin/status/$', 'status_consumer', name='key_status'),     
    url(r'^admin/list/(?P<status>([\w-]+))/$', 'list_consumers_admin', name='key_list_admin'), 
)