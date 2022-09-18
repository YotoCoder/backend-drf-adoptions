FROM python:alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt


# RUN python manage.py collectstatic --no-input