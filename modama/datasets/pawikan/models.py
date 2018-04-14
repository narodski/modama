from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from modama.models.dataset_base import BaseObservation, Sex


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
