web: gunicorn bullet.wsgi
release: python manage.py makemigrations
release: python manage.py migrate
release: python manage.py migrate django_celery_results
release: celery -A bullet worker -l info
