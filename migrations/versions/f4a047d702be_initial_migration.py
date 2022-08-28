"""Initial migration.

Revision ID: f4a047d702be
Revises: 
Create Date: 2022-08-27 17:30:57.759405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4a047d702be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('informacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('nome', sa.String(length=45), nullable=True),
    sa.Column('imagem', sa.String(length=2048), nullable=True),
    sa.Column('hoje', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('informacao')
    # ### end Alembic commands ###