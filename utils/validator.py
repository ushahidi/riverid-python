import re

class Validtor(object):
    def password(string):
        if 8 < len(string) < 100:
            raise Exception('Please provide a password between 8 and 100 characters in length.')

    def email(string):
        if re.match(r'(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)', string, re.IGNORECASE) == None:
            raise Exception('Please provide a valid email address.')
