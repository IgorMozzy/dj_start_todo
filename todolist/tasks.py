from datetime import datetime

from celery import shared_task
from .models import Comment, Task
import re


@shared_task
def check_comment_for_bad_words(comment_id):
    bad_words = ['продать', 'крипта', 'ставки']
    comment = Comment.objects.get(id=comment_id)
    original_text = comment.text

    for word in bad_words:
        comment.text = re.sub(rf'\b{word}\b', '###', comment.text, flags=re.IGNORECASE)

    if comment.text != original_text:
        comment.save()


@shared_task
def check_tasks_deadlines():
    tasks = Task.objects.all()
    today = datetime.now().date()

    for task in tasks:
        if task.deadline and task.deadline.date() <= today:
            task.deadline = datetime.combine(today, task.deadline.time())
            task.save()
