from django.db import models

# Create your models here.
class MyModel(models.Model):
    serial = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=300 
    )
    date = models.DateField(
        blank=True,
        null=True
    )
    datetime = models.DateTimeField()
    decimal = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
