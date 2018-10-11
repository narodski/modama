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


@manager.command
def generate_views(dataset):
    ds = getattr(modama.datasets, dataset)
    ds_title = dataset.title()
    models = [m for m in ds.models.__dict__.values() if isclass(m)
              and issubclass(m, Model)
              and m.__module__ == 'modama.datasets.pawikan.models']
    ##
    template = Template("""
    class {{model.__name__}}View:
        _pretty_name = '{{model_pretty}}'
        datamodel = GeoSQLAInterface({{model.__name__}})
        add_columns = ["{{'", "'.join(add_columns)}}"]
        list_columns = ["{{'", "'.join(list_columns)}}"]
        edit_columns = ["{{'", "'.join(edit_columns)}}"]
        show_columns = ["{{'", "'.join(show_columns)}}"]
        related_views = [{{', '.join(related_views)}}]
        add_title = ''
        show_title = ''
        list_title = ''
        edit_title = ''
        _conditional_relations = [
            oneOf({}),
        ]
    """)
    ##

    for m in models[:-4]:
        print(m.__name__)
        interf = SQLAInterface(m)
        props = [(k, v) for k, v in m.__dict__.items()
                 if isinstance(v, InstrumentedAttribute)]
        data = {'model': m,
                'view_name': get_view_name(m),
                'model_pretty': get_model_pretty(m, ds_title),
                'add_columns': [],
                'list_columns': [],
                'show_columns': [],
                'edit_columns': [],
                'related_views': []
                }
        for name, prop in props:
            if interf.is_relation(name):
                rel_m = interf.get_related_model(name)
                data['add_columns'].append(name)
                data['related_views'].append(get_view_name(rel_m))
            elif not interf.is_fk(name):
                data['add_columns'].append(name)
                data['edit_columns'].append(name)
                data['show_columns'].append(name)
                data['list_columns'].append(name)
        print(autopep8.fix_code(template.render(data)))


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
