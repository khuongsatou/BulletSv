from celery import shared_task

from django.core.mail import send_mail
from time import sleep
from home.notify import handle_notification

@shared_task
def sleepy(duration):
    sleep(duration)
    handle_notification()
    return None

@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
    'This is proof the task worked!',
    'support@prettyprinted.com',
    ['sasa@be-breathtaking.net'])

    return None