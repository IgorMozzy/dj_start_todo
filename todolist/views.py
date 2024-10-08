from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwner
from .models import Task, Comment, Tag
from todolist.serializers import TaskSerializer, CommentSerializer, TagSerializer


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .tasks import check_comment_for_bad_words, check_tasks_deadlines


@method_decorator(cache_page(60 * 15), name='get')
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def base_html(request):
    tasks = Task.objects.all()
    return render(request, template_name='todolist/base.html', context={'tasks': tasks})


def check_deadlines(request):
    check_tasks_deadlines.delay()
    return HttpResponse("Task triggered")


AUTH_MODE = [IsAuthenticated]


# Task Views
class TaskCreateView(generics.CreateAPIView):
    """Task creating"""
    permission_classes = AUTH_MODE
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(generics.ListAPIView):
    """Task list view"""
    permission_classes = AUTH_MODE
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveView(generics.RetrieveAPIView):
    """Task detailed view"""
    permission_classes = AUTH_MODE
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateView(generics.UpdateAPIView):
    """Task update"""
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyView(generics.DestroyAPIView):
    """Task deletion"""
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# Comment Views
class CommentCreateView(generics.CreateAPIView):
    """Comment creation"""
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        comment = serializer.save()
        check_comment_for_bad_words.delay(comment.id)


class CommentListView(generics.ListAPIView):
    """Comments list view"""
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveView(generics.RetrieveAPIView):
    """Comment detailed view"""
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    """Comment update"""
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyView(generics.DestroyAPIView):
    """Comment deletion"""
    permission_classes = AUTH_MODE
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Tag Views
class TagCreateView(generics.CreateAPIView):
    """Tag creation"""
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagListView(generics.ListAPIView):
    """Tags list view"""
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveView(generics.RetrieveAPIView):
    """Tag detailed view"""
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagUpdateView(generics.UpdateAPIView):
    """Tag update"""
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDestroyView(generics.DestroyAPIView):
    """Tag deletion"""
    permission_classes = AUTH_MODE
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
