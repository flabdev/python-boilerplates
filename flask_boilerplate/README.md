
## Features
- Predefined basic structure, so you'll end up with a clean architecture.
- Database support via **SQLAlchemy**. However, you can skip database setup and use Flask-Backbone without the database. I also do not use Flask-SQLAlchemy, but you can.
- **Alembic** for your database migrations.
- Development/Production/You own configs with **instance_relative_config**.
- Cache support via **flask_caching**. Setup easily with configuration.
- **Flask-Debug**
- **Sentry** support. Just add your DSN, and you're good to go.
- **Jinja** filters and custom variables.
- Designed to be **blueprint-first**. Keep your structure clean and steady with blueprints. Everything is a blueprint. Your future self will thank you.
- Interactive commands to create your next blueprint. Define your blueprint skeletons to speed up your development. To create your next blueprint simply run flask app create-blueprint. It's up to you and you can completely ignore or remove this part and everything will work perfectly fine.
- Initial setup with a configuration script.
- WSGI config

## Getting Started

**1** — As a rule of thumb, make sure that you use a virtual environment. For example python3 -m venv pythonenv. This will create an environment in the folder pythonenv. I prefer to name my python environment as a pythonenv, because it's more descriptive.

`python3 -m venv pythonenv`

`. pythonenv/bin/activate`

`pip install -r requirements.txt`

**2** — Launch configure.py. It will ask you some question about your future setup.
`python configure.py`

This utility will create: .env, alembic.ini and instance/config.py.

Note: if you're using port other than 5000, then don't forget to update your SERVER_NAME in the config/development.py.
