from django.urls import path
from .views import book_list, book_detail

urlpatterns = [
    path("", book_list, name="book-list"),
    path("<int:pk>/", book_detail, name="book-detail"),
]