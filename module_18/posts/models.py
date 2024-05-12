from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(
        max_length=150
    )
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title