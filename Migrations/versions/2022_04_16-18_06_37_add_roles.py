"""Add roles

Revision ID: 45ddc843a0cf
Revises: 9190790ddd76
Create Date: 2022-04-16 18:06:37.697486

"""
from alembic import op
import sqlalchemy as sa
from Tables import Role


# revision identifiers, used by Alembic.
revision = '45ddc843a0cf'
down_revision = '9190790ddd76'
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