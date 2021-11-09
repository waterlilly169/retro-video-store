"""change chars in zip

Revision ID: fc92d7e3f6a3
Revises: e9918e2a35c4
Create Date: 2021-11-08 15:47:01.546747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc92d7e3f6a3'
down_revision = 'e9918e2a35c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('postal_code', sa.String(length=50), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    # ### end Alembic commands ###