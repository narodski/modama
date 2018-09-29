from fab_geoalchemy.views import GeoModelView
from wtforms import DateTimeField, validators, TextField
from ..widgets import DateTimeTZPickerWidget, ROTextFieldWidget
from ..models.filters import FilterM2MRelationOverlapFunction
from flask_appbuilder.models.sqla.filters import FilterEqual
from modama import appbuilder


class BaseObservationView(GeoModelView):

    _base_edit = ['report_id', 'observation_datetime', 'reporter',
                  'reporter_contact']
    _base_add = ['observation_datetime', 'reporter', 'reporter_contact']
    _base_list = ['observation_datetime', 'reporter', 'verified']
    _base_show = ['report_id', 'observation_datetime', 'reporter', 'verified',
                  'reporter_contact',
                  'created_by', 'created_on', 'changed_by', 'changed_on']

    edit_form_extra_fields = {'observation_datetime':
                              DateTimeField('Observation date/time',
                                            validators=[validators.required()],
                                            format='%Y-%m-%d %H:%M:%S%z',
                                            widget=DateTimeTZPickerWidget()),
                              'report_id':
                              TextField(widget=ROTextFieldWidget())}
    add_form_extra_fields = {'observation_datetime':
                             DateTimeField('Observation date/time',
                                           validators=[validators.required()],
                                           format='%Y-%m-%d %H:%M:%S%z',
                                           widget=DateTimeTZPickerWidget())}

    base_filters = [['created_by.organizations',
                     FilterM2MRelationOverlapFunction,
                     appbuilder.sm.my_organizations]]


class BaseVerificationView(GeoModelView):
    _base_edit = ['observation_datetime', 'reporter', 'reporter_contact',
                  'created_by', 'verified']
    _base_list = ['observation_datetime', 'reporter', 'reporter_contact',
                  'created_on', 'created_by']
    _base_show = ['report_id', 'observation_datetime', 'reporter', 'verified',
                  'reporter_contact',
                  'created_by', 'created_on', 'changed_by', 'changed_on']

    edit_form_extra_fields = {'observation_datetime':
                              DateTimeField('Observation date/time',
                                            validators=[validators.required()],
                                            format='%Y-%m-%d %H:%M:%S%z',
                                            widget=DateTimeTZPickerWidget()),
                              'report_id':
                              TextField(widget=ROTextFieldWidget())
                              }

    base_filters = [['verified', FilterEqual, False],
                    ['created_by.organizations',
                     FilterM2MRelationOverlapFunction,
                     appbuilder.sm.my_organizations]]

    base_permissions = ['can_list', 'can_show', 'can_edit']
