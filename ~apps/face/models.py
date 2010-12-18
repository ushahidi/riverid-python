from django.db.models import permalink

from mongoengine import *
from mongoengine.django.auth import User

class Face(Document):
    user = ReferenceField(User)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)
    about = StringField()
    
    def __unicode__(self):
        return self.user.username
    
    @permalink
    def get_absolute_url(self):
        return ('face_detail', None, {'username': self.user.username})
