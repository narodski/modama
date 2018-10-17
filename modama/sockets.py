from modama import socketio, appbuilder
from modama.formService import FormService
from modama.exceptions import PermissionDeniedError
from flask_socketio import emit
from flask import g, request
from flask_login import login_user, current_user
import logging
import jwt

log = logging.getLogger(__name__)


@socketio.on_error_default
def error_handler(exc):
    log.exception(exc)
    return {'success': False, 'message': str(exc)}


def login(token):
    av = appbuilder.sm.auth_view
    user = None
    try:
        user = av.getUserFromJWT(token)
    except jwt.exceptions.InvalidTokenError:
        return False
    log.info("User {} logged in on websocket.".format(user))
    if user is not None:
        login_user(user)
        g.user = current_user
        token = av.encodeJWT(av.getJWT())
        return user
    else:
        log.error("Could not find user from valid JWT {}".format(token))
        return None


@socketio.on('connect')
def connect():
    token = request.args.get('token')
    log.info("Connection made with token: {} ".format(token))
    user = login(token)
    if user is not None:
        datasets = FormService.getDatasets()
        log.debug("Got the following datasets: {}".format(datasets))
        json_schema = FormService.getJsonSchema(datasets)
        log.info("Sending datasets %s" % json_schema.keys())
        emit('newToken', token)
        emit('newDatasets', json_schema)
    else:
        return False


@socketio.on('saveData')
def saveData(data):
    token = request.args.get('token')
    user = login(token)
    if token is not None:
        log.info('Saving data for user {}'.format(user))
        formname = data['form']
        datasetname = data['dataset']
        formdata = data['formdata']
        formdata['device_id'] = data['device_id']
        formdata['report_id'] = data['report_id']
        view = FormService.getView(datasetname, formname)
        if not FormService.currentUserViewAccess(view, 'add'):
            raise PermissionDeniedError(
                "User {} does not have add access to {}".format(
                    FormService.getCurrentUser(), view)
            )
        FormService.storeData(datasetname, formname, formdata)
        return {'success': True}
    else:
        return False
