from django.conf.urls.defaults import *

urlpatterns = patterns('face.views',
    url(r'^edit$', 'edit', name='face_edit'),
    url(r'^(?P<username>([\w-]+))/$', 'detail', name='face_detail'),

    url(r'^admin/delete/$', 'delete_face', name='face_delete'),    
    url(r'^admin/active/$', 'active_face', name='face_active'), 
    url(r'^admin/admin/$', 'admin_face', name='face_admin'),     
    url(r'^admin/list/(?P<filter>([\w-]+))/$', 'list_faces_admin', name='face_list_admin'),   
)