from celery import shared_task
from time import sleep
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    sleep(10)
    msg_html = render_to_string('templates/mail.html', None)
    for x in range(2):
        send_mail('Celery Task Worked!'+str(x),
                  'Celery is working totally fine',
                  'monbiswas909@gmail.com',
                  ['danielkaushik1@gmail.com'])
    return None
