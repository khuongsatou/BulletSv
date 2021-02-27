FROM python:3

WORKDIR /Users/apple/Desktop/mai/BulletSv

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT wsgi