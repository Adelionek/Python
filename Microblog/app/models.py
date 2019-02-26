from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# user class inhereits from db.Model

# snake case, so User will be named user. Can add attribute __tablename_


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

# one to many relation. posts variable by 'one' side. 1st argument is 'many' table
# author - we will define an author in each added post

    def __repr__(self):
        return '<User {}>'.format(self.username)
# repr tells Python how to print obj of this class

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # added author attribute

    def __repr__(self):
        return '<Post {}>'.format(self.body)
