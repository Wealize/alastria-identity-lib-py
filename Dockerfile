FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN pip install 'poetry==1.0.5'
COPY pyproject.toml poetry.lock ./
RUN poetry install
