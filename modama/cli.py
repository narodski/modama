#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_migrate import MigrateCommand
from flask_script import Manager

from modama import app, db
from modama.models import common, dataset_base
from modama.datasets import _datasets

config = app.config


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def load_base_data():
    db.session.add(dataset_base.Sex(name='Male'))
    db.session.add(dataset_base.Sex(name='Female'))
    db.session.add(common.Dataset(name="Pawikan",
                                  description="BMB Pawikan Monitoring",
                                  module="pawikan"))
    db.session.commit()
    for ds in _datasets:
        ds.load_base_data()
        db.session.commit()
