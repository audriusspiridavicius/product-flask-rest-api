import pprint
from marshmallow import INCLUDE, ValidationError, post_load, validates,fields
from init import app, db
from flask_restful import Api, Resource, marshal_with, reqparse
from flask import abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 
from schema.productschema import ProductSchema
from schema.commentschema import CommentSchema
from model.product import Product
api = Api(app)
marshmallow = Marshmallow(app)

# product_fields = {"name": fields.Raw, "description": fields.Raw, "price": fields.Float, "quantity": fields.Integer}

products_chema = ProductSchema(many=True)
class ProductApi(Resource):
    
    # @marshal_with(product_fields)
    def get(self,product_id):
        
        product = db.session.get(Product,product_id)

        return ProductSchema().dump(product) if product else abort(401,f"Product with id={product_id} was not found")
    
    def post(self):
        
        try:
           product = ProductSchema().loads(request.data)
           print(f" product type = {type(product)}")
        except ValidationError as err:
            return abort(501,err.messages)
        
        
        db.session.add(product)
        db.session.commit()
        
        return ProductSchema().dump(product)
    
    def delete(self, product_id):
        
        product = db.session.query(Product).get(product_id)
        if product:
        
            db.session.delete(product)
            db.session.commit()
            return ProductSchema().dump(product)
        else:
           return {"message": "Such product was not found"} 
    
    def put(self, product_id):
        
        product:Product = db.session.get(Product,product_id)
        
        if product:
            try:
                new_data_product:Product = ProductSchema().loads(request.data)

            except ValidationError as error:
                return abort(501,error.messages)
            
            product.name = new_data_product.name
            product.description = new_data_product.description
            product.price = new_data_product.price
            product.quantity = new_data_product.quantity

            db.session.commit()
                
            return ProductSchema().dump(product)
        else:
            return abort(500, "no such product was found")
        
    
class ProductsApi(Resource):
    def get(self):
        
        products = Product.query.all()
        
        return products_chema.dump(products)
    
class CommentApi(Resource):
    
    def post(self):
        print(request)
        # pprint(request.data)
        comment = CommentSchema().loads(request.data)        
        
        db.session.add(comment)
        db.session.commit()
        return CommentSchema().dump(comment)
        # return 0
        



api.add_resource(ProductApi,'/product/<int:product_id>','/product')
api.add_resource(ProductsApi,'/products')
api.add_resource(CommentApi,'/comment')

if __name__ == '__main__':
    app.run(port=8000, debug=True)