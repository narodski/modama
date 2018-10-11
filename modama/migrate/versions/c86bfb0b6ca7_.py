"""empty message

Revision ID: c86bfb0b6ca7
Revises: 65e5f80a687b
Create Date: 2018-10-12 00:02:32.353337

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = 'c86bfb0b6ca7'
down_revision = '65e5f80a687b'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column('pawikan_general', 'alive')
    op.add_column(
        'pawikan_general',
        sa.Column('alive', sa.Enum('alive', 'dead', name='pawikanalivedeadenum'), autoincrement=False, nullable=True)
    )


def downgrade():
    op.drop_column('pawikan_general', 'alive')
    op.add_column(
        'pawikan_general',
        sa.Column('alive', sa.Enum('yes', 'no', name='pawikanyesnoenum'), autoincrement=False, nullable=True)
    )
