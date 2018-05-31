from modama import socketio
from modama.formService import FormService
from flask_socketio import emit
from flask import g
import logging

log = logging.getLogger(__name__)


@socketio.on('connect')
def checkAuth():
    log.info("Connection made")
    # if g.user is not None and g.user.is_authenticated():
    datasets = FormService.getDatasets()
    json_schema = FormService.getJsonSchema(datasets)
    log.info("Sending datasets %s" % json_schema)
    emit('newDatasets', json_schema)
    # else:
    #     return False
