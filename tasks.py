from celery import Celery
from time import sleep


app = Celery('tasks',broker='amqp://localhost',backend='db+sqlite:///db.sqlite3')

@app.task
def reverse(text):
    sleep(20)
    return text[::-1]

print("123")