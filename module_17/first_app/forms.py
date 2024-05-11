from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class RegisterFrom(UserCreationForm):
    first_name = forms.CharField(
        required=True,
    )
    last_name = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        required=True
    )
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]


class ChangeUserDataForm(UserChangeForm):
    password = None
    
    class Meta():
        model = User
        exclude = ['password']
        fields = [
            'username',
            'first_name',
            'last_name',
            'email'
        ]
