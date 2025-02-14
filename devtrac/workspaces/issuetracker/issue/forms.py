from ..packages.crud.forms import BaseForm
from ..packages.crud.form_fields import ModelField

from .models import Issue

class IssueForm(BaseForm):
    title = ModelField(placeholder="Enter Title ", required=True, required_msg="This field is required.")
    description = ModelField(placeholder="Enter description", required=True, required_msg="This field is required.")
    assignee = ModelField(placeholder="Select an assignee", required=False)
    status = ModelField(placeholder="Select status of issue", required=False)

    class Meta:
        title = "Issue"
        model = Issue
        fields = "__all__" 
