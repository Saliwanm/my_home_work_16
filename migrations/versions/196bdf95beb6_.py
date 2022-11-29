"""empty message

Revision ID: 196bdf95beb6
Revises: 5ff9ea75c32a
Create Date: 2022-11-21 18:15:18.370948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '196bdf95beb6'
down_revision = '5ff9ea75c32a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reset_password_uuid', sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('reset_password_uuid')

    # ### end Alembic commands ###
