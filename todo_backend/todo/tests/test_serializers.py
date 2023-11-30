from todo.serializers import TodoSerializer
from rest_framework.test import APITestCase

from todo.models import Todo


class TodoSerializerTest(APITestCase):
    def setUp(self):
        self.todo_data = {
            "title": "Test todo",
            "description": "This is just for testing",
            "completed": True,
        }

        self.todo_instance = Todo.objects.create(**self.todo_data)

    def test_serialized_todo(self):
        serializer = TodoSerializer(instance=self.todo_instance)
        serialized_data = serializer.data
        for field in ("title", "description", "completed"):
            self.assertTrue(serialized_data[field], self.todo_data[field])

    def test_deserialize_todo_valid_data(self):
        serializer = TodoSerializer(data=self.todo_data)
        self.assertTrue(serializer.is_valid())
        todo_instance = serializer.save()
        for field in ("title", "description", "completed"):
            self.assertTrue(getattr(todo_instance, field), self.todo_data[field])

    def test_deserialize_todo_misisng_required_field(self):
        data_without_title = {"description": "Incoming todo"}
        serializer = TodoSerializer(data=data_without_title)
        self.assertFalse(serializer.is_valid())

    def test_deserialize_todo_invalid_boolearn_field(self):
        data_invalid_completed = {
            "title": "Test todo",
            "description": "This have invalid bool",
            "completed": "not a boolean",
        }
        serializer = TodoSerializer(data=data_invalid_completed)
        self.assertFalse(serializer.is_valid())
