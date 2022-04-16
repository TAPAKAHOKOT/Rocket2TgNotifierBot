"""Add roles

Revision ID: 8395343a49e7
Revises: a067fa177d6e
Create Date: 2022-04-16 18:59:00.285918

"""
from alembic import op
import sqlalchemy as sa
from Tables import Role, roles


# revision identifiers, used by Alembic.
revision = '8395343a49e7'
down_revision = 'a067fa177d6e'
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
       
