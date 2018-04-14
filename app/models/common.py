from flask_appbuilder import Model
# from flask_appbuilder.models.mixins import AuditMixin, FileColumn
# from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, Text  # , ForeignKey
# from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Dataset(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    module = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return self.name
