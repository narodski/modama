from fab_addon_geoalchemy.views import GeoModelView
from datetime import datetime
from wtforms import DateTimeField, validators, TextField
from ..widgets import DateTimeTZPickerWidget, ROTextFieldWidget
from ..models.filters import FilterM2MRelationOverlapFunction
from flask_appbuilder.models.sqla.filters import FilterEqual
from flask_appbuilder.widgets import ShowWidget
from flask_appbuilder.actions import action
from modama import appbuilder
from modama.views.widgets import (ShowPrintWidget, ListPrintWidget,
                                  ModamaShowWidget)
import logging
from flask_weasyprint import render_pdf, HTML

log = logging.getLogger(__name__)


class BaseModamaView(GeoModelView):

    show_widget = ModamaShowWidget
    show_template = 'general/model/show.html'

    # def _get_related_views_widgets(self, item, *args, **kwargs):
    #     log.debug("Getting related views widgets for {}".format(item))
    #     widgets = super()._get_related_views_widgets(item, *args, **kwargs)
    #     for widget in widgets['related_views']:
    #         log.debug("Got widget {}".format(widget))
    #     return widgets

    def _get_related_view_widget(self, item, related_view,
                                 order_column='', order_direction='',
                                 page=None, page_size=None):

        log.debug("Getting view for {}".format(related_view))
        fk = related_view.datamodel.get_related_fk(self.datamodel.obj)
        filters = related_view.datamodel.get_filters()
        # Check if it's a many to one model relation
        if related_view.datamodel.is_relation_many_to_one(fk):
            filters.add_filter_related_view(
                fk, self.datamodel.FilterRelationOneToManyEqual,
                self.datamodel.get_pk_value(item))
        # Check if it's a many to many model relation
        elif related_view.datamodel.is_relation_many_to_many(fk):
            filters.add_filter_related_view(
                fk, self.datamodel.FilterRelationManyToManyEqual,
                self.datamodel.get_pk_value(item))
        elif related_view.datamodel.is_relation_one_to_one(fk):
            log.debug("Got a one-to-one relation")
            backref = self.datamodel.get_related_fk(related_view.datamodel.obj)
            rel_item = getattr(item, backref)
            log.debug("backref {} rel_item {} item {}"
                      .format(backref, rel_item, item))
            if rel_item is not None:
                rel_pk = related_view.datamodel.get_pk_value(rel_item)
                return related_view._get_show_widget(rel_pk, rel_item)['show']
            filters.add_filter_related_view(
                fk, self.datamodel.FilterRelationOneToManyEqual,
                self.datamodel.get_pk_value(item))
        else:
            log.error("Can't find relation on related view {0}"
                      .format(related_view.name))
            return None
        log.debug("Got a different relation")
        return related_view._get_view_widget(filters=filters,
                                             order_column=order_column,
                                             order_direction=order_direction,
                                             page=page, page_size=page_size)

    base_filters = [['created_by.organizations',
                     FilterM2MRelationOverlapFunction,
                     appbuilder.sm.my_organizations]]

    base_permissions = ['can_list', 'can_edit', 'can_show', 'can_add',
                        'can_delete']


class BaseObservationView(BaseModamaView):

    _base_edit = ['report_id', 'observation_datetime']
    _base_add = ['observation_datetime']
    _base_list = ['observation_datetime', 'verified', 'created_by']
    _base_show = ['report_id', 'observation_datetime', 'verified',
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
            log.debug("Widget: {}".format(w))
            log.debug("args: {}".format(w.template_args.keys()))
            if isinstance(w, ShowWidget):
                arg_keys = ['modelview_name', 'label_columns',
                            'formatters_columns', 'actions', 'value_columns',
                            'fieldsets', 'pk', 'include_columns']
                widget = self.print_show_widget
            else:
                arg_keys = ['label_columns', 'include_columns', 'value_columns',
                            'order_columns', 'formatters_columns', 'page',
                            'page_size', 'count', 'pks', 'actions', 'filters',
                            'modelview_name']
                widget = self.print_list_widget
            for a in arg_keys:
                args[a] = w.template_args[a]
            w2 = widget(**args)
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
    base_permissions = ['can_list', 'can_show', 'can_edit', 'can_print',
                        'can_delete', 'can_add']


class BaseVerificationView(GeoModelView):
    _base_edit = ['observation_datetime',
                  'created_by', 'verified']
    _base_list = ['observation_datetime',
                  'created_on', 'created_by']
    _base_show = ['report_id', 'observation_datetime', 'verified',
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
