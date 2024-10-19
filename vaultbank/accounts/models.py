from django.db import models
from django.contrib.auth.models import User
# Create your models here.

ACCOUNT_TYPE = (
    ("savings", "savings"),
    ("current", "current")
)

GENDER_TYPE = (
    ("male", "male"),
    ("female", "female"),
    ("other", "other")
)

class Accounts(models.Model):
    # one user can have multiple account
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")

    account_no = models.IntegerField(unique=True)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    birth_date = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER_TYPE)
    activation_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)


    class Meta:
        verbose_name_plural = "Accounts"



class Address(models.Model):
    # one user will have only one address
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="address")

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)