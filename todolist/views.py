from django.contrib.auth import authenticate
from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.permissions import IsOwner
from .models import Task, Comment, Tag
from todolist.serializers import TaskSerializer, CommentSerializer, TagSerializer


from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


@method_decorator(cache_page(60 * 15), name='get')
class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def base_html(request):
    tasks = Task.objects.all()
    return render(request, template_name='todolist/base.html', context={'tasks': tasks})


class TaskViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class TagViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# # Task Views
# class TaskCreateView(generics.CreateAPIView):
#     """Класс-контроллер для создания объектов модели Task"""
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class TaskListView(generics.ListAPIView):
#     """Класс-контроллер для просмотра списка объектов модели Task"""
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# class TaskRetrieveView(generics.RetrieveAPIView):
#     """Класс-контроллер для просмотра отдельного объекта модели Task"""
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class TaskUpdateView(generics.UpdateAPIView):
#     """Класс-контроллер для редактирования объектов модели Task"""
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
# class TaskDestroyView(generics.DestroyAPIView):
#     """Класс-контроллер для удаления объектов модели Task"""
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#
#
# # Comment Views
# class CommentCreateView(generics.CreateAPIView):
#     """Класс-контроллер для создани объектов модели Comment"""
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
# class CommentListView(generics.ListAPIView):
#     """Класс-контроллер для просомтра списка объектов модели Comment"""
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentRetrieveView(generics.RetrieveAPIView):
#     """Класс-контроллер для просмотра отдельного объекта модели Comment"""
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
# class CommentUpdateView(generics.UpdateAPIView):
#     """Класс-контроллер для редактирования объектов модели Comment"""
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
# class CommentDestroyView(generics.DestroyAPIView):
#     """Класс-контроллер для удаления объектов модели Comment"""
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# # Tag Views
# class TagCreateView(generics.CreateAPIView):
#     """Класс-контроллер для создани объектов модели Tag"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
# class TagListView(generics.ListAPIView):
#     """Класс-контроллер для просомтра списка объектов модели Tag"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
#
# class TagRetrieveView(generics.RetrieveAPIView):
#     """Класс-контроллер для просмотра отдельного объекта модели Tag"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
# class TagUpdateView(generics.UpdateAPIView):
#     """Класс-контроллер для редактирования объектов модели Tag"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
#
# class TagDestroyView(generics.DestroyAPIView):
#     """Класс-контроллер для удаления объектов модели Comment"""
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer
