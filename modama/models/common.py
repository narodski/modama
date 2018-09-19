from flask_appbuilder import Model
# from flask_appbuilder.models.mixins import AuditMixin, FileColumn
# from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_appbuilder.security.sqla.models import User
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Organization(Model):
    __tablename__ = 'ab_organization'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class MyUser(User):
    organization_id = Column(Integer, ForeignKey('ab_organization.id'),
                             nullable=False)
    organization = relationship(Organization, backref='users')
