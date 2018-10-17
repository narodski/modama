import eventlet
eventlet.monkey_patch()
from modama import app, socketio

socketio.run(app, host='127.0.0.1', debug=True)
