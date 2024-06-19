"""fixed_db_inconsistency

Revision ID: c61830e22bf8
Revises: 368673a367ac
Create Date: 2024-06-03 12:39:28.387287

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c61830e22bf8'
down_revision = '368673a367ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('layout', 'data',
                    existing_type=mysql.MEDIUMTEXT(),
                    type_=sa.TEXT(),
                    existing_nullable=False)
    op.alter_column('organization_bi', 'meta',
                    existing_type=sa.TEXT(),
                    nullable=False)
    op.alter_column('organization_gemini', 'stats',
                    existing_type=mysql.MEDIUMTEXT(),
                    type_=sa.TEXT(),
                    existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('layout', 'data',
                    existing_type=sa.TEXT(),
                    type_=mysql.MEDIUMTEXT(),
                    existing_nullable=False)
    op.alter_column('organization_bi', 'meta',
                    existing_type=sa.TEXT(),
                    nullable=True)
    op.alter_column('organization_gemini', 'stats',
                    existing_type=sa.TEXT(),
                    type_=mysql.MEDIUMTEXT(),
                    existing_nullable=True)
    # ### end Alembic commands ###
