
from marshmallow import ValidationError, validates, fields, post_load
from model.product import Product
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema




class ProductSchema(SQLAlchemyAutoSchema):
    
    class Meta:
        model = Product
        # load_instance = True
        include_relationships = True
        # strict = True
        # skip_on_field_errors=False
        # # INCLUDE: pass those keys/values as is, with no validation performed
        # unknown = INCLUDE
        # postprocess = True
        # sqla_session = db.session
    quantity = fields.Integer(load_default=0, dump_default=0)    
    comments = fields.List(fields.Nested("CommentSchema", only=("id", "comment","date_created")))    
    @post_load
    def create_product(self, data,**kwargs)-> Product:
        return Product(**data)
    
    @validates('name')
    def validate_name(self,value):
        if not value:
            raise ValidationError(f"missing value for column name")
        if len(value) < 10:
            raise ValidationError(f"name has to be at least 10 symbols long")
        return value
    
    # @validates('name')
    # def validate_name_length(self,value):
    #     if not value:
    #         raise ValidationError(f"missing value for column name")
    #     return value
    
    @validates('price')
    def validate_less_zero(self, value):
        if value:
            if value < 0:
                raise ValidationError(f"price ({value}) value cannot be less than zero")
        return value
    
    @validates('quantity')
    def validate_quantity(self, value):
        print(f" quantity value {value}")
        if value:
            if value < 0:
                raise ValidationError(f"quantity ({value}) value cannot be less than zero")
        
            return value
        else:
            return 0





    