from flask_appbuilder.security.sqla.manager import SecurityManager
from werkzeug.security import generate_password_hash
from .views import AuthDBJWTView, MyUserDBModelView
from ..models.common import MyUser, Organization
from flask_appbuilder import const as c
import logging

log = logging.getLogger(__name__)


class ModamaSecurityManager(SecurityManager):
    authdbview = AuthDBJWTView
    user_model = MyUser
    userdbmodelview = MyUserDBModelView

    def add_user(self, username, first_name, last_name, email,
                 role, organization, password='', hashed_password=''):
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
            user.organization = organization
            self.get_session.add(user)
            self.get_session.commit()
            log.info(c.LOGMSG_INF_SEC_ADD_USER.format(username))
            return user
        except Exception as e:
            print(c.LOGMSG_ERR_SEC_ADD_USER.format(str(e)))
            log.error(c.LOGMSG_ERR_SEC_ADD_USER.format(str(e)))
            return False
