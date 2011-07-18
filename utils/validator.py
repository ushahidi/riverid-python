import re

class Validator(object):
    @staticmethod
    def password(string):
        if not 8 <= len(string) <= 128:
            raise Exception('Please provide a password between 8 and 128 characters in length.')

    @staticmethod
    def email(string):
        if re.match(r'(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)', string, re.IGNORECASE) == None:
            raise Exception('Please provide a valid email address.')
