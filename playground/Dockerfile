ARG PYTHON_VER=3.8

FROM python:${PYTHON_VER}

WORKDIR /app

RUN git clone https://github.com/ashb/requests.git

WORKDIR /app/requests

RUN git checkout charset_normalizer
RUN python setup.py install

WORKDIR /app

COPY ./app.py app.py

RUN python -m requests.help

ENTRYPOINT python app.py
