from modama import appbuilder
from modama.datasets import _datasets
from modama import db
from flask import g
from flask_appbuilder.const import PERMISSION_PREFIX
from wtforms_jsonschema2.geofab import GeoFABConverter
from wtforms_jsonschema2.utils import _get_view_name
from wtforms import fields
from fab_addon_geoalchemy.fields import PointField
import logging
from modama.exceptions import (UnkownDatasetError, UnkownFormError,
                               ValidationError)
from dateutil import parser as dt_parser
from tzlocal import get_localzone
from werkzeug.datastructures import ImmutableMultiDict

from flask_appbuilder.upload import ImageUploadField

import base64
from io import BytesIO
from werkzeug.datastructures import FileStorage

log = logging.getLogger(__name__)

_FORMTYPES = {
    'add': 'add_form',
    'edit': 'edit_form',
    'show': 'show_form',
    'list': 'list_form'
}


class FormService(object):

    converter = GeoFABConverter()

    @classmethod
    def currentUserViewAccess(cls, view, permission):
        if cls.getCurrentUser() is None:
            return False
        permission_str = PERMISSION_PREFIX + permission
        return appbuilder.sm.has_access(permission_str, view.__name__)
        # return True

    @classmethod
    def getDatasets(cls):
        datasets = {}
        for ds in _datasets:
            accessible_views = []
            for v in ds.mobile_views:
                if cls.currentUserViewAccess(v, 'add'):
                    accessible_views.append(v)
            if len(accessible_views) > 0:
                datasets[ds.name] = accessible_views
        return datasets

    @classmethod
    def getJsonSchema(cls, datasets):
        json_schema = {}
        for dsname, ds in datasets.items():
            json_schema[dsname] = cls.converter.convert(ds)
        return json_schema

    @classmethod
    def getView(cls, datasetname, formname):
        dataset = None
        for ds in _datasets:
            if ds.name == datasetname:
                dataset = ds
                break
        if(dataset is None):
            raise UnkownDatasetError(
                "Dataset {} does not exist".format(datasetname))
        for v in dataset.mobile_views:
            if _get_view_name(v) == formname \
                    and cls.currentUserViewAccess(v, 'add'):
                return v
        raise UnkownFormError(
            "No such form {} in dataset {} to which you have access".format(
                formname, datasetname)
        )

    @classmethod
    def getCurrentUser(cls):
        if g.user is not None and g.user.is_authenticated:
            return g.user
        else:
            return None

    @classmethod
    def getForm(cls, view, formType='add'):
        return getattr(view(), _FORMTYPES[formType])

    @classmethod
    def preprocessFormData(cls, form, cols, data):
        current_user = cls.getCurrentUser()

        filename_base = "".join([
            c for c in str(current_user).replace(' ', '_')
            if c.isalnum()]).rstrip()

        for col in cols:
            field = getattr(form(), col)
            log.debug("Processing column {}".format(col))
            if col in data.keys():
                if data[col] is None:
                    del data[col]
                    continue
                if isinstance(field, PointField) and 'lat' in data[col].keys()\
                        and 'lon' in data[col].keys():
                    log.debug("Converting pointfield")
                    data[col] = field._getpoint(data[col]['lat'],
                                                data[col]['lon'])
                elif isinstance(field, fields.BooleanField):
                    data[col] = str(data[col])
                elif isinstance(field, fields.IntegerField):
                    data[col] = data[col] or ''
                elif isinstance(field, fields.DateTimeField)\
                        and data[col] is not None:
                    dt = dt_parser.parse(data[col])
                    try:
                        dt = dt.astimezone(get_localzone())
                    except ValueError:
                        pass
                    data[col] = dt.strftime(field.format)
                elif isinstance(field, ImageUploadField):
                    pos = data[col].find('base64,/')
                    if pos > -1:
                        bstr = data[col][pos + 7:].strip()
                    else:
                        bstr = data[col].strip()
                    log.debug("Image start: {}".format(bstr[:30]))
                    log.debug("Image end: {}".format(bstr[-30:]))
                    stream = BytesIO(base64.b64decode(bstr))
                    data[col] = FileStorage(stream=stream)
                    data[col].filename = "{}.jpg".format(filename_base)
        return ImmutableMultiDict(data)

    @classmethod
    def processView(cls, view, data, backrefs={}):
        log.debug("Processing view {}".format(view))
        # log.debug("with data {}".format(data))
        cols = view.add_columns
        log.debug("for columns {}".format(cols))
        form = cls.getForm(view, 'add')
        related_data = {}

        related_views = view.related_views or []
        formdata = cls.preprocessFormData(form, cols, data)
        view = view()
        form = form(formdata, csrf_enabled=False)

        # Populate backreference data for related views
        for k, v in backrefs.items():
            if hasattr(form, k):
                field = getattr(form, k)
                field.data = v

        if not form.validate():
            raise ValidationError(
                "\n".join(["{}: {}".format(k, ';'.join(v))
                           for k, v in form.errors.items()])
            )

        # Process the form. Basically the same as
        # flask_appbuilder.baseviews.BaseCRUDView._add

        view.process_form(form, True)
        instance = view.datamodel.obj()
        form.populate_obj(instance)
        try:
            view.pre_add(instance)
        except Exception as e:
            log.exception(e)
            raise

        # Process the form for the related views
        for rv in related_views:
            attrs = rv.datamodel.get_related_fks([view])
            backrefs = dict([(k, instance) for k in
                             view.datamodel.get_related_fks([rv])])
            log.debug("Reverse attrs: {}".format(backrefs))
            for attr in attrs:
                if attr not in data.keys() or data[attr] is None:
                    continue
                if view.datamodel.is_relation_one_to_many(attr):
                    related_data[attr] = []
                    for val in data[attr].values():
                        rel_inst = cls.processView(rv, val, backrefs=backrefs)
                        related_data[attr].append(rel_inst)
                if view.datamodel.is_relation_one_to_one(attr):
                    related_data[attr] = cls.processView(rv, data[attr],
                                                         backrefs=backrefs)

        # Add the related instances to this instance
        for k, v in related_data.items():
            setattr(instance, k, v)

        # Separately add device_id and report_id even if theyre not in the form
        if(hasattr(instance, 'report_id') and 'report_id' in data.keys()):
            instance.report_id = data['report_id']
        if(hasattr(instance, 'device_id') and 'device_id' in data.keys()):
            instance.device_id = data['device_id']

        # if view.datamodel.add(instance):
        #     view.post_add(instance)
        return instance

    @classmethod
    def saveInstance(cls, instance):
        db.session.add(instance)
        try:
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def storeData(cls, datasetname, formname, data):
        view = cls.getView(datasetname, formname)
        instance = cls.processView(view, data)
        cls.saveInstance(instance)
        return instance
