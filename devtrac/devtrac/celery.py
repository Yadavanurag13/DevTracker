from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devtrac.settings.settings')

# Initialize Celery app
app = Celery('devtrac')

# Configure Celery using settings from Django settings
class CeleryConfig:
    # Import Celery settings from Django settings
    broker_url = settings.CELERY_BROKER_URL
    result_backend = settings.CELERY_RESULT_BACKEND
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']
    enable_utc = True

app.config_from_object(CeleryConfig)

# Auto-discover tasks from all installed apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')