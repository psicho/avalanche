FROM python:3.9.12-alpine

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /application
COPY . /application

RUN apk upgrade \
 && apk add gcc musl-dev zlib-dev jpeg-dev python3-dev py3-setuptools

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

