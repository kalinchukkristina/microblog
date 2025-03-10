"""followers

Revision ID: 1898cbb8852e
Revises: a524776a1ebb
Create Date: 2023-11-08 21:42:09.652208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1898cbb8852e'
down_revision = 'a524776a1ebb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    info={'bind_key': None}
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
