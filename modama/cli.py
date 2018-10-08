#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_migrate import MigrateCommand
from flask_script import Manager, prompt_pass, prompt
from sqlalchemy.orm.exc import NoResultFound


from modama import app, db, appbuilder
from modama.models import common, dataset_base
from modama.datasets import _datasets

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
    if db.session.query(dataset_base.Sex).count() == 0:
        db.session.add(dataset_base.Sex(name='Male'))
        db.session.add(dataset_base.Sex(name='Female'))
        db.session.commit()
    for ds in _datasets:
        ds.load_base_data()
        db.session.commit()
