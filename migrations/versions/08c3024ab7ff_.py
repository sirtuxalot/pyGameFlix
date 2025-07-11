"""empty message

Revision ID: 08c3024ab7ff
Revises: 
Create Date: 2025-06-10 16:33:57.862132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08c3024ab7ff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('consoles',
    sa.Column('console_id', sa.Integer(), nullable=False),
    sa.Column('console_name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('console_id')
    )
    op.create_table('subscriptions',
    sa.Column('subscription_id', sa.Integer(), nullable=False),
    sa.Column('subscription_name', sa.Text(), nullable=True),
    sa.Column('rentals_allowed', sa.Integer(), nullable=True),
    sa.Column('price', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('subscription_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=True),
    sa.Column('last_name', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('city', sa.Text(), nullable=True),
    sa.Column('state', sa.Text(), nullable=True),
    sa.Column('zip', sa.Integer(), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.Column('subscription_id', sa.Integer(), nullable=True),
    sa.Column('access_level', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['subscription_id'], ['subscriptions.subscription_id'], ),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('catalog',
    sa.Column('game_id', sa.Integer(), nullable=False),
    sa.Column('game_name', sa.Text(), nullable=True),
    sa.Column('console_id', sa.Integer(), nullable=True),
    sa.Column('renter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['console_id'], ['consoles.console_id'], ),
    sa.ForeignKeyConstraint(['renter_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('game_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('catalog')
    op.drop_table('users')
    op.drop_table('subscriptions')
    op.drop_table('consoles')
    # ### end Alembic commands ###
