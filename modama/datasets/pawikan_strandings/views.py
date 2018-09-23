from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from modama import appbuilder
from modama.views.dataset_base import BaseObservationView
from wtforms.validators import NumberRange
from .models import PawikanStrandingSpecies, PawikanStranding
from .models import PawikanStrandingPicture
from fab_geoalchemy.interface import GeoSQLAInterface


class PawikanStrandingPictureView(ModelView):
    _pretty_name = 'Picture'
    datamodel = SQLAInterface(PawikanStrandingPicture)
    edit_columns = ['picture']
    show_columns = ['picture_img',
                    'created_on', 'created_by', 'changed_on', 'changed_by']
    add_columns = ['picture', "stranding"]
    list_columns = ['picture_img_thumbnail', 'changed_on', 'changed_by']
    list_title = 'Pictures'
    show_title = 'Picture'
    edit_title = 'Edit Picture'
    add_title = 'Add Picture'


class PawikanStrandingView(BaseObservationView):
    _pretty_name = 'Stranding'
    datamodel = GeoSQLAInterface(PawikanStranding)
    label_columns = {'num_pictures': 'Number Of Pictures'}
    list_columns = ['created_on', 'created_by', 'species',
                    'ccl', 'sex', 'num_pictures'] +\
        BaseObservationView._base_list
    edit_columns = ['species', 'ccl', 'sex', 'location'] +\
        BaseObservationView._base_edit
    add_columns = ['species',  'ccl', 'sex', 'location'] +\
        BaseObservationView._base_add
    show_columns = ['species', 'ccl',
                    'sex', 'num_pictures'] + BaseObservationView._base_show
    search_exclude_columns = ['location']
    validators_columns = {
        'ccl': [
            NumberRange(min=50, max=250,
                        message='CCL should be between 50cm and 250cm')
        ]
    }
    related_views = [PawikanStrandingPictureView]
    list_title = "Strandings"
    edit_title = "Edit Stranding"
    add_title = "Add Stranding"
    show_title = "Stranding"


class PawikanStrandingSpeciesView(ModelView):
    _pretty_name = 'Species'
    datamodel = SQLAInterface(PawikanStrandingSpecies)
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


appbuilder.add_view(PawikanStrandingView, "Strandings",
                    category="Pawikan Strandings")
appbuilder.add_view(PawikanStrandingPictureView, "Pictures",
                    category="Pawikan Strandings")
appbuilder.add_view(PawikanStrandingSpeciesView, "Species",
                    category="Pawikan Strandings")

