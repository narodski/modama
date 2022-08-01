# modama
Monitoring Data Management webapplication

## Installation
1. Clone the repository and cd to directory.
2. With python and pip installed, run the following command to install initial dependencies of pipenv, docker, docker-compose:
    ```
    https://docs.docker.com/get-docker/
    pip install pipenv docker-compose
    ```
3. Install dependencies with pipenv:
   ```
   pipenv install
   ```
4. Activate environment with pipenv:
   ```
   pipenv shell
   ```
5. Start the database with docker-compose:
   ```
   docker-compose up
   ``` 
6. Run migrations:
   ```
    ./modama/bin/modama db upgrade
    ./modama/bin/modama create_admin
   ```
7. Run locally:
   ```
   python run.py
   ```
8. Run the web application with gunicorn:
   ```
   gunicorn -c gunicorn.conf.py wsgi:app --bind 0.0.0.0.0:8000
   ```
    to bind localhost to port 8000.

```
git clone https://github.com/narodski/modama.git
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
