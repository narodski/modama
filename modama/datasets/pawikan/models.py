from flask_appbuilder import Model
from sqlalchemy import (Column, Integer, String, ForeignKey, Text, Enum,
                        Boolean)
from sqlalchemy.orm import relationship
from modama.models.dataset_base import BaseObservation, Sex
from flask_appbuilder.models.mixins import ImageColumn
from modama.models.common import ModamaAuditMixin
from modama.utils import make_image
from flask_appbuilder.filemanager import ImageManager
from flask import url_for
from fab_addon_geoalchemy.models import Geometry


class PawikanEncounterPicture(Model, ModamaAuditMixin):
    id = Column(Integer, primary_key=True)
    picture = Column(ImageColumn(size=(2048, 2048, False),
                                 thumbnail_size=(800, 800, True)))
    encounter_id = Column(Integer, ForeignKey('pawikan_encounter.id'),
                          nullable=False)
    encounter = relationship('PawikanEncounter', backref='pictures')

    def picture_img(self):
        im = ImageManager()
        alt = str(self.encounter)
        link_url = url_for('PawikanEncounterPictureView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url(self.picture), link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def picture_img_thumbnail(self):
        im = ImageManager()
        alt = str(self.encounter)
        link_url = url_for('PawikanEncounterPictureView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url_thumbnail(self.picture),
                              link_url, alt)
        else:
            return make_image(None, link_url, alt)


class PawikanSpecies(Model):
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
        link_url = url_for('PawikanSpeciesView.show', pk=self.id)
        if self.picture:
            return make_image(im.get_url(self.picture), link_url, alt)
        else:
            return make_image(None, link_url, alt)

    def picture_img_thumbnail(self):
        im = ImageManager()
        alt = str(self)
        link_url = url_for('PawikanSpeciesView.show', pk=self.id)
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


class PawikanStranding(Model):

    id = Column(Integer, primary_key=True)
    alive = Column(Boolean, nullable=False)
    encounter_id = Column(Integer, ForeignKey('pawikan_encounter.id'),
                          nullable=False)
    encounter = relationship('PawikanEncounter', back_populates='stranding',
                             uselist=False)


class PawikanEncounter(BaseObservation):
    __versioned__ = {}

    id = Column(Integer, ForeignKey('base_observation.id'), primary_key=True)
    species_id = Column(Integer, ForeignKey('pawikan_species.id'),
                        nullable=False)
    species = relationship(PawikanSpecies, backref='encounters')
    encounter_type = Column(Enum('Stranding', 'Fisheries bycatch',
                                 'Nesting'), nullable=False)
    ccl = Column(Integer)
    sex_id = Column(Integer, ForeignKey('sex.id'))
    sex = relationship(Sex)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    stranding = relationship(PawikanStranding, back_populates='encounter',
                             uselist=False)

    @property
    def num_pictures(self):
        return len(self.pictures)

    __mapper_args__ = {
        'polymorphic_identity': 'pawikan'
    }

    def __repr__(self):
        return "%s, %s" % (self.created_on, str(self.species))
