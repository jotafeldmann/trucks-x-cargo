FROM python:3.8.1-buster AS base

COPY . .
RUN pip install pipenv
RUN pipenv install --system --dev --skip-lock