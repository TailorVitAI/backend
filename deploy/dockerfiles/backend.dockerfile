# Use a base image
FROM python:3.11-slim AS base
LABEL maintainer="mahdi.massahi@gmail.com"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"

# Compile stage
FROM base AS compile-image
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc libpq-dev python3-dev \
    && python -m venv /opt/venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY deploy/requirements/base.txt .
RUN . /opt/venv/bin/activate && pip install --no-cache-dir -U pip wheel \
    && pip install --no-cache-dir -r ./base.txt

# Build stage
FROM base AS build-image
COPY --from=compile-image /opt/venv /opt/venv
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget nano curl python3-psycopg2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code/.media/
RUN mkdir -p /code/logs/
VOLUME /code/logs/
COPY core /code/core
COPY apps /code/apps
COPY .media /code/.media
COPY manage.py /code/manage.py
COPY deploy/config/gunicorn.conf.py /code/gunicorn.conf.py
COPY deploy/entrypoints/backend.sh /code/entrypoints/backend.sh
RUN sed -i 's/\r$//g' /code/entrypoints/backend.sh \
    && chmod +x /code/entrypoints/backend.sh

WORKDIR /code/
ENTRYPOINT ["/code/entrypoints/backend.sh"]
HEALTHCHECK --start-period=5s --interval=15s --timeout=5s --retries=5 CMD curl --fail https://localhost/ || exit 1
