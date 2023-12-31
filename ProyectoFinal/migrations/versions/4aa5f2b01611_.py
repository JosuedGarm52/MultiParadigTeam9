"""empty message

Revision ID: 4aa5f2b01611
Revises: 
Create Date: 2023-11-24 16:51:51.025351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aa5f2b01611'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cuenta',
    sa.Column('id_cuenta', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('primer_nombre', sa.String(length=255), nullable=False),
    sa.Column('otros_nombres', sa.String(length=255), nullable=True),
    sa.Column('primer_apellido', sa.String(length=255), nullable=False),
    sa.Column('segundo_apellido', sa.String(length=255), nullable=True),
    sa.Column('fecha_nacimiento', sa.DateTime(), nullable=False),
    sa.Column('telefono', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id_cuenta')
    )
    op.create_table('foto',
    sa.Column('id_foto', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('link', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id_foto')
    )
    op.create_table('admin',
    sa.Column('id_admin', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cuenta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cuenta_id'], ['cuenta.id_cuenta'], ),
    sa.PrimaryKeyConstraint('id_admin')
    )
    op.create_table('mod',
    sa.Column('id_mod', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cuenta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cuenta_id'], ['cuenta.id_cuenta'], ),
    sa.PrimaryKeyConstraint('id_mod')
    )
    op.create_table('perfil',
    sa.Column('usuario', sa.String(length=255), nullable=False),
    sa.Column('pais_origen', sa.String(length=255), nullable=False),
    sa.Column('genero', sa.String(length=255), nullable=False),
    sa.Column('busqueda', sa.String(length=255), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.Column('estado_civil', sa.String(length=255), nullable=False),
    sa.Column('cuenta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cuenta_id'], ['cuenta.id_cuenta'], ),
    sa.PrimaryKeyConstraint('usuario')
    )
    op.create_table('documento',
    sa.Column('usuario_name', sa.String(length=255), nullable=False),
    sa.Column('link', sa.String(length=255), nullable=False),
    sa.Column('isaprobado', sa.Boolean(), nullable=False),
    sa.Column('tipo', sa.String(length=255), nullable=False),
    sa.Column('mod_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mod_id'], ['mod.id_mod'], ),
    sa.ForeignKeyConstraint(['usuario_name'], ['perfil.usuario'], ),
    sa.PrimaryKeyConstraint('usuario_name')
    )
    op.create_table('mensaje',
    sa.Column('id_mensaje', sa.Integer(), nullable=False),
    sa.Column('usuario_rem', sa.String(length=255), nullable=False),
    sa.Column('usuario_dest', sa.String(length=255), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('contenido', sa.String(), nullable=False),
    sa.Column('isvisible', sa.Boolean(), nullable=False),
    sa.Column('isread', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['usuario_dest'], ['perfil.usuario'], ),
    sa.ForeignKeyConstraint(['usuario_rem'], ['perfil.usuario'], ),
    sa.PrimaryKeyConstraint('id_mensaje')
    )
    op.create_table('perfil_foto',
    sa.Column('usuario_name', sa.Integer(), nullable=False),
    sa.Column('foto_id', sa.Integer(), nullable=False),
    sa.Column('isperfil', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['foto_id'], ['foto.id_foto'], ),
    sa.ForeignKeyConstraint(['usuario_name'], ['perfil.usuario'], ),
    sa.PrimaryKeyConstraint('usuario_name', 'foto_id')
    )
    op.create_table('chat',
    sa.Column('mensaje_id', sa.Integer(), nullable=False),
    sa.Column('mod_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mensaje_id'], ['mensaje.id_mensaje'], ),
    sa.ForeignKeyConstraint(['mod_id'], ['mod.id_mod'], ),
    sa.PrimaryKeyConstraint('mensaje_id', 'mod_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('chat')
    op.drop_table('perfil_foto')
    op.drop_table('mensaje')
    op.drop_table('documento')
    op.drop_table('perfil')
    op.drop_table('mod')
    op.drop_table('admin')
    op.drop_table('foto')
    op.drop_table('cuenta')
    # ### end Alembic commands ###
