from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from modama import appbuilder
from modama.views.dataset_base import BaseObservationView
from wtforms.validators import NumberRange
from .models import PawikanEncounterType, PawikanSpecies, PawikanEncounter
from .models import PawikanEncounterPicture
from fab_geoalchemy.interface import GeoSQLAInterface


class PawikanEncounterPictureView(ModelView):
    _pretty_name = 'Picture'
    datamodel = SQLAInterface(PawikanEncounterPicture)
    edit_columns = ['picture']
    show_columns = ['picture_img',
                    'created_on', 'created_by', 'changed_on', 'changed_by']
    add_columns = ['picture', "encounter"]
    list_columns = ['picture_img_thumbnail', 'changed_on', 'changed_by']
    list_title = 'Pictures'
    show_title = 'Picture'
    edit_title = 'Edit Picture'
    add_title = 'Add Picture'


class PawikanEncounterTypeView(ModelView):
    _pretty_name = 'Encounter Type'
    datamodel = SQLAInterface(PawikanEncounterType)
    list_columns = ['name', 'description']
    edit_columns = ['name', 'description']
    add_columns = ['name', 'description']


class PawikanEncounterView(BaseObservationView):
    _pretty_name = 'Encounter'
    datamodel = GeoSQLAInterface(PawikanEncounter)
    label_columns = {'num_pictures': 'Number Of Pictures'}
    list_columns = ['created_on', 'created_by', 'species', 'encounter_type',
                    'ccl', 'sex', 'num_pictures'] +\
        BaseObservationView._base_list
    edit_columns = ['species', 'encounter_type', 'ccl', 'sex', 'location'] +\
        BaseObservationView._base_edit
    add_columns = ['species', 'encounter_type', 'ccl', 'sex', 'location'] +\
        BaseObservationView._base_add
    show_columns = ['species', 'encounter_type', 'ccl',
                    'sex', 'num_pictures'] + BaseObservationView._base_show
    search_exclude_columns = ['location']
    validators_columns = {
        'ccl': [
            NumberRange(min=50, max=250,
                        message='CCL should be between 50cm and 250cm')
        ]
    }
    related_views = [PawikanEncounterPictureView]
    list_title = "Encounters"
    edit_title = "Edit Encounter"
    add_title = "Add Encounter"
    show_title = "Encounter"


class PawikanSpeciesView(ModelView):
    _pretty_name = 'Species'
    datamodel = SQLAInterface(PawikanSpecies)
    label_columns = {'picture_img_thumbnail': 'Picture',
                     'picture_img': 'Picture'}
    list_columns = ['genus', 'species', 'common_name', 'picture_img_thumbnail']
    edit_columns = ["genus", "species", "common_name", 'picture']
    add_columns = ["genus", "species", "common_name", 'picture']
    show_columns = ['genus', 'species', 'common_name', 'picture_img']
    list_title = "Species"
    edit_title = "Edit Species"
    add_title = "Add Species"
    show_title = "Species"


appbuilder.add_view(PawikanEncounterView, "Encounters", category="Pawikan")
appbuilder.add_view(PawikanEncounterPictureView, "Pictures",
                    category="Pawikan")
appbuilder.add_view(PawikanSpeciesView, "Species", category="Pawikan")
appbuilder.add_view(PawikanEncounterTypeView, "Encounter Types",
                    category="Pawikan")
