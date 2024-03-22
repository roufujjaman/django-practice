from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(
        primary_key=True
    )
    name = models.CharField(
        max_length=20,
    )
    address = models.TextField()
    email = models.TextField(default=None)

    def __str__(self):
        return f"{self.roll}, {self.name}"