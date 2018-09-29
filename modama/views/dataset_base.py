from fab_geoalchemy.views import GeoModelView
from datetime import datetime
from wtforms import DateTimeField, validators, TextField
from ..widgets import DateTimeTZPickerWidget, ROTextFieldWidget
from ..models.filters import FilterM2MRelationOverlapFunction
from flask_appbuilder.models.sqla.filters import FilterEqual
from flask_appbuilder.actions import action
from modama import appbuilder
from modama.views.widgets import ShowPrintWidget, ListPrintWidget
import logging
from flask_weasyprint import render_pdf, HTML

log = logging.getLogger(__name__)


class BaseObservationView(GeoModelView):

    _base_edit = ['report_id', 'observation_datetime', 'reporter',
                  'reporter_contact']
    _base_add = ['observation_datetime', 'reporter', 'reporter_contact']
    _base_list = ['observation_datetime', 'reporter', 'verified']
    _base_show = ['report_id', 'observation_datetime', 'reporter', 'verified',
                  'reporter_contact',
                  'created_by', 'created_on', 'changed_by', 'changed_on']

    print_template = 'print.html'
    print_show_widget = ShowPrintWidget
    print_list_widget = ListPrintWidget

    @action('print', 'Print', '', icon='fa-file-pdf-o', multiple=False,
            single=True)
    def print(self, item):
        pk = item.id
        widgets = self._show(pk)
        show_widget = widgets.get('show')
        show_args = show_widget.template_args
        widgets['print_show'] = self.print_show_widget(**show_args)
        widgets['related_print_views'] = []
        for w in widgets['related_views']:
            args = {}
            for a in ['label_columns', 'include_columns', 'value_columns',
                      'order_columns', 'formatters_columns', 'page',
                      'page_size', 'count', 'pks', 'actions', 'filters',
                      'modelview_name']:
                args[a] = w.template_args[a]
            w2 = self.print_list_widget(**args)
            log.debug("Converting {} into {} with template {}".format(
                w, w2, w2.template))
            widgets['related_print_views'].append(w2)

        html = self.render_template(self.print_template,
                                    pk=pk,
                                    title=self.show_title,
                                    widgets=widgets,
                                    last_modified=datetime.now(),
                                    related_views=self._related_views)
        return render_pdf(HTML(string=html))

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

    base_permissions = ['can_list', 'can_edit', 'can_show', 'can_add',
                        'can_delete', 'can_print']


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
