
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True, nullable = False)
    access_token = db.Column(db.String(500), nullable = False)
    refresh_token = db.Column(db.String(500), nullable = False)
