"""Comments table added

Revision ID: 301ab582a2cc
Revises: dd69a4863961
Create Date: 2023-08-26 17:19:29.662836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '301ab582a2cc'
down_revision = 'dd69a4863961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('quantity',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###