from __future__ import absolute_import, unicode_literals
import os
from celery import Celery 
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'email_campaign_manager.settings')

app = Celery('email_campaign_manager')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
  'send-mail-every-day-at-8am': {
    'task': 'campaign_manager.tasks.send_ad_mails',
    'schedule': crontab(hour=8, minute=0)
  }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
  print(f'Request: {self.request!r}')
