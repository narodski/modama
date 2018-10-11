from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from modama import appbuilder
from modama.views.dataset_base import BaseObservationView, BaseVerificationView
from wtforms.validators import NumberRange
from fab_addon_geoalchemy.models import GeoSQLAInterface
from wtforms_jsonschema2.conditions import oneOf

"""
class PawikanEncounterPictureView(ModelView):
    _pretty_name = 'Picture'
    datamodel = SQLAInterface(PawikanEncounterPicture)
    edit_columns = ['picture']
    show_columns = ['picture_img',
                    'created_on', 'created_by', 'changed_on', 'changed_by']
    add_columns = ['picture', 'encounter']
    list_columns = ['picture_img_thumbnail', 'changed_on', 'changed_by']
    list_title = 'Pictures'
    show_title = 'Picture'
    edit_title = 'Edit Picture'
    add_title = 'Add Picture'


class PawikanStrandingView(ModelView):
    _pretty_name = 'Stranding'
    datamodel = GeoSQLAInterface(PawikanStranding)
    add_columns = ['alive', 'encounter']
    show_columns = ['alive']
    list_columns = ['alive']
    edit_columns = ['alive']
    show_title = 'Stranding'
    edit_title = 'Edit Stranding'
    add_title = 'Add Stranding'
    list_title = 'Strandings'


class PawikanEncounterView(BaseObservationView):
    _pretty_name = 'Encounter'
    datamodel = GeoSQLAInterface(PawikanEncounter)
    label_columns = {'num_pictures': 'Number Of Pictures'}
    list_columns = ['created_on', 'created_by', 'species', 'encounter_type',
                    'ccl', 'sex', 'num_pictures'] +\
        BaseObservationView._base_list
    edit_columns = BaseObservationView._base_edit +\
        ['species', 'encounter_type', 'ccl', 'sex', 'location']
    add_columns = BaseObservationView._base_add +\
        ['species', 'encounter_type', 'ccl', 'sex', 'location']
    show_columns = BaseObservationView._base_show +\
        ['species', 'encounter_type', 'ccl', 'sex', 'num_pictures']

    search_exclude_columns = ['location', 'report_id', 'device_id']
    validators_columns = {
        'ccl': [
            NumberRange(min=50, max=250,
                        message='CCL should be between 50cm and 250cm')
        ]
    }
    related_views = [PawikanEncounterPictureView, PawikanStrandingView]
    list_title = "Encounters"
    edit_title = "Edit Encounter"
    add_title = "Add Encounter"
    show_title = "Encounter"

    _conditional_relations = [
        oneOf({
            PawikanStrandingView: {'encounter_type': 'Stranding'},
        })
    ]


class PawikanVerificationView(BaseVerificationView):
    __pretty_name = 'Verification'
    datamodel = GeoSQLAInterface(PawikanEncounter)
    label_columns = {'num_pictures': 'Number Of Pictures'}

    edit_columns = BaseVerificationView._base_edit +\
        ['species', 'encounter_type', 'ccl', 'sex', 'location']
    show_columns = BaseVerificationView._base_show +\
        ['species', 'encounter_type', 'ccl', 'sex', 'num_pictures']
    list_columns = BaseVerificationView._base_list +\
        ['created_on', 'created_by', 'species', 'encounter_type', 'ccl',
         'sex', 'num_pictures']

    search_exclude_columns = ['location', 'report_id', 'device_id']
    validators_columns = {
        'ccl': [
            NumberRange(min=50, max=250,
                        message='CCL should be between 50cm and 250cm')
        ]
    }

    related_views = [PawikanEncounterPictureView]
    list_title = "Unverified Encounters"
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
appbuilder.add_view(PawikanStrandingView, "Strandings", category="Pawikan")
appbuilder.add_view(PawikanVerificationView, "Verify Encounters",
                    category="Pawikan")
appbuilder.add_view(PawikanEncounterPictureView, "Pictures",
                    category="Pawikan")
appbuilder.add_view(PawikanSpeciesView, "Species", category="Pawikan")"""
