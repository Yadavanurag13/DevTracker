from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol

from .models import Issue
from .forms import IssueForm

class IssueTable(ModelTable):
    id = ModelCol(display_as='ID', sortable=True, searchable=True)
    title = ModelCol(display_as='Title', sortable=True, searchable=True)
    description = ModelCol(display_as='Description', sortable=True, searchable=True)
    status = ModelCol(display_as='Status', sortable=True, searchable=True)
    assignee = ModelCol(display_as='Assignee',sortable=True,searchable=True,)
    created_at = ModelCol(display_as='Created',sortable=True,date_format='%Y-%m-%d %H:%M', searchable=True)

    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Issue",
            "type": "form",
            "form": IssueForm,
        },
    ]

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'status', 'assignee', 'created_at']
        row_selector = {'enabled': False, 'multi': False}
