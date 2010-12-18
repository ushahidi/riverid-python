#m from django.db import models
from mongoengine.queryset import QuerySet
#m from django.contrib.auth.models import User
from mongoengine.django.auth import User

KEY_SIZE = 18
SECRET_SIZE = 32
#m
class KeyManager(QuerySet):
    '''Add support for random key/secret generation
    '''
    def generate_random_codes(self):
        key = User.objects.make_random_password(length=KEY_SIZE)
        secret = User.objects.make_random_password(length=SECRET_SIZE)

        while self.filter(key=key, secret=secret).count(): #m removed __exact on key and secret for filter            
            secret = User.objects.make_random_password(length=SECRET_SIZE)

        return key, secret


class ConsumerManager(KeyManager):
    def create_consumer(self, name, description=None, user=None):
        """
        Shortcut to create a consumer with random key/secret.
        """
        consumer, created = self.get_or_create(name=name)

        if user:
            consumer.user = user

        if description:
            consumer.description = description

        if created:
            consumer.key, consumer.secret = self.generate_random_codes()
            consumer.save()

        return consumer

    _default_consumer = None
#m
class ResourceManager(QuerySet):
    _default_resource = None

    def get_default_resource(self, name):
        """
        Add cache if you use a default resource.
        """
        if not self._default_resource:
            self._default_resource = self.get(name=name)

        return self._default_resource        

class TokenManager(QuerySet):
    #m note put generate_random_codes method inside here not to subclass from keymanager (got an issue)
    '''Add support for random key/secret generation
    '''
    def generate_random_codes(self):
        key = User.objects.make_random_password(length=KEY_SIZE)
        secret = User.objects.make_random_password(length=SECRET_SIZE)

        while self.filter(key=key, secret=secret).count(): #m removed __exact on key and secret for filter            
            secret = User.objects.make_random_password(length=SECRET_SIZE)

        return key, secret
        
    def create_token(self, consumer, token_type, timestamp, user=None):
        """
        Shortcut to create a token with random key/secret.
        """
        token = self.get_or_create(consumer=consumer, token_type=token_type, timestamp=timestamp)

        if not (token.key and token.secret):
            token.key, token.secret = self.generate_random_codes()
            token.save()

        return token
        
