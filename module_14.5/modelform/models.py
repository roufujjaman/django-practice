from django.db import models

# Create your models here.
class MyModel(models.Model):
    SHIRT_SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large"
    }
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        max_length=300 
    )
    size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES
    )
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.name}"