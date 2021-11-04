# syntax=docker/dockerfile:1

FROM python:3-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY run_server.py /app/run_server.py
COPY app.py /app/app.py
COPY . /app

EXPOSE 8000

CMD python run_server.py
