# Captains Log

This is just some documentation on the goals of this project. For notes on Django see the `READEME.md` at the root of the `django-sandbox` project.

## Enter the virtual env

1. From the root of the `captains_log` project run `source env/bin/activate` then `pip install`
1. Run the project with `python manage.py runserver`

## Captains Log goals

1. Create a CrewMember and have it tied to the built in User
   1. CrewMemebers should have = `name`, `rank`
1. Create a Log
   1. Logs should have = `star_date`, `content`, `user association`, `redacted_status`
   1. A CrewMember can only see their own `Logs`, and only if they are not `redacted`.
   1. A `Log` can be added to as `suplamental`, however content cannot be overwritten.
   1. Captains can see all `Logs`, even if `redacted`.
   1. Captains can `redact` `Logs`.
