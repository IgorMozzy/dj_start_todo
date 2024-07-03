from django.shortcuts import render
from .models import Task

# Create your views here.


def base(request):
    tasks = Task.objects.all()
    return render(request, template_name='todolist/base.html', context={'tasks': tasks})
