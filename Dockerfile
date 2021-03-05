FROM python:latest

WORKDIR /Users/apple/Desktop/mai/BulletSv


COPY . .

RUN pip install -r requirements.txt

#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
# add and run as non-root user

CMD gunicorn bullet.wsgi