from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from modama.models.dataset_base import BaseObservation, Sex
from flask_appbuilder.models.mixins import ImageColumn, AuditMixin
from modama.models.common import ModamaAuditMixin
from modama.utils import make_image
from flask_appbuilder.filemanager import ImageManager
from flask import url_for
from geoalchemy2 import Geometry


class PawikanStrandingPicture(Model, ModamaAuditMixin):
    id = Column(Integer, primary_key=True)
    picture = Column(ImageColumn(size=(2048, 2048, False),
                                 thumbnail_size=(800, 800, True)))
    stranding_id = Column(Integer, ForeignKey('pawikan_stranding.id'),
                          nullable=False)
    stranding = relationship('PawikanStranding', backref='pictures')

    def picture_img(self):
        im = ImageManager()
        alt = str(self.stranding)
        link_url = url_for('PawikanStrandingPictureView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url(self.picture), link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def picture_img_thumbnail(self):
        im = ImageManager()
        alt = str(self.stranding)
        link_url = url_for('PawikanStrandingPictureView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url_thumbnail(self.picture),
                              link_url, alt)
        else:
            return make_image(None, link_url, alt)


class PawikanStrandingSpecies(Model):
    id = Column(Integer, primary_key=True)
    genus = Column(String(255), nullable=False)
    species = Column(String(255), nullable=False)
    common_name = Column(String(255))
    description = Column(Text)
    picture = Column(ImageColumn(size=(800, 800, True),
                                 thumbnail_size=(100, 100, True)))

    def picture_img(self):
        im = ImageManager()
        alt = str(self)
        link_url = url_for('PawikanStrandingSpeciesView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url(self.picture), link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def picture_img_thumbnail(self):
        im = ImageManager()
        alt = str(self)
        link_url = url_for('PawikanStrandingSpeciesView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url_thumbnail(self.picture),
                              link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def __repr__(self):
        if self.common_name is not None:
            return self.common_name
        else:
            return "%s %s" % (self.genus, self.species)


class PawikanStranding(BaseObservation):
    __versioned__ = {}

    id = Column(Integer, ForeignKey('base_observation.id'), primary_key=True)
    species_id = Column(Integer, ForeignKey('pawikan_stranding_species.id'),
                        nullable=False)
    species = relationship(PawikanStrandingSpecies, backref='strandings')
    ccl = Column(Integer)
    sex_id = Column(Integer, ForeignKey('sex.id'))
    sex = relationship(Sex)
    location = Column(Geometry(geometry_type='POINT', srid=4326))

    @property
    def num_pictures(self):
        return len(self.pictures)

    __mapper_args__ = {
        'polymorphic_identity': 'pawikan_stranding'
    }

    def __repr__(self):
        return "%s, %s" % (self.created_on, str(self.species))
