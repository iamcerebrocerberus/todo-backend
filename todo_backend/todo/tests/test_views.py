from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoListViewTest(APITestCase):
    def setUp(self):
        self.todo_data = [
            {"title": "Test 1", "description": "Test data 1", "completed": False},
            {"title": "Test 2", "description": "Test data 2", "completed": False},
            {"title": "Test 3", "description": "Test data 3", "completed": True},
        ]

        [Todo.objects.create(**todo) for todo in self.todo_data]

    def test_get_all_todo(self):
        response = self.client.get(reverse("todo"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), len(self.todo_data))

        # checking if serialized data matches data in database
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_todo(self):
        new_todo = {
            "title": "New Todo",
            "description": "Newly created todo",
            "completed": False,
        }

        response = self.client.post(reverse("todo"), data=new_todo)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Todo.objects.filter(title=new_todo["title"]).exists())
