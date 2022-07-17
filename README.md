## Getting Started
1. Clone the project
1. Create an env `python3 -m venv .`
1. Enter the env `source bin/activate`
1. Install requirements `pip install -r requirements.txt`

## Virtual Environments

create a venv: `python3 -m venv .`
enter venv: `source bin/activate`
exit venv: `deactivate`
freeze requirements: `pip freeze > requirements.txt`
install from requirements.txt: `pip install -r requirements.txt`

## VSCode

point to the correct python intruprter by pressing `shift + cmd + p`, then type `Python: Select Interpreter`, then select which you'd like!

## Django

create a project: `python -m django startproject project_name .`
run server: `python manage.py run server`