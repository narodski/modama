from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from flask_appbuilder.security.sqla.models import User
from sqlalchemy.ext.declarative import declared_attr
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

user_organization_table = Table('ab_user_organization', Model.metadata,
                                Column('user_id', Integer,
                                       ForeignKey('ab_user.id')),
                                Column('organization_id', Integer,
                                       ForeignKey('ab_organization.id'))
                                )


class ModamaAuditMixin(AuditMixin):
    @declared_attr
    def created_by(cls):
        return relationship("MyUser",
                            primaryjoin='{}.created_by_fk == MyUser.id'.format(
                                cls.__name__), enable_typechecks=False)

    @declared_attr
    def changed_by(cls):
        return relationship("MyUser",
                            primaryjoin='{}.changed_by_fk == MyUser.id'.format(
                                cls.__name__), enable_typechecks=False)


class Organization(Model):
    __tablename__ = 'ab_organization'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return self.name


class MyUser(User):
    __tablename__ = 'ab_user'
    organizations = relationship(Organization,
                                 secondary=user_organization_table,
                                 backref='users')
