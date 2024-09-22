from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from celery_project import settings


@shared_task(bind=True)
def task_func():
    for i in range(10):
        print(i)
    return "Task Completed Successfully! Done"


@shared_task
def send_email_func():
    User = get_user_model()
    users = User.objects.all()
    for user in users:
        mail_subject = 'Hi! Celery Testing Team'
        message = 'This is a test email for Celery Testing Team on the site!!'
        to_email = user.email

        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return 'Email sent successfully! Done👍✅'
