## Demo Payment Web Server

**server.py**

Main Flask application file.

**wsgi.py**

[uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
entry point for Flask application.

**options.py**

Application-level Options

**models.py**

Database Models

**handlers.py**

Handlers for URL Endpoints

**errors.py**

Application Errors

**config_create**

Creates uWSGI YAML config file based on options in options file

**/static**

Static files like images, css, and javascript files.

**/templates**

Markup files (HTML files)
