from flask_appbuilder.security.sqla.manager import SecurityManager
from .views import AuthDBJWTView


class ModamaSecurityManager(SecurityManager):
    authdbview = AuthDBJWTView
