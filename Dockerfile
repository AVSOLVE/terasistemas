####
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .tmp-build-depsgdal  \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    g++ \
    py-pip \
    build-base \
    cmake \
    postgresql-dev \
    py3-psycopg2 \
    pkgconfig \
    cargo

RUN mkdir /code
# RUN mkdir /code/staticfiles
WORKDIR /code
COPY . /code

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install 
EXPOSE 80 


