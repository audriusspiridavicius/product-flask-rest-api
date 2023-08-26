from sqlalchemy import Text
from init import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String, nullable=True)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    price = db.Column(db.Float, nullable=False, default=Text("0.00"))
    
    
