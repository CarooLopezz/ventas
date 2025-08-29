from models.db import db

class Category (db.Model):
    __tablename__='category'
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25), nullable=False)
    description=db.Column(db.String(20), unique=True, nullable=False)
    
    def __init__(self,name,description):
        self.name=name
        self.description=description
        
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            'description':self.description
        }