from marshmallow import ValidationError
from sqlalchemy import Text
from sqlalchemy.orm import validates
from init import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String, nullable=True)
    quantity = db.Column(db.Integer, default=0, nullable=False)
    price = db.Column(db.Float, nullable=False, default=Text("0.00"))
    
    
    
    @validates('name','description')
    def validate_name_length(self, key,name):
        if len(name) < 10:
            raise ValidationError(f"{key} has to be at least 10 symbols long")
        return name