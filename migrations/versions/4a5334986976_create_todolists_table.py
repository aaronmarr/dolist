"""Create TodoLists table

Revision ID: 4a5334986976
Revises: c4cbb0f94593
Create Date: 2020-06-01 22:10:38.697211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a5334986976'
down_revision = 'c4cbb0f94593'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_todo_list_created_at'), 'todo_list', ['created_at'], unique=False)
    op.create_index(op.f('ix_todo_list_updated_at'), 'todo_list', ['updated_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_todo_list_updated_at'), table_name='todo_list')
    op.drop_index(op.f('ix_todo_list_created_at'), table_name='todo_list')
    op.drop_table('todo_list')
    # ### end Alembic commands ###