"""10 testdb

Revision ID: 67d9b91f9376
Revises: 70f812d9b3f6
Create Date: 2024-04-11 21:00:57.615236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67d9b91f9376'
down_revision = '70f812d9b3f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ticket', schema=None) as batch_op:
        batch_op.drop_column('date_posted')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ticket', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_posted', sa.DATE(), nullable=True))

    # ### end Alembic commands ###
