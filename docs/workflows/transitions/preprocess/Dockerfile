FROM python:3.11-alpine

WORKDIR /root

ENV TRANSITION_ID not_provided
ENV EXECUTION_ID not_provided

COPY requirements.txt .

RUN apk add build-base openssl-dev
RUN pip install -r requirements.txt

COPY preprocess preprocess

ENTRYPOINT ["python", "-m", "preprocess"]