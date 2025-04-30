from rest_framework import serializers

from todo_backend.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'first_name', 'surname', 'description', 'done']
