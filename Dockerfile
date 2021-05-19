FROM python:3.9-buster
WORKDIR /var/app
COPY shop/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY shop .

EXPOSE 8000
