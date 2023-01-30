FROM python:3.10.9-alpine

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requeriments.txt .

RUN pip install -r requeriments.txt

COPY . .