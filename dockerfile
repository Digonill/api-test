FROM python:3.8

WORKDIR /opt/demo

COPY ./ ./

RUN pip install -r requirements.txt

ENV PYTHON_ENV=dev

ENTRYPOINT python app.py