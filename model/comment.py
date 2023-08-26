from init import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String,nullable=False)
    date_created = db.Column(db.String, 
                             nullable=False,
                             default=datetime.now().
                             strftime("%Y-%m-%d %H:%M:%S"))
    product_id = db.Column(db.Integer,
                           db.ForeignKey('product.id'))

    product = db.relationship('Product',
                              backref="comments")