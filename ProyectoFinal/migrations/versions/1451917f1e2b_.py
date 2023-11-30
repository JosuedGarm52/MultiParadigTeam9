"""empty message

Revision ID: 1451917f1e2b
Revises: 85e1f7286f3d
Create Date: 2023-11-28 23:01:19.615869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1451917f1e2b'
down_revision = '85e1f7286f3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mod', schema=None) as batch_op:
        batch_op.add_column(sa.Column('linkcsv', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mod', schema=None) as batch_op:
        batch_op.drop_column('linkcsv')

    # ### end Alembic commands ###
