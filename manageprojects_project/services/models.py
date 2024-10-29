from django.db import models

# Create your models here.
class Categories(models.Model):
    order = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=150)
    duration_days_default = models.PositiveSmallIntegerField()

class SubCategories(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField()

    name = models.CharField(max_length=150)
    duration_days_default = models.PositiveSmallIntegerField()


class Submittals(models.Model):
    pass