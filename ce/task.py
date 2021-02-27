from celery import shared_task,Celery
from time import sleep
# from api.src.views.notify import handle_notification
app = Celery()

@shared_task
def add(x, y):
    print("123")
    sleep(20)
    return x + y

# @app.task
# def add(x, y):
#     print("123")
#     sleep(2)
#     # handle_notification()
#     return x + y


@shared_task
def mul(x, y):
    print("456")
    return x * y


@shared_task
def xsum(numbers):
    print("789")
    return sum(numbers)

