from zango.apps.dynamic_models.models import DynamicModelBase
from zango.apps.appauth.models import AppUserModel
from zango.apps.dynamic_models.fields import ZForeignKey
from django.db import models


class Issue(DynamicModelBase):
    OPEN = "Open"
    IN_PROGRESS = "In_progress"
    RESOLVED = "Resolved"

    ISSUE_STATUS_CHOICES = [
        (OPEN, "Open"),
        (IN_PROGRESS, "In progress"),
        (RESOLVED, "Resolved")
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=ISSUE_STATUS_CHOICES, default=OPEN)
    assignee = ZForeignKey(AppUserModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
