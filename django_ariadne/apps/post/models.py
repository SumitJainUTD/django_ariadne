from django.db import models


# Create your models here.

class Post(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
