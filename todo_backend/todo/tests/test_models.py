from django.test import TestCase
from todo.models import Todo


class TodoModelTest(TestCase):
    def setUp(self):
        self.todo_data = {
            "title": "Test Todo",
            "description": "This is a test dodo task",
            "completed": False,
        }

        self.todo = Todo.objects.create(**self.todo_data)

    def tearDown(self):
        self.todo.delete()

    def test_todo_can_be_created(self):
        self.assertEqual(self.todo.title, self.todo_data["title"])
        self.assertEqual(self.todo.description, self.todo_data["description"])
        self.assertEqual(self.todo.completed, self.todo_data["completed"])

    def test_todo_returns_name_and_description(self):
        self.assertEqual(
            str(self.todo),
            f"{self.todo_data['title']} - {self.todo_data['description']}",
        )
