First, create a virtual env by `virtualenv env`

Then, get into that environment with `cd env/Scripts && activate && cd ../../` (Windows cmdpromt).

In the env, hit `pip install django`, and then `django-admin startproject [project name]` to start a project.

`cd [project name]` to get into the project, and then `py manage.py startapp [app name]` to start the app.

Migrations are Django's way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. Therefore,
after creating django apps and add them into "installed apps" in settings.py,
you should `py manage.py migrate`.

We can create a supueruser to login via the login page by `py manage.py createsuperuser`.

To run the server, use `py manage.py runserver`

You can exit the virtualenv by just using `deactivate` (because you are in a Linux virtual env so no need to find Windows command for it).

In case I forget: admin - catungthongkhi2002@gmail.com - blabla