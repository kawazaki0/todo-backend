import json
from unittest import skip

from django.test import TestCase
from rest_framework.test import APIClient

from todo_backend.models import Task


class TaskTestCase(TestCase):
    def test_task_is_retrieved_by_id(self):
        test_created = Task.objects.create(title="test_title",
                                           description="test_desc",
                                           done=False)

        task = Task.objects.get(id=test_created.id)

        self.assertEqual(task.title, "test_title")
        self.assertEqual(task.description, "test_desc")
        self.assertEqual(task.done, False)


class TaskControllerTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TaskControllerTestCase, cls).setUpClass()
        cls.client = APIClient()

    def _create_task(self, title="test_title", description="test_desc",
                     done=False):
        task_data = {"title": title, "description": description, "done": done}
        request = self.client.post('/todo/api/v1/tasks',
                                   json.dumps(task_data),
                                   content_type='application/json')
        task_id = request.json()['id']
        return Task.objects.get(id=task_id)

    def test_tasks_are_listed(self):
        self._create_task()
        task_count = Task.objects.count()

        response = self.client.get('/todo/api/v1/tasks',
                                   content_type='application/json')

        self.assertEqual(task_count, len(response.json()))

    def test_task_is_retrieved(self):
        task_title = "title"
        task = self._create_task(title=task_title)

        response = self.client.get(f'/todo/api/v1/tasks/{task.id}',
                                   content_type='application/json')

        self.assertEqual(task_title, response.json()['title'])

    def test_task_is_created(self):
        task_data = {"title": "title",
                     "description": "desc",
                     "done": True}

        task = self._create_task(**task_data)

        self.assertEqual(task.title, task_data['title'])
        self.assertEqual(task.description, task_data['description'])
        self.assertEqual(task.done, task_data['done'])

    def test_task_is_updated(self):
        task = self._create_task(title="title")
        title_changed = "title_changed"

        self.client.put(f'/todo/api/v1/tasks/{task.id}',
                        json.dumps({"title": title_changed,
                                    "description": task.description,
                                    "done": task.done}),
                        content_type='application/json')
        task = Task.objects.get(id=task.id)

        self.assertEqual(task.title, title_changed)

    def test_task_is_deleted(self):
        task = self._create_task(title="title")

        self.client.delete(f'/todo/api/v1/tasks/{task.id}',
                           content_type='application/json')

        self.assertFalse(Task.objects.filter(id=task.id).exists())
