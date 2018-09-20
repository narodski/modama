from flask_appbuilder.security.sqla.manager import SecurityManager
from werkzeug.security import generate_password_hash
from .views import AuthDBJWTView, MyUserDBModelView
from ..models.common import MyUser
from flask_appbuilder import const as c
import logging
from flask import g
from modama.models.common import Organization

log = logging.getLogger(__name__)


class ModamaSecurityManager(SecurityManager):
    authdbview = AuthDBJWTView
    user_model = MyUser
    userdbmodelview = MyUserDBModelView

    def add_user(self, username, first_name, last_name, email,
                 role, organizations, password='', hashed_password=''):
        try:
            user = self.user_model()
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.active = True
            user.roles.append(role)
            if hashed_password:
                user.password = hashed_password
            else:
                user.password = generate_password_hash(password)
            user.organizations = organizations
            self.get_session.add(user)
            self.get_session.commit()
            log.info(c.LOGMSG_INF_SEC_ADD_USER.format(username))
            return user
        except Exception as e:
            print(c.LOGMSG_ERR_SEC_ADD_USER.format(str(e)))
            log.error(c.LOGMSG_ERR_SEC_ADD_USER.format(str(e)))
            return False

    def get_admin_org(self):
        return self.get_session.query(Organization).filter_by(name='Admins')\
            .first()

    def my_organizations(self):
        admin_org = self.get_admin_org()
        if admin_org in g.user.organizations:
            return self.get_session.query(Organization).all()
        else:
            return g.user.organizations
