# syntax=docker/dockerfile:1

FROM alpine:3.7
EXPOSE 8000

RUN apk add --no-cache \
    uwsgi-python3 \
    python3\
    gcc

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "uwsgi", "uwsgi_conf.ini" ]
