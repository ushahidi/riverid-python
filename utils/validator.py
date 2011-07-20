from re import match, IGNORECASE

class Validator(object):
    @staticmethod
    def email(string):
        if match(r'(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)', string, IGNORECASE) == None:
            raise Exception('Please provide a valid email address.')

    @staticmethod
    def password(string):
        if not 8 <= len(string) <= 128:
            raise Exception('Please provide a password between 8 and 128 characters in length.')

    @staticmethod
    def session(string):
        if match(r'^[a-zA-Z0-9]{128}$', string) == None:
            raise Exception('Please provide a valid session identifier.')

    @staticmethod
    def token(string):
        if match(r'^[a-zA-Z0-9]{16}$', string) == None:
            raise Exception('Please provide a valid token.')
