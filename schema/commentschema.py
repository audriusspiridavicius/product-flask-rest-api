from model.comment import Comment

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import validates, post_load, post_dump, fields


class OnlyCommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        include_relationships = True
        include_fk = True
        include_relationships = False
    product_id = fields.Integer(required=True)
    
    @post_load
    def create_comment(self, data,**kwargs)-> Comment:
        return Comment(**data)
    
    
    
class CommentSchema(OnlyCommentSchema):
    class Meta:
   
        model = Comment
        include_relationships = True
        include_fk = True
    product = fields.Nested("ProductSchema",exclude=("comments",))
    

    

