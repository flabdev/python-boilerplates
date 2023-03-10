# Fission Django Template

## Dependencies

Django
python
Docker
Docker-compose
Poetry
Black
Flake8
pytest

## Development

1. Clone the repository
2. To start development server inside docker you will need to run.

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f docker-compose.yml` to your docker command.
Like this:

```bash
docker-compose -f docker-compose.yml -f docker-compose.yml --project-directory . up
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "src"
src
├── manage.py
├── myapp
│   ├── apps.py
│   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── index.html
│   ├── tests
│   │   └── test_models.py
│   └── views.py
└── webapp
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possibe bugs);


You can read more about pre-commit here: https://pre-commit.com/

## SonarQube

If you want to run it in docker, simply run:

```bash
docker run --rm --net=host -v ${PWD}:/fission_django_template sonarsource/sonar-scanner-cli sonar-scanner -D sonar.projectBaseDir=/fission_django_template -D sonar.login=<project token generated from the below steps>
```

Open the browser and checkout localhost:9000 URL to open Sonarqube.

username: admin

password: admin

Add a project manually

Give a name to the project

Generate a new token for analysis purposes, so that you will not use user credentials for analysing.

Store the token somewhere safe as it will not be visible once the project is set up.

Choose the project main language, as in this case I have chosen “Other” cause the sonarqube-

api project’s main language is python. Then the OS will give you the sonar scanner command that we have to run to populate static code analysis.

Finally, the project is set up, we can see the project listing on the projects tab without any analysis.
