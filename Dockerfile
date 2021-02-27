FROM rabbitmq

WORKDIR /Users/apple/Desktop/mai/BulletSv

COPY . .

CMD gunicorn --bind 0.0.0.0:5672 wsgi