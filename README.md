## Getting Started

1. Clone the project
1. Create an env `python3 -m venv .`
1. Enter the env `source bin/activate`
1. Install requirements `pip install -r requirements.txt`

## Virtual Environments

- create a venv: `python3 -m venv .`
- enter venv: `source bin/activate`
- exit venv: `deactivate`
- freeze requirements: `pip freeze > requirements.txt`
- install from requirements.txt: `pip install -r requirements.txt`

## VSCode

point to the correct python intruprter by pressing `shift + cmd + p`, then type `Python: Select Interpreter`, then select which you'd like!

## Django

- create a project: `python -m django startproject project_name .`
- create an app: `python manage.py startapp app_name`
- run server: `python manage.py runserver`

- create user: `python manage.py createsuperuser`

Serializers:

You can use `Serializer` and define every part of the serialization object, or use `ModelSerializer` and the serializer references the model to help out a little!

```
* django-rest-framework docs *

It's important to remember that ModelSerializer classes don't do anything particularly magical, they are simply a shortcut for creating serializer classes:

- An automatically determined set of fields.
- Simple default implementations for the create() and update() methods.
```

## Migrations

- run migrations: `python manage.py migrate`
- create a migration: `python manage.py makemigrations`
