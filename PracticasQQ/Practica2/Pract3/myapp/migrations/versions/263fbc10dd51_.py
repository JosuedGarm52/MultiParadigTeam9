"""empty message

Revision ID: 263fbc10dd51
Revises: 
Create Date: 2023-11-01 22:28:04.202539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '263fbc10dd51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cliente')
    # ### end Alembic commands ###
