from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets

from todo_backend.models import Task
from todo_backend.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer


class HomeView(generic.View):
    def get(self, request):
        return HttpResponse(render(request, 'index.html'))


def create_task(requests):
    x = Task.objects.create(title='Task 2', done=False)
    return HttpResponse(f'created. id = {TaskSerializer(x).data}')


def list_tasks(requests):
    t = Task.objects.all()
    serialized = TaskSerializer(t, many=True).data
    return HttpResponse(f"Tasks: {serialized}")
