from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin  # , FileColumn
# from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from geoalchemy2.types import Geometry
from flask_appbuilder.security.sqla.models import User


class Sex(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class BaseObservation(Model, AuditMixin):
    id = Column(Integer, primary_key=True)
    # location = Column(Geometry(geometry_type='POINT', srid=4326))
    verified = Column(Boolean, nullable=False, default=False)
    observation_datetime = Column(DateTime(timezone=True), nullable=False)
    observer_id = Column(Integer, ForeignKey('ab_user.id'), nullable=False)
    observer = relationship(User, foreign_keys=[observer_id])
    dataset = Column(String(50))

    __mapper_args__ = {
        'polymorphic_on': dataset,
        'polymorphic_identity': 'base'
    }

    def __repr__(self):
            return "%s %s" % (self.observation_datetime.isoformat(),
                              self.observer)
