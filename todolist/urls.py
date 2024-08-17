from django.urls import path
from .views import base_html

from .views import *


app_name = 'todolist'

urlpatterns = [
    path('html', base_html, name='base'),
    path('check_deadlines/', check_deadlines, name='check'),
    
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveView.as_view(), name='task-retrieve'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDestroyView.as_view(), name='task-destroy'),

    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveView.as_view(), name='comment-retrieve'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDestroyView.as_view(), name='comment-destroy'),

    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagRetrieveView.as_view(), name='tag-retrieve'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDestroyView.as_view(), name='tag-destroy')
]
