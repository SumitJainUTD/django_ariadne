from django.contrib import admin

# Register your models here.
from django_ariadne.apps.post.models import Post
# from .models import Post

admin.site.register(Post)
