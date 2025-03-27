from rest_framework import viewsets

from todo_backend.models import Task
from todo_backend.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('id')
    serializer_class = TaskSerializer
