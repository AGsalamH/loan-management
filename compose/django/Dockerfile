FROM python:3.12-alpine3.19
LABEL maintainer="AGsalamH"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/

RUN apk add  --update --no-cache\
    --virtual .tmp_build_deps \
    postgresql-dev\
    musl-dev\
    build-base\
    zlib zlib-dev linux-headers && \
    apk add --update --no-cache postgresql-client && \
    pip install -r requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp_build_deps

COPY . /app
