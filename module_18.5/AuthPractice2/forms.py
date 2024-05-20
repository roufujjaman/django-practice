from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserSignup(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]

class UserProfile(UserChangeForm):
    password = None
    class Meta():
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]