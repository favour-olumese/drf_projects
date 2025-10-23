from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer


class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailAPIView(generics.RetrieveAPIView):
    queryset = Todo
    serializer_class = TodoSerializer