from celery import shared_task
from time import sleep

from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
              'This is proof the task worked!',
              'monbiswas909@gmail.com',
              ['abuh69377@gmail.com'])
    return None
