"""Add roles

Revision ID: baf6628bff12
Revises: 4f7c8c1aef14
Create Date: 2022-04-19 22:37:31.832612

"""
from alembic import op
import sqlalchemy as sa
from Tables import Role


# revision identifiers, used by Alembic.
revision = 'baf6628bff12'
down_revision = '4f7c8c1aef14'
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
