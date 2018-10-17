"""empty message

Revision ID: 2f2c0523320b
Revises: f8e4603be726
Create Date: 2018-10-17 11:53:44.746522

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = '2f2c0523320b'
down_revision = 'f8e4603be726'
branch_labels = None
depends_on = None


def upgrade():
    engine = op.get_bind()
    md = sa.MetaData(bind=engine)
    tab = sa.Table('pawikan_encounter_type', md, autoload=True)
    engine.execute(tab.insert().values(name="Nesting"))


def downgrade():
    engine = op.get_bind()
    md = sa.MetaData(bind=engine)
    tab = sa.Table('pawikan_encounter_type', md, autoload=True)
    engine.execute(tab.delete().where(tab.c.name == "Nesting"))
