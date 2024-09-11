from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task

class TaskAPITest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

        self.task = Task.objects.create(
            title="Sample Task",
            description="Task description",
            completed=False,
            owner=self.user
        )

    def test_get_task_list(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            "title": "New Task",
            "description": "Task created via API",
            "completed": False,
            "owner": self.user.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
