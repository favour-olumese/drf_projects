from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "Great Strides",
            body = "Great strides begins with a step.",
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "Great Strides")
        self.assertEqual(self.todo.body, "Great strides begins with a step.")
        self.assertEqual(str(self.todo), "Great Strides")

    def test_api_listview(self):
        response = self.client.get(reverse("todo-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(reverse(
            'todo-detail', kwargs={'pk': self.todo.id}),
            format='json',
            )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "Great Strides")
