FROM python:3.11.1-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt