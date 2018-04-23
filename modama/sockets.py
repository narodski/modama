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
    forms = {}
    # if g.user is not None and g.user.is_authenticated():
    for ds in _datasets:
        forms[ds.name] = []
        for v in ds.mobile_views:
            # if appbuilder.sm.has_access(permission_str, v.__name__):
            forms[ds.name].append(converter.convert(v().add_form))
        if len(forms[ds.name]) == 0:
            del(forms[ds.name])
    log.info("Sending forms %s" % forms)
    emit('newForms', forms)
    # else:
    #     return False
