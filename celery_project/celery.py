from __future__ import absolute_import, unicode_literals
from celery.schedules import timedelta
from celery import Celery
from django.conf import settings
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_project.settings")

app = Celery("celery_project")

app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings, namespace="CELERY")

# Celery Beat settings

app.conf.beat_schedule = {
    'send-email-every-10-seconds': {
        'task': 'celery_project.tasks.send_email_func',
        'schedule': timedelta(seconds=10),
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
