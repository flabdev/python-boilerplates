# fission_project_template

This project was generated using fastapi_template.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m fission_project_template
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "fission_project_template"
fission_project_template
├── conftest.py  # Fixtures for all tests.
├── db  # module contains db configurations
│   ├── dao  # Data Access Objects. Contains different classes to interact with database.
│   └── models  # Package contains different models for ORMs.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variabels should start with "FISSION_PROJECT_TEMPLATE_" prefix.

For example if you see in your "fission_project_template/settings.py" a variable named like
`random_parameter`, you should provide the "FISSION_PROJECT_TEMPLATE_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `fission_project_template.settings.Settings.Config`.

An exmaple of .env file:
```bash
FISSION_PROJECT_TEMPLATE_RELOAD="True"
FISSION_PROJECT_TEMPLATE_PORT="8000"
FISSION_PROJECT_TEMPLATE_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

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


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . run --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml --project-directory . down
```

For running tests on your local machine.
1. you need to start a database.

I prefer doing it with docker:
```
docker run -p "3306:43306" -e "MYSQL_PASSWORD=fission_project_template" -e "MYSQL_USER=fission_project_template" -e "MYSQL_DATABASE=fission_project_template" -e ALLOW_EMPTY_PASSWORD=yes bitnami/mysql:8.0.30
```


2. Run the pytest.
```bash
pytest -vv .
```


## SonarQube

If you want to run it in docker, simply run:

```bash
docker run --rm --net=host -v ${PWD}:/fission_project_template sonarsource/sonar-scanner-cli sonar-scanner -D sonar.projectBaseDir=/fission_project_template -D sonar.login=<project token generated from the below steps>
```

Open the browser and checkout localhost:9000 URL to open Sonarqube.

username: admin

password: admin

Add a project manually

Give a name to the project

Generate a new token for analysis purposes, so that you will not use user credentials for analysing.

Store the token somewhere safe as it will not be visible once the project is set up.

Choose the project main language, as in this case I have chosen “Other” cause the sonarqube-fastapi project’s main language is python. Then the OS will give you the sonar scanner command that we have to run to populate static code analysis.

Finally, the project is set up, we can see the project listing on the projects tab without any analysis.
