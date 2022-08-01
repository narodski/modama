import os

filepath = os.path.dirname(os.path.abspath(__file__))

workers = 2
# Access log - records incoming HTTP requests
accesslog = os.path.join(filepath, "logs/gunicorn.access.log")
# Error log - records Gunicorn server goings-on
errorlog = os.path.join(filepath, "logs/gunicorn.error.log")
# Whether to send Django output to the error log 
capture_output = True
# How verbose the Gunicorn error logs should be 
loglevel = "info"
timeout=60 * 15