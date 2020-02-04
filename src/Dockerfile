FROM python:3.8.1-buster

WORKDIR trucksxcargo

COPY . .
RUN pip install pipenv
RUN pipenv install --system --dev --skip-lock