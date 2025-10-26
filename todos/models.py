from django.db import models
from django.conf import settings


class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    private = models.BooleanField(default=True)

    def __str__(self):
        return self.title