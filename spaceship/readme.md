# API
In this section you will find all the APIs which have been created for this project. 

## Technology Stack
Python , Django 

## Installation Steps for linux interface

- Make sure you have sqlite3 installed

- Upgrade pip and create python3 environment and activate the new environment
```(bash)
python3 -m pip install --upgrade pip
python3 -m pip install --user --upgrade pip

python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```

- cd to api directory

- pip install requirements.txt
```(bash)
python3 -m pip install -r requirement.txt
```

- skip these commands if there is database/sqlite3 file in the files.
```(bash)
python3 manage.py makemigrations api

python3 manage.py migrate api


python3 manage.py makemigrations
python3 manage.py migrate
```

- runt he following command to run the server
```(bash)
python3 manage.py runserver
```
=======
