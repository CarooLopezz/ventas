from models.db import db
from datetime import datetime

class Sale(db.Model):
    __tablename__= "sales"

    id= db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    discount= db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float, nullable=False)
    items= db.relationship('SaleItem', backref='sale', cascade="all, delete-orphan")
    
    def __init__(self, client_id, date, discount, total_amount):
        self.client_id = client_id
        self.date = date
        self.discount = discount
        self.total_amount = total_amount
    
    def serialize(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'date': self.date.strftime('%Y-%m-%d'),
            'discount' : self.discount,
            'total_amount': self.total_amount,
            'items': [item.serialize() for item in self.items],


        }

class SaleItem(db.Model):
    __tablename__ = "sale_items"

    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)

    def __init__(self, sale_id, product_name, unit_price, quantity):
        self.sale_id = sale_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity
        self.subtotal = unit_price * quantity

    def serialize(self):
        return {
            'id': self.id ,
            'product_name': self.product_name ,
            'unit_price' : self.unit_price,
            'quantity' : self.quantity,
            'subtotal' : self.subtotal
        }