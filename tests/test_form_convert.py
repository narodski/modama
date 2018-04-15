from modama.form_convert import FormConvert, UnsupportedFieldException
from unittest import TestCase
from wtforms.form import Form
from wtforms import validators
from wtforms.fields.core import (StringField, DecimalField, SelectField,
                                 IntegerField, Field)
from wtforms.widgets import TextInput


class CustomField(Field):
    widget = TextInput()


class UnsupportedForm(Form):
    custom_field = CustomField('Custom Field')
    first_name = StringField('First Name', validators=[validators.required()])


class StringTestForm(Form):
    _schema = {
        'type': 'object',
        'properties': {
            'email': {
                'type': 'string',
                'format': 'email',
                'title': 'Email Address'
            },
            'length_string': {
                'type': 'string',
                'minLength': 5,
                'maxLength': 10,
                'title': 'Name'
            },
            'simplestring': {
                'type': 'string',
                'title': 'Simple String'
            }
        }
    }
    email = StringField('Email Address', validators=[validators.Email()])
    length_string = StringField('Name', validators=[validators.Length(5, 10)])
    simplestring = StringField('Simple String')


class SimpleTestForm(Form):
    _schema = {
        'type': 'object',
        'properties': {
            'first_name': {
                'type': 'string',
                'title': 'First Name',
            },
            'nick_name': {
                'type': 'string',
                'title': 'Nickname'
            },
            'age': {
                'type': 'integer',
                'title': 'Age',
                'minimum': 0,
                'maximum': 10
            },
            'average': {
                'type': 'number',
                'title': 'Average'
            },
            'gender': {
                'type': 'string',
                'title': 'Gender',
                'enum': ['Male', 'Female', 'Alien', 'Other']
            },
            'some_field': {
                'type': 'integer',
                'title': 'Bla',
                'enum': [1, 2, 3]
            }
        },
        'required': ['first_name', 'age']
    }
    first_name = StringField('First Name', validators=[validators.required()])
    nick_name = StringField('Nickname')
    age = IntegerField('Age', validators=[validators.number_range(0, 10),
                                          validators.required()])
    average = DecimalField('Average')
    gender = SelectField("Gender", choices=['Male', 'Female', 'Alien',
                                            'Other'])
    some_field = SelectField("Bla", choices=[1, 2, 3])


class TestFormConvert(TestCase):
    def setUp(self):
        self.converter = FormConvert()
        self.maxDiff = None

    def tearDown(self):
        pass

    def test_string_fields(self):
        self.assertEqual(self.converter.convert(StringTestForm),
                         StringTestForm._schema)

    def test_unsupported_form(self):
        with self.assertRaises(UnsupportedFieldException):
            self.converter.convert(UnsupportedForm)

    def test_simple_form(self):
        self.assertEqual(self.converter.convert(SimpleTestForm),
                         SimpleTestForm._schema)
