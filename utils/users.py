class Users(object):
    def __init__(self, db):
        self.db = db

    def delete(self, email):
        self.db.users.remove({'email': email})

    def get(self, email):
        self.db.users.find_one({'email': email})

    def insert(self, email, **values):
        values['email'] = email
        self.db.users.insert(values)

    def update(self, email, **values):
        self.db.users.update({'email': email}, {'$set': values})
