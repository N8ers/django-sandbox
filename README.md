# Django Sandbox

This is a place for me to messaround with Django.

## Setting up a virtual environment with **pipenv**

### Install pipenv

1. `mkdir test-project`
1. `cd test-project`
1. `pipenv install django`

### Activating/Deactivating pipenv

1. `pipenv shell` (activate)
1. `deactivate` (...deactivate)

## Creating Django Project

`django-admin startproject test-project .`
This will create a directory and `manage.py` file. `manage.py` is a wrapper for the project. So we will use `manage.py` as a command instead of `django-admin`.

## Run Django Server

`python3 manage.py runserver`
# django-sandbox
