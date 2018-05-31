from modama import appbuilder
from modama.datasets import _datasets
from modama import db
from flask import g
from flask_appbuilder.const import PERMISSION_PREFIX
from wtforms_jsonschema2.fab import FABConverter
from wtforms import fields
import logging
from modama.exceptions import (UnkownDatasetError, UnkownFormError,
                               ValidationError)
from dateutil import parser as dt_parser
from tzlocal import get_localzone

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

    converter = FABConverter()

    @staticmethod
    def currentUserViewAccess(cls, view, permission):
        if cls.getCurrentUser() is None:
            return False
        permission_str = PERMISSION_PREFIX + permission
        return appbuilder.sm.has_access(permission_str, view.__name)

    @staticmethod
    def getDatasets():
        datasets = {}
        for ds in _datasets:
            accessible_views = []
            for v in ds.mobile_views:
                # if cls.currentUserViewAccess(v, 'add' ):
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
            if cls.converter._get_pretty_name(v, 'show') == formname:
                # and cls.currentUserViewAccess(v, 'add' ):
                return v
        raise UnkownFormError(
            "No such form {} in dataset {}".format(datasetname, formname)
        )

    @classmethod
    def getCurrentUser(cls):
        if g.user is not None and g.user.is_authenticated():
            return g.user
        else:
            return None

    @classmethod
    def getForm(cls, view, formType='add'):
        return getattr(view(), _FORMTYPES[formType])(csrf_enabled=False)

    @classmethod
    def processView(cls, view, data):
        cols = view.add_columns
        form = cls.getForm(view, 'add')
        related_data = {}

        current_user = cls.getCurrentUser()
        filename_base = "".join([
            c for c in str(current_user).replace(' ', '_')
            if c.isalnum()]).rstrip()

        for col in cols:
            if col in data.keys():
                field = getattr(form, col)
                field.raw_data = data[col]
                if isinstance(field, fields.IntegerField) and data[col] == '':
                    continue
                elif isinstance(field, fields.DateTimeField):
                    dt = dt_parser.parse(data[col])
                    try:
                        dt = dt.astimezone(get_localzone())
                    except ValueError:
                        pass
                    data[col] = dt.strftime(field.format)
                elif isinstance(field, ImageUploadField):
                    stream = BytesIO(base64.b64decode(data[col]))
                    data[col] = FileStorage(stream=stream)
                    data[col].filename = "{}.jpg".format(filename_base)
                field.process_formdata([data[col]])

        instance = None

        if form.validate():
            instance = view.datamodel.obj()
            form.populate_obj(instance)
        else:
            raise ValidationError(
                "\n".join(["{}: {}".format(k, ';'.join(v))
                           for k, v in form.errors.items()])
            )

        if view.related_views is not None:
            for rv in view.related_views:
                attrs = rv.datamodel.get_related_fks([view])
                for attr in attrs:
                    if attr not in data.keys():
                        continue
                    if view.datamodel.is_relation_one_to_many(attr):
                        related_data[attr] = []
                        for val in data[attr]:
                            obj = cls.processView(rv, val)
                            related_data[attr].append(obj)

        for k, v in related_data.items():
            setattr(instance, k, v)

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
