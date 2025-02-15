from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from ..packages.crud.base import BaseCrudView
from .models import Issue
from .tables import IssueTable
from .forms import IssueForm
from .workflow import IssueWorkflow
from .bgtasks import send_assignment_email

class IssueCrudView(BaseCrudView):
    page_title = "Issues"
    add_btn_title = "Add Issue"
    table = IssueTable
    form = IssueForm
    workflow = IssueWorkflow

    def form_valid(self, form):
        response = super().form_valid(form)
        issue = form.instance

        if issue.assignee:
            try:
                send_assignment_email.delay(issue.id, issue.assignee.email)
                messages.success(self.request, f"Assignment email will be sent to {issue.assignee.email}")
            except Exception as e:
                messages.error(self.request, f"Failed to queue email: {str(e)}")
        
        return response

    def display_add_button_check(self, request):
        return True


