from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from app import appbuilder, db
from app.models.common import Dataset
from app.models.dataset_base import Sex


class DatasetView(ModelView):
    datamodel = SQLAInterface(Dataset)
    list_columns = ['name']


class SexView(ModelView):
    datamodel = SQLAInterface(Sex)


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template,
                           appbuilder=appbuilder), 404


db.create_all()

appbuilder.add_view(DatasetView, "List Datasets", category="Datasets")
appbuilder.add_view(SexView, "Sexes", category="Datasets")
