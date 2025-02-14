from django.contrib.auth.mixins import LoginRequiredMixin
from ..packages.crud.base import BaseCrudView
from .models import Issue
from .tables import IssueTable
from .forms import IssueForm
from .workflow import IssueWorkflow

class IssueCrudView(BaseCrudView):
    page_title = "Issues"
    add_btn_title = "Add Issue"
    table = IssueTable
    form = IssueForm
    workflow = IssueWorkflow

    def display_add_button_check(self, request):
        return True


