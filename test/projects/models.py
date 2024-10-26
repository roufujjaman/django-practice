from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    progress = models.PositiveSmallIntegerField(default=0)
