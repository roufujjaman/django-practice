from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    


obj = User.objects.filter(username='humayra', password='easyPASS2024')


print(obj.__sizeof__)