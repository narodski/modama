from flask_appbuilder import Model
from .common import ModamaAuditMixin
# from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Sex(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class BaseObservation(Model, ModamaAuditMixin):
    id = Column(Integer, primary_key=True)
    # location = Column(Geometry(geometry_type='POINT', srid=4326))
    verified = Column(Boolean, default=False)
    observation_datetime = Column(DateTime(timezone=True), nullable=False)
    report_id = Column(UUID(as_uuid=True), unique=True, nullable=False,
                       default=uuid.uuid1())
    device_id = Column(String(50), unique=False, nullable=False,
                       default='webinterface')
    reporter = Column(String(255), nullable=False)
    reporter_contact = Column(String(255), nullable=False)
    dataset = Column(String(50))

    __mapper_args__ = {
        'polymorphic_on': dataset,
        'polymorphic_identity': 'base'
    }

    def __repr__(self):
            return "%s %s" % (self.observation_datetime.isoformat(),
                              self.observer)
