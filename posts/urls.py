from django.urls import path, include
from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]