from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer
from .permissions import IsAuthorOrIsNotPrivate


class TodoListAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthorOrIsNotPrivate,]

    def get_queryset(self):
        # Base queryset
        queryset = Todo.objects.all()

        # Hide lists that are marked as private
        queryset = queryset.filter(private=False)

        # Also show user’s own private todos
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset | Todo.objects.filter(author=user)

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class TodoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo
    serializer_class = TodoSerializer
    permission_classes = [IsAuthorOrIsNotPrivate,]