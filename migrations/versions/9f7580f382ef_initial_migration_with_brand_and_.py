"""Initial migration with Brand and Manufacturer models

Revision ID: 9f7580f382ef
Revises: 
Create Date: 2024-10-19 17:13:55.407936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f7580f382ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logo', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('internal_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('internal_id')
    )
    op.create_table('manufacturer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('country', sa.String(length=80), nullable=True),
    sa.Column('certificates', sa.String(length=255), nullable=True),
    sa.Column('internal_id', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('internal_id')
    )
    op.create_table('association',
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturer.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('manufacturer')
    op.drop_table('brand')
    # ### end Alembic commands ###
