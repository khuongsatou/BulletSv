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


source venv/bin/activate

pip install -r requirements.txt

python3 -m venv venv
source venv/bin/activate