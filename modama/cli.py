#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_migrate import MigrateCommand
from flask_script import Manager, prompt_pass, prompt
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound


from modama import app, db, appbuilder
from modama.models import common, dataset_base
from modama.datasets import _datasets
import modama.datasets
from modama.data.psgc import barangays, municipalities, provinces, regions


from inspect import isclass
from flask_appbuilder import Model
from flask_appbuilder.models.sqla.interface import SQLAInterface
from sqlalchemy.orm.attributes import InstrumentedAttribute
from jinja2 import Template
import re
import autopep8
from geoalchemy2 import Geometry


app.config['CSRF_ENABLED'] = False
config = app.config


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def shell():
    import code
    code.interact()


@manager.command
def create_admin(username=None, firstname=None, lastname=None,
                 email=None, password=None):
    if username is None:
        username = prompt('Username', default='admin')
    if firstname is None:
        firstname = prompt('Firstname', default='admin')
    if lastname is None:
        lastname = prompt('Lastname', default='user')
    if email is None:
        email = prompt('Email', default='admin@fab.org')
    if password is None:
        password = prompt_pass('Password')
    try:
        q = db.session.query(common.Organization)
        org = q.filter_by(name='Admins').one()
    except NoResultFound:
        org = common.Organization(name='Admins')
        db.session.add(org)
        db.session.commit()
    role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
    user = appbuilder.sm.add_user(username, firstname, lastname, email,
                                  role_admin, [org], password)
    if user:
        print('Admin User {0} created.'.format(username))
    else:
        print('No user created. An error occured!')


def get_view_name(m):
    return "{}View".format(m.__name__)


def get_model_pretty(m, ds_title):
    return re.sub("([a-z])([A-Z])", r"\1 \2", m.__name__.replace(ds_title, ''))


@manager.option('-d', '--dataset', dest='dataset')
@manager.option('-f', '--file', dest='filename')
def generate_views(dataset, filename):
    ds = getattr(modama.datasets, dataset)
    ds_title = dataset.title()
    models = [m for m in ds.models.__dict__.values() if isclass(m) and
              issubclass(m, Model) and
              m.__module__ == 'modama.datasets.pawikan.models']
    ##
    observation_template = Template('''
class {{view_name}}(BaseObservationView):
    _pretty_name = '{{model_pretty}}'
    datamodel = GeoSQLAInterface({{model.__name__}})
    add_columns = BaseObservationView._base_add +\\
                   ["{{'", "'.join(add_columns)}}"] +\\
                   ["{{'", "'.join(related_columns)}}"]
    list_columns = BaseObservationView._base_list +\\
                   ["{{'", "'.join(list_columns)}}"] +\\
                   ["{{'", "'.join(related_columns)}}"]
    edit_columns = BaseObservationView._base_edit +\\
                   ["{{'", "'.join(edit_columns)}}"]
    show_columns = BaseObservationView._base_show +\\
                   ["{{'", "'.join(show_columns)}}"] +\\
                   ["{{'", "'.join(related_columns)}}"]
    related_views = [{{', '.join(related_views)}}]
    search_exclude_columns = ["{{'", "'.join(search_exclude_columns)}}"]
    add_title = 'Add {{model_pretty}}'
    show_title = '{{model_pretty}}'
    list_title = '{{model_pretty}}s'
    edit_title = 'Edit {{model_pretty}}'
    """
    label_columns = {
        "{{'": "",\n        "'.join(label_columns)}}": ""
    }
    validator_columns = {}
    _conditional_relations = [
    ]
    """


''')
    template = Template('''
class {{view_name}}(ModelView):
    _pretty_name = '{{model_pretty}}'
    datamodel = GeoSQLAInterface({{model.__name__}})
    # add_columns = ["{{'", "'.join(add_columns)}}"] +\\
    #               ["{{'", "'.join(related_columns)}}"]
    # list_columns = ["{{'", "'.join(list_columns)}}"] +\\
    #                ["{{'", "'.join(related_columns)}}"]
    # edit_columns = ["{{'", "'.join(edit_columns)}}"]
    # show_columns = ["{{'", "'.join(show_columns)}}"] +\\
    #                ["{{'", "'.join(related_columns)}}"]
    # related_views = [{{', '.join(related_views)}}]
    search_exclude_columns = ["{{'", "'.join(search_exclude_columns)}}"]
    add_title = 'Add {{model_pretty}}'
    show_title = '{{model_pretty}}'
    list_title = '{{model_pretty}}s'
    edit_title = 'Edit {{model_pretty}}'
    """
    label_columns = {
        "{{'": "",\n        "'.join(label_columns)}}": ""
    }
    validator_columns = {}
    _conditional_relations = [
    ]
    """


''')
    ##
    head_template = Template("""
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from modama import appbuilder
from modama.views.dataset_base import BaseObservationView, BaseVerificationView
from wtforms.validators import NumberRange
from fab_addon_geoalchemy.models import GeoSQLAInterface
from wtforms_jsonschema2.conditions import oneOf
from modama.datasets.{{dataset}}.models import ({{", ".join(models)}})
""")
    tail_template = Template("""
{% for v in observation_views %}
appbuilder.add_view({{v['name']}}, "{{v['list_title']}}",
                    category="{{ds_title}}")
{% endfor %} {% for v in other_views %}
appbuilder.add_view_no_menu({{v['name']}}){% endfor %}
""")
    views = {}
    meta_cols = ['changed_by', 'changed_on', 'created_by', 'created_on',
                 'report_id']
    ignore_always_cols = ['device_id', 'dataset', 'versions']
    for m in models:
        observation_view = False
        if issubclass(m, dataset_base.BaseObservation):
            tmpl = observation_template
            observation_view = True
        else:
            tmpl = template
        interf = SQLAInterface(m)
        view_name = get_view_name(m)
        props = [(k, v) for k, v in m.__dict__.items()
                 if isinstance(v, InstrumentedAttribute)]
        data = {'model': m,
                'view_name': view_name,
                'model_pretty': get_model_pretty(m, ds_title),
                'add_columns': [],
                'list_columns': [],
                'show_columns': [],
                'edit_columns': [],
                'related_views': [],
                'label_columns': [],
                'related_columns': [],
                'search_exclude_columns': [],
                }
        for name, prop in props:
            if name in ignore_always_cols:
                continue
            if name in meta_cols:
                continue
            # Loop over the fields

            if interf.is_relation(name):
                # relation properties
                rel_m = interf.get_related_model(name)
                data['related_columns'].append(name)
                if (not interf.is_relation_many_to_one(name) and
                    interf.is_pk(
                        interf.get_relation_fk(name).name)):
                    # only add if we're on the side of a relation without
                    # foreign key (so fk points to our primary key)
                    data['label_columns'].append(name)
                    data['related_views'].append(get_view_name(rel_m))
            elif interf.is_fk(name):
                data['search_exclude_columns'].append(name)
            else:
                if isinstance(prop.type, Geometry):
                    # don't search geometry columns
                    data['search_exclude_columns'].append(name)
                data['label_columns'].append(name)
                data['add_columns'].append(name)
                data['edit_columns'].append(name)
                data['list_columns'].append(name)
                data['show_columns'].append(name)

            views[view_name] = {'code': tmpl.render(data),
                                'observation_view': observation_view,
                                'name': view_name,
                                'num_cols': len(data['show_columns']),
                                'list_title': data['model_pretty'] + 's',
                                'related_views': data['related_views']}
    views_list = sorted(views.values(), key=lambda x: x['num_cols'])
    head = head_template.render({'models': [m.__name__ for m in models],
                                 'dataset': dataset})
    tail = tail_template.render(
        ds_title=ds_title,
        observation_views=[v for v in views_list if v['observation_view']],
        other_views=[v for v in views_list if not v['observation_view']])
    full_template = "{}\n\n{}\n\n{}".format(
        head, "\n".join([v['code'] for v in views_list]), tail)
    with open(filename, 'w') as f:
        f.write(autopep8.fix_code(full_template))


@manager.command
def load_base_data():
    add = db.session.add
    exec = db.session.bind.execute
    commit = db.session.commit
    reg = dataset_base.Region.__table__
    prov = dataset_base.Province.__table__
    mun = dataset_base.Municipality.__table__
    bar = dataset_base.Barangay.__table__
    if db.session.query(dataset_base.Region).count() == 0:
        print("Inserting Region data")
        data = [dict(zip(['psgc', 'name'], row)) for row in regions]
        db.session.bulk_insert_mappings(dataset_base.Region,
                                        data)
        db.session.commit()

    if db.session.query(dataset_base.Province).count() == 0:
        print("Inserting Province data")
        for row in provinces:
            data = dict(zip(['psgc', 'name'], row))
            data['region_id'] = exec(select([reg.c.id]).where(
                reg.c.psgc == row[2])).fetchone()[0]
            exec(prov.insert().values(**data))

    if db.session.query(dataset_base.Municipality).count() == 0:
        print("Inserting municipality data")
        data = []
        for i, row in enumerate(municipalities):
            # print('Processing municipality {}'.format(i))
            new_row = dict(zip(['psgc', 'name'], row))
            new_row['province_id'] = exec(select([prov.c.id]).where(
                prov.c.psgc == row[2])).fetchone()[0]
            data.append(new_row)
        exec(mun.insert(), data)

    if db.session.query(dataset_base.Barangay).count() == 0:
        print("Inserting barangay data")
        data = []
        for i, row in enumerate(barangays):
            # print('Processing barangay {}'.format(i))
            new_row = dict(zip(['psgc', 'name'], row))
            new_row['municipality_id'] = exec(select([mun.c.id]).where(
                mun.c.psgc == row[2])).fetchone()[0]
            data.append(new_row)
        exec(bar.insert(), data)

    if db.session.query(dataset_base.Sex).count() == 0:
        print("Inserting Sex data")
        add(dataset_base.Sex(name='Male'))
        add(dataset_base.Sex(name='Female'))
        commit()

    for ds in _datasets:
        print("Inserting data for dataset {}".format(ds))
        ds.load_base_data()
        db.session.commit()
