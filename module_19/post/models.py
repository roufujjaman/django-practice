from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=150,
    )
    slug = models.SlugField()


class Post(models.Model):
    title = models.CharField(
        max_length=150
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )