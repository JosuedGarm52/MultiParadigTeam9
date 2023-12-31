"""empty message

Revision ID: d550de214e83
Revises: 
Create Date: 2023-11-02 20:21:28.596701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd550de214e83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agencia',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('num_telef', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('direccion', sa.String(length=250), nullable=True),
    sa.Column('edad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vendedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=True),
    sa.Column('apellido', sa.String(length=250), nullable=True),
    sa.Column('num_iden_ven', sa.String(length=250), nullable=True),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=True),
    sa.Column('num_telefono', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_producto', sa.String(length=250), nullable=True),
    sa.Column('valor', sa.Float(), nullable=True),
    sa.Column('categoria', sa.String(length=100), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venta')
    op.drop_table('vendedor')
    op.drop_table('cliente')
    op.drop_table('agencia')
    # ### end Alembic commands ###
