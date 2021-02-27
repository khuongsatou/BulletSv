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

// Tạo trong App file static.
chứa 1 tấm ảnh.

// Chạy lệnh:
python manage.py collectstatic

// Tạo file requirements.txt
requests
Django

// Tạo file runtime.txt
python-3.8.7

// Xem tất cả remove.
git remote -v

// Chỉ định remote.
heroku git:remote -a ten_remote

// Chỉ định ngôn ngữ python.
heroku buildpacks:set heroku/python


// Tạo git
git init

// Kiểm tra có thay đổi hay không
git status


git add .
git commit -m "init"

// Đưa lên heroku.
git push heroku main

// Lệnh install tất cả thư viện
pip install -r requirements.txt

// Lệnh tạo venv
python3 -m venv venv

// Lên active
source venv/bin/activate

// Lệnh chạy server khi deloy lên heroku
gunicorn bullet.wsgi

// Kiểm tra xem có lỗi không trước khi upload
heroku local

https://help.heroku.com/GDQ74SU2/django-migrations


https://www.youtube.com/watch?v=zF_DroDICaM


// log.
heroku logs -n 1500

python manage.py migrate django_celery_results

# Docker.
# Liệt kê các file đang chạy
docker ps
docker ps -a
docker ps -all

# Lệnh chạy 1 images trong container với network publish là 5672
# Thực tế thì là map giữa port localhost với port của container
docker run -d -p 5672:5672 rabbitmq

# Log container:
docker logs --follow your_name_container

# xem ls volume : fea865d4e0a4020e6d536412ee414561ec1718d435e6bee1226b83c4a6be7634
docker volume ls

# Dùng docker run.
docker stop your_name_container


# tải image: 
docker pull ten_img
# build một image từ Dockerfile và context: Context ở đây là một tập file được xác đinh bởi đường dẫn hoặc url cụ thể. Ta có thể sử dụng thêm tham số -t để gắn nhãn cho image.
docker build -t your_name_container

# xóa.
docker container rm your_name_container

release: docker run -d -p 5672:5672 rabbitmq

heroku container:login

heroku container:push web

heroku open
