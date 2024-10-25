from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="roles")
    role = models.CharField(max_length=100)
    number = models.CharField(max_length=3)


    class Meta:
        verbose_name_plural = "Role"