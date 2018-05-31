from modama import socketio
from modama.formService import FormService
from modama.exceptions import PermissionDeniedError
from flask_socketio import emit
from flask import g
import logging

log = logging.getLogger(__name__)


@socketio.on_error_default
def error_handler(exc):
    log.error(exc)
    raise RuntimeError(str(exc))


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


@socketio.on('saveData')
def saveData(datasetname, formname, data):
    log.info('Saving data for user {}'.format(g.user))
    view = FormService.getView(datasetname, formname)
    if not FormService.currentUserViewAccess(view, 'add'):
        raise PermissionDeniedError(
            "User {} does not have add access to {}".format(
                FormService.getCurrentUser(), view)
        )
    FormService.storeData(datasetname, formname, data)
