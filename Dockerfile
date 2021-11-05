# syntax=docker/dockerfile:1

FROM python:3.8-slim

EXPOSE 3031

RUN apt-get update
RUN apt-get install -y build-essential

COPY . .

RUN pip3 install uwsgi
RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "uwsgi_conf.ini" ]
