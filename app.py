from init import app, db
from flask_restful import Api, Resource
from flask import json, request, jsonify
from flask_marshmallow import Marshmallow


from model.product import Product
api = Api(app)
m = Marshmallow(app)

 
# class ProductSchema(Schema):
#     name = fields.Str()
#     description = fields.Str()
#     quantity = fields.Float()
#     price = fields.Float()
# Užduoties schema

class ProductSchema(m.Schema):
    class Meta:
        fields = ('id','name', 'description', 'quantity', 'price')


products_chema = ProductSchema(many=True)
class ProductApi(Resource):
    
    
    def get(self,id):
        
        product = Product.query.filter_by(id=id).first()
        
        return ProductSchema().jsonify(product)
    
    def post(self):
        product_dict = ProductSchema().loads(request.data)
        product = Product(**product_dict)
        
        db.session.add(product)
        db.session.commit()
        
        return ProductSchema().jsonify(product)
         
class ProductsApi(Resource):
    def get(self):
        
        products = Product.query.all()
        
        return products_chema.jsonify(products)
    


api.add_resource(ProductApi,'/product/<int:id>','/add-product')
api.add_resource(ProductsApi,'/products')





if __name__ == '__main__':
    app.run(port=8000, debug=True)