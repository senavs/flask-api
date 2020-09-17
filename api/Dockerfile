FROM python:3.8-alpine

RUN mkdir /code
COPY . /code
WORKDIR /code

RUN pip3 install .

CMD ["gunicorn", "-c", "python:project.wsgi", "project.app:app"]