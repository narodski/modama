#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_migrate import MigrateCommand
from flask_script import Manager, prompt_pass, prompt
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound


from modama import app, db, appbuilder
from modama.models import common, dataset_base
from modama.datasets import _datasets
from modama.data.psgc import barangays, municipalities, provinces, regions


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
