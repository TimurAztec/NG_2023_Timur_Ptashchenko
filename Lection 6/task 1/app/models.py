from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(256))

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer)
    username = db.Column(db.String(64))
    message = db.Column(db.String(256))
    messageDate = db.Column(db.DateTime)

class Sessions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    username = db.Column(db.String(64))
    expires = db.Column(db.DateTime, nullable=False)