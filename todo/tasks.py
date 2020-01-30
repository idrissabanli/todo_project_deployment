from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

@shared_task
def send_mail_to(mail=None):
    if not mail:
        mail = 'idris.sabanli@gmail.com'
    send_mail('celery task isleyir', 'celery', settings.EMAIL_HOST_USER, [mail])