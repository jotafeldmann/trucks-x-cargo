FROM python:3.8.1-buster

ARG WORKDIR=trucksxcargo

WORKDIR ${WORKDIR}

COPY . .

RUN pip install pipenv
RUN pipenv install --system --dev --skip-lock