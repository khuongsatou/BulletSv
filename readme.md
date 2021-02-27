python -m django --version
django-admin startproject mysite
python manage.py runserver
python manage.py runserver 0:8000
python manage.py startapp polls

python manage.py makemigrations
python manage.py migrate

// Settings:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Tạo trong App file static.
chứa 1 tấm ảnh.

# Chạy lệnh:
python manage.py collectstatic

# Tạo file requirements.txt
requests
Django

# Tạo file runtime.txt
python-3.8.7

# Xem tất cả remove.
git remote -v

# Chỉ định remote.
heroku git:remote -a ten_remote

# Chỉ định ngôn ngữ python.
heroku buildpacks:set heroku/python


# Tạo git
git init

# Kiểm tra có thay đổi hay không
git status


git add .
git commit -m "init"

# Đưa lên heroku.
git push heroku main

# Lệnh install tất cả thư viện
pip install -r requirements.txt

# Lệnh tạo venv
python3 -m venv venv

# Lên active
source venv/bin/activate

# Lệnh chạy server khi deloy lên heroku
gunicorn bullet.wsgi

# Kiểm tra xem có lỗi không trước khi upload
heroku local

https://help.heroku.com/GDQ74SU2/django-migrations


https://www.youtube.com/watch?v=zF_DroDICaM


# log.
heroku logs -n 1500

# Error:  account limit
heroku restart
Khác
----
$ heroku plugins:install heroku-builds
$ heroku builds:cancel
$ heroku restart

# Cài docker cho macos. docker.com 
# Kiểm tra docker có run hay chưa.
docker ps


#  docker run -d -p 5672:5672 rabbitmq
# Để lấy broker
# app = Celery('tasks',broker='amqp://localhost',backend='db+sqlite:///db.sqlite3')

# celery xem task log sau khi đã có docker
celery -A tasks worker --loglevel=info
https://stackoverflow.com/questions/18133249/django-celery-cannot-connect-to-amqp-guest127-0-0-80005672


# Truy cập sqlite3
sqlite3 db.sqlite3

# Xem tất cả table.
.tables
.exit

# select * from celery_taskmeta; task lưu vào database local

#  python.
#  from tasks import reverse
#  result=reverse.delay('Khuong')
#  result.status
#  result.get






python manage.py createsuperuser

# Django log selery
# celery -A bullet  worker -l info

# Bật rabbitmq
sudo systemctl start rabbitmq-server
# Stop rabbitmq
sudo rabbitmqctl stop