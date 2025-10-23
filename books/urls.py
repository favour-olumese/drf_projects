from django.urls import path
from .views import BookListView, BookAPIView

urlpatterns = [
    path("", BookListView.as_view(), name="book-home"),
    path("api/", BookAPIView.as_view(), name="book-api")
]