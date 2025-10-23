from django.urls import path
from .views import TodoListAPIView, TodoDetailAPIView


urlpatterns = [
    path('api/', TodoListAPIView.as_view(), name='todo-list'),
    path('api/<int:pk>', TodoDetailAPIView.as_view(), name='todo-detail'),
]