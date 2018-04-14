# modama
Monitoring Data Management webapplication

## Installation

```
git clone https://github.com/dolfandringa/modama.git
mkvirtualenv modama
cd modama
pip install -r requirements.txt
./modama/bin/modama db upgrade
fabmanager create-admin --app=modama
```

## Running
The best is to run it in production with gunicorn/nginx/etc and use your preferred manager for staring up the application
like Circus, Systemd, etc.

For development, start it with
```
fabmanager run --app=modama
```
