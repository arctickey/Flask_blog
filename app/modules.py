from app import db

class User(db.Model):
    id = db.column(db.Integer,primary_key=True)
    username = db.column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(64),index=True,unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)