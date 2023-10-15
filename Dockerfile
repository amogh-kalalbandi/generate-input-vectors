FROM python:3.9.2-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /application
COPY requirements.txt /application/
RUN pip install -r requirements.txt
COPY . /application/
