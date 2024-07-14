from django.db import models

# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=150)

class Problem(models.Model):
    titile = models.CharField(max_length=300)
    platform = models.ForeignKey(
        Platform,
        on_delete=models.CASCADE
    )
    url = models.URLField()
    series = models.IntegerField()