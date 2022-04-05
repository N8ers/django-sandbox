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

# Setting virtual environment in vsCode

1. `pipenv --venv` >> returns path
1. copy path and append `/bin/python` > it should look something like this `/Users/nathansheryak/.local/share/virtualenvs/storefront-XjSxL3vY/bin/python`
1. vsCode > view > command pallet > `Python: Select Interpreter` > `Enter interpreter path...` > insert path from above

# Creating an `app`

In `settings.py` you'll notice `INSTALLED_APPS`. This is a list of apps Django is using. To add a new app run: `python manage.py startapp playground`. After running the command, notice a new dir `playground` was created. You'll then need to add `'playground'` to the `INSTALLED_APPS` list.

# Add an endpoint and render a template

1. Create a new app using `python manage.py startapp {name}`
1. Add it to `INSTALLED_APPS` in `settings.py`
1. Add to the root `urls.py`
1. Create a `urls.py` file in the new app folder
