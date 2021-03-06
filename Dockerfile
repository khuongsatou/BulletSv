FROM python:3.8-slim

WORKDIR /src/bullet

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "bullet.wsgi"]