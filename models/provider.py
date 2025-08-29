# models/provider.py
from models.db import db

class Provider(db.Model):
    __tablename__ = 'provider'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone
        }
