FROM python:3.8

EXPOSE 5000

WORKDIR /app

RUN pip install -U Flask

COPY ./app.py app.py
COPY ./data data

ENTRYPOINT flask run --host=0.0.0.0
