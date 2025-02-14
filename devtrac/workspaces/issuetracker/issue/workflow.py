from ..packages.workflow.base.engine import WorkflowBase
from .models import Issue

class IssueWorkflow(WorkflowBase):
    status_transitions = [
        {
            "name": "open_to_progress",
            "display_name": "Start Progress",
            "description": "Move issue to in progress state",
            "from": "Open",
            "to": "In Progress",
            "confirmation_message": "Are you sure you want to start working on this issue?",
        },
        {
            "name": "open_to_resolved",
            "display_name": "Direct Resolution",
            "description": "Mark issue as resolved directly",
            "from": "Open",
            "to": "Resolved",
            "confirmation_message": "Are you sure you want to mark this issue as resolved?",
        },
        {
            "name": "progress_to_resolved",
            "display_name": "Mark Resolved",
            "description": "Mark this issue as resolved",
            "from": "In Progress",
            "to": "Resolved",
            "confirmation_message": "Are you sure you want to mark this issue as resolved?",
        },
        {
            "name": "progress_to_open",
            "display_name": "Move Back to Open",
            "description": "Move issue back to open state",
            "from": "In Progress",
            "to": "Open",
            "confirmation_message": "Are you sure you want to move this issue back to open?",
        },
        {
            "name": "resolved_to_progress",
            "display_name": "Reopen for Progress",
            "description": "Reopen this issue and move to in progress",
            "from": "Resolved",
            "to": "In Progress",
            "confirmation_message": "Are you sure you want to reopen this issue for progress?",
        },
        {
            "name": "resolved_to_open",
            "display_name": "Reopen as Open",
            "description": "Reopen this issue as open",
            "from": "Resolved",
            "to": "Open",
            "confirmation_message": "Are you sure you want to reopen this issue?",
        }
    ]

    def open_to_progress_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.IN_PROGRESS
        object_instance.save()

    def open_to_resolved_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.RESOLVED
        object_instance.save()

    def progress_to_resolved_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.RESOLVED
        object_instance.save()

    def progress_to_open_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.OPEN
        object_instance.save()

    def resolved_to_progress_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.IN_PROGRESS
        object_instance.save()

    def resolved_to_open_done(self, request, object_instance, transaction_obj):
        object_instance.status = Issue.OPEN
        object_instance.save()

    def after_transition(self, request, object_instance, from_status, to_status):
        """Hook called after any transition"""
        super().after_transition(request, object_instance, from_status, to_status)
        if hasattr(self, 'crud_view_instance'):
            self.crud_view_instance.refresh_table()

    class Meta:
        statuses = {
            "Open": {
                "color": "#3498db",  
                "label": "Open",
                "description": "Issue is newly created or reopened"
            },
            "In Progress": {
                "color": "#f1c40f",  
                "label": "In Progress",
                "description": "Work is actively being done on the issue"
            },
            "Resolved": {
                "color": "#2ecc71",  
                "label": "Resolved",
                "description": "Issue has been completed"
            }
        }
        model = Issue
        on_create_status = "Open"
