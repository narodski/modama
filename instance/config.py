import os
from flask_appbuilder.security.manager import AUTH_OID, AUTH_REMOTE_USER, AUTH_DB, AUTH_LDAP, AUTH_OAUTH
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = "W$|=&TXWAp+_Fm-ovXE!kg*Jges/2+K&6&m>F#(}6c1W(Ln4^6ycI@GwBN1L#kCu@RZBb)4O-O2R\rq?eO5OzO3-y5-R:dN'9\Q"
SQLALCHEMY_DATABASE_URI = 'postgresql:///modama'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

SESSION_TYPE = 'filesystem'

JWT_SECRET = "?gAeF8ruo=_[_/u}]aisOo?.8O~x7{PUPm=w,&s[MY\?QzeHcV_NDvriiee153NSlr]^}X(s1/Kd*_Y:h@<S0C25NfoK/2*zzB."

AUTH_TYPE = AUTH_DB

# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + '/modama/static/uploads/'

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + '/modama/static/uploads/'

# The image upload url, when using models with images
IMG_UPLOAD_URL = '/static/uploads/'
# Setup image size default is (300, 200, True)
# IMG_SIZE = (300, 200, True)

# Theme configuration
# these are located on static/appbuilder/css/themes
# you can create your own and easily use them placing them on the same dir
# structure to override
# APP_THEME = 'modama.css'
# APP_THEME = "bootstrap-theme.css"  # default bootstrap
# APP_THEME = "cerulean.css"
# APP_THEME = "amelia.css"
# APP_THEME = "cosmo.css"
# APP_THEME = "cyborg.css"
# APP_THEME = "flatly.css"
# APP_THEME = "journal.css"
# APP_THEME = "readable.css"
# APP_THEME = "simplex.css"s
# APP_THEME = "slate.css"
APP_THEME = "spacelab.css"
# APP_THEME = "united.css"
# APP_THEME = "yeti.css"
