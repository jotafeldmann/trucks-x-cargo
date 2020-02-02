FROM python:3.8.1-buster AS base

RUN apt-get update
WORKDIR /trucksxcargo
EXPOSE 8000

COPY Pipfile .
RUN pip install pipenv

FROM base AS dependencies
RUN pipenv install --system --skip-lock

FROM base AS development
RUN apt-get -y install inotify-tools
RUN make install
COPY . .

FROM dependencies AS production
COPY ../src src