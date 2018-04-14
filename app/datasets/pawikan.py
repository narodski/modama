from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.models.dataset_base import BaseObservation, Sex
from app.views.dataset_base import BaseObservationView
from wtforms.validators import DataRequired, NumberRange

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
        return self.common_name


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


class PawikanEncounterTypeView(ModelView):
    datamodel = SQLAInterface(PawikanEncounterType)
    list_columns = ['name', 'description']
    edit_columns = ['name', 'description']
    add_columns = ['name', 'description']


class PawikanEncounterView(BaseObservationView):
    datamodel = SQLAInterface(PawikanEncounter)
    list_columns = BaseObservationView._base_list + [
        'created_on', 'created_by', 'species', 'encounter_type', 'ccl', 'sex']
    edit_columns = BaseObservationView._base_edit + [
        'species', 'encounter_type', 'ccl', 'sex']
    add_columns = BaseObservationView._base_add + [
        'species', 'encounter_type', 'ccl', 'sex']
    validators_columns = {
        'ccl': [
            NumberRange(min=50, max=250,
                        message='CCL should be between 50cm and 250cm')
        ]
    }


class PawikanSpeciesView(ModelView):
    datamodel = SQLAInterface(PawikanSpecies)
    list_columns = ['genus', 'species', 'common_name']
    edit_columns = ["genus", "species", "common_name"]
    add_columns = ["genus", "species", "common_name"]


db.create_all()


appbuilder.add_view(PawikanEncounterView, "Encounters", category="Pawikan")
appbuilder.add_view(PawikanSpeciesView, "Species", category="Pawikan")
appbuilder.add_view(PawikanEncounterTypeView, "Encounter Types",
                    category="Pawikan")

views = [PawikanEncounterView]
