# modama
Monitoring Data Management webapplication

## Installation

```
git clone https://github.com/dolfandringa/modama.git
mkvirtualenv modama
cd modama
pip install -r requirements.txt
./modama/bin/modama db upgrade
./modama/bin/modama create_admin
```

## Testing
Unittests can be run with pytest.
Make sure you install the dev dependencies first with
```
pip install -r requirements-dev.txt
```
Then from the root folder you can run the tests with
```
pytest
```

## Running
The best is to run it in production with gunicorn/nginx/etc and use your preferred manager for staring up the application
like Circus, Systemd, etc.

For development, start it with
```
python run.py
```
