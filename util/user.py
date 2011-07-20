class User(object):
    def __init__(self, db):
        self.db = db

    def delete(self, email):
        self.db.user.remove({'email': email})

    def get(self, email):
        self.db.user.find_one({'email': email})

    def insert(self, email, **values):
        values['email'] = email
        self.db.user.insert(values)

    def update(self, email, **values):
        self.db.user.update({'email': email}, {'$set': values})
