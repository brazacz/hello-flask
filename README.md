# Hello Flask

This is a tutorial how to build a simple web app with Python. We’ll use a micro-framework called **[Flask](https://flask.palletsprojects.com)**.

Flask is based on the **Werkzeug** WSGI toolkit and and **Jinja2** template engine.

## Prerequisites
- Install [Python 3](https://www.python.org)
- Update pip to newest version: `python -m pip install --upgrade pip`
- Install pipenv (virtual environment): `pip install pipenv`

## Run Flask app
- Create project directory: `mkdir hello-flask`
- Go to project directory: `cd hello-flask`
- Inside project directory create a web app `index.py`  
  ```py
  from flask import Flask
  app = Flask(__name__)
  @app.route('/')
  def home():
  return '<h1>Hello Flask!<h1>'
  ```
- Create virtual environment and install dependencies: `pipenv install`
- Install Flask into virtual environment: `pipenv install flask`
- Open pipenv shell: `pipenv shell`
- Define which app to run: `export FLASK_APP=index.py`
- Run the app: `flask run`
