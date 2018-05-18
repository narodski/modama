from modama import socketio, appbuilder
from flask_socketio import send, emit
from flask import g
from modama.datasets import _datasets 
from flask_appbuilder.const import PERMISSION_PREFIX
from wtforms_jsonschema2.fab import FABConverter
import logging

log = logging.getLogger(__name__)


@socketio.on('connect')
def checkAuth():
    log.info("Connection made")
    permission_str = PERMISSION_PREFIX + 'add'
    converter = FABConverter()
    datasets = {}
    # if g.user is not None and g.user.is_authenticated():
    for ds in _datasets:
        accessible_views = []
        for v in ds.mobile_views:
            # if appbuilder.sm.has_access(permission_str, v.__name__):
            accessible_views.append(v)
        if len(accessible_views) > 0:
            datasets[ds.name] = converter.convert(accessible_views)
    log.info("Sending datasets %s" % datasets)
    emit('newDatasets', datasets)
    # else:
    #     return False
