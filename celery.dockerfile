FROM python:3.6

RUN mkdir -p /code
WORKDIR /code
ADD . .

RUN pip install -r requirements.txt

CMD [ "celery", "-A", "todo_project", "worker", "--beat", "--scheduler", "django", "--loglevel=info" ]