"""Add roles

Revision ID: 8a7fc0b5c794
Revises: 4c45ee24ffea
Create Date: 2022-04-17 17:42:52.668221

"""
from alembic import op
import sqlalchemy as sa
from Tables import Role


# revision identifiers, used by Alembic.
revision = '8a7fc0b5c794'
down_revision = '4c45ee24ffea'
branch_labels = None
depends_on = None

roles_table = Role.__table__

def upgrade():
    op.execute(
        roles_table.insert().values([
            {
                'role': 'root'
            },
            {
                'role': 'admin'
            }
        ])
    )
def downgrade():
    op.execute(
        roles_table.delete()
    )