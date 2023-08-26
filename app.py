from pprint import pprint
from marshmallow import ValidationError
from init import app, db
from flask_restful import Api, Resource, marshal_with, fields, reqparse
from flask import abort, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow 


from model.product import Product
api = Api(app)
marshmallow = Marshmallow(app)

product_fields = {"name": fields.Raw, "description": fields.Raw, "price": fields.Float, "quantity": fields.Integer}

# class ProductSchema(marshmallow.Schema):
#     class Meta:
#         fields = ('id','name', 'description', 'quantity', 'price')

class ProductSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Product


products_chema = ProductSchema(many=True)
class ProductApi(Resource):
    
    @marshal_with(product_fields)
    def get(self,product_id):
        
        product = db.session.query(Product).get(product_id)

        return product if product else abort(401,f"Product with id={product_id} was not found")
    
    def post(self):
        
        try:
           product_dict = ProductSchema().loads(request.data)
           product = Product(**product_dict)
        except ValidationError as err:
            return abort(501,err.messages)
        
        
        
        db.session.add(product)
        db.session.commit()
        
        return ProductSchema().jsonify(product)
    
    def delete(self, product_id):
        
        product = db.session.query(Product).get(product_id)
        if product:
        
            db.session.delete(product)
            db.session.commit()
            return ProductSchema().jsonify(product)
        else:
           return {"message": "Such product was not found"} 
    
    def put(self, product_id):
        
        product:Product = db.session.query(Product).get(product_id)
        
        if product:

            product_data_parser = reqparse.RequestParser()
            product_data_parser.add_argument('name', type=str, help='name message error')
            product_data_parser.add_argument('description', type=str, help='description message')
            product_data_parser.add_argument('quantity', type=int, help='quantity message')
            product_data_parser.add_argument('price', type=float, help='Invalid field!')
        
            update_product_args = product_data_parser.parse_args()
            
            product.description = update_product_args["description"]
            product.price = update_product_args["price"]
            
            db.session.commit()
                
            return ProductSchema().jsonify(product)
        else:
            return abort(500, "no such product was found")
        
    
class ProductsApi(Resource):
    def get(self):
        
        products = Product.query.all()
        
        return products_chema.jsonify(products)
    

api.add_resource(ProductApi,'/product/<int:product_id>','/product')
api.add_resource(ProductsApi,'/products')


if __name__ == '__main__':
    app.run(port=8000, debug=True)