# The base image we want to inherit from
FROM python:3.10-slim-buster as development_build

ARG DJANGO_ENV

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_VERSION=1.0.5 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# Install System deps:
RUN apt-get update \
  && apt-get install --no-install-recommends -y \
    bash \
    build-essential \
    curl \
    gettext \
    git \
    libpq-dev \
    wget \
  # Cleaning cache:
  && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION" && poetry --version

COPY ./poetry.lock ./pyproject.toml ./requirements.txt ./
# set work directory
WORKDIR /src/

# # Install python dependencies
RUN pip install --upgrade pip --no-cache-dir \
    && pip install --no-cache-dir -r /requirements.txt

# RUN python3 -m pip install -r requirements.txt
# Install dependencies:
RUN poetry install 

# copy project
COPY ./src/ /src/

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]