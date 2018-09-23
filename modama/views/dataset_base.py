from fab_geoalchemy.views import GeoModelView
from wtforms import DateTimeField, validators
from ..widgets import DateTimeTZPickerWidget
from ..models.filters import FilterM2MRelationOverlapFunction
from modama import appbuilder


class BaseObservationView(GeoModelView):

    _base_edit = ['observation_datetime', 'reporter', 'verified']
    _base_add = ['observation_datetime', 'reporter']
    _base_list = ['observation_datetime', 'reporter', 'verified']
    _base_show = ['report_id', 'observation_datetime', 'reporter', 'verified',
                  'created_by', 'created_on', 'changed_by', 'changed_on']

    edit_form_extra_fields = {'observation_datetime':
                              DateTimeField('Observation date/time',
                                            validators=[validators.required()],
                                            format='%Y-%m-%d %H:%M:%S%z',
                                            widget=DateTimeTZPickerWidget())}
    add_form_extra_fields = {'observation_datetime':
                             DateTimeField('Observation date/time',
                                           validators=[validators.required()],
                                           format='%Y-%m-%d %H:%M:%S%z',
                                           widget=DateTimeTZPickerWidget())}

    base_filters = [['created_by.organizations',
                     FilterM2MRelationOverlapFunction,
                     appbuilder.sm.my_organizations]]
