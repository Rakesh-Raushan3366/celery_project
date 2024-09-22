from django.http import HttpResponse
from django.shortcuts import render
from celery_project.tasks import task_func
from celery_project.tasks import send_email_func


# Create your views here.


def test(request):
    task_func.delay()
    return HttpResponse("Done!")


def send_email_to_all_func(request):
    send_email_func.delay()
    return HttpResponse("Email sent successfully!")
