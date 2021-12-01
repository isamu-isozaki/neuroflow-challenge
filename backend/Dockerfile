FROM python:3.8-slim-buster

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libffi-dev python3-dev gcc
RUN apt-get install -y python-psycopg2
RUN pip3 install --upgrade pip \
  && pip3 install --upgrade pipenv \
  && pip3 install --upgrade -r /app/requirements.txt

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . /app

CMD python3 run.py