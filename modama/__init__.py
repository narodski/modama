import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
import os
from flask_migrate import Migrate

APP_DIR = os.path.dirname(__file__)

"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)

migrate = Migrate(app, db, directory=APP_DIR + '/migrate')
appbuilder = AppBuilder(app, db.session, base_template='modama_base.html')


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from modama.views import common
from modama.datasets import _datasets
