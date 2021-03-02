FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt --no-cache-dir

COPY . .

WORKDIR /opt/services/djangoapp/src/djangoapp
