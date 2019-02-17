FROM python:3-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /code/docker
WORKDIR /code

RUN \
  apk add --no-cache postgresql-libs && \
  apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/main openssl && \
  apk add --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing gdal-dev geos-dev && \
  apk add --no-cache --virtual \
  .build-deps \
  gcc \
  musl-dev \
  postgresql-dev

ENTRYPOINT /code/docker/docker-entrypoint.sh
