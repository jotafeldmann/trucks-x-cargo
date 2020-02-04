FROM python:3.8.1-buster AS base

RUN apt-get update
WORKDIR .
EXPOSE 8000

COPY . .
RUN pip install pipenv
RUN pipenv install --system --dev --skip-lock