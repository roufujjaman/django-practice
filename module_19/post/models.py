from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=150,
    )
    slug = models.SlugField()


class Post(models.Model):
    title = models.CharField()
    author = models.ForeignKey(
        User
    )
    content = models.TextField()
    category = models.ForeignKey(
        Category
    )