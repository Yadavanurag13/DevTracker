from celery import shared_task
from django.core.mail import send_mail  # Correct function for sending emails
from .models import Issue
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_assignment_email(issue_id, assignee_email):
    try:
        issue = Issue.objects.get(id=issue_id)

        subject = f'You have been assigned to issue #{issue.id}'
        message = f'''
        You have been assigned to the following issue:
        
        Title: {issue.title}
        Description: {issue.description}
        Status: {issue.status}
        
        Please review and take necessary action.
        '''

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[assignee_email],
            fail_silently=False,
        )

        logger.info(f"Assignment email sent successfully for issue #{issue_id} to {assignee_email}")
        return f"Email sent successfully to {assignee_email}"
    except Issue.DoesNotExist:
        logger.error(f"Failed to send assignment email: Issue #{issue_id} not found")
        return f"Issue {issue_id} not found"
    except Exception as e:
        logger.error(f"Failed to send assignment email for issue #{issue_id}: {str(e)}")
        return f"Failed to send email: {str(e)}"