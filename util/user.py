class User(object):
    def __init__(self, db):
        self.db = db

    def delete(self, email):
        self.db.user.remove({'email': email})

    def exists(self, email):
        return self.db.user.find_one({'email': email}) != None

    def get(self, email):
        user = self.db.user.find_one({'email': email})
        if not user:
            raise Exception('The email address does not appear to be registered.')
        return user

    def insert(self, email, **values):
        values['email'] = email
        self.db.user.insert(values)

    def update(self, email, **values):
        self.db.user.update({'email': email}, {'$set': values})
