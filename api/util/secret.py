from hashlib import sha512
from random import choice
from string import ascii_letters, digits

class Secret(object):
    @staticmethod
    def hash(string, salt):
        return sha512(salt + string).hexdigest()

    @staticmethod
    def generate(length=64):
        characters = ascii_letters + digits
        return ''.join([choice(characters) for i in range(length)])