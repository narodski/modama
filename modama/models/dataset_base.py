from flask_appbuilder import Model
from .common import ModamaAuditMixin
# from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Sex(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Region(Model):
    id = Column(Integer, primary_key=True)
    psgc = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return str(self.name)


class Province(Model):
    id = Column(Integer, primary_key=True)
    psgc = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    province = relationship(Region, backref='provinces')

    def __repr__(self):
        return str(self.name)


class Municipality(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    psgc = Column(String, nullable=False, unique=True)
    province_id = Column(Integer, ForeignKey('province.id'), nullable=False)
    province = relationship(Province, backref='municipalities')

    def __repr__(self):
        return "{}, {}".format(self.name, self.municipality)


class Barangay(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    psgc = Column(String, nullable=False, unique=True)
    municipality_id = Column(Integer, ForeignKey('municipality.id'),
                             nullable=False)
    municipality = relationship(Municipality, backref='barangays')

    def __repr__(self):
        return "{}, {}, {}".format(self.name, self.municipality.name,
                                   self.municipality.province.name)


class BaseObservation(Model, ModamaAuditMixin):
    id = Column(Integer, primary_key=True)
    # location = Column(Geometry(geometry_type='POINT', srid=4326))
    verified = Column(Boolean, default=False)
    observation_datetime = Column(DateTime(timezone=True), nullable=False)
    report_id = Column(UUID(as_uuid=True), unique=True, nullable=False,
                       default=uuid.uuid1())
    device_id = Column(String(50), unique=False, nullable=False,
                       default='webinterface')
    dataset = Column(String(50))

    __mapper_args__ = {
        'polymorphic_on': dataset,
        'polymorphic_identity': 'base'
    }

    def __repr__(self):
            return "%s %s" % (self.observation_datetime.isoformat(),
                              self.observer)
