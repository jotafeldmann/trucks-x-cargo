FROM python:3.8.1-buster AS base

WORKDIR trucksxcargo

COPY . .
RUN pip install pipenv
RUN pipenv install --system --dev --skip-lock