from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .constants import ACCOUNT_TYPE, GENDER_TYPE


class UserRegistrationForm(UserCreationForm):
    pass
    # # UserAccount
    # birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # gender = forms.ChoiceField(choices=GENDER_TYPE)
    # # UserAddress
    # street_address = forms.CharField(max_length=100)
    # city = forms.CharField(max_length=100)
    # postal_code = forms.IntegerField()
    # country = forms.CharField(max_length=150)

    # class Meta:
    #     model = User
    #     fields = ['username', 'password', 'password2', 'first_name', 'last_name',
    #               'email', 'account_type', 'genter', 'postal_code', 'country']
    
    # def save(self, commit=True):
    #     user = super().save(commit=False)