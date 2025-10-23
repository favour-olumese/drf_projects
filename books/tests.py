from django.test import TestCase
from django.urls import reverse
from .models import Book
from rest_framework import status
from rest_framework.test import APITestCase


class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="The Beauty of Meekness",
            subtitle="The power inherent in being meek",
            author="Olumese Favour T. E.",
            isbn="1268871370134",
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "The Beauty of Meekness")
        self.assertEqual(self.book.subtitle, "The power inherent in being meek")
        self.assertEqual(self.book.author, "Olumese Favour T. E.")
        self.assertEqual(self.book.isbn, "1268871370134")

    def test_book_listview(self):
        response = self.client.get(reverse("book-home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "being meek")


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="The Power Inherent in Truth",
            subtitle="Truth, a principle of the righteous",
            author="Olumese Favour T. E.",
            isbn="1262792040233",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book-api"))
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book.title)