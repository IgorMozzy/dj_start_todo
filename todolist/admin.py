from django.contrib import admin

# Register your models here.

# from todolist import models

# admin.site.register(models.Task)

from .models import Task, Comment, Tag


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # removes additional empty fields


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'deadline', 'description')
    search_fields = ('title', 'description')
    list_filter = ('deadline', 'author', 'tags')

    inlines = [
        CommentInline,
    ]


admin.site.register(Comment)
admin.site.register(Tag)
