FROM python:3.9

ENV PYTHONBUFFERED 1

ONBUILD RUN set -ex && mkdir /app

RUN apt-get update

RUN apt-get install -y locales

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app

RUN locale-gen es_CL.UTF-8
ENV LANG es_CL.UTF-8
ENV LANGUAGE es_CL:es
ENV LC_ALL es_CL.UTF-8

ADD . /app
COPY . /app

