from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from modama.models.dataset_base import BaseObservation, Sex
from flask_appbuilder.models.mixins import ImageColumn
from modama.utils import make_image
from flask_appbuilder.filemanager import ImageManager
from flask import url_for


class PawikanEncounterType(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(255))

    def __repr__(self):
        return self.name


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


class PawikanEncounter(BaseObservation):

    id = Column(Integer, ForeignKey('base_observation.id'), primary_key=True)
    species_id = Column(Integer, ForeignKey('pawikan_species.id'))
    species = relationship(PawikanSpecies, backref='encounters')
    encounter_type_id = Column(Integer,
                               ForeignKey('pawikan_encounter_type.id'))
    encounter_type = relationship('PawikanEncounterType', backref='encounters')
    ccl = Column(Numeric)
    sex_id = Column(Integer, ForeignKey('sex.id'))
    sex = relationship(Sex)

    __mapper_args__ = {
        'polymorphic_identity': 'pawikan'
    }

    def __repr__(self):
        return "%(s), %(s)" % (self.created_on, self.species.common_name)
