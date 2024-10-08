from django.db import models

from users.models import User


# Create your models here.


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(null=True, blank=True, max_length=25)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag', related_name='tasks')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Completion at')
    description = models.TextField(null=True, blank=True, verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.pk} on {self.created_at}'  # primary key = id


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
