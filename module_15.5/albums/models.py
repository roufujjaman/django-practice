from django.db import models
from musicians.models import Musician
# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=150)
    musician = models.ForeignKey(
        Musician,
        on_delete=models.CASCADE,
        related_name='albums'
    )
    release_date = models.DateField()
    RATING_CHOICES = (
        ('1', 'One'),
        ('2', 'Two'),
        ('3', 'Three'),
        ('4', 'Four'),
        ('5', 'Five')
    )
    rating = models.CharField(
        max_length=1,
        choices=RATING_CHOICES
    )

    def __str__(self) :
        return self.name