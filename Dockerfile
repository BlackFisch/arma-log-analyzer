# syntax=docker/dockerfile:1

FROM python:3.10-slim-bullseye

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD [ "python3", "run_server.py"]
