from django.db import models

# Create your models here.

class Problems(models.Model):
    titile = models.CharField(max_length=300)
    platform = models.ForeignKey()
    url = models.URLField()