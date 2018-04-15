from wtforms.form import FormMeta
from wtforms.fields.core import (StringField, IntegerField,
                                 SelectField, DecimalField)
from wtforms.validators import (Required, InputRequired, NumberRange, Length,
                                Email)
from decimal import Decimal
import logging
from collections import OrderedDict

log = logging.getLogger(__name__)


class UnsupportedFieldException(Exception):
    def __init__(self, field_class):
        self.message = "Field %s is not supported." % field_class


def converts(*args):
    def _inner(func):
        func._converter_for = frozenset(args)
        return func
    return _inner


class FormConvert(object):
    """
    The FormConverter converts wtforms to JSONSchema which can be
    communicated with other applications, and turned back into forms there.
    """

    def __init__(self):
        self.converters = {}
        for name in dir(self):
            obj = getattr(self, name)
            if hasattr(obj, '_converter_for'):
                for classname in obj._converter_for:
                    self.converters[classname] = obj

    def _is_required(self, vals):
        return InputRequired in vals.keys() or Required in vals.keys()

    @converts(StringField)
    def string_field(self, field):
        fieldtype = 'string'
        options = {}
        required = False
        vals = dict([(v.__class__, v) for v in field.validators])

        if Email in vals.keys():
            options['format'] = 'email'
        required = self._is_required(vals)
        if Length in vals.keys():
            options['minLength'] = vals[Length].min
            options['maxLength'] = vals[Length].max

        return fieldtype, options, required

    @converts(DecimalField)
    def decimal_field(self, field):
        fieldtype = 'number'
        options = {}
        required = False
        vals = dict([(v.__class__, v) for v in field.validators])

        required = self._is_required(vals)
        if NumberRange in vals.keys():
            options['minmum'] = vals[NumberRange].min
            options['maximum'] = vals[NumberRange].max

        return fieldtype, options, required

    @converts(IntegerField)
    def integer_field(self, field):
        fieldtype = 'integer'
        options = {}
        required = False
        vals = dict([(v.__class__, v) for v in field.validators])

        required = self._is_required(vals)
        if NumberRange in vals.keys():
            options['minimum'] = vals[NumberRange].min
            options['maximum'] = vals[NumberRange].max

        return fieldtype, options, required

    @converts(SelectField)
    def select_field(self, field):
        choices = field.choices
        if all([isinstance(c, int) for c in choices]):
            fieldtype = 'integer'
        elif all([isinstance(c, float) for c in choices]) or \
                all([isinstance(c, Decimal) for c in choices]):
            fieldtype = 'number'
        else:
            fieldtype = 'string'
        options = {'enum': choices}
        required = False
        vals = dict([(v.__class__, v) for v in field.validators])
        required = self._is_required(vals)

        return fieldtype, options, required

    def convert(self, form):
        log.info("Converting form %s to JSON Schema" % form)
        if isinstance(form, FormMeta):
            form = form()
        fields = OrderedDict([(f.name, f) for f in form])
        schema = {
            "type": "object",
            "properties": {}
        }
        required = []

        for key, field in fields.items():
            log.debug('Converting field %s' % key)
            cls = field.__class__
            if cls not in self.converters.keys():
                raise UnsupportedFieldException(cls)
            d = {}
            fieldtype, attrs, req = self.converters[cls](field)
            log.debug('fieldtype, attrs, req: %s, %s, %s' % (fieldtype, attrs,
                                                             req))
            d['type'] = fieldtype
            for k, v in attrs.items():
                d[k] = v
            d['title'] = field.label.text
            if field.description != '':
                d['description'] = field.description
            schema['properties'][key] = d
            if req:
                required.append(key)
        if len(required) > 0:
            schema['required'] = required
        return schema
