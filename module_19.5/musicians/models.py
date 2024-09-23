from django.db import models

class Musicians(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    instrument = models.CharField(max_length=50)