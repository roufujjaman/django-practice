from django.db import models
from categories.models import Categories

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateField()
    categories = models.ManyToManyField(to=Categories)


    def __str__(self):
        return self.title