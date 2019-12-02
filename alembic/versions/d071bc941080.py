"""empty message

Revision ID: d071bc941080
Revises: 
Create Date: 2019-06-24 02:06:26.225786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd071bc941080'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('log_id', sa.Integer(), nullable=False),
    sa.Column('log_name', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.Column('log_status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('log_id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('entrypoint', sa.String(), nullable=True),
    sa.Column('base_url', sa.String(), nullable=True),
    sa.Column('doc_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('detail',
    sa.Column('detail_id', sa.Integer(), nullable=False),
    sa.Column('detail_name', sa.String(), nullable=False),
    sa.Column('detail_description', sa.String(), nullable=True),
    sa.Column('log_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['log_id'], ['log.log_id'], ),
    sa.PrimaryKeyConstraint('detail_id', 'detail_name')
    )
    op.create_table('endpoint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('label', sa.String(), nullable=True),
    sa.Column('template', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('parameters', sa.String(), nullable=True),
    sa.Column('service_name', sa.String(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('endpoints_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('service_name', sa.String(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('filter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('similar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tag')
    op.drop_table('similar')
    op.drop_table('filter')
    op.drop_table('endpoints_list')
    op.drop_table('endpoint')
    op.drop_table('detail')
    op.drop_table('service_list')
    op.drop_table('service')
    op.drop_table('log')
    # ### end Alembic commands ###