FROM python:3.9

WORKDIR /root

ENV TRANSITION_ID not_provided
ENV EXECUTION_ID not_provided

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY postprocess postprocess

ENTRYPOINT ["python", "-m", "postprocess"]