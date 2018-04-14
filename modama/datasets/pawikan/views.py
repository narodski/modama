from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from modama import appbuilder
from modama.views.dataset_base import BaseObservationView
from wtforms.validators import NumberRange
from .models import PawikanEncounterType, PawikanSpecies, PawikanEncounter


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


appbuilder.add_view(PawikanEncounterView, "Encounters", category="Pawikan")
appbuilder.add_view(PawikanSpeciesView, "Species", category="Pawikan")
appbuilder.add_view(PawikanEncounterTypeView, "Encounter Types",
                    category="Pawikan")
