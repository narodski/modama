import logging
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
import os
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_session import Session
from modama.security.manager import ModamaSecurityManager
from flask_cors import CORS

APP_DIR = os.path.dirname(__file__)

"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
log = logging.getLogger()
log.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')

try:
    from instance import config
    log.info("Loading custom config")
    d = dict([(k, v) for k, v in config.__dict__.items()
              if not k.startswith('_')])
    app.config.update(d)
except Exception as e:
    log.info("No custom config found: {}".format(e))
    pass

log.info("Running in debug mode: {}".format(app.debug))

if app.debug:
    cors = CORS(app)

sess = Session(app)
db = SQLA(app)
socketio = SocketIO(app, manage_session=False)

migrate = Migrate(app, db, directory=APP_DIR + '/migrate')
appbuilder = AppBuilder(app, db.session, base_template='modama_base.html',
                        security_manager_class=ModamaSecurityManager)


@appbuilder.sm.lm.request_loader
def load_user_from_token(request):
    user = appbuilder.sm.auth_view.getUserFromAuthHeader()
    if user is not None:
        log.debug("Got user from header: {}".format(user))
        return user
    user = appbuilder.sm.auth_view.getUserFromCookie()
    log.debug("Got user from cookie: {}".format(user))
    return user


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
from modama import datasets
from modama import sockets
