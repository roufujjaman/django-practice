from django.db import models

# Create your models here.

from datetime import datetime


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance)
    n,ext = filename.split(".")
    return "image_{}.{}".format(12312, ext)

class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to="service/images/")


