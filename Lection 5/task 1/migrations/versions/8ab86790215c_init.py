"""Init

Revision ID: 8ab86790215c
Revises: 
Create Date: 2023-11-21 21:14:35.875596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ab86790215c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('message', sa.String(length=256), nullable=True),
    sa.Column('messageDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('messages')
    # ### end Alembic commands ###
