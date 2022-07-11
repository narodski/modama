import logging
import logging.config
from flask import Flask
from flask_appbuilder import SQLA, AppBuilder
import os
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_session import Session
from modama.security.manager import ModamaSecurityManager
from flask_cors import CORS
from sqlalchemy import orm
from sqlalchemy_continuum import make_versioned
from .security.views import OrganizationView
from flask_babel import lazy_gettext as _
import jinja2

APP_DIR = os.path.dirname(__file__)

"""
 Logging configuration
"""
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
log = logging.getLogger()
log.setLevel(logging.DEBUG)

make_versioned(user_cls=None)
app = Flask(__name__)
app.config.from_object('config')

try:
    from instance import config
    log.info("Loading custom config")
    d = dict([(k, v) for k, v in config.__dict__.items()
              if not k.startswith('_')])
    app.config.update(d)
except ImportError as e:
    log.info("No custom config found: {}".format(e))
    pass
logconfig = os.path.abspath(os.path.join(APP_DIR, '..', 'instance', 'log.ini'))
print('Checking for {}'.format(logconfig))
if os.path.exists(logconfig):
    logging.config.fileConfig(logconfig)
else:
    print('using default log config')

log.info("Running in debug mode: {}".format(app.debug))

if app.debug:
    cors = CORS(app)


#@jinja2.contextfunction
@jinja2.pass_context
def get_context(c):
    return c


app.jinja_env.globals['context'] = get_context
app.jinja_env.globals['callable'] = callable

sess = Session(app)
db = SQLA(app)

socketio = SocketIO(app, manage_session=False, message_queue='redis://',
                    ping_timeout=300)

migrate = Migrate(app, db, directory=APP_DIR + '/migrate')
appbuilder = AppBuilder(app, db.session, base_template='modama_base.html',
                        security_manager_class=ModamaSecurityManager)


appbuilder.add_view(OrganizationView, "List Organizations",
                    icon="fa-group", label=_("List Organizations"),
                    category='Security', category_icon="fa-cogs",
                    category_label=_("Security"))


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
from modama.views import upload
orm.configure_mappers()
appbuilder.sm.get_session.close()
