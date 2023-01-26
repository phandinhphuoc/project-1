from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + '|' + str(self.author)

class tracnghiem(models.Model):
    title = models.TextField(max_length=255)
    dA = models.TextField()
    dB = models.TextField()

    def __str__(self):
        return self.title