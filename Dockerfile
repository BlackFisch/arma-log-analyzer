# syntax=docker/dockerfile:1

FROM python:3.10-bullseye

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD [ "python3", "run_server.py"]
