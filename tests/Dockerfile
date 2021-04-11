FROM python:3

RUN pip install --upgrade pip && \
    pip install selenium
RUN apt-get update
RUN apt-get install -y vim less

ENV TZ "Asia/Tokyo"

WORKDIR /tests/src