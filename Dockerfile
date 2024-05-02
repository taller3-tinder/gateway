FROM python:3.11-alpine

WORKDIR /code

RUN apk update && \
    apk add --no-cache git && \
    rm -rf /var/cache/apk/*

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    rm -rf /root/.cache && \
    apk del git

COPY ./app /code/app

CMD uvicorn app.main:app --host=0.0.0.0 --port=${PORT}
