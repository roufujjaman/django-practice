from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts, Address


class CreateUserForm(UserCreationForm):
    class Meta:
        pass

class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ["account_no", "account_type", "birth_date", "gender"]


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["street", "city", "postal_code", "country"]

