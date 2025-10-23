from django.views.generic import ListView
from .models import Book
from rest_framework import generics
from books.serializers import BookSerializer

class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


# DRF
class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer